# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 15:46:25 2018

@author: verascity
"""

import pandas as pd
import numpy as np
import plotly.plotly as py

df = pd.read_csv('expenditurestats.csv')



'''data = [ dict(
        type = 'choropleth',
        locations = df['Code'],
        z = df['Trend'],
        text = df['Country'],
        colorscale = [[0,"rgb(24, 24, 24)"],[0.35,"rgb(44, 70, 39)"],[0.5,"rgb(64, 116, 55)"],\
            [0.6,"rgb(84, 162, 70)"],[0.7,"rgb(104, 208, 86)"],[1,"rgb(124, 255, 102)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(0,0,0)',
                width = 0.75
            ) ),
        colorbar = dict(
            autotick = False,
            ticksuffix = '%',
            title = 'Change in<br>Percentage'),
      ) ]

layout = dict(
    title = 'Global Trends in Population Statistics of Depressed Women, 2002-2014<br>(As Change in Percentage of total Female Population)',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)

fig = dict( data=data, layout=layout )
py.plot(fig, validate=False, filename='d1-world-map' )'''