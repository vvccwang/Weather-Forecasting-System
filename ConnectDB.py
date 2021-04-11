'''
连接MySQL数据库
'''
import datetime

import pymysql
import json,urllib.request
from urllib.parse import urlencode

class ConnectDB():
    # 打开数据库连接
    def __init__(self):
        self.db= pymysql.connect(host="localhost", user="root", password="v9ningmeng", database="weatherdata")
    # 使用cursor()方法创建一个游标对象cursor
        self.cursor = self.db.cursor()
    # # 使用execute()方法执行SQL查询
    #     self.cursor.execute("SELECT VERSION()")
    # # 使用 fetchone() 方法获取单条数据.
    #     versioninfo = self.cursor.fetchone()
    #     print("Database version : %s " % versioninfo)

    # 存储需要更新的每日单条数据
        self.New_weadata=[]


    def UpdateData(self,cityid,date,weadata):
        pass

    def QuaryWeaType(self):
        self.cursor.execute("SELECT * FROM weathertype")
        self.data=self.cursor.fetchall()
        for i in self.data:
            print(i)
        pass

    def ChangeData(self,cityid,date,keyname,value):
        pass

    def DeleteData(self):
        pass

    def GetHisData(self,hisdate,cityid):
        url = 'http://api.k780.com'
        params = {
            'app': 'weather.history',
            'weaid': cityid,
            'date': hisdate,
            'appkey': '58433',
            # 'appkey': '58300',
            'sign': '2f6f16436696acab39e15d3a14065f85',
            # 'sign': 'ad4e13e10023397dbfe02f1ca75290ae',
            'format': 'json',
        }
        params = urlencode(params)

        f = urllib.request.urlopen('%s?%s' % (url, params))
        nowapi_call = f.read()
        a_result = json.loads(nowapi_call)
        if a_result:
            if a_result['success'] != '0':
                for wd_dict in a_result['result']:
                    value_list = [cityid]
                    value_list.append(wd_dict['uptime'])
                    value_list.append(wd_dict['temp'])
                    value_list.append(wd_dict['humidity'][:-1])
                    value_list.append(wd_dict['aqi'])
                    value_list.append(wd_dict['weatid'])
                    value_list.append(wd_dict['wind'])
                    value_list.append(wd_dict['winp'][:-1])
                    # value_list = [cityid]
                    # value_list.append(wd_dict['uptime'])
                    # # print(wd_dict['uptime'])
                    # value_list.append(int(wd_dict['temp']))
                    # value_list.append(int(wd_dict['humidity'][:-1]))
                    # value_list.append(int(wd_dict['aqi']))
                    # value_list.append(int(wd_dict['weatid']))
                    # value_list.append(wd_dict['wind'])
                    # value_list.append(int(wd_dict['winp'][:-1]))
                    # for va in value_list:
                    #     print(va)
                    # uptime=wd_dict['uptime']
                    # temp=wd_dict['temp']
                    # hum=wd_dict['humidity']
                    # aqi=wd_dict['aqi']
                    # weather=wd_dict['weatid']
                    # windtype=wd_dict['wind']
                    # windlevel=wd_dict['winp']
                    # print(uptime, temp, hum, aqi, weather, windtype, windlevel)
                    # print(value_list)
                    self.cursor.execute("INSERT INTO weatherinfo VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",value_list)
                    self.db.commit()

            else:
                print(a_result['msgid'] + ' ' + a_result['msg']+'  ---ERROR')
        else:
            print('Request nowapi fail.')

    # 关闭数据库连接
    def closeDB(self):
        self.db.close()

def getDatesByTimes(sDateStr, eDateStr):
    list = []
    datestart = datetime.datetime.strptime(sDateStr, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(eDateStr, '%Y-%m-%d')
    list.append(datestart.strftime('%Y-%m-%d'))
    while datestart < dateend:
        datestart += datetime.timedelta(days=1)
        list.append(datestart.strftime('%Y-%m-%d'))
    return list

# 历史日期
datalist=getDatesByTimes('2020-02-12','2021-04-10')
# cityid:311淄博城区、811高青、936桓台、1281临淄、2087沂源、2347淄川、2348博山、2349周村
citylist=['311','811','936','1281','2087','2347','2348','2349']

R1=ConnectDB()

for city in citylist:
    for data in datalist:
        R1.GetHisData(data,city)
        print(data,'ok')
    print(city,'ok')
# R1.QuaryWeaType()
R1.closeDB()











