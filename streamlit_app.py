import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd


### importamdo dados excel
importa_dados = st.file_uploader("Carregar arquivo Excel", type=["xlsx"])
if importa_dados is not None:
    df = pd.read_excel(importa_dados, sheet_name=None)
    # Exibir os nomes das planilhas
    st.write("Planilhas disponíveis:")
    for sheet_name in df.keys():
        st.write(sheet_name)

    # Carregar uma planilha específica
    sheet_name = st.selectbox("Selecione uma planilha", df.keys())
    dados = df[sheet_name]
    
    # Exibir os dados da planilha selecionada
    st.write(f"Dados da planilha '{sheet_name}':")
    st.dataframe(dados)

### Configuração da página
with st.sidebar:
    pagina = option_menu("Menu", ["Home", "Sobre", "Contato","pagina do projeto"], 
                         icons=["house", "info", "envelope"],
                         menu_icon="cast", default_index=0)

if pagina == "Home":
    st.title("Página Inicial")
    st.write("Bem-vindo!")

elif pagina == "Sobre":
    st.title("Sobre")
    st.write("Informações sobre o projeto.")

elif pagina == "Contato":
    st.title("Contato")
    st.write("Envie-nos uma mensagem.")
elif pagina == "pagina do projeto":
    st.title("Página do Projeto")
    st.write("Detalhes do projeto.")

# fim configuração da página
