# VERSÃO FINAL V1.0 EM BARRAS
# ALTERADO EM 03/04 - 00:31

import plotly.express as px
from pandas import read_excel
from dash import Dash, dcc, html



app = Dash(__name__)

df = read_excel('UnidadesReceita.xlsx')
lista = df.values

opcoes1 = list(df['Unidades Receita Federal'])
opcoes1.insert(0, 'TODOS')

df2 = []
for n in lista:
    df2 += [[n[0], n[1], 'Importação Jan/Fev2022']]
    df2 += [[n[0], n[3], 'Exportação Jan/Fev2022']]
    df2 += [[n[0], n[5], 'Importação Jan/Fev2021']]
    df2 += [[n[0], n[7], 'Exportação Jan/Fev2021']]


fig = px.bar(df2, x=0, y=1, color=2, barmode="group", labels={
             '0': 'Unidade Da Receita Federal',
             '1': 'Sacas (60kg)',
             '2': 'Tipo'
            })

app.layout = html.Div(children=[

    dcc.Dropdown(opcoes1, value='Todos os Continentes', id='Filtro_Unidade', style={
        "border-radius": "30px",
        "background-color": "darkgrey"
    }),

    dcc.Graph(
        id='Grafico_dados',
        figure=fig
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)