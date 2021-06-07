import datetime
import calendar


import Data_quary
from Dao import oper_database
import pandas as pd
import numpy as np

class Data_Analyse():
    #温度30、60天可视化
    def Quary_many(self,city, flag):
        timelist=[30,60]
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            datelist = dc.date_add(today,timelist[flag-1])
            start = datelist[0]
            datam = dc.QuaryWeaDataSE(city,start,today)
            list = []
            for index,value in datam.items():
                dict = {}
                dict['date'] = index
                dict['max'] = value[0]
                dict['min'] = value[1]
                list.append(dict)
            dc.closeDB()
            # not none
            if list != []:
                return list
            else:
                return 0
                # 数据库无此数据
        else:
            return -1 # 数据库连接异常
    #温度历年对比
    def Year_contrast(self,city):
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:

            datam1 = dc.QuaryWeaDataSE(city, '2019-01-01','2019-12-31')
            datam2 = dc.QuaryWeaDataSE(city, '2020-01-01','2020-12-31')
            datam3 = dc.QuaryWeaDataSE(city, '2021-01-01', today)

            list1 = []
            list2 = []
            list3 = []

            for index,value in datam1.items():
                dict = {}
                dict['date'] = index
                dict['max'] = value[0]
                dict['min'] = value[1]
                list1.append(dict)

            for index,value in datam2.items():
                dict = {}
                dict['date'] = index
                dict['max'] = value[0]
                dict['min'] = value[1]
                list2.append(dict)

            for index,value in datam3.items():
                dict = {}
                dict['date'] = index
                dict['max'] = value[0]
                dict['min'] = value[1]
                list3.append(dict)

            list=[]
            list.append(list1)
            list.append(list2)
            list.append(list3)

            dc.closeDB()

            # not none
            if list != []:
                return list
            else:
                return 0
                # 数据库无此数据
        else:
            return -1  # 数据库连接异常
    #天气类型统计可视化
    def Weather_type_days(self,city,flag):
        timelist = [30, 60]
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        today_last1 = today[:3]+'0'+today[4:]
        today_last2 = today[:2]+'19'+today[4:]
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            datelist1 = dc.date_add(today, timelist[flag - 1])
            datelist2 = dc.date_add(today_last1, timelist[flag - 1])
            datelist3 = dc.date_add(today_last2, timelist[flag - 1])
            weatype = dc.wealist
            weatype = np.array(weatype)
            key = np.unique(weatype)

            result = {}
            for k in key:
                result[k] = 0
            data1 = dc.QuaryWeaDataSEType(city,datelist1[0],today)
            if data1 != -1:
                wea = np.array(data1)
                for k in key:
                    mask = (wea == k)
                    list_new = wea[mask]
                    v = list_new.size
                    result[k] += v
            d_order1 = result

            result = {}
            for k in key:
                result[k] = 0
            data1 = dc.QuaryWeaDataSEType(city, datelist2[0], today_last1)
            if data1 != -1:
                wea = np.array(data1)
                for k in key:
                    mask = (wea == k)
                    list_new = wea[mask]
                    v = list_new.size
                    result[k] += v
            d_order2 = result

            result = {}
            for k in key:
                result[k] = 0
            data1 = dc.QuaryWeaDataSEType(city, datelist3[0], today_last2)
            if data1 != -1:
                wea = np.array(data1)
                for k in key:
                    mask = (wea == k)
                    list_new = wea[mask]
                    v = list_new.size
                    result[k] += v
            d_order3 = result

            resultlist=[]
            resultlist.append(d_order1)
            resultlist.append(d_order2)
            resultlist.append(d_order3)
            dc.closeDB()

            # not none
            if resultlist != []:
                return resultlist
            else:
                return 0
        else:
            return -1  # 数据库连接异常
    #天气类型历年对比
    def Weather_type_year(self,city):
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            datelist3 = dc.getDatesByTimes('2019-01-01', '2019-12-31')
            datelist2 = dc.getDatesByTimes('2020-01-01', '2020-12-31')
            datelist1 = dc.getDatesByTimes('2021-01-01', today)

            weatype = dc.wealist
            weatype = np.array(weatype)
            key = np.unique(weatype)

            result = {}
            for k in key:
                result[k] = 0
            data1 = dc.QuaryWeaDataSEType(city, '2021-01-01', today)
            if data1 != -1:
                wea = np.array(data1)
                for k in key:
                    mask = (wea == k)
                    list_new = wea[mask]
                    v = list_new.size
                    result[k] += v
            d_order1 = result

            result = {}
            for k in key:
                result[k] = 0
            data1 = dc.QuaryWeaDataSEType(city, '2020-01-01', '2020-12-31')
            if data1 != -1:
                wea = np.array(data1)
                for k in key:
                    mask = (wea == k)
                    list_new = wea[mask]
                    v = list_new.size
                    result[k] += v
            d_order2 = result

            result = {}
            for k in key:
                result[k] = 0
            data1 = dc.QuaryWeaDataSEType(city, '2019-01-01', '2019-12-31')
            if data1 != -1:
                wea = np.array(data1)
                for k in key:
                    mask = (wea == k)
                    list_new = wea[mask]
                    v = list_new.size
                    result[k] += v
            d_order3 = result

            resultlist = []
            resultlist.append(d_order1)
            resultlist.append(d_order2)
            resultlist.append(d_order3)
            dc.closeDB()
            # not none
            if resultlist != []:
                return resultlist
            else:
                return 0
                # 数据库无此数据
        else:
            return -1  # 数据库连接异常
    #按月平均气温
    def AverageTemp_Month(self,city):
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            yearlist=[2019,2020,2021]
            monthlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            datelist = []
            for y in yearlist:
                datelist_y = []
                for m in monthlist:
                    d='-30'
                    #闰年
                    if ( (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) ) and m==2:
                        d='-29'
                    elif m==2:
                        d='-28'
                    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                        d = '-31'
                    datelist_m = dc.getDatesByTimes(str(y)+'-'+str(m)+'-01', str(y)+'-'+str(m)+d)
                    datelist_y.append(datelist_m)
                datelist.append(datelist_y)
            avetemp_y = []

            for y in datelist:#每年
                avetemp_m = []
                for m in y:#每月
                    datam = dc.QuaryWeaDataSETemp(city,m[0],m[-1])
                    if datam != -1:
                        average_a = np.mean(datam)
                    else:
                        average_a = 0
                    avetemp = round(average_a,2)
                    avetemp_m.append(avetemp)
                avetemp_y.append(avetemp_m)
            dc.closeDB()
            if avetemp_y != []:
                return avetemp_y
            else:
                return 0
        else:
            return -1  # 数据库连接异常

# da = Data_Analyse()
# da.AverageTemp_Month('311')