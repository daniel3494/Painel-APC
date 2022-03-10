# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from ast import Div
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd 
app = Dash(__name__) 


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Frutas": ["Maçãs", "Laranjas", "Bananas", "Soja", "Maçãs", "Laranjas", "Bananas","Soja"],
    "Quantidade": [100, 150, 650, 1000, 250, 100, 130, 2000],
    "Cidades": ["Bahia", "Bahia", "Bahia", "Bahia", "Santa Catarina", "Santa Catarina", "Santa Catarina", "Santa Catarina"]
})

fig = px.bar(df, x="Frutas", y="Quantidade", color="Cidades", barmode="group")

app.layout =html.Div(children=[

    html.Div(children=[
        html.H1(children='Test')
    ]),

    html.H1(children='Diferença de produção entre Bahia e Rio Grande do Sul'),

    html.Div(children='''
        Teste de-Mostragem de Dados 
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
