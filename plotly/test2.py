# coding=utf-8
import pandas as pd
from sqlalchemy import create_engine
from plotly.graph_objs import *
import json
import numpy as np
import plotly

engine = create_engine("mysql://root:123456@127.0.0.1:3306/grm_production2?charset=utf8")

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
    temp_z = np.full((temp_width, temp_breadth), (i + 1) * 1.5)  # 记录高度
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

cmax = np.max(temper)  # 返回一个最大的元素
# cmax == np.max(temper)  #　找到所有满足最大值的元素返回一个集合
# list = np.where(temper == cmax)　#　找到所有满足要求的元素的坐标
cmin = np.min(temper)  # 返回一个最小的元素

"""
颜色条

因为是绿色渐进到红色　
rgb　所占比为 (0,255,0) -> (255, 255,0) -> (255, 0, 0)
所以合成两个序列进行合并

cmax 即是温度矩阵中最大的值
cmin 即是温度矩阵中最小的值

Scatter3d 中 marker　各键值多对应选项的含义

color 指定各结点的权值　默认是温度 此处可以是字符串　如 'hot'　指定所有结点的颜色为 hot 但是当color　为数字数组时 colorscale启动
以权值所占百分比对应的颜色进行动态调节

colorscale　为结点权值在cmax与cmin区间之间百分比对应的颜色值 如下列形式

[[0,1 ,'rgb(255,255,0)'], [0,2 ,'rgb(255,200,0)']]


"""

color_scale = [[1.0 * _index / 510, 'rgb(' + str(_index) + ', 255, 0)'] for _index in range(0, 256, 1)]
color_scale += [[1.0 * _index / 510 + 0.5, 'rgb(255, ' + str(255 - _index) + ', 0)'] for _index in range(0, 256, 1)]

for temp in range(len(z)):
    line = temper[temp].reshape(1, temp_breadth * temp_width)[0]
    temp_trace = Scatter3d(
        x=x.reshape(1, temp_breadth * temp_width)[0],
        y=y.reshape(1, temp_breadth * temp_width)[0],
        z=z[temp].reshape(1, temp_breadth * temp_width)[0],
        showlegend=False,
        text=map(lambda _x: ' 温度' + str(_x) + ' ℃', line),
        mode='markers',
        marker=dict(  # 通过marker　设置　颜色
            color=line,  # 即各结点的权值　默认是温度
            colorscale=color_scale,
            showscale=True if temp == 0 else False,
            cmax=cmax,
            cmin=cmin,
        )
    )

    data.append(temp_trace)

# for temp in range(len(z)):
#     temp_trace = {
#         "x": x,
#         "y": y,
#         "z": z[temp],
#         'name': '第%d层温度变化' % (temp + 1, ),
#         "surfacecolor": temper[temp],
#         "colorbar": {"title": "温度与位置关系"},
#         "colorscale": "Hot",
#         "showscale": True if temp == 0 else False,
#         "type": "surface",
#     }
#     data.append(temp_trace)

layout = Layout(
    scene=dict(
        xaxis=dict(
            title='长度'
        ),
        yaxis=dict(
            title='宽度'
        ),
        zaxis=dict(
            title='高度'
        ),
    )
)

fig = Figure(data=data, layout=layout)
# plotly.offline.init_notebook_mode(connected=True)
# py.iplot(fig)
plotly.offline.plot(fig)
