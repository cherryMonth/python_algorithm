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
    "and entry_temperature.store_id = 1 and entry_time > '2018-01-01 01:05:04';", con=engine)

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
    print len(temp[temp == None])
    print temp
    temper.append(temp)
    temp_z = np.full((temp_width, temp_breadth), (temp_layer - i - 1) * 1.5)  # 记录高度
    z.append(temp_z)

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
