from dash import html
import dash_bootstrap_components as dbc

derecha = dbc.Container([
    html.H1("Prueba"),
    html.H2("Dato de entrada"),
    html.H2("Grafica Esfurezo-Deformación")
])

derecha = dbc.Container([
    dbc.Row([
        dbc.Col('Datos de entrada', md=6, style={'background-color':'red'}),
        dbc.Col('Grafica esfuerzo deformación', md=6, style={'background-color':'blue'}),
    ])

])