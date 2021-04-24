from Dao import oper_database
import pandas
import numpy

class Data_Quary():
    def Quary_Max_Min_temp(self,cityid,startdatetime,enddatetime):
        db = oper_database.ConnectDB()
        data_list=db.QuaryWeaData(cityid,startdatetime,enddatetime)
        for i in data_list:
            # print(type(i[1]))
            print(i[1])
        pass
    def Quary_Sunny_Rain(self,cityid,startdatetime,enddatetime):
        pass
    def Quary_Hum(self,cityid,startdatetime,enddatetime):
        pass
    def Quary_Aqi(self,cityid,startdatetime,enddatetime):
        pass
    def Quary_Wind_Level(self,cityid,startdatetime,enddatetime):
        pass
dq=Data_Quary()
dq.Quary_Max_Min_temp('311','2021-4-15','2021-4-15')