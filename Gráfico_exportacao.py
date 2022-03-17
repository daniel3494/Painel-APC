import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

df = pd.read_excel("NovoPainel_DASH\Banco de Dados\Brasil-Exportacao_cafe_por_pais.xlsx")
opcoes = list(df["CONTINENTE"].unique())

opcoes.insert(0, 'Todos os Continentes')
del opcoes[6]

fig = px.bar(df, x="CONTINENTE", y="CONILLON (Por sacas de 60kg)", color="PAÍS DESTINO", height=900, width=700, text='PAÍS DESTINO', title='Exportação Brasileira por País')

app.layout = html.Div(children=[

    dcc.Dropdown(opcoes, value='Todos os Continentes', id='Filtro_Continentes'),

    dcc.Graph(
        id='Grafico_dados',
        figure=fig
    )

])

@app.callback(
    Output('Grafico_dados', 'figure'),
    Input('Filtro_Continentes', 'value')
)
def update_output(value):
    if value == "Todos os Continentes":
            
        fig = px.bar(df, x="CONTINENTE", y="CONILLON (Por sacas de 60kg)", color="PAÍS DESTINO", height=900, width=700, text='PAÍS DESTINO', title='Exportação Brasileira por País')
    
    else:

        tabela_filtrada = df.loc[df['CONTINENTE']==value, :]
        fig = px.bar(tabela_filtrada, x="CONTINENTE", y="CONILLON (Por sacas de 60kg)", color="PAÍS DESTINO", height=900, width=700, text='PAÍS DESTINO', title='Exportação Brasileira por País')

        return fig

if __name__ == '__main__':
    app.run_server(debug=True)
