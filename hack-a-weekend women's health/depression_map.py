# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 11:05:32 2018

@author: verascity
"""

import pandas as pd
import plotly.plotly as py

df = pd.read_csv('depressionstats.csv')

df = df[['Entity', 'Year', 'Code', 'Percentage of Female Suffering from Depression']]
df = df.rename(index=str, columns={'Entity':'Country',
           'Percentage of Female Suffering from Depression':'Fpct'})
df['Fpct'] = df['Fpct'].str.rstrip('%').astype('float')


df = df.loc[df['Year'].isin([2002, 2014])]
df = df.loc[df['Code'].str.len() == 3]


print(df)


#Skeleton cloropleth code from Plotly website
'''data = [ dict(
        type = 'choropleth',
        locations = df['CODE'],
        z = df['GDP (BILLIONS)'],
        text = df['COUNTRY'],
        colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            tickprefix = '$',
            title = 'GDP<br>Billions US$'),
      ) ]

layout = dict(
    title = '2014 Global GDP<br>Source:\
            <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
            CIA World Factbook</a>',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)

fig = dict( data=data, layout=layout )
py.iplot( fig, validate=False, filename='d3-world-map' )'''