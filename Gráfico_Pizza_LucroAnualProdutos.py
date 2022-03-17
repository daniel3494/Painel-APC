import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output

df = pd.read_excel("https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Agricultura-valor-da-produo-brasil.xlsx?raw=true")

fig = px.pie(df, values="valor", names="produto",title="Lucro Anual dos Principais Produtos Agrícolas", hole= .3, color_discrete_sequence=px.colors.sequential.RdBu)

fig.show()