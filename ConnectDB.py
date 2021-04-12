'''
连接MySQL数据库
'''
import datetime

import pymysql
import json,urllib.request
from urllib.parse import urlencode

class ConnectDB():
    # 打开数据库连接，使用cursor()方法创建一个游标对象cursor
    def __init__(self):
        self.db= pymysql.connect(host="localhost", user="root", password="v9ningmeng", database="weatherdata")
        self.cursor = self.db.cursor()

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

    # 从数据库删除指定条件的信息，根据要求编辑
    def DeleteData(self):
        self.cursor.execute("DELETE FROM weatherinfo WHERE cityid = 811")
        self.db.commit()
        pass

    # 获取指定日期和城市的天气数据，插入数据库
    def GetHisData(self,hisdate,cityid):
        url = 'http://api.k780.com'
        params = {
            'app': 'weather.history',
            'weaid': cityid,
            'date': hisdate,
            # 'appkey': '58433',
            'appkey': '58300',
            # 'sign': '2f6f16436696acab39e15d3a14065f85',
            'sign': 'ad4e13e10023397dbfe02f1ca75290ae',
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
                    print(value_list)
                    self.cursor.execute("INSERT INTO weatherinfo VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",value_list)
                    self.db.commit()
            else:
                print(a_result['msgid'] + ' ' + a_result['msg']+'  ---ERROR'+hisdate)
                return 0
        else:
            print('Request nowapi fail.')

    # 关闭数据库连接
    def closeDB(self):
        self.db.close()

# 获取两个日期之间的所有日期
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
datalist=getDatesByTimes('2020-03-02','2021-04-11')
# cityid:311淄博城区、811高青、936桓台、1281临淄、2087沂源、2347淄川、2348博山、2349周村

R1=ConnectDB()
# R1.DeleteData()
# R1.GetHisData('2021-02-23','311')

for data in datalist:
    f=R1.GetHisData(data,'936')
    if f==0:
        break
    print(data,'ok')
print('811','ok')
# R1.QuaryWeaType()
R1.closeDB()











