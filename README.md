# AIchat
一个借助图灵机器人实现智能聊天机器人的[MCDReforged](https://github.com/Fallen-Breath/MCDReforged)插件

_使用腾讯AI的版本可以在`Tencent-AI`分支找到_
***

## 简介
借助腾讯AI实现智能聊天,并附带有道翻译机器人

![image](https://github.com/A-JiuA/AIchat/blob/master/pictures/0.png)

***

## 使用方式:
将AIchat.py放入MCDReforge主目录下的plugins文件夹中。

如果仅使用翻译功能，不需要配置即可使用。

如需启用智能聊天功能，将你的APIkey填入AIchat.py开头的变量中，例如:
```
TULING_API_KEY = 'xxxxxxxxxx'
```
然后把智能聊天功能启用，将`CHAT_SWITCH`设置为`True`，例如:
```
CHAT_SWITCH = True
```
如需关闭翻译功能，将`TRANSLATE_SWITCH`设置为`False`，例如:
```
TRANSLATE_SWITCH = False
```

## APIkey申请教程:
暂无

[图灵机器人]http://www.turingapi.com/
