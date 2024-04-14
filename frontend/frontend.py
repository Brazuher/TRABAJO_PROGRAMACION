import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col('Izquierda', md=6, style={'background-color':'red'}),
        dbc.Col('Derecha', md=6, style={'background-color':'blue'}),
    ])
    
])