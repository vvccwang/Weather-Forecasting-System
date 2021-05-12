import datetime



import Data_quary
from Dao import oper_database
import pandas as pd
import numpy as np

class Data_Analyse():
    #温度7/30天可视化
    def Quary_many(self,city, flag):
        timelist=[7,30]
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            datelist = dc.date_add(today,timelist[flag-1])
            # print(datelist)
            list = []
            for time in datelist:
                data = dc.QuaryWeaData(city, time)
                dict = {}
                # not none
                if data != -1:
                    temp = [t[2] for t in data]
                    temp.sort(reverse=True)
                    max = temp[0]
                    min = temp[len(temp) - 1]
                    dict['date'] = str(time)
                    dict['max'] = int(max)
                    dict['min'] = int(min)
                    # print(dict)
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
            datelist1 = dc.getDatesByTimes('2019-01-01','2019-12-31')
            datelist2 = dc.getDatesByTimes('2020-01-01','2020-12-31')
            datelist3 = dc.getDatesByTimes('2021-01-01', today)
            list1 = []
            list2 = []
            list3 = []
            for time in datelist1:
                data = dc.QuaryWeaData(city, time)
                dict = {}
                # not none
                if data != -1:
                    temp = [t[2] for t in data]
                    temp.sort(reverse=True)
                    max = temp[0]
                    min = temp[len(temp) - 1]
                    dict['date'] = str(time)
                    dict['max'] = int(max)
                    dict['min'] = int(min)
                    # print(dict)
                    list1.append(dict)
            for time in datelist2:
                data = dc.QuaryWeaData(city, time)
                dict = {}
                # not none
                if data != -1:
                    temp = [t[2] for t in data]
                    temp.sort(reverse=True)
                    max = temp[0]
                    min = temp[len(temp) - 1]
                    dict['date'] = str(time)
                    dict['max'] = int(max)
                    dict['min'] = int(min)
                    # print(dict)
                    list2.append(dict)

            for time in datelist3:
                data = dc.QuaryWeaData(city, time)
                dict = {}
                # not none
                if data != -1:
                    temp = [t[2] for t in data]
                    temp.sort(reverse=True)
                    max = temp[0]
                    min = temp[len(temp) - 1]
                    dict['date'] = str(time)
                    dict['max'] = int(max)
                    dict['min'] = int(min)
                    # print(dict)
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
        timelist = [7, 30]
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        today_last1 = today[:3]+'0'+today[4:]
        today_last2 = today[:2]+'19'+today[4:]
        # print(today_last1,today_last2)
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            #2019-2021三年的日期list
            datelist1 = dc.date_add(today, timelist[flag - 1])
            datelist2 = dc.date_add(today_last1, timelist[flag - 1])
            datelist3 = dc.date_add(today_last2, timelist[flag - 1])

            # print(len(datelist1),len(datelist2),len(datelist3))

            weatype = dc.wealist
            weatype = np.array(weatype)
            key = np.unique(weatype)

            result = {}
            for k in key:
                result[k] = 0
            # 统计一天中各个天气类型的数量
            for t in datelist1:
                data=dc.QuaryWeaData(city,t)
                if data != -1:
                    # print(1)
                    wea = [w[5] for w in data]
                    wea = np.array(wea)
                    for k in key:
                        mask = (wea == k)
                        list_new = wea[mask]
                        v = list_new.size
                        result[k] += v
            d_order1 = result
            # d_order1 = sorted(result.items(), key=lambda x: x[1], reverse=True)
            # print(d_order)

            result = {}
            for k in key:
                result[k] = 0
            for t in datelist2:
                data=dc.QuaryWeaData(city,t)
                if data != -1:
                    # print(2)
                    wea = [w[5] for w in data]
                    wea = np.array(wea)
                    for k in key:
                        mask = (wea == k)
                        list_new = wea[mask]
                        v = list_new.size
                        result[k] += v
            d_order2 = result

            result = {}
            for k in key:
                result[k] = 0
            for t in datelist3:
                data=dc.QuaryWeaData(city,t)
                if data != -1:
                    # print(3)
                    wea = [w[5] for w in data]
                    wea = np.array(wea)
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
                # 数据库无此数据
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
            # 统计一天中各个天气类型的数量
            for t in datelist1:
                data = dc.QuaryWeaData(city, t)
                if data != -1:
                    # print(1)
                    wea = [w[5] for w in data]
                    wea = np.array(wea)
                    for k in key:
                        mask = (wea == k)
                        list_new = wea[mask]
                        v = list_new.size
                        result[k] += v
            d_order1 = result
            # d_order1 = sorted(result.items(), key=lambda x: x[1], reverse=True)
            # print(d_order)

            result = {}
            for k in key:
                result[k] = 0
            for t in datelist2:
                data = dc.QuaryWeaData(city, t)
                if data != -1:
                    # print(2)
                    wea = [w[5] for w in data]
                    wea = np.array(wea)
                    for k in key:
                        mask = (wea == k)
                        list_new = wea[mask]
                        v = list_new.size
                        result[k] += v
            d_order2 = result

            result = {}
            for k in key:
                result[k] = 0
            for t in datelist3:
                data = dc.QuaryWeaData(city, t)
                if data != -1:
                    # print(3)
                    wea = [w[5] for w in data]
                    wea = np.array(wea)
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
