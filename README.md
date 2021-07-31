# AIchat
一个借助腾讯AI实现智能聊天机器人的[MCDReforged](https://github.com/Fallen-Breath/MCDReforged)插件

***

## 简介
借助腾讯AI实现智能聊天,并附带有道翻译机器人
![image](https://github.com/A-JiuA/AIchat/blob/master/pictures/0.png)

***

## 使用方式:
将AIchat.py放入MCDReforge主目录下的plugins文件夹中。

如果仅使用翻译功能，不需要配置即可使用。

如需启用智能聊天功能，将你的APPid与APIkey填入AIchat.py开头的变量中，例如:
```
app_id = '111111111'
app_key = 'xxxxxxxxxxxxxx'
```
然后把智能聊天功能启用，将`CHAT_SWITCH`设置为`True`，例如:
```
CHAT_SWITCH = True
```
如需关闭翻译功能，将`TRANSLATE_SWITCH`设置为`False`，例如:
```
TRANSLATE_SWITCH = False
```

## APPid与APIkey申请教程:
前往[腾讯AI开放平台](https://ai.qq.com/console/),完成注册后会自动进入[创建应用](https://ai.qq.com/console/application/create-app)的界面,填写信息,点击创建按钮
![image](https://github.com/A-JiuA/AIchat/blob/master/pictures/1.png)
提示创建成功,点击接入能力,找到智能闲聊>智能闲聊,点击进入
![image](https://github.com/A-JiuA/AIchat/blob/master/pictures/2.png)
点击接入能力,选择你的应用名称,点击确定接入
![image](https://github.com/A-JiuA/AIchat/blob/master/pictures/3.png)
在上方应用管理中找到你的应用,点击进入,进入应用信息栏,找到你的APPid与APIkey,填入AIchat.py开头的变量中
![image](https://github.com/A-JiuA/AIchat/blob/master/pictures/4.png)

你也可以自行配置你的闲聊画像
![image](https://github.com/A-JiuA/AIchat/blob/master/pictures/5.png)
