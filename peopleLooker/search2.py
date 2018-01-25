# coding=utf8
import sys
import time
from imp import reload
reload(sys)

import requests, json

# https://www.peoplelooker.com/hk/teaser?age=&city=DUETTE&exporttype=json&fn=William&ln=Blosch&mn=&state= 搜索不用登陆都能拿数据
# https://www.peoplelooker.com/api/v4/reports 根据bvid获取reportid，参数是payload
# https://www.peoplelooker.com/api/v4/reports/aeab6f3af7fb600c313592cbb5500f323ce50df9e5e88708d2e8ea 需要登录的cookie

def searchPeople(param):

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))



searchPeople()

