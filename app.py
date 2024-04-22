import dash
from dash import html, dcc, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd


#IMPORTAMOS LAS VARIABLES DE OTRAS CARPETAS
from frontend.Derecha.derecha import derecha
from frontend.Izquierda.izquierda import variable
from frontend.derechainferior.derechainferior import derechainferior
from frontend.Izquierda.izquierda import izquierdainferior
from backend.backend import cbr
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
miVariable = dbc.Container([
    html.H1("Texto 50"),
    html.H2("Subtexto"),
])

app.layout = dbc.Container (
    [
    html.H1('CÁLCULO DE CBR',  style={'background-color':'#FFD700','textAlign': 'center',"font-family": "Calibri Light, sans-serif", "font-weight": "bold", "font-size": "65px"}),
    dbc.Row([
        dbc.Col(derecha, md=4, style={'background-color':'#DCDCDC', "height":"100 vh", "padding": "20px"}),
        dbc.Col(app, md=8, style={'background-color':'#F0E68C',"padding": "20px",'margin-left':'auto'}),
    
    
]),


html.H2(),
    dbc.Row([
        dbc.Col(izquierdainferior,md=12, style={'background-color': '#DCDCDC', 'margin-left':'auto',"padding":"20px"}),
    ]),
    
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
    