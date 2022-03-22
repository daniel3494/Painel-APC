import plotly.express as px # Importação do Plotly para criar o design dos gráficos
from pandas import read_excel # Importação da função read_excel, para ler excel, da biblioteca Pandas
from dash import Dash, dcc, html, Input, Output
'''
A importação da biblioteca Dash fara a função da construção do layout do site em que os gráficos serão inseridos, dentre
as funções declaradas, temos:

@ Dash: Está servindo somente para colocar o site em funcionamento;

@ dcc: Função responsável por inserir o gráfico na página Web;

@ html: Função responsável por permitir organizar e criar um layout com nossa cara para o site, contudo ele não personaliza
o gráfico, somente a página web:

@ Input: Será utilizado mais a frente para que, dependendo de um gatilho disparada pelo usuário, algo será modificado na
página, neste caso, o input será a caixa de seleção (dropdown). O input será a origem do gatilho.

@ Output: Será utilizado mais a frente, este é o destinatário do gatilho efetuado pelo usuário, ou seja, a função que define
quem será alterado, neste caso o gráfico.
'''

app = Dash(__name__) # Isso aqui tem a função de colocar o site pra funcionar

# DECLARAÇÃO DO BANCO DE DADOS A SER UTILIZADO:
df = read_excel("https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Brasil-Exportacao_cafe_por_pais.xlsx?raw=true")

# ORGANIZAÇÃO DAS OPÇÕES PARA O DROPDOWN:
opcoes = list(df["CONTINENTE"].unique())
opcoes.insert(0, 'Todos os Continentes')
del opcoes[6]

'''
Nesta etapa, esta sendo efetuada as seguintes questões:

@ Primeiro é declarada a variável OPCOES, que fará uma lista (através da função 'list') das opções presentes na coluna
CONTINENTE do dataframe "df" (variável declarada para armazenar a leitura realizada pelo pandas na linha 25). A função
'unique()' logo adiante, tem como objetivo organizar esta lista sem repetir as opções que já foram escritas nela;

@ Na linha seguinte (Linha 29), é feito uma inserção na posição 0 dessa lista, cujo receberá uma string
'Todos os Continentes';

@ Na última linha, mandei deletar a informação da 6º posição, pois NO ARQUIVO do excel (banco de dados), a última linha é
nula, ou seja, não possui nada escrita nela e, por isso, estava sendo armazenada na lista um valor 'null' para representa-la.
Como ela não será útil, apaguei.
'''

# DECLARAÇÃO DE COMO O GRÁFICO IRÁ SER ORGANIZADO:
fig = px.bar(df, x="CONTINENTE", y="TOTAL", color="PAÍS DESTINO", height=900, width=700, text='PAÍS DESTINO', title='Exportação Brasileira por País')


# DECLARAÇÃO DO LAYOUT DA PÁGINA WEB COM HTML, CSS E O DCC:
app.layout = html.Div(children=[

    dcc.Dropdown(opcoes, value='Todos os Continentes', id='Filtro_Continentes', style={
        "border-radius": "30px",
        "background-color": "darkgrey"
    }),

    dcc.Graph(
        id='Grafico_dados',
        figure=fig
    )

])

'''
Nesta etapa temos:

@ Declaração do app.layout que indica o início na organização visual do site;

@ O html.div serve como uma divisão no HTML, para separar grupos de imagens, textos ou até mesmo uma mistura de ambas.
Basicamente é um bloco de informação dentro dela.

@ Quando criamos um bloco em que dentro dela terá mais informações, chamamos a origem de pai e as informações dispostas
em seu interior, ou originadas a partir desse bloco, de filhas ('Children'). A função div aqui no python precisa desse
parâmetro para que seja descritas as informações que ficarão dentro dela;


@ O dcc.Dropdown está criando, na página web, a tal caixa de seleção. Entre parênteses temos:

- Definição das opções que serão mostradas na caixa de seleção, neste caso, será a lista criada na linha 28 'OPCOES';

- O valor (value) inicial que a caixa de seleção estará selecionada.

- Um id para nomear essa função que, porém, será utilizadas para chamar ela mais tarde.

- O Style recebe um '={}', pois são propriedades de outra "Linguagem", por assim dizer, que é o CSS, responsável por
pequenas e grandes modificações na contrução web. Em resumo:

HTML: Funciona como ESQUELETO do site, ele define onde ficará o botão, a caixa de texto, a barra de navegação, a imagem,
o rodapé, e por aí vai.

CSS: Funciona como a MAQUIAGEM do site, ele define como será o botão, a fonte e cor da caixa de texto, o estilo da barra
de navegação, o tamanho e posição da imagem, etc.

- Sendo assim, estamos alterando 2 características do Dropdown em CSS: O Raio da borda (Border-Radius) para que as 
quinas da caixa de seleção fique redonda, e a Cor de Fundo do Dropdown (Background-Color) para Darkgrey;


@ Logo após criarmos o Dropdown e dar característicar à ela, temos o dcc.Graph, que só coloca a figura do gráfico que
fizemos na linha 48 no site.
'''

# DEFINIÇÃO PARA QUE A MUDANÇA, DEPENDENDO DO QUE ESTIVER SELECIONADO NO DROPDOWN, FUNCIONE:
@app.callback(
    Output('Grafico_dados', 'figure'),
    Input('Filtro_Continentes', 'value')
)
def update_de_dash(value):
    if value == "Todos os Continentes":
            
        fig = px.bar(df, x="CONTINENTE", y="TOTAL", color="PAÍS DESTINO", height=900, width=700, text='PAÍS DESTINO', title='Exportação Brasileira por País')
    
    else:

        tabela_filtrada = df.loc[df['CONTINENTE']==value, :]
        fig = px.bar(tabela_filtrada, x="CONTINENTE", y="TOTAL", color="PAÍS DESTINO", height=900, width=700, text='PAÍS DESTINO', title=f'Exportação: {value}')

    return fig

'''
Por último temos um callback e, logo embaixo, uma função.

@ O callback serve para conectar o Dropdown com o Gráfico com os seguintes parâmetros:


# INPUT: QUEM SERÁ O GATILHO PARA ALTERAÇÃO? 
Iremos definir essas informações após o parênteses:

- O nome (id) do objeto a ser o gatilho, este caso definimos ele como 'Filtro_Continentes', que é o nome da caixa de
seleção (dropdown);

- Após definirmos o nome do objeto a ser o gatilho, definimos o que exatamente funcionará como gatilho presente neste
objeto. Neste caso, será o 'value' selecionado na caixa de seleção.


# OUTPUT: QUEM SERÁ MODIFICADO PELO GATILHO?
Iremos definir essas informações após os parênteses:

- O nome (id) do objeto a ser modificado, este caso definimos ele como 'Gráfico_dados', que é o nome do dcc responsável
em inserir a figura do gráfico no site;

- Após definirmos o nome do objeto a ser o modificado, definimos o que exatamente será modificado neste dcc. 
Neste caso, será o 'figure' dele.


@ Agora criamos a função que dará o funcionamento dessa mudança. Usamos o def para iniciar a função e chamamos esse processo
de 'update_de_dash'.

@ Para que ele possa trabalhar, precisamos de um argumento para que seja usada na função: O valor (value) selecionado na
caixa de seleção (Dropdown). Conseguimos usar esse argumento graçãs ao callback que definiu isso para a gente.


@ Com o 'value' em mãos, a função irá avaliar: A opção selecionada no dropdown é "Todos os Continentes"?

# Se sim, a função só irá mostrar o gráfico de todos os continentes presentes na coluna CONTINENTES do dataframe 'df',
definido na linha 25;

# Se não, a função irá criar um novo dataframe a partir da filtragem do dataframe original. Para isso criamos uma variável
que irá armazenar essa filtragem, chamada 'tabela_filtrada'. Após o igual temos:

- O dataframe original a ser filtrada, neste caso será o 'df' lido pelo pandas na linha 25. (df.);

- Chamamos a função 'loc', que é responsável por filtrar uma tabela. (df.loc)

$ Entre parênteses do loc, temos:

- A coluna a ser filtrada, neste caso será a coluna 'CONTINENTES' do dataframe 'df'. (df[CONTINENTES]);

- Para que a mudança no gráfico esteja correta, é necessário que ele nos mostre somente os países presentes no continente
escolhido no 'value' da caixa de seleção (Dropdown), ou seja, a coluna CONTINENTES do dataframe 'df' deve ser igual ao
value do Dropdown. (df[CONTINENTES]==value).

@ Na linha abaixo (Linha 117), estamos redefinindo novamente a organização do gráfico, que irá sobre escrever a variável
fig, dessa vez, não pegaremos mais todas as linhas da coluna CONTINENTES, mas somente as filtradas pela função. Entre
parênteses o que muda é:

- Dataframe a ser utilizado, neste caso usaremos o dataframe filtrado 'Tabela_Filtrada'.
'''
# OUTRA VEZ, PARA MARCAR O FIM DA CONTRUÇÃO DO APP, E PARA DEIXAR O SITE FUNCIONANDO:
if __name__ == '__main__':
    app.run_server(debug=True)
