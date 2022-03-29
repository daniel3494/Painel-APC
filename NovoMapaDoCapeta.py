# VERSÃO BETA V1.0 EM MAPA
# EDITADO EM 28/03 ÀS 23:55

import plotly.express as px
from pandas import read_excel
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

# DEFINIÇÃO DO BANCO DE DADOS:
df = read_excel('Painel-APC\Banco de Dados\Paises_exportadores_cafe.xlsx')
ListaDeFiltro = df.values

# LISTA DE TODOS OS PAÍSES DIVIDIDO POR CONTINENTES PARA SER UTILIZADO NO PASSSO MAIS ABAIXO:
Oceania = ['Estados Federados da Micronésia', 'Fiji', 'Ilhas Marshall', 'Ilhas Salomão', 'Kiribati' ,'Nauru', 'Nova Zelândia', 'Palau', 'Papua-Nova Guiné', 'Samoa', 'Tonga', 'Tuvalu', 'Vanuatu', 'Ilhas Cook']
América_do_Norte = ['Canadá', 'Estados Unidos da América', 'México']
América_Central = ['Antígua e Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Costa Rica', 'Cuba', 'Dominica', 'El Salvador', 'Granada', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica', 'Nicarágua', 'Panamá', 'República Dominicana', 'Santa Lúcia', 'São Cristóvão e Névis', 'São Vicente e Granadinas', 'Trindade e Tobago']
América_do_Sul = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Guiana Francesa', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela']
Europa = ['Albânia', 'Alemanha', 'Andorra', 'Áustria', 'Bélgica', 'Bielorrússia', 'Bósnia e Herzegovina', 'Bulgária', 'Cazaquistão', 'Chipre', 'Croácia', 'Dinamarca', 'Eslováquia', 'Eslovênia', 'Espanha', 'Estônia', 'Finlândia', 'França', 'Grécia', 'Hungria', 'Irlanda', 'Islândia', 'Itália', 'Letônia', 'Liechtenstein', 'Lituânia', 'Luxemburgo', 'Malta', 'Moldávia', 'Mônaco', 'Montenegro', 'Noruega', 'Países Baixos', 'Polônia', 'Portugal', 'Tchéquia', 'Macedônia do Norte', 'Inglaterra', 'Irlanda do Norte', 'Escócia', 'País de Gales', 'Romênia', 'Rússia', 'San Marino', 'Sérvia', 'Suécia', 'Suíça', 'Turquia', 'Ucrânia', 'Vaticano']
Ásia = ['Timor Leste', 'Birmânia', 'Afeganistão', 'Arábia Saudita', 'Armênia', 'Azerbaijão', 'Bahrein', 'Bangladesh', 'Brunei', 'Butão', 'Camboja', 'Cazaquistão', 'Catar', 'China', 'Chipre', 'Cingapura', 'Coreia do Norte', 'Coreia do Sul', 'Egito', 'Emirados Árabes', 'Filipinas', 'Geórgia', 'Iêmen', 'Índia', 'Indonésia', 'Irã', 'Iraque', 'Israel', 'Japão', 'Jordânia', 'Kuwait', 'Laos', 'Líbano', 'Malásia', 'Maldivas', 'Mianmar', 'Mongólia', 'Nepal', 'Omã', 'Paquistão', 'Quirguistão', 'Rússia', 'Síria', 'Sri Lanka', 'Tajiquistão', 'Tailândia', 'Timor-Leste', 'Turcomenistão', 'Turquia', 'Uzbequistão', 'Vietnã', 'Taiwan', 'República Popular da China']
África = ['África do Sul', 'Angola', 'Argélia', 'Benim', 'Botswana', 'Burquina Faso', 'Burundi', 'Camarões', 'Chade', 'Costa do Marfim', 'Djibouti', 'Egito', 'Eritreia', 'Etiópia', 'Gabão', 'Gâmbia', 'Gana', 'Guiné', 'Guiné-Bissau', 'Guiné Equatorial', 'Madagáscar', 'Cabo Verde', 'Comores', 'São Tomé e Príncipe', 'Seychelles', 'Lesoto', 'Libéria', 'Líbia', 'Malawi', 'Mali', 'Marrocos', 'Mauritânia', 'Moçambique', 'Namíbia', 'Níger', 'Nigéria', 'Quênia', 'República da África Central', 'República Democrática do Congo', 'República do Congo', 'República de Maurício', 'Ruanda', 'Senegal', 'Serra Leoa', 'Somália', 'Eswatini', 'Sudão', 'Sudão do Sul', 'Tanzânia', 'Togo', 'Tunísia', 'Uganda', 'Zâmbia', 'Zimbábue', 'República Popular do Congo']

# DISTRIBUIÇÃO DOS CONTINENTES AOS PAÍSES:
Novalista = []


for ln in ListaDeFiltro:
    for cont in Oceania:
        if ln[1] == cont:
            Novalista += [[ln[0], ln[1], ln[2],'Oceania']]

    for cont in América_do_Norte:
        if ln[1] == cont:
            Novalista += [[ln[0], ln[1], ln[2], 'América do Norte']]

    for cont in América_Central:
        if ln[1] == cont:
            Novalista += [[ln[0], ln[1], ln[2], 'América Central']]

    for cont in América_do_Sul:
        if ln[1] == cont:
            Novalista += [[ln[0], ln[1], ln[2], 'América do Sul']]

    for cont in Europa:
        if ln[1] == cont:
            Novalista += [[ln[0], ln[1], ln[2], 'Europa']]

    for cont in Ásia:
        if ln[1] == cont:
            Novalista += [[ln[0], ln[1], ln[2], 'Ásia']]

    for cont in África:
        if ln[1] == cont:
            Novalista += [[ln[0], ln[1], ln[2], 'África']]
    
# DEFINIÇÃO DA ORGANIZAÇÃO DO MAPA:
map_fig = px.scatter_geo(Novalista,
                         locations= 0,
                         projection= 'orthographic',
                         opacity= .8,
                         hover_name= 1,
                         color=3,
                         hover_data=[2]
)

# LAYOUT DO SITE:
app.layout = html.Div(children=[

    dcc.Graph(
        id='Grafico_dados',
        figure=map_fig
    )

]) 

if __name__ == '__main__':
    app.run_server(debug=True)