#coding=utf-8
import yagmail
import time
import urllib.request
import subprocess
import requests
# 检查网络连通性
def check_network():
    while True:
        try:
            result=urllib.request.urlopen('http://www.baidu.com')
            print (result)
            print ("Network is Ready!")
            break
        except Exception as e:
            print (e)
            print ("Network is not ready,Sleep 5s...")
            time.sleep(5)
    return True
# 运行iwconfig命令行，返回信息
def iwconfig():
    result=subprocess.getoutput('iwconfig') 
    return result
# 运行ifconfig命令行，返回信息
def ifconfig():
    result1=requests.get(url="http://ip.42.pl/raw").text
    result2=requests.get('http://jsonip.com').text
    result3=requests.get('http://httpbin.org/ip').text
    result4=requests.get('https://api.ipify.org/?format=json').text

    return result1,result2,result3,result4
# 发送邮件
def sendEmail():
    check_network()
    yag = yagmail.SMTP(
        user = "XXXX@qq.com",   # 发件人邮箱
        password='XXXX',  # 授权码
        host = 'smtp.qq.com')
    #邮件内容
    contents = ['服务器IP地址:\n',ifconfig(),'#===========分页符===========#', iwconfig()]
    yag.send(to = '1002887385@qq.com',# 收件人邮箱
             subject = 'deep learning station',  # 邮件主题
             contents = contents)

if  __name__ == '__main__' :
    sendEmail()
