# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    #访问网址
    url = 'http://www.whatismyip.com.tw/'
    url = 'http://www.ip138.com/'
    url = 'http://2017.ip138.com/ic.asp'
    url = 'http://www.whatismyip.com.tw/'
    #这是代理IP
    #本机ip 219.239.110.100   121.22.243.18

    proxy = {'http':'115.29.236.46:3128'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36')]
    #安装OPener
    request.install_opener(opener)
    #使用自己安装好的Opener
    response = request.urlopen(url)
    #读取相应信息并解码
    html = response.read().decode("utf-8")
    #打印信息
    print("html:")
    print(html)
