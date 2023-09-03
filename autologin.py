# _*_ coding : utf-8 _*_
import time
import requests    # 用于向目标网站发送请求
import socket  # 用于获得自己的IP
from ping3 import ping  # 用于判断是否联网
import pywifi   # 用于尝试并连接wifi
import comtypes  # 似乎封装成EXE时需要这个模块
import base64  # 用于base64加密


def isConnected():  # 自动连接wifi
    if ifaces.status() == pywifi.const.IFACE_CONNECTED:
        return True
    else:
        return False


def ping_host(ip):  # 联网测试
    ip_address = ip
    response = requests.get(ip_address, allow_redirects=False)
    return response.status_code


def get_host_ip():  # 变动IP获取
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


# 需要输入数据的校园网登录界面
url = 'http://47.98.217.39/lfradius/libs/portal/unify/portal.php/login/cmcc_login'

# 对data进行base64编码
myip = get_host_ip()
data = '{"usrname":"你的学号","passwd":"你的密码","usrmac":"30:e2:47:8a:f8:f7","usrip":"'+myip +\
    '","basip":"172.17.127.254","nasid":"3","success":"http:\/\/47.98.217.39\/lfradius\/libs\/portal\/unify\/portal.php\/login\/success\/","fail":"http:\/\/47.98.217.39\/lfradius\/libs\/portal\/unify\/portal.php\/login\/fail\/","v":1,"t":"pap"}'
encodedata = base64.b64encode(data.encode('utf-8'))
finaldata = 'cmcc_login_value='+str(encodedata, 'utf-8')

# 数据包请求头
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connectin": "keep-alive",
    "Content-Length": "376",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "47.98.217.39",
    "Origin": "http://47.98.217.39",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
# POST 方式向 URL 发送数据包,实际上登录按钮就是发post数据包
if __name__ == '__main__':

    # 断开之前连接,尝试连接SZTU-student
    wifi = pywifi.PyWiFi()  # 创建一个无线对象
    ifaces = wifi.interfaces()[0]  # 取一个无限网卡
    if (isConnected() == False):
        ifaces.disconnect()  # 断开网卡连接
        time.sleep(0.5)  # 缓冲0.5秒
        profile = pywifi.Profile()  # 配置文件
        profile.ssid = "SZTU-student"  # wifi名称
        tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件
        ifaces.connect(tmp_profile)  # 连接
        time.sleep(0.5)  # 等待0.5秒后看下是否成功连接了
        if (isConnected() == False):
            time.sleep(5)  # 若未成功，等待5秒
    else:
        if (isConnected() == True):  # 连接SZTU-student成功,尝试登录
            print("网卡已连上SZTU-student,正在尝试登录")
            if (ping_host('http://www.baidu.com') != 302):
                print("您已登录,无需重复登录")
            else:
                response = requests.post(url, finaldata, headers=header)
                time.sleep(1)
                if (ping_host('http://www.baidu.com') != 302):
                    print("登录完毕,联网成功")
                else:
                    print("未知错误")
        else:  # 连接失败
            print("网卡连不上SZTU-student,请自行排除错误")
    time.sleep(2)
