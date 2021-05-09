import datetime

from Dao import oper_database
import pandas as pd
import numpy as np

class Data_Analyse():
    def Quary_many(self,city, flag):
        timelist=[30,90,180,365,730]
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
