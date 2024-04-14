import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc

#iMPORTAMOS ENLACES DE OTRAS CARPETAS
from frontend.Izquierda.izquierda import variable

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

miVariable = dbc.Container([
    html.H1("Texto 50"),
    html.H2("Subtexto"),
])

app.layout = dbc.Container([
    html.H1('Calculo de CBR'),
    dbc.Row([
        dbc.Col('CALCULO DE CBR', md=12, style={'background-color':'#FFD700'}),
        dbc.Col('Ensayo', md=6, style={'background-color':'#DCDCDC'}),
        dbc.Col('Datos de entrada', md=6, style={'background-color':'#F0E68C'}),
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)