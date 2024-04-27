from dash import Dash, html, Input, Output,dcc,State,dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd


#IMPORTAMOS LAS VARIABLES DE OTRAS CARPETAS
from frontend.Derecha.derecha import derecha
from frontend.Izquierda.izquierda import variable
from frontend.izquierdainferior.izquierdainf import izquierdainferior
from backend.backend2 import cbr
app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
miVariable = dbc.Container([
    html.H1("Texto 50"),
    html.H2("Subtexto"),
])

app.layout = dbc.Container (
    [
    html.H1('CÁLCULO DE CBR',  style={'background-color':'#FFD700','textAlign': 'center',"font-family": "Calibri Light, sans-serif", "font-weight": "bold", "font-size": "65px"}),
    dbc.Row([
        dbc.Col(derecha, md=4, style={'background-color':'#DCDCDC', "height":"100 vh", "padding": "20px"}),
        dbc.Col(variable, md=8, style={'background-color':'#F0E68C',"padding": "20px",'margin-left':'auto'}),
    
    
]),


html.H2(),
    dbc.Row([
        dbc.Col(izquierdainferior,md=12, style={'background-color': '#DCDCDC', 'margin-left':'auto',"padding":"20px"}),
    ]),
    
    ])


@app.callback(
    Output('Tabla_CBR','data'),
    Input('Tabla_CBR','data'),
    Input('Tabla_CBR', 'columns')
)

def update_cbr_table(rows, columns):
    cbr = pd.DataFrame(rows)
    cbr["Carga_(lbf)"] = cbr ["Carga_(lbf)"].astype("int")
    cbr["Esfuerzo"]= cbr["Carga_(lbf)"].astype(float) / cbr["Area_(pulg)"].astype(float)
    cbr["CBR_1_%"]= cbr["Esfuerzo"]/1000
    cbr["CBR_2_%"]= cbr["Esfuerzo"]/1500
    return cbr.to_dict('records') 

@app.callback(
        Output("cbr-plot","figure"),
        Input("Tabla_CBR", "data")

)

def update_cbr_plot(rows):

    cbr = pd.DataFrame(rows)

    trace = go.Scatter(
        x=cbr["Deformación_(pulg)"],
        y=cbr["Esfuerzo"],
        mode= 'lines',
        line=dict(color="blue", width=3),
        name= "Esfuerzo vs Deformación"
    )

    return {'data' : [trace]}



if __name__ == '__main__':
    app.run_server(debug=True)
    