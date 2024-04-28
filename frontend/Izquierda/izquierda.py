import dash
from dash import Dash, html, dcc, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import dash_html_components as html
from dash_table.Format import Format

#Importamos Backend

from backend.backend2 import cbr

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
            {'name':'Esfuerzo','id':'Esfuerzo','editable': False, 'type': 'numeric', 'format': Format(precision=3)},
            {'name':'CBR_1_%','id':'CBR_1_%','editable': False, 'type': 'numeric', 'format': Format(precision=2)},
            {'name':'CBR_2_%','id':'CBR_2_%','editable': False, 'type': 'numeric', 'format': Format(precision=2)},
            ],
        
         data= cbr.to_dict('records'),
        style_data={'fontSize': '16px', 'font-family': 'Calibri Light, sans-serif', 'textAlign': 'center','backgroundColor': '#f2f2f2', 'color': 'black'},  # Estilo para los datos
        style_header={'fontSize': '18px', 'font-family': 'Calibri Light, sans-serif', 'textAlign': 'center', 'backgroundColor': '#FFD700', 'color': 'black', "font-weight": "bold"},  # Estilo para los encabezados
    ),
   
    html.P("*Por favor ingrese los datos de Carga, Deformación y Area (el area corresponde por igual en cada dato)", style={"font-family": "Calibri Light, sans-serif"}),
    
])
