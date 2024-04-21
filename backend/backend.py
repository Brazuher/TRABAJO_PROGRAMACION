import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

Lectura=[ #Para cada lectura
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]

Carga=[
    "17.76",
    "23.60",
    "32.59",
    "37.99",
    "43.38",
    "50.80",
    "56.20",
    "62.49",
    "69.01",
    "76.88"
]

Deformacion=[
    "0.023",
    "0.093",
    "0.162",
    "0.224",
    "0.286",
    "0.363",
    "0.440",
    "0.502",
    "0.564",
    "0.626"
]

Area=[
   "28.27",
   "28.27",
   "28.27",
   "28.27",
   "28.27",
   "28.27",
   "28.27",
   "28.27", 
   "28.27",
   "28.27",
   "28.27",
]

cbr= pd.DataFrame({ #Creamos Dataframe del CBR
    "Lectura": Lectura,
    "Carga_(lbf)": Carga,
    "Deformación_(pulg)": Deformacion,
    "Area_(pulg)": Area
})

cbr[""]