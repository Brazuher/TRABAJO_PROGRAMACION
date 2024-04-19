from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

## formula cálculo a 0,1 pulgadas
derechainferior= dbc.Row([
         html.H1("Resultados de CBR", style={'background-color':'#F0E68C','textAlign': 'center'}),
            html.Label('Cálculo a 0,1 pulgadas'),
            dcc.Markdown('0,1"= deformación 0,1/1000psi'),
            dbc.Input(id = 'valor de la deformación', value = 1 , type = 'number'),
            html.Label(id = 'CBR 0,1"'),
            ]),
    
dbc.Row([
        dbc.Col('Datos de entrada', md=6, style={'background-color':'#FFD700'}),
        dbc.Col('Grafica esfuerzo deformación', md=6, style={'background-color':'white'}),
    ]),