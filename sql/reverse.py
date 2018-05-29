# coding=utf-8

from sqlalchemy import create_engine
import pandas as pd
import json
import numpy as np

engine = create_engine("mysql://root:123456@192.168.1.15:3306/grm_production2?charset=utf8")
data = pd.read_sql(
    "select store_temp_layer, store_temp_breadth, store_temp_width, store_length, store_breadth , "
    "entry_time , entry_data from entry_temperature, "
    "store where entry_temperature.store_id = store.store_id and entry_temperature.store_id = 1 "
    "and entry_time='2017-01-05 13:00:05';", con=engine)
temp_width = data.loc[0, "store_temp_width"]  # x 行数
temp_layer = data.loc[0, "store_temp_layer"]  # 层数
temp_breadth = data.loc[0, "store_temp_breadth"]  # 列数

json_data = data.loc[0, 'entry_data']

breadth = float(data.loc[0, "store_length"][:-2])  # 去除 一个空格和 ‘ 米’ 长度
width = float(data.loc[0, "store_breadth"][:-2])  # 宽度

data_dict = json.loads(json_data, "utf-8")
r_list = data_dict['data']
# r_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
z = list()
index = 0
temp = index


# def reverse(temp):
#     nums = temp
#     for num in range(len(nums) / 2):
#         end = len(nums) - 1 - num
#         tmp = nums[num]
#         nums[num] = nums[end]
#         nums[end] = tmp
#     return nums


for k in range(temp_layer):
    r = np.zeros((temp_width, temp_breadth))
    for i in range(temp_width):
        for j in range(temp_breadth):
            if k % 2 == 0:
                r[i][j] = r_list[temp]
            else:
                r[temp_width - i - 1][j] = r_list[temp]
            temp += temp_layer * temp_width
        temp = index + i + 1
    index += temp_width
    temp = index
    z.append(r)

# for k in range(temp_layer):
#     r = np.zeros((temp_width, temp_breadth))
#     for i in range(temp_width):
#         for j in range(temp_breadth):
#             r[i][j] = r_list[temp]
#             temp += temp_width
#         temp = index + i + 1
#     index += temp_width * temp_breadth
#     temp = index
#     z.append(r)
print r_list[150:155]
print z[0]
