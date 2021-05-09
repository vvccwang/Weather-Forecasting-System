from Dao import oper_database
import pandas as pd
import numpy as np

class Data_Quary():
    def Quary_one(self,city,startdate):
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            onedata = dc.QuaryWeaData(city, startdate)
            dc.closeDB()
            if onedata == -1:
                return 0
                # 数据库无此数据
            else:
                list=[]
                for index, item in enumerate(onedata):
                    dlist=[]
                    dlist.append(item[1][11:])
                    dlist.append(item[5])
                    dlist.append(str(item[2]))
                    dlist.append(item[3])
                    if item[4] == '-1' or item[4] == '0':
                        dlist.append('暂无数据')
                    else:
                        dlist.append(item[4])
                    dlist.append(item[6])
                    dlist.append(item[7])
                    list.append(dlist)
                return list
        else:
            return -1
        # 数据库连接错误

    def Quary_many(self,city, startdate, enddate):
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            datelist = dc.getDatesByTimes(startdate, enddate)
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

                    wea = [w[5] for w in data]
                    wea = np.array(wea)
                    key = np.unique(wea)
                    result = {}
                    for k in key:
                        mask = (wea == k)
                        list_new = wea[mask]
                        v = list_new.size
                        result[k] = v
                    d_order = sorted(result.items(), key=lambda x: x[1], reverse=True)
                    wea_1 = d_order[0][0]
                    if len(d_order) > 1 and (
                            d_order[0][0].find('晴') != -1 or d_order[0][0].find('多云') != -1 or d_order[0][0].find(
                            '阴') != -1):
                        if (d_order[1][0].find('雨') != -1 or d_order[1][0].find('雪') != -1) and d_order[1][1] > 3:
                            wea_1 = d_order[1][0]
                        elif (d_order[1][0].find('霾') != -1 or d_order[1][0].find('雾') != -1) and d_order[1][1] > 5:
                            wea_1 = d_order[1][0]
                    dict['date'] = str(time)
                    dict['weather'] = wea_1
                    dict['max'] = str(max)
                    dict['min'] = str(min)
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
