from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from openpyxl import Workbook
wb = Workbook()


app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
wb.save("E:\Projetos-Estudos\APC\Painel-APC\Vendas.xlsx")
df = pd.read_excel("E:\Projetos-Estudos\APC\Painel-APC\Vendas.xlsx")

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)