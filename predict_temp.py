import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import datetime

from Dao import oper_database
import pandas as pd
import numpy as np
from Func_Data import Data_quary

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow import keras

da = Data_quary.Data_Quary()
today = datetime.datetime.now().strftime('%Y-%m-%d')
dc = oper_database.ConnectDB()
list = []
if dc.Error_flag == 0:
    datelist = dc.getDatesByTimes('2019-01-01',today)
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
            # print(hsum)
            temp.sort(reverse=True)
            max = temp[0]
            min = temp[len(temp) - 1]
            list_one.append(int(max))
            list_one.append(int(min))
            list_one.append(aveh)
            list.append(list_one)
    dc.closeDB()
print(len(list))
N=7

X=[]
Y=[]
for i in range(N,len(list)):
    s=[]
    for j in range(i-N,i):
        s.append(list[j][0])
    X.append(s)
    Y.append(list[i][0])
X=np.array(X)
Y=np.array(Y)
print(X)
print(Y)

#数据均值化
min_max_scaler = MinMaxScaler()
min_max_scaler.fit(X)
x = min_max_scaler.transform(X)#均值化处理
x_ = min_max_scaler.transform([[24.5,25.0,24.0,25.0,21.0,20.5,21.0]])#这里随便取一组数据，作为后面预测用，注意数据维度
y=Y
#划分数据集,按训练集:测试集=8:2比例划分
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2)
#模型结构，采用relu函数为激活函数，输入层为N个属性
#下面为4层隐含层，每层的神经元个数依次为500，500，250，250
#输入层对应N个属性
model = keras.Sequential([
        keras.layers.Dense(500,activation='relu',input_shape=[N]),
        keras.layers.Dense(500,activation='relu'),
        keras.layers.Dense(250,activation='relu'),
        keras.layers.Dense(250,activation='relu'),
        keras.layers.Dense(1)])#最后输出为一个结果，也就是预测的值
#定义损失函数loss，采用的优化器optimizer为Adam
model.compile(loss='mean_absolute_error',optimizer='Adam')
#开始训练模型
model.fit(x_train,y_train,batch_size = 126,epochs=1000)#训练1000个批次，每个批次数据量为126   梯度下降 126个样本作为一批次
#输出结果预测
y_=model.predict(x_)
print('预测结果为：',y_)

