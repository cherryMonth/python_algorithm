from plotly.graph_objs import *
import numpy as np
import plotly

temp_width = 2

temp_breadth = 2

temp_layer = 2

_x = [[0.0, 26.5], [0.0, 26.5]]

_y = [[0.0, 0.0], [17.4, 17.4]]

_z = [[[2, 6], [4, 8]], [[1, 5], [3, 7]]]

"""
[ 0.  26.5  0.  26.5]
[ 0.   0.  17.4 17.4]
"""

x = np.array(_x)
y = np.array(_y)
z = np.array(_z)


color_scale = [[1.0 * _index / 510, 'rgb(' + str(_index) + ', 255, 0)'] for _index in range(0, 256, 1)]
color_scale += [[1.0 * _index / 510 + 0.5, 'rgb(255, ' + str(255 - _index) + ', 0)'] for _index in range(0, 256, 1)]
trace = Scatter3d(x=x.reshape(1, temp_breadth * temp_width)[0], y=y.reshape(1, temp_breadth * temp_width)[0],
                  z=z[0].reshape(1, temp_breadth * temp_width)[0]
                  ,
                  showlegend=False,
                  text=z[0].reshape(1, temp_breadth * temp_width)[0],
                  mode='markers',
                  marker=dict(
                      color=z[0].reshape(1, temp_breadth * temp_width)[0],
                      colorscale=color_scale,
                      showscale=True,
                      cmax=8,
                      cmin=2,
                  )
                  )

plotly.offline.plot([trace])
