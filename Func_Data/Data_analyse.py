import datetime

from Dao import oper_database
import pandas as pd
import numpy as np

class Data_Analyse():
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

