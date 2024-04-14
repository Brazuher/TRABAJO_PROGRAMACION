import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Col('Izquierda', md=6, style={'bacjground-color':'red'}),
    dbc.Col('Derecha', md=6, style={'bacjground-color':'red'}),
])