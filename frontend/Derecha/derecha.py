from dash import html
import dash_bootstrap_components as dbc

derecha = dbc.Container([
    html.H1("Prueba"),
    html.H2("Dato de entrada"),
    html.H2("Grafica Esfurezo-Deformación"),
    ## formula cálculo a 0,1 pulgadas
    html.Div([
            html.Label('Cálculo a 0,1 pulgadas'),
            dcc.Input(id = 'valor de la deformación', value = 1 , type = 'number'),
            html.Label(id = 'CBR 0,1"'),])
])

derecha = dbc.Container([
    dbc.Row([
        dbc.Col('Datos de entrada', md=6, style={'background-color':'red'}),
        dbc.Col('Grafica esfuerzo deformación', md=6, style={'background-color':'blue'}),
    ])

])