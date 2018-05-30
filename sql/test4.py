# coding=utf-8

import pandas as pd
from sqlalchemy import create_engine
from plotly.graph_objs import *
import json
import plotly


engine = create_engine("mysql://root:123456@192.168.1.15:3306/grm_production2?charset=utf8")

store_id = 1

start_time = '2017-01-06 01:00:05'

end_time = '2017-02-06 21:00:05'

data = pd.read_sql(
    "select store_temp_layer, store_temp_breadth, store_temp_width, store_length, store_breadth ,entry_time , entry_data "
    "from grm_production2.entry_temperature, grm_production2.store where entry_temperature.store_id = store.store_id "
    "and entry_temperature.store_id = '{}' and entry_temperature.entry_time >= '{}' and entry_temperature.entry_time <= '{}';".format(store_id, start_time, end_time), con=engine)

line_num = len(data)

house_temp_list = list()
max_data_list = list()
min_data_list = list()
out_temp_list = list()
house_Mois_list = list()
out_Mois_list = list()
x = list()

for num in range(line_num):
    time = data.loc[num, 'entry_time']
    json_data = data.loc[num, 'entry_data']
    data_dict = json.loads(json_data, "utf-8")
    max_data = max(data_dict['data'])
    min_data = min(data_dict['data'])
    houseTemp = data_dict['houseTemp']
    houseMois = data_dict['houseMois']
    outTemp = data_dict['outTemp']
    outMois = data_dict['outMois']
    x.append(time)
    house_temp_list.append(houseTemp)
    house_Mois_list.append(houseMois)
    out_Mois_list.append(outMois)
    out_temp_list.append(outTemp)
    max_data_list.append(max_data)
    min_data_list.append(min_data)

trace0 = Scatter(  # 室温
    x=x,
    y=house_temp_list,
    name="室内温度"
)

trace1 = Scatter(  # 室外温度
    x=x,
    y=out_temp_list,
    name="室外温度"
)

trace2 = Scatter(  # 室外温度
    x=x,
    y=max_data_list,
    name="仓库最高温度"
)

trace3 = Scatter(  # 室外温度
    x=x,
    y=min_data_list,
    name="仓库最低温度"
)

x_axis_template=dict(
    showgrid=True,  # 网格
    zeroline=True,  # 是否显示基线,即沿着(0,0)画出x轴和y轴
    nticks=20,
    showline=True,
    title='时间',
    mirror='all'
)

y_axis_template=dict(
    showgrid=True,  # 网格
    zeroline=True,  # 是否显示基线,即沿着(0,0)画出x轴和y轴
    nticks=20,
    showline=True,
    title='温度 (℃)',
    mirror='all'
)

layout = Layout(
    xaxis=x_axis_template,
    yaxis=y_axis_template
)

data = Data([trace0, trace1, trace2, trace3])

fig = Figure(data=data, layout=layout)
plotly.offline.plot(fig)

