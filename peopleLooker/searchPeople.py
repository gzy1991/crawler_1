# coding=utf8
import sys
import time
from imp import reload
reload(sys)
#sys.setdefaultencoding('utf8')

import requests, json, time

# https://www.peoplelooker.com/hk/teaser?age=&city=DUETTE&exporttype=json&fn=William&ln=Blosch&mn=&state= 搜索不用登陆都能拿数据
# https://www.peoplelooker.com/api/v4/reports 根据bvid获取reportid，参数是payload
# https://www.peoplelooker.com/api/v4/reports/aeab6f3af7fb600c313592cbb5500f323ce50df9e5e88708d2e8ea 需要登录的cookie
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
session = requests.session()
session.headers['"Referer'] = 'https://www.peoplelooker.com/f/dashboard'
response = session.post('https://www.peoplelooker.com/api/v4/session', data={'user[email]':'83390332@qq.com','user[password]':'hxjxqs1122'})
try:
    for i in range(1,5000):
        search_response = session.get(
            'https://www.peoplelooker.com/hk/teaser?age=&city=DUETTE&exporttype=json&fn=William&ln=Blosch&mn=&state=')
        print (i,1,response.status_code)
        bvid = search_response.json()['response']['Records']['Record'][0]['bvid']
        reports_response =session.get('https://www.peoplelooker.com/api/v4/reports',data = json.dumps({'report_type': "detailed_person_report", 'meta': {'person_id': bvid}}))
        print (i, 2, response.status_code,"bvid= "+bvid)
        personId=reports_response.json()['reports'][0]['permalink']
        response = session.get('https://www.peoplelooker.com/api/v4/reports/' + personId)
        print (i, 3, response.status_code,"personId= "+personId)
        time.sleep(2)
    #print response.content
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
except ValueError:
    print("ValueError")
    print(response.status_code)
    print( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

except KeyError:
    print("KeyError")
    print(response.status_code)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
