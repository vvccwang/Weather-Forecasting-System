from Dao import oper_database

class Func_Login():
    def Login(self,id,pwd):
        if id == '' or pwd == '':
            return 0     # 帐号或密码不能为空
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            f = dc.login(id, pwd)
            if f == 1:
                return 1
            elif f == -1:
                return -1
                # 密码错误
            else:
                return 2
                #账户不存在
        else:
            return -2
            # 数据库连接异常