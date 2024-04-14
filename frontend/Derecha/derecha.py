from dash import html
import dash_bootstrap_components as dbc

derecha = dbc.Container([
    html.H1("¿Qué es el CBR?"),
    html.H2("¿Para qué sirve un ensayo de CBR?"),
    ## formula cálculo a 0,1 pulgadas
    html.Div([
            html.Label('Cálculo a 0,1 pulgadas'),
            dbc.Input(id = 'valor de la deformación', value = 1 , type = 'number'),
            html.Label(id = 'CBR 0,1"'),
            ]),
    
    dbc.Row([
        dbc.Col('Datos de entrada', md=6, style={'background-color':'#FFD700'}),
        dbc.Col('Grafica esfuerzo deformación', md=6, style={'background-color':'white'}),
    ]),
   
])
