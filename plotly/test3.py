# Learn about API authentication here: https://plot.ly/pandas/getting-started
# Find your api_key here: https://plot.ly/settings/api

from plotly.graph_objs import *
import pandas as pd
import plotly
import numpy as np

df = pd.read_csv('iris.csv')
df.head()

data = []
clusters = []
colors = ['rgb(228,26,28)', 'rgb(55,126,184)', 'rgb(77,175,74)']

for i in range(len(df['Name'].unique())):
    name = df['Name'].unique()[i]
    color = colors[i]
    x = df[df['Name'] == name]['SepalLength']
    y = df[df['Name'] == name]['SepalWidth']
    z = df[df['Name'] == name]['PetalLength']
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    print name
    print x

    trace = dict(
        name=name,
        x=x, y=y, z=z,
        type="scatter3d",
        mode='markers',
        marker=dict(size=3, color=color, line=dict(width=0)))
    data.append(trace)
layout = dict(
    width=800,
    height=550,
    autosize=False,
    title='Iris dataset',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        aspectratio=dict(x=1, y=1, z=0.7),
        aspectmode='manual',
        hovermode='closest',
    ),
)

fig = Figure(data=data, layout=layout)
# plotly.offline.init_notebook_mode(connected=True)
# py.iplot(fig)
plotly.offline.plot(fig)
