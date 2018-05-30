# Get this figure: fig = py.get_figure("https://plot.ly/~RPlotBot/3384/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~RPlotBot/3384/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="3", fileopt="extend")
# Get z data of first trace: z1 = py.get_figure("https://plot.ly/~RPlotBot/3384/").get_data()[0]["z"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *

trace1 = {
    "z": [
        [8.83, 8.92, 8.8, 8.91, 8.97, 9.2], [8.89, 8.93, 8.82, 8.95, 8.97, 9.23], [8.81, 8.91, 8.78, 8.94, 8.91, 9.2],
        [8.87, 8.79, 8.91, 8.74, 9.09, 8.99], [8.9, 8.85, 8.94, 8.81, 9.11, 8.99], [8.87, 8.79, 8.92, 8.76, 9.11, 8.98],
        [8.89, 8.9, 8.75, 8.93, 9.04, 9.18], [8.94, 8.94, 8.78, 8.98, 9.08, 9.2], [8.85, 8.92, 8.77, 8.99, 9.05, 9.19],
        [8.94, 8.79, 8.91, 8.89, 9.25, 8.93], [8.96, 8.88, 8.95, 8.99, 9.28, 8.97],
        [8.92, 8.81, 8.92, 8.92, 9.27, 8.97], [8.84, 8.9, 8.8, 9.1, 9, 9.18], [8.9, 8.95, 8.8, 9.13, 9.01, 9.2],
        [8.82, 8.92, 8.77, 9.11, 9, 9.1]],
        "colorbar": {
                        "ticklen": 2,
                        "title": "z<br>z2<br>z3"
                    },

                    "colorscale": [
    ["0", "rgba(68,1,84,1)"], ["0.0236220472440947", "rgba(69,11,91,1)"], ["0.0511811023622043", "rgba(71,22,100,1)"],
    ["0.0669291338582677", "rgba(71,27,105,1)"], ["0.074803149606299", "rgba(71,29,108,1)"],
    ["0.0905511811023624", "rgba(72,34,113,1)"], ["0.103346456692913", "rgba(72,38,117,1)"],
    ["0.173228346456693", "rgba(68,60,129,1)"], ["0.333333333333332", "rgba(49,104,142,1)"],
    ["0.41732283464567", "rgba(42,124,142,1)"], ["0.444881889763779", "rgba(38,130,142,1)"],
    ["0.460629921259843", "rgba(38,134,141,1)"], ["0.468503937007874", "rgba(38,136,141,1)"],
    ["0.483103674540682", "rgba(37,140,140,1)"], ["0.496062992125984", "rgba(37,143,140,1)"],
    ["0.566929133858268", "rgba(34,161,135,1)"], ["0.666666666666663", "rgba(53,183,121,1)"],
    ["0.811023622047245", "rgba(133,210,78,1)"], ["0.836614173228347", "rgba(149,214,69,1)"],
    ["0.854330708661418", "rgba(160,217,61,1)"], ["0.862204724409449", "rgba(165,218,58,1)"],
    ["0.875492125984253", "rgba(172,220,51,1)"], ["0.889763779527559", "rgba(181,222,44,1)"],
    ["0.956528871391076", "rgba(225,228,40,1)"], ["1", "rgba(253,231,37,1)"]],
                                                       "showscale": False,
                                                                    "type": "surface"
}
trace2 = {
    "z": [
        [9.83, 9.92, 9.8, 9.91, 9.97, 10.2], [9.89, 9.93, 9.82, 9.95, 9.97, 10.23],
        [9.81, 9.91, 9.78, 9.94, 9.91, 10.2], [9.87, 9.79, 9.91, 9.74, 10.09, 9.99],
        [9.9, 9.85, 9.94, 9.81, 10.11, 9.99], [9.87, 9.79, 9.92, 9.76, 10.11, 9.98],
        [9.89, 9.9, 9.75, 9.93, 10.04, 10.18], [9.94, 9.94, 9.78, 9.98, 10.08, 10.2],
        [9.85, 9.92, 9.77, 9.99, 10.05, 10.19], [9.94, 9.79, 9.91, 9.89, 10.25, 9.93],
        [9.96, 9.88, 9.95, 9.99, 10.28, 9.97], [9.92, 9.81, 9.92, 9.92, 10.27, 9.97], [9.84, 9.9, 9.8, 10.1, 10, 10.18],
        [9.9, 9.95, 9.8, 10.13, 10.01, 10.2], [9.82, 9.92, 9.77, 10.11, 10, 10.1]],
        "colorbar": {
                        "ticklen": 2,
                        "title": "z<br>z2<br>z3"
                    },
                    "colorscale": [
    ["0", "rgba(68,1,84,1)"], ["0.0236220472440947", "rgba(69,11,91,1)"], ["0.0511811023622043", "rgba(71,22,100,1)"],
    ["0.0669291338582677", "rgba(71,27,105,1)"], ["0.074803149606299", "rgba(71,29,108,1)"],
    ["0.0905511811023624", "rgba(72,34,113,1)"], ["0.103346456692913", "rgba(72,38,117,1)"],
    ["0.173228346456693", "rgba(68,60,129,1)"], ["0.333333333333332", "rgba(49,104,142,1)"],
    ["0.41732283464567", "rgba(42,124,142,1)"], ["0.444881889763779", "rgba(38,130,142,1)"],
    ["0.460629921259843", "rgba(38,134,141,1)"], ["0.468503937007874", "rgba(38,136,141,1)"],
    ["0.483103674540682", "rgba(37,140,140,1)"], ["0.496062992125984", "rgba(37,143,140,1)"],
    ["0.566929133858268", "rgba(34,161,135,1)"], ["0.666666666666663", "rgba(53,183,121,1)"],
    ["0.811023622047245", "rgba(133,210,78,1)"], ["0.836614173228347", "rgba(149,214,69,1)"],
    ["0.854330708661418", "rgba(160,217,61,1)"], ["0.862204724409449", "rgba(165,218,58,1)"],
    ["0.875492125984253", "rgba(172,220,51,1)"], ["0.889763779527559", "rgba(181,222,44,1)"],
    ["0.956528871391076", "rgba(225,228,40,1)"], ["1", "rgba(253,231,37,1)"]],
                                                       "opacity": 0.98,
                                                                  "showscale": False,
                                                                               "type": "surface"
}
trace3 = {
    "z": [
        [7.83, 7.92, 7.8, 7.91, 7.97, 8.2], [7.89, 7.93, 7.82, 7.95, 7.97, 8.23], [7.81, 7.91, 7.78, 7.94, 7.91, 8.2],
        [7.87, 7.79, 7.91, 7.74, 8.09, 7.99], [7.9, 7.85, 7.94, 7.81, 8.11, 7.99], [7.87, 7.79, 7.92, 7.76, 8.11, 7.98],
        [7.89, 7.9, 7.75, 7.93, 8.04, 8.18], [7.94, 7.94, 7.78, 7.98, 8.08, 8.2], [7.85, 7.92, 7.77, 7.99, 8.05, 8.19],
        [7.94, 7.79, 7.91, 7.89, 8.25, 7.93], [7.96, 7.88, 7.95, 7.99, 8.28, 7.97],
        [7.92, 7.81, 7.92, 7.92, 8.27, 7.97], [7.84, 7.9, 7.8, 8.1, 8, 8.18], [7.9, 7.95, 7.8, 8.13, 8.01, 8.2],
        [7.82, 7.92, 7.77, 8.11, 8, 8.1]],
        "colorbar": {
                        "ticklen": 2,
                        "title": "z<br>z2<br>z3"
                    },
                    "colorscale": [
    ["0", "rgba(68,1,84,1)"], ["0.0236220472440947", "rgba(69,11,91,1)"], ["0.0511811023622043", "rgba(71,22,100,1)"],
    ["0.0669291338582677", "rgba(71,27,105,1)"], ["0.074803149606299", "rgba(71,29,108,1)"],
    ["0.0905511811023624", "rgba(72,34,113,1)"], ["0.103346456692913", "rgba(72,38,117,1)"],
    ["0.173228346456693", "rgba(68,60,129,1)"], ["0.333333333333332", "rgba(49,104,142,1)"],
    ["0.41732283464567", "rgba(42,124,142,1)"], ["0.444881889763779", "rgba(38,130,142,1)"],
    ["0.460629921259843", "rgba(38,134,141,1)"], ["0.468503937007874", "rgba(38,136,141,1)"],
    ["0.483103674540682", "rgba(37,140,140,1)"], ["0.496062992125984", "rgba(37,143,140,1)"],
    ["0.566929133858268", "rgba(34,161,135,1)"], ["0.666666666666663", "rgba(53,183,121,1)"],
    ["0.811023622047245", "rgba(133,210,78,1)"], ["0.836614173228347", "rgba(149,214,69,1)"],
    ["0.854330708661418", "rgba(160,217,61,1)"], ["0.862204724409449", "rgba(165,218,58,1)"],
    ["0.875492125984253", "rgba(172,220,51,1)"], ["0.889763779527559", "rgba(181,222,44,1)"],
    ["0.956528871391076", "rgba(225,228,40,1)"], ["1", "rgba(253,231,37,1)"]],
                                                       "opacity": 0.98,
                                                                  "showscale": False,
                                                                               "type": "surface"
}
data = Data([trace1, trace2, trace3])
layout = {
    "margin": {
        "r": 10,
        "t": 25,
        "b": 40,
        "l": 60
    },
    "scene": {"zaxis": {"title": "z"}},
    "xaxis": {"domain": [0, 1]},
    "yaxis": {"domain": [0, 1]}
}
fig = Figure(data=data, layout=layout)
