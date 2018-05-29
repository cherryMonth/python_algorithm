# coding=utf-8
import pandas as pd
from sqlalchemy import create_engine
import plotly.plotly as py
from plotly.graph_objs import *
import json
import numpy as np
import plotly

engine = create_engine("mysql://root:123456@192.168.1.15:3306/grm_production2?charset=utf8")

data = pd.read_sql(
    "select store_temp_layer, store_temp_breadth, store_temp_width, store_length, store_breadth ,entry_time , entry_data "
    "from grm_production2.entry_temperature, grm_production2.store where entry_temperature.store_id = store.store_id "
    "and entry_temperature.store_id = 14 and entry_time > '2018-01-01 01:05:04';", con=engine)

line_num = 1

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
temp_list = np.array(r_list).reshape((temp_width, temp_layer, temp_breadth))

z = list()
for i in range(temp_layer):
    temper.append(temp_list[:, temp_layer - i - 1, :])  # 记录每层的温度
    temp_z = np.full((temp_width, temp_breadth), (temp_layer - i - 1) * 1.5)  # 记录高度
    z.append(temp_z)

trace1 = Scatter3d(
    x=x.reshape(1, temp_breadth * temp_width)[0],
    y=y.reshape(1, temp_breadth * temp_width)[0],
    z=z[0].reshape(1, temp_breadth * temp_width)[0],
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

trace2 = Scatter3d(
    x=x.reshape(1, temp_breadth * temp_width)[0],
    y=y.reshape(1, temp_breadth * temp_width)[0],
    z=z[1].reshape(1, temp_breadth * temp_width)[0],
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

trace3 = Scatter3d(
    x=x.reshape(1, temp_breadth * temp_width)[0],
    y=y.reshape(1, temp_breadth * temp_width)[0],
    z=z[2].reshape(1, temp_breadth * temp_width)[0],
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

trace4 = Scatter3d(
    x=x.reshape(1, temp_breadth * temp_width)[0],
    y=y.reshape(1, temp_breadth * temp_width)[0],
    z=z[3].reshape(1, temp_breadth * temp_width)[0],
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

tracea = {
    "x": x,
    "y": y,
    "z": z[0],
    "surfacecolor": temper[0],
    "colorbar": {"title": "温度与位置关系"},
    # "colorscale": [[0.0, '#171c42'], [0.07692307692307693, '#263583'],
    #                [0.15384615384615385, '#1a58af'], [0.23076923076923078, '#1a7ebd'],
    #                [0.3076923076923077, '#619fbc'], [0.38461538461538464, '#9ebdc8'],
    #                [0.46153846153846156, '#d2d8dc'], [0.5384615384615384, '#e6d2cf'],
    #                [0.6153846153846154, '#daa998'], [0.6923076923076923, '#cc7b60'],
    #                [0.7692307692307693, '#b94d36'], [0.8461538461538461, '#9d2127'],
    #                [0.9230769230769231, '#6e0e24'], [1.0, '#3c0911']],
    "type": "surface",
}
traceb = {
    "x": x,
    "y": y,
    "z": z[1],
    "surfacecolor": temper[1],
    "showscale": False,
    "type": "surface",
}
tracec = {
    "x": x,
    "y": y,
    "z": z[2],
    "showscale": False,
    "surfacecolor": temper[2],
    "type": "surface",
}
traced = {
    "x": x,
    "y": y,
    "z": z[3],
    "showscale": False,
    "surfacecolor": temper[3],
    "type": "surface",
}

data = [trace1, trace2, trace3, trace4, tracea, traceb, tracec, traced]
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
