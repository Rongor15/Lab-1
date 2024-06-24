from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np
from data1 import df

layout = dbc.Container([
    html.Div([
        html.H1("Статистика по участникам"),
        ], style = {
            'backgroundColor': 'rgb(93, 138, 168)',
            'padding': '10px 5px'
        }),
        html.Div(
            dcc.Slider(
                id = 'crossfilter-year',
                min = df['year'].min(),
                max = df['year'].max(),
                value = 2009,
                step = None,
                marks = {str(year):
                    str(year) for year in df['year'].unique()}
                ),
            style = {'width': '95%', 'padding': '0px 20px 20px 20px'}
        ),
    html.Div(
        dcc.Graph(id='pie'),
        style={'width': '50%', 'display': 'inline-block'}
    ),
     html.Div(
        dcc.Graph(id='pie1'),
        style={'width': '50%','float': 'right',  'display': 'inline-block'}
    ),
    html.Div([
        html.Label('Выбери категорию участника:'),
        dcc.RadioItems(
            id='category-filter',
            options=[
                {'label': 'Победителей', 'value': 'winner'},
                {'label': 'Призеров', 'value': 'prize-winner'},
                {'label': 'Участников с похвальными грамотами', 'value': 'honourable mention'},
                {'label': 'Участников', 'value': 'participant'}
            ],
            value='winner',
            labelStyle={'display': 'inline-block'}
        ),
    ], style={'padding': '20px'}),
     html.Div(
        dcc.Graph(id='bar'),
        style={'width': '100%', 'display': 'inline-block'}
    ),
], fluid=True)
@callback(
    Output('pie', 'figure'),
    [Input('crossfilter-year', 'value')]
)
def update_pie(selected_year):
    filtered_df = df[df['year'] == selected_year]
    status_counts = filtered_df['status'].value_counts().reset_index()
    status_counts.columns = ['Статус', 'Количество']
    figure = px.pie(status_counts, names='Статус', values='Количество', title=f'Участники по статусу участника на год {selected_year}')
    return figure
@callback(
    Output('pie1', 'figure'),
    [Input('crossfilter-year', 'value')]
)
def update_pie(selected_year):
    filtered_df = df[df['year'] == selected_year]
    filtered_df1 = filtered_df[df['status_eng'] == 'winner']
    status_counts = filtered_df1['grade'].value_counts().reset_index()
    status_counts.columns = ['Класс', 'Количество']
    figure = px.pie(status_counts, names='Класс', values='Количество', title=f'Из какого класса победители на год {selected_year}')
    return figure
@callback(
    Output('bar', 'figure'),
    [Input('crossfilter-year', 'value'),Input('category-filter', 'value')]
)
def update_charts(selected_year, selected_category):
    filtered_df = df[df['year'] == selected_year]
    winners_df = filtered_df[filtered_df['status_eng'] == selected_category]
    school_counts = winners_df['school'].value_counts().reset_index().head(5)
    school_counts.columns = ['Школа', f'Количество {selected_category}']
    bar = px.bar(school_counts, x='Школа', y=f'Количество {selected_category}', title=f'Топ 5 школ по количеству {selected_category}')
    return bar