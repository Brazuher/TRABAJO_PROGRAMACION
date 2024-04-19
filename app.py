import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

#IMPORTAMOS LAS VARIABLES DE OTRAS CARPETAS
from frontend.Derecha.derecha import derecha
from frontend.Izquierda.izquierda import variable
from frontend.derechainferior.derechainferior import derechainferior
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
miVariable = dbc.Container([
    html.H1("Texto 50"),
    html.H2("Subtexto"),
])

app.layout = dbc.Container (
    [
    html.H1('CÁLCULO DE CBR',  style={'background-color':'#FFD700','textAlign': 'center'}),
    dbc.Row([
        dbc.Col(derecha, md=4, style={'background-color':'#DCDCDC'}),
        dbc.Col(variable, md=8, style={'background-color':'#F0E68C'}),
        
    html.H2( style={'background-color':'#FFD700','textAlign': 'center'}),
    dbc.Col(derechainferior,md=4, style={'background-color':'#DCDCDC'})
    
])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
    