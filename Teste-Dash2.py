# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from ast import Div
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd 
app = Dash(__name__) 


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_excel("https://github.com/Trabalho-APC-DASH/Painel-APC/blob/3b1946f9c34e8e7ca8ef6ad4b6e905e302f05969/Vendas_1.xlsx?raw=true")


fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

app.layout =html.Div(children=[

    html.Div(children=[
        html.H1(children='Covid', style={"textAlign": "center", "font-family": "Century Gothic"})
    ]),

    html.H2(children='Diferença de produção entre Bahia e Rio Grande do Sul'),

    html.Div(children='''
        T1
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
