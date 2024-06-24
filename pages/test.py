from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np
from data1 import df

task_sums = df[['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8']].sum().reset_index()
task_sums.columns = ['Task', 'Scores']

bar_fig = px.bar(task_sums, x='Task', y='Scores', labels={'Task': 'Номер Задания', 'Scores': 'Очки'})
bar_fig.update_layout(title='Баллы за задания', xaxis_title='Номер Задания', yaxis_title='Очки')


layout = dbc.Container([
    html.Div([
        html.H1("Статистика по задачам"),
        ], style = {
            'backgroundColor': 'rgb(93, 138, 168)',
            'padding': '10px 5px'
        }),
    html.Div(
        dcc.Graph(figure=bar_fig),
        style={'width': '100%', 'float': 'right' , 'display': 'inline-block'}
    ),
    html.Div([
                html.Label('Номер задачи'),
                dcc.RadioItems(
                options = [
                    {'label':'№1', 'value': 'p1'},
                    {'label':'№2', 'value': 'p2'},
                    {'label':'№3', 'value': 'p3'},
                    {'label':'№4', 'value': 'p4'},
                    {'label':'№5', 'value': 'p5'},
                    {'label':'№6', 'value': 'p6'},
                    {'label':'№7', 'value': 'p7'},
                    {'label':'№8', 'value': 'p8'},
                ],
                id = 'crossfilter-ind',
                value = 'p1',
                labelStyle={'display': 'inline-block'}
                )
            ],
            style = {'width': '100%',  'float': 'right', 'display': 'inline-block'}),
    html.Div(
        dcc.Graph(id='histogram'),
        style={'width': '100%',  'display': 'inline-block'}
    ),
], fluid=True)
@callback(
    Output('histogram', 'figure'),
    [Input('crossfilter-ind', 'value')]
)
def update_histogram(task):
    figure = px.histogram(df, x='year', y=task, nbins=len(df['year']), labels={'year': 'Год', task: 'Очки'})
    figure.update_layout(title=f'Гистограмма баллов для номера {task}', xaxis_title='Год', yaxis_title='Очки')
    return figure






