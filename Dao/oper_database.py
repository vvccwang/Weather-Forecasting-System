from filecmp import cmp
from functools import cmp_to_key
import pymysql
import datetime
import json,urllib.request
from urllib.parse import urlencode
import numpy as np
from collections import Counter

class ConnectDB():
    # 打开数据库连接，使用cursor()方法创建一个游标对象cursor
    def __init__(self):
        self.wealist = ['晴', '多云', '阴', '阵雨', '雷阵雨', '雷阵雨有冰雹', '雨夹雪', '小雨', '中雨', '大雨', '暴雨', '大暴雨', '特大暴雨', '阵雪', '小雪', '中雪',
                '大雪', '暴雪', '雾', '冻雨', '沙尘暴', '小到中雨', '中到大雨', '大到暴雨','暴雨到大暴雨', '大暴雨到特大暴雨', '小雪到中雪', '中雪到大雪', '大雪到暴雪', '浮尘',
                '扬尘', '强沙尘暴', '霾', '浓雾', '强浓雾', '中度霾', '重度霾', '严重霾', '大雾', '特强浓雾', '雨', '雪']
        # cityid:311淄博城区、811高青、936桓台、1281临淄、2087沂源、2347淄川、2348博山、2349周村
        self.citylist = ['311', '811', '936', '1281', '2087', '2347', '2348', '2349']
        self.Error_flag=0
        try:
            self.db= pymysql.connect(host="localhost", user="root", password="v9ningmeng", database="weatherdata")
            self.cursor = self.db.cursor()
        except:
            self.Error_flag = 1

    # 关闭数据库连接
    def closeDB(self):
        self.db.close()

    # 根据城市id和时间，查询天气情况
    def QuaryWeaData(self,cityid,datetime):
        sql="SELECT * FROM weatherinfo WHERE cityid = "+cityid+" AND uptime BETWEEN '"+datetime+" 00:00:00' AND '"+datetime+" 23:59:59'"
        self.cursor.execute(sql)
        self.data=self.cursor.fetchall()
        # print(self.data)
        # self.closeDB()
        if self.data == None:
            return -1
        else:
            list = []
            for i in self.data:
                list.append([str(item) for item in i])
            for i in list:
                i[2]=int(i[2])
                if i[5] == '99':
                    i[5] = '无'
                else:
                    i[5] = self.wealist[int(i[5])-1]
            return list

    def QuaryWeaData_maxmin(self,cityid,startdatetime,enddatetime):
        datelist=self.getDatesByTimes(startdatetime,enddatetime)
        list=[]
        for time in datelist:
            data=self.QuaryWeaData(cityid,time)
            dict={}
            if data != -1:
                temp=[t[2] for t in data]
                temp.sort(reverse=True)
                max=temp[0]
                min=temp[len(temp)-1]

                wea=[w[5] for w in data]
                wea = np.array(wea)
                key = np.unique(wea)
                result = {}
                for k in key:
                    mask = (wea == k)
                    list_new = wea[mask]
                    v = list_new.size
                    result[k] = v
                d_order = sorted(result.items(), key=lambda x: x[1], reverse=True)
                wea_1=d_order[0][0]
                if len(d_order)>1 and (d_order[0][0].find('晴') != -1 or d_order[0][0].find('多云') != -1 or d_order[0][0].find('阴') != -1) :
                    if (d_order[1][0].find('雨') != -1 or d_order[1][0].find('雪') != -1) and d_order[1][1]>3 :
                        wea_1=d_order[1][0]
                    elif (d_order[1][0].find('霾') != -1 or d_order[1][0].find('雾') != -1) and d_order[1][1]>5:
                        wea_1 = d_order[1][0]
                dict['date'] = str(time)
                dict['weather'] =wea_1
                dict['max'] = str(max)
                dict['min'] = str(min)
                # print(dict)
                list.append(dict)
        self.closeDB()
        if list != []:
            return list
        else:
            return -1




    # 获取两个日期间的日期列表
    def getDatesByTimes(self,sDateStr, eDateStr):
        list = []
        datestart = datetime.datetime.strptime(sDateStr, '%Y-%m-%d')
        dateend = datetime.datetime.strptime(eDateStr, '%Y-%m-%d')
        list.append(datestart.strftime('%Y-%m-%d'))
        while datestart < dateend:
            datestart += datetime.timedelta(days=1)
            list.append(datestart.strftime('%Y-%m-%d'))
        return list

    # 获取指定日期和城市的天气数据，插入数据库
    # return:1正常 0超出 -1出错
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
                    # print(value_list)
                    self.cursor.execute("INSERT INTO weatherinfo VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",value_list)
                    self.db.commit()
                    self.closeDB()
            else:
                print(a_result['msgid'] + ' ' + a_result['msg']+'  ---ERROR'+hisdate)
                if a_result['msgid']=='1000701':
                    return 0
        else:
            print('Request nowapi fail.')
            return -1

        return 1

    # 更新数据库信息
    def UpdateWeaData(self):
        sql = "SELECT uptime FROM weatherinfo ORDER BY uptime desc"
        self.cursor.execute(sql)
        time_tup = self.cursor.fetchone()
        for i in time_tup:
            uptime=i.strftime('%Y-%m-%d')
            break
        today=datetime.datetime.now().strftime('%Y-%m-%d')
        self.DeleteWeaData(uptime,uptime)
        datelist=self.getDatesByTimes(uptime,today)
        for dl in datelist:
            for cid in self.citylist:
                flag=self.GetHisData(dl,cid)

        self.closeDB()
        pass

    # return：账户不存在0、账户存在密码不正确-1、密码正确1
    def login(self,name,passwprd):
        sql = "SELECT password FROM user WHERE username = '"+name+"'"
        self.cursor.execute(sql)
        realpwd = self.cursor.fetchone()

        self.closeDB()
        if realpwd == None:
            return 0
        elif passwprd == realpwd[0]:
            return 1
        else:
            return -1

    # 更改数据库中的气象数据,暂时无用
    def ChangeData(self,cityid,date,keyname,value):
        self.closeDB()
        pass

    # 从数据库删除指定条件的信息，根据要求编辑
    def DeleteWeaData(self,startdatetime,enddatetime):
        sql="DELETE FROM weatherinfo WHERE uptime BETWEEN '"+startdatetime+" 00:00:00' AND '"+enddatetime+" 23:59:59'"
        self.cursor.execute(sql)
        self.db.commit()
        self.closeDB()
        pass




dc = ConnectDB()
if dc.Error_flag == 0:
    dc.QuaryWeaData_maxmin('311','2020-1-1','2020-1-2')

