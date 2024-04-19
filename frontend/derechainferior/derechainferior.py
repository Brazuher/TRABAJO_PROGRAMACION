from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

## formula cálculo a 0,1 pulgadas
derechainferior= dbc.Container([
         html.H1("Resultados de CBR", style={'background-color':'#F0E68C','textAlign': 'center'}),
            html.Label('Cálculo a 0,1 pulgadas'),
            dcc.Input(type='number', value=0, id="Esfuerzo en 0,1 pulgadas"),
            dcc.Markdown('0,1"= deformación 0,1/1000psi'),
            dcc.Input(type='number', value=0, id="Esfuerzo en 0,2 pulgadas"),
            dcc.Markdown('0,2"= deformación 0,2/1500psi'),
            ]),
    
