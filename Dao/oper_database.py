
import pymysql
import datetime
import json,urllib.request
from urllib.parse import urlencode


class ConnectDB():
    # 打开数据库连接，使用cursor()方法创建一个游标对象cursor
    def __init__(self):
        self.Error_flag = 0
        try:
            self.db= pymysql.connect(host="localhost", user="root", password="123456", database="weather")
            self.cursor = self.db.cursor()
        except:
            self.Error_flag = 1
        self.wealist = ['晴', '多云', '阴', '阵雨', '雷阵雨', '雷阵雨有冰雹', '雨夹雪', '小雨', '中雨', '大雨', '暴雨', '大暴雨', '特大暴雨', '阵雪', '小雪',
                        '中雪',
                        '大雪', '暴雪', '雾', '冻雨', '沙尘暴', '小到中雨', '中到大雨', '大到暴雨', '暴雨到大暴雨', '大暴雨到特大暴雨', '小雪到中雪', '中雪到大雪',
                        '大雪到暴雪', '浮尘',
                        '扬尘', '强沙尘暴', '霾', '浓雾', '强浓雾', '中度霾', '重度霾', '严重霾', '大雾', '特强浓雾', '雨', '雪']
        # cityid:311淄博城区、811高青、936桓台、1281临淄、2087沂源、2347淄川、2348博山、2349周村
        self.citylist = ['311', '811', '936', '1281', '2087', '2347', '2348', '2349']
    # 关闭数据库连接
    def closeDB(self):
        self.db.close()
    # 根据城市id和时间，查询天气情况
    def QuaryWeaData(self,cityid,datetime):
        sql="SELECT * FROM weatherinfo WHERE cityid = "+cityid+" AND uptime BETWEEN '"+datetime+" 00:00:00' AND '"+datetime+" 23:59:59'"
        self.cursor.execute(sql)
        self.data=self.cursor.fetchall()
        if self.data == None:
            return -1
        else:
            list = []
            for i in self.data:
                list.append([str(item) for item in i])
            for i in list:
                i[1]=i[1]
                i[2]=int(i[2])
                if i[5] == '99':
                    i[5] = '无'
                else:
                    i[5] = self.wealist[int(i[5])-1]
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

    #获取 date_str 往前days_count天的日期列表
    def date_add(self, date_str, days_count):
        list = []
        start = datetime.datetime.strptime(date_str, '%Y-%m-%d')

        list.append(start.strftime('%Y-%m-%d'))
        while days_count > 1 :
            start -= datetime.timedelta(days=1)
            list.append(start.strftime('%Y-%m-%d'))
            days_count-=1
        return list[::-1]
    # 获取指定日期和城市的天气数据，插入数据库
    # return:1正常 0超出 -1出错
    def GetHisData(self,hisdate,cityid):
        count=0
        url = 'http://api.k780.com'
        params = {
            'app': 'weather.history',
            'weaid': cityid,
            'date': hisdate,
            # 'appkey': '58433',
            'appkey': '58300',
            # 'appkey': '58940',
            # 'sign': '2f6f16436696acab39e15d3a14065f85',
            'sign': 'ad4e13e10023397dbfe02f1ca75290ae',
            # 'sign': '5f75eff0e853fbf8e8738f54692549be',
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
                    self.cursor.execute("INSERT INTO weatherinfo VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",value_list)
                    self.db.commit()
                    count+=1
            else: # print(a_result['msgid'] + ' ' + a_result['msg']+'  ---ERROR'+hisdate)
                if a_result['msgid']=='1000701':
                    return -2 #print(a_result['msgid']+'error')
        else:
            return -1 # print('Request nowapi fail.')
        return count
    # 更新数据库信息
    def UpdateWeaData(self):
        count=0
        sql = "SELECT uptime FROM weatherinfo ORDER BY uptime desc"
        self.cursor.execute(sql)
        time_tup = self.cursor.fetchone()
        for i in time_tup:
            utime=i.strftime('%Y-%m-%d')
            break
        # print(utime)
        today=datetime.datetime.now().strftime('%Y-%m-%d')
        self.DeleteWeaData(utime,utime)
        datelist=self.getDatesByTimes(utime,today)
        for dl in datelist:
            for cid in self.citylist:
                flag=self.GetHisData(dl,cid)
                if flag==-1:
                    # print('api error')
                    return -1
                elif flag==-2:
                    # print('limit error')
                    return 0
                elif dl != utime:
                    count += flag
        self.closeDB()
        list=[str(utime),str(count),str(today)]
        return list
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
    # 从数据库删除指定条件的信息，根据要求编辑
    def DeleteWeaData(self,startdatetime,enddatetime):
        sql="DELETE FROM weatherinfo WHERE uptime BETWEEN '"+startdatetime+" 00:00:00' AND '"+enddatetime+" 23:59:59'"
        self.cursor.execute(sql)
        self.db.commit()

    def QuaryWeaDataSE(self,cityid,stime,etime):
        sql = "SELECT * FROM weatherinfo WHERE cityid = " + cityid + " AND uptime BETWEEN '" + stime + " 00:00:00' AND '" + etime + " 23:59:59'"
        self.cursor.execute(sql)
        self.data = self.cursor.fetchall()
        if self.data == None:
            return -1
        else:
            list = []
            for i in self.data:
                list.append([str(item) for item in i])
            for i in list:
                i[2] = int(i[2])
                if i[5] == '99':
                    i[5] = '无'
                else:
                    i[5] = self.wealist[int(i[5]) - 1]
            if list != []:
                return list
            else:
                return -1


# dc = ConnectDB()
# if dc.Error_flag == 0:
    # datelist=dc.getDatesByTimes('2019-07-21','2019-12-31')
    # datelist = dc.getDatesByTimes('2019-01-01', '2019-07-20')
    # for date in datelist:
    #     dc.GetHisData(date,'2349')
    # for c in dc.citylist:
    #     dc.GetHisData('2021-05-11', c )
    # dc.QuaryWeaDataSE('311','2021-01-01','2021-02-01')
