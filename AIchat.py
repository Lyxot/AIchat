# -*- coding: UTF-8 -*-
import hashlib
import time
import random
import string
from json import JSONDecodeError

import requests
from requests import ReadTimeout, ConnectTimeout

from mcdreforged.api.decorator import new_thread

try:
    from urllib import quote
except:
    from urllib.parse import quote

PLUGIN_METADATA = {
    'id': 'ai_chat',
    'version': '1.0.0',
    'name': 'AIchat',
    'author': 'A-JiuA',
    'link': 'https://github.com/A-JiuA/AIchat'
}

# 设置AI回复默认关闭
CHAT_SWITCH = False
TRANSLATE_SWITCH = True

# 这里修改成自己的id和key，CHAT_SWITCH为关时可以不配置
app_id = '111111111'
app_key = 'xxxxxxxxxxxxxxxx'


def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))
    # 将得到的MD5值所有字符转换成大写
    return m.hexdigest().upper()


def get_params(plus_item):
    # 请求时间戳（秒级），用于防止请求重放（保证签名5分钟有效）
    t = time.time()
    time_stamp = str(int(t))
    # 请求随机字符串，用于保证签名不可预测
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    params = {'app_id': app_id,
              'question': plus_item,
              'time_stamp': time_stamp,
              'nonce_str': nonce_str,
              'session': '10000'
              }
    sign_before = ''
    # 要对key排序再拼接
    for key in sorted(params):
        # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。
        sign_before += '{}={}&'.format(key, quote(params[key], safe=''))
    # 将应用密钥以app_key为键名，拼接到字符串sign_before末尾
    sign_before += 'app_key={}'.format(app_key)
    # 对字符串sign_before进行MD5运算，得到接口请求签名
    sign = curlmd5(sign_before)
    params['sign'] = sign
    return params


def get_content(plus_item):
    # 聊天的API地址
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
    # 获取请求参数
    plus_item = plus_item.encode('utf-8')
    payload = get_params(plus_item)
    try:
        try:
            r = requests.post(url, data=payload, timeout=2)
            return r.json()["data"]["answer"]
        except JSONDecodeError:
            error_message = "AI聊天id或key配置错误"
            return error_message
    except (ReadTimeout, ConnectTimeout):
        error_message = "AI聊天接口超时"
        return error_message


# 中文判断
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


@new_thread
def ai_chat_feature(comment, server):
    answer = get_content(comment)
    if answer != '':
        server.execute('tellraw @a {"text":"<智能聊天> %s","color":"aqua"}' % answer)
    else:
        pass


@new_thread
def translate_feature(comment, server):
    txt = comment
    data = {
        "i": txt,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "true"
    }
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    try:
        res = requests.post(url, data=data, timeout=2)
        js = res.json()
        comment = js['translateResult'][0][0]['tgt']
        if comment != txt:
            server.execute('tellraw @a {"text":"<翻译君> %s","color":"yellow"}' % comment)
            if CHAT_SWITCH:
                ai_chat_feature(comment, server)
        else:
            pass
    except (ReadTimeout, ConnectTimeout):
        error_message = "有道翻译接口超时"
        server.execute('tellraw @a {"text":"<翻译君> %s","color":"yellow"}' % error_message)
        pass


def on_info(server, info):
    if info.is_player and is_contains_chinese(info.content):
        language = 'zh-cn'
    elif info.is_player:
        try:
            language = 'else'
        except:
            language = 'zh-cn'
    comment = info.content
    if info.is_player and language != 'zh-cn' and info.content[0:2] != '!!' and TRANSLATE_SWITCH:
        # 将信息翻译为中文后回复
        translate_feature(comment, server)
    elif info.is_player and language == 'zh-cn' and info.content[0:2] != '!!' and CHAT_SWITCH:
        ai_chat_feature(comment, server)
