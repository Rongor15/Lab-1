from dash import html, dcc, callback, Output, Input,dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
from data1 import df,counties
agg_df = df.groupby('region').agg({'points': 'sum', 'region_id': 'first'}).reset_index()
rusmap = px.choropleth_mapbox(
                        agg_df,
                        geojson=counties,
                        featureidkey='properties.name',
                        color='points',
                        locations='region',
                        color_continuous_scale=px.colors.sequential.Teal,
                        mapbox_style="carto-positron",
                        zoom=20,
                        # center = {'lat':55.755773, 'lon':37.617761},
                        opacity=0.5,
                        hover_name = 'region',
                        hover_data = {'region':True, 'region_id':False,'points':True},
                        labels={'region':'Субъект РФ'}
)
rusmap.update_layout(mapbox_style="carto-positron",
                        margin={"r":0,"t":0,"l":0,"b":0}, geo_scope='world',
                        mapbox_zoom=1, mapbox_center = {"lat": 66, "lon": 94}, height=500,
                        showlegend=False)
layout = dbc.Container([
    dbc.Row( [
        dbc.Col(
            html.Div([
                html.H3("Карта регионов Российской Федерации"),
                html.Hr(style={'color':'black'})
            ], style={'textAlign': 'center'})
        )
    ] ),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=rusmap)
        ],width=12)
    ]),
])