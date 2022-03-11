# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from ast import Div
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd 
app = Dash(__name__) 


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv("Painel-APC\owid-covid-latest.csv")


fig = px.bar(df, x="location", y="new_deaths")

app.layout =html.Div(children=[

    html.Div(children=[
        html.H1(children='Covid', style={"textAlign": "center", "font-family": "Century Gothic"})
    ]),

    html.H2(children='Número de Mortes por País', style={"textAlign": "center", "font-family": "Century Gothic"}),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
