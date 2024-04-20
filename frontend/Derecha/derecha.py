from dash import html
import dash_bootstrap_components as dbc

derecha = dbc.Container([
    html.H1 ("Ensayo de CBR", style={'background-color':'#F0E68C','textAlign': 'center'}),
    html.H2("¿Qué es el CBR?"),
    html.P("El ensayo CBR (California Bearing Ratio o Relación de Soporte de California) es una prueba de laboratorio estandarizada que se utiliza para evaluar la resistencia y la capacidad de compactación de un suelo. Se realiza aplicando una carga controlada a una muestra de suelo compactada en un molde cilíndrico, y comparando la penetración del punzón con la de una piedra de referencia. El resultado se expresa como un porcentaje, denominado índice CBR, que representa la relación entre la resistencia del suelo y la de la piedra.", style={'textAlign': 'justify'}),
    html.H3("¿Para qué sirve un ensayo de CBR?"),
    html.P("En términos simples, el ensayo CBR nos dice qué tan bien un suelo puede soportar el peso de una estructura, como un pavimento o una carretera. Es una herramienta fundamental en la ingeniería civil para el diseño de cimentaciones y subrasantes", style={'textAlign': 'justify'}),

   
])
