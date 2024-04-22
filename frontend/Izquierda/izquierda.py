import dash
from dash import Dash, html, dcc, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import dash_html_components as html

#Importamos Backend
from backend.backend import cbr

#Layout

variable = dbc.Container([
    html.H1("DATOS DE ENTRADA", style={'background-color':'#DCDCDC','textAlign': 'center',"font-family": "Calibri Light, sans-serif", "font-weight": "bold"}),
    dash_table.DataTable(
        id='Tabla_CBR',
        columns=[
            {'name':'Lectura','id':'Lectura','editable': False},
            {'name':'Carga_(lbf)','id':'Carga_(lbf)','editable': True},
            {'name':'Deformación_(pulg)','id':'Deformación_(pulg)','editable': True},
            {'name':'Area_(pulg)','id':'Area_(pulg)','editable': True},
            {'name':'Esfuerzo','id':'Esfuerzo','editable': False},
            {'name':'CBR_1_%','id':'CBR_1_%','editable': False},
            {'name':'CBR_2_%','id':'CBR_2_%','editable': False},
            ],
         data= cbr.to_dict('records') 
    ),


    
])

@variable.callback(
    Output('Tabla_CBR','data'),
    Input('Tabla_CBR','data'),
    Input('tabla_cbr', 'columns')
)

def update_cbr_table(rows, columns):
    cbr = pd.DataFrame(rows)
    cbr["Carga"] = cbr ["Carga"].astype("int")
    cbr["Esfuerzo"]=cbr["Carga_(lbf)"].astype(float) / cbr["Area_(pulg)"].astype(float)
    return cbr.to_dict('records') 

izquierdainferior = dbc.Container([
        html.H1('Gráfica esfuerzo deformación', style={'background-color':'#F0E68C','textAlign': 'center',"font-family": "Calibri Light, sans-serif","font-weight": "bold"}),
    ]),

