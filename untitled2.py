# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q83uBOwL5E0-gMfERZM4cbpzZpWKrXrK
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import plotly.express as pr
import plotly.graph_objects as go

df = pd.read_csv('/content/drive/MyDrive/project_dataset.csv (1).xls')

df

df1 = df.copy()

df1.head()

df1.head(10)

df1.head(60)

df1.shape

df1.columns

df1.dtypes

df1.info()

df1.describe()

df1.duplicated()

df1.isna()

df1.isna().sum()

df1.isna().sum()/df1.shape[0]

df1.dropna(axis = 1,inplace = True)

df1.dtypes

df1

df1.dtypes

df1.shape

data = df1.sample(n = 500, random_state = 42)

data

data.shape
data.columns
data.head()
data.tail

data.count()

data = data.drop(['Unnamed: 0'], axis = 1)

data.shape

data

fig = go.Figure(data =go.Scatter(x=df['Distance'], y =df['DepTime'],mode='markers',marker=dict(color='red')))

#fig.update_layout(title='Scatter plot for Distance vs Departure time', xaxis_title = 'Distance', yaxis_title='Deparure')

fig.update_layout(title='Scatter plot for Distance vs Departure time', xaxis_title = 'Distance', yaxis_title='Deparure')
fig.show()

line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

line_data

fig = go.Figure(data =go.Scatter(x=df['Month'], y =df['ArrDelay'],mode='lines',marker=dict(color='green')))
fig.update_layout(title='Monthly average delay plot for an year', xaxis_title = 'Months', yaxis_title='Delay of Flights (in minuts)')
fig.show()

bar_data = df.groupby('DestState')['Flights'].sum().reset_index()
bar_data

fig = pr.bar(bar_data, x ='DestState', y = 'Flights' , title = 'Total numbers of flights from each destination states')
fig.show()

bub_data = df.groupby('Reporting_Airline')['Flights'].sum().reset_index()

