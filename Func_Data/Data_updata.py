from Dao import oper_database
import pandas as pd
import numpy as np

class Data_Updata():
    def Updata(self):
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            data = dc.UpdateWeaData()
            if data == -1:
                QMessageBox.critical(self, 'ERROR', 'API Error')
            elif data == 0:
                QMessageBox.critical(self, 'ERROR', 'Limit Error')
            else:
                # print(data)
                self.label_db_datetime.setText("更新前数据库截止日期为：" + data[0])
                self.label_newtime.setText("更新后数据库截止日期为：" + data[2])
                self.label_counttip.setText("数据更新条数：" + data[1])

        else:
            QMessageBox.critical(self, 'ERROR', '数据库连接异常')
