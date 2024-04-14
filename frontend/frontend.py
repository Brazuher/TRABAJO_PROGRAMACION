import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc

#Importar
from frontend.Derecha.derecha import derecha
from frontend.Izquierda.izquierda import izquierda


layout = dbc.Container([
    dbc.Row([
        dbc.Col('Izquierda', md=6, style={'background-color':'red'}),
        dbc.Col('Derecha', md=6, style={'background-color':'blue'}),
    ])
    
])