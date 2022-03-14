import pandas as pd # Importação da biblioteca Pandas para ler arquivos externos, como o Banco de Dados. ("As pd" é uma renomeação para o Pandas)
import plotly.express as px # Importação do plotly para construção dos gráficos.
import streamlit as st # Importação do streamlit para facilitar na construção web.


# Configuração das características do site:
st.set_page_config(page_title="DashBoard - Criptomoedas",
                   page_icon=":coin:",
                   layout="wide")


# Chamada para pegar o banco de dados:
df = pd.read_csv("Projeto-APC\coin_Bitcoin.csv")

st.dataframe(df)

