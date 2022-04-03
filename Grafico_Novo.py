import plotly.express as px
from pandas import read_excel
from dash import Dash, dcc, html

df = read_excel('https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Consumo_cafe.xlsx?raw=true')
print(df)