# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Painel-APC\Excelchips.xlsx")
fig = px.line(df, x='Datas', y='Preço', color='Categoria', markers=True)
    
app.layout = html.Div(children=[
    html.H1(children='Preços de Produtos dependentes de microchips', style={
        "textAlign": "center",
        "font-family": "Century Gothic",
        "color": "white"
    }),

    html.Div(children='Gráfico baseado em peços no ano de 2020', style={
        "textAlign": "center",
        "font-family": "Century Gothic",
        "color": "white"
    }),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
], style={
    "background-color": "#274472"
})

if __name__ == '__main__':
    app.run_server(debug=True)
