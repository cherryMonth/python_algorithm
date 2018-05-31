# coding=utf-8
import pandas as pd
from sqlalchemy import create_engine
from plotly.graph_objs import *
import json
import numpy as np
import plotly

engine = create_engine("mysql://root:123456@192.168.1.15:3306/grm_production2?charset=utf8")

data = pd.read_sql(
    "select store_temp_layer, store_temp_breadth, store_temp_width, store_length, store_breadth ,entry_time , entry_data "
    "from grm_production2.entry_temperature, grm_production2.store where entry_temperature.store_id = store.store_id "
    "and entry_temperature.store_id = 14 and entry_time = '2018-01-01 01:05:04';", con=engine)

line_num = 0
temp_width = data.loc[line_num, "store_temp_width"]  # 行数
temp_layer = data.loc[line_num, "store_temp_layer"]  # 层数
temp_breadth = data.loc[line_num, "store_temp_breadth"]  # 列数

json_data = data.loc[line_num, 'entry_data']

breadth = float(data.loc[line_num, "store_length"][:-2])  # 去除 一个空格和 ‘ 米’ 长度
width = float(data.loc[line_num, "store_breadth"][:-2])  # 宽度

data_dict = json.loads(json_data, "utf-8")
r_list = data_dict['data']

temp_x = np.linspace(0, breadth, temp_breadth)
temp_y = np.linspace(0, width, temp_width)
(x, y) = np.meshgrid(temp_x, temp_y)
temper = list()

temp_list = np.array(r_list).reshape((temp_breadth, temp_width, temp_layer))

z = list()
for i in range(temp_layer):
    temp = temp_list[:, :, temp_layer - i - 1].transpose()  # 记录每层的温度
    temper.append(temp)
    temp_z = np.full((temp_width, temp_breadth), (temp_layer - i - 1) * 1.5)  # 记录高度
    z.append(temp_z)

miss_num = len(temper[temper == None])  # 缺失的数量

miss_percent = 1.0 * miss_num / (temp_layer * temp_width * temp_breadth) * 100  # 所占百分比


def replace_miss(matrix):

    """
    由于缺失值要取平均 因为在最外面的元素只能从内部或相邻的元素求平均,此时有5个(面上),3个(顶角),4个(棱上) 三种情况，需要分别考虑很麻烦；
    所以我构造了一个最外层全为0的矩阵 这样就不需要考虑该元素是不是最外层 只需要判断该元素是否缺失 然后从周围六个元素取平均即可

    :param matrix:
    :return:
    """

    temp_matrix = np.zeros((temp_layer + 2, temp_width + 2, temp_breadth + 2))
    for index in range(1, len(temp_matrix) - 1):
        temp_matrix[index][1:-1, 1:-1] = matrix[index - 1]

    for _i in range(temp_layer):
        for _j in range(temp_width):
            for _k in range(temp_breadth):
                if matrix[_i][_j][_k] is None:

                    """
                    如果结果为缺失 则用上下左右的值取平均替换 
                    matrix矩阵各元素与 temp_matrix 矩阵的下标各少1
                    即 matrix[_i][_j][_k] 等于 temp_matrix[_i + 1][_j + 1][_k + 1]
                    """

                    _temp = np.nansum(temp_matrix[_i][_j + 1][_k + 1] + temp_matrix[_i + 2][_j + 1][_k + 1])
                    _temp += np.nansum(temp_matrix[_i + 1][_j][_k + 1] + temp_matrix[_i + 1][_j + 2][_k + 1])
                    _temp += np.nansum(temp_matrix[_i + 1][_j + 1][_k] + temp_matrix[_i + 1][_j + 1][_k + 2])
                    matrix[_i][_j][_k] = round(_temp * 1.0 / 6, 2)


if miss_percent > 0.06:  # 若大于 6% 则用周围平均值代替
    replace_miss(temper)

data = list()

for temp in z:
    temp_trace = Scatter3d(
        x=x.reshape(1, temp_breadth * temp_width)[0],
        y=y.reshape(1, temp_breadth * temp_width)[0],
        z=temp.reshape(1, temp_breadth * temp_width)[0],
        mode='markers',
        showlegend=False,
        marker=dict(
            size=12,
            line=dict(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5
            ),
            opacity=0.8
        )
    )
    data.append(temp_trace)

for temp in range(len(z)):
    temp_trace = {
        "x": x,
        "y": y,
        "z": z[temp],
        "surfacecolor": temper[temp],
        "colorbar": {"title": "温度与位置关系"},
        "colorscale": "Hot",
        "showscale": True if temp == 0 else False,
        "type": "surface",
    }
    data.append(temp_trace)


layout = Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)

fig = Figure(data=data, layout=layout)
plotly.offline.plot(fig)
