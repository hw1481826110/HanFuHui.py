#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ast import main
from multiprocessing.spawn import _main
from re import L
import requests
import json
import configparser
import platform
import os


dengluhoutiken=""
def write_config_file(token32,token256,data):
    
    system = platform.system()
    if system == 'Windows':
        print("Windows")
        filename= 'C:/hanfu.ini'
    elif system == 'Linux':
        print("Linux")
        filename= '/mnt/sata1-4/code/hanfu.ini'
    else:
        print("其他系统")
        raise NotImplementedError(f"Unsupported system: {system}")
    if os.path.exists(filename):
        config = configparser.ConfigParser()
        config['汉服荟'] = {
            'token32': token32,
            'token256': token256,
            'data': data
        }

        with open(filename, 'w') as configfile:
            config.write(configfile)

def qiandao(token):
    if token is not None:
        print("token")
    else:
        print("token为空")
    print(token)
    url = 'https://api5.hanfuhui.com/Hanbi/InsertSignin'
    token256=gettoken_dengluhou(token)
    headers = {
    'Host': 'api5.hanfuhui.com',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'sec-ch-ua': '"Android WebView";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'hanfuhui_app': 'hanfuhui',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; KB2000 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.193 Mobile Safari/537.36hui_android',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'hanfuhui_fromclient': 'h5',
    'hanfuhui_token': token,
    'sec-ch-ua-platform': '"Android"',
    'Origin': 'https://www.hanfuhui.com',
    'X-Requested-With': 'com.hanfuhui',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.hanfuhui.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'hanfuhui_signature': token256
    }
    cookies = {}
    data = {}
    

    html = requests.post(url, headers=headers,  cookies=cookies, data=json.dumps(data))
    print(html.text)
    html = requests.post(url, headers=headers,  cookies=cookies, data=json.dumps(data))
    print(html.text)
    write_config_file(token,token256,html.text)
    
   # gettoken_dengluhou(token)
    

def res_code(text): # 获取res加密数据
    #html = requests.post("https://www.hanfuhui.com/Home/Rsa?text=" +, ,  , data=json.dumps(data))
    html = requests.get("https://www.hanfuhui.com/Home/Rsa?text=" +text)
    print(html.text)
    return html.text

def gettoken():
    url = "https://www.hanfuhui.com/Api/GetAppToken"

    
    payload = ""
    headers = {
    
    "Host": "www.hanfuhui.com",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "Referer": "https://www.hanfuhui.com/Account?from=http%253a%252f%252fwww.hanfuhui.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
    response = requests.request("GET", url, data=payload, headers=headers)
    print(response.text)
    return response.text
def gettoken_dengluhou(token):
    url = "https://www.hanfuhui.com/Api/GetAppToken"
    payload = ""
    headers = {
    
    "Host": "www.hanfuhui.com",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "Referer": "https://www.hanfuhui.com/Account?from=http%253a%252f%252fwww.hanfuhui.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
    ck={"cookie_user_token":token}
    response = requests.request("GET", url, data=payload, headers=headers,cookies=ck)
    print(response.text)
    return response.text
def login(user,password):#登录

    url = "https://api5.hanfuhui.com/Account/LoginForPhone"
    userOrName=res_code(user+","+password)
    payload = "usersecret="+userOrName+"&phonecountry=86"
    headers = {
    "Host": "api5.hanfuhui.com",
    "Connection": "keep-alive",
    "Content-Length": "213",
    "hanfuhui_app": "hanfuhui",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "hanfuhui_fromclient": "PC",
    "hanfuhui_token": "null",

     "hanfuhui_signature": gettoken(),
    "Origin": "https://www.hanfuhui.com",
    "Referer": "https://www.hanfuhui.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    if(response.status_code==200):
        print("sueeses")
        a=json.loads(response.text)
        AccessTokenken=a.get("Data", {}).get("AccessToken")
        return AccessTokenken
    
    else:
        print("false")
    return AccessTokenken
    
if __name__ == '__main__':
    #token=
    qiandao(login("13145487071","hw1481826110"))





    
    