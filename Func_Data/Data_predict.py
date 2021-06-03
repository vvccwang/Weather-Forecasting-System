#中国科学院院士袁亚湘：一里路一里路把地面划分成几十亿个格子，每个点处的上方将大气划分成10-20层；最终有几百亿个点，每个点有不同的数据特征等；
import os
import time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)


import datetime
from Dao import oper_database
import pandas as pd
import numpy as np
from Func_Data import Data_quary
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow import keras

class Data_Predict():
    #获取数据：最高温、最低温、湿度
    #-1：数据库连接错误
    #list：数据列表
    def __init__(self):
        self.epochs = 700
        self.N = 7
    def GetData(self):
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            self.list = []
            datelist = dc.getDatesByTimes('2019-01-01', today)
            # print(datelist)
            for time in datelist:
                data = dc.QuaryWeaData('311', time)
                list_one = []
                # not none
                if data != -1:
                    # print(data)
                    temp = [t[2] for t in data]
                    hum = np.array([int(h[3]) for h in data])
                    aveh = int(np.average(hum))
                    # print(aveh)
                    temp.sort(reverse=True)
                    max = temp[0]
                    min = temp[len(temp) - 1]
                    list_one.append(int(max))
                    list_one.append(int(min))
                    list_one.append(aveh)
                    self.list.append(list_one)
            dc.closeDB()
        else:
            return -1

    #预测最高温
    #数据库错误：return 100
    def Predict_max(self):
        list=self.list
        if list == -1:
            return 100
        else:
            N = self.N
            X = []
            Y = []
            X_= []
            for i in range(N, len(list)-1):
                s = []
                for j in range(i - N, i):
                    s.append(list[j][0])
                X.append(s)
                Y.append(list[i][0])
            X_a = np.array(X)
            Y_a = np.array(Y)
            for j in range(len(list)-N-1,len(list)-1):
                X_.append(list[j][0])
            X_ = [X_]
            # 数据均值化
            min_max_scaler = MinMaxScaler()
            min_max_scaler.fit(X_a)
            x = min_max_scaler.transform(X_a)  # 均值化处理
            #预测所需最近七天数值
            x_ = min_max_scaler.transform(X_)  # 这里随便取一组数据，作为后面预测用，注意数据维度
            y = Y_a
            # 划分数据集,按训练集:测试集=8:2比例划分
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
            # 模型结构，采用relu函数为激活函数，输入层为N个属性
            # 下面为4层隐含层，每层的神经元个数依次为500，500，250，250
            # 输入层对应N个属性
            model = keras.Sequential([
                keras.layers.Dense(500, activation='relu', input_shape=[N]),
                keras.layers.Dense(500, activation='relu'),
                keras.layers.Dense(250, activation='relu'),
                keras.layers.Dense(250, activation='relu'),
                keras.layers.Dense(1)])  # 最后输出为一个结果，也就是预测的值
            # 定义损失函数loss，采用的优化器optimizer为Adam
            model.compile(loss='mean_absolute_error', optimizer='Adam')
            model.fit(x_train, y_train, batch_size=128, epochs=self.epochs) # 开始训练模型 # 训练700批次，每个批次数据量为126   梯度下降 126个样本作为一批次
            # 输出结果预测:对今天的预测
            y_ = model.predict(x_)
            return y_

    #预测最低温
    #数据库错误：return 100
    def Predict_min(self):

        list=self.list
        if list == -1:
            return 100
        else:
            N = self.N
            X = []
            Y = []
            X_= []
            for i in range(N, len(list)-1):
                s = []
                for j in range(i - N, i):
                    s.append(list[j][1])
                X.append(s)
                Y.append(list[i][1])
            X = np.array(X)
            Y = np.array(Y)

            for j in range(len(list)-N-1,len(list)-1):
                X_.append(list[j][1])
            X_ = [X_]
            # print(X_)

            # 数据均值化
            min_max_scaler = MinMaxScaler()
            min_max_scaler.fit(X)
            x = min_max_scaler.transform(X)  # 均值化处理
            #预测所需最近七天数值
            x_ = min_max_scaler.transform(X_)  # 这里随便取一组数据，作为后面预测用，注意数据维度
            y = Y
            # 划分数据集,按训练集:测试集=8:2比例划分
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
            # 模型结构，采用relu函数为激活函数，输入层为N个属性
            # 下面为4层隐含层，每层的神经元个数依次为500，500，250，250
            # 输入层对应N个属性
            model = keras.Sequential([
                keras.layers.Dense(500, activation='relu', input_shape=[N]),
                keras.layers.Dense(500, activation='relu'),
                keras.layers.Dense(250, activation='relu'),
                keras.layers.Dense(250, activation='relu'),
                keras.layers.Dense(1)])  # 最后输出为一个结果，也就是预测的值
            # 定义损失函数loss，采用的优化器optimizer为Adam
            model.compile(loss='mean_absolute_error', optimizer='Adam')
            # 开始训练模型
            model.fit(x_train, y_train, batch_size=128, epochs=self.epochs)  # 训练1000个批次，每个批次数据量为126   梯度下降 126个样本作为一批次
            # 输出结果预测
            y_ = model.predict(x_)
            return y_

    #预测最湿度
    #数据库错误：return 100
    def Predict_hum(self):

        list=self.list
        if list == -1:
            return 100
        else:
            N = self.N
            X = []
            Y = []
            X_= []
            for i in range(N, len(list)-1):
                s = []
                for j in range(i - N, i):
                    s.append(list[j][2])
                X.append(s)
                Y.append(list[i][2])
            X = np.array(X)
            Y = np.array(Y)

            for j in range(len(list)-N-1,len(list)-1):
                X_.append(list[j][2])
            X_ = [X_]
            # print(X_)

            # 数据均值化
            min_max_scaler = MinMaxScaler()
            min_max_scaler.fit(X)
            x = min_max_scaler.transform(X)  # 均值化处理
            #预测所需最近七天数值
            x_ = min_max_scaler.transform(X_)  # 这里随便取一组数据，作为后面预测用，注意数据维度
            y = Y
            # 划分数据集,按训练集:测试集=8:2比例划分
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
            # 模型结构，采用relu函数为激活函数，输入层为N个属性
            # 下面为4层隐含层，每层的神经元个数依次为500，500，250，250
            # 输入层对应N个属性
            model = keras.Sequential([
                keras.layers.Dense(500, activation='relu', input_shape=[N]),
                keras.layers.Dense(500, activation='relu'),
                keras.layers.Dense(250, activation='relu'),
                keras.layers.Dense(250, activation='relu'),
                keras.layers.Dense(1)])  # 最后输出为一个结果，也就是预测的值
            # 定义损失函数loss，采用的优化器optimizer为Adam
            model.compile(loss='mean_absolute_error', optimizer='Adam')
            # 开始训练模型
            model.fit(x_train, y_train, batch_size=128, epochs=self.epochs)  # 训练1000个批次，每个批次数据量为126   梯度下降 126个样本作为一批次
            # 输出结果预测
            y_ = model.predict(x_)
            return y_

    def Predict_tommorw(self):
        today_max=self.Predict_max()
        today_min=self.Predict_min()
        today_hum=self.Predict_hum()
        s=[today_max,today_min,today_hum]
        self.list.append(s)
        tom_max = self.Predict_max()
        tom_min = self.Predict_min()
        tom_hum = self.Predict_hum()
        tma = round(np.double(tom_max), 2)
        tmi = round(np.double(tom_min), 2)
        thu = round(np.double(tom_hum), 2)

        return [tma,tmi,thu]
