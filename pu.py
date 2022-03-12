# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#282120',
    'text': '#F8EFE4'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_excel("Painel-APC\Excelchips.xlsx")

fig = px.line(df, x='Datas', y='Preço', color='Categoria', markers=True, height=580, text="Preço")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
    
app.layout = html.Div(style={'backgroundColor': "#282120"} ,children=[
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
])

if __name__ == '__main__':
    app.run_server(debug=True)
