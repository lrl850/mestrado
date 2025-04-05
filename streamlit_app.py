import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Navegação com Menu", layout="wide")

# Menu lateral
with st.sidebar:
    pagina = option_menu(
        "Menu",
        ["Home", "Sobre", "Contato", "Projeto", "DataLake"],
        icons=["house", "info", "envelope", "file-earmark-code", "database"],
        menu_icon="cast",
        default_index=0
    )

# Página: Home
if pagina == "Home":
    st.title("Página Inicial")
    st.write("Bem-vindo!")

# Página: Sobre
elif pagina == "Sobre":
    st.title("Sobre")
    st.write("Informações sobre o projeto.")

# Página: Contato
elif pagina == "Contato":
    st.title("Contato")
    st.write("Envie-nos uma mensagem.")

# Página: Projeto
elif pagina == "Projeto":
    st.title("Página do Projeto")
    st.write("Detalhes do projeto.")
<<<<<<< HEAD
    if st.button("Ir para DataLake"):
        st.session_state.pagina = "DataLake"
        st.experimental_rerun()

# Página: DataLake
elif pagina == "DataLake":
    st.title("Página DataLake")
    st.write("Bem-vindo à página DataLake!")
=======
    ### colocando o arquivo excel na página 
    def mostrar_pagina():
        st.title("Página DataLake")
        st.write("Bem-vindo à página DataLake!")
    # Adicione aqui o conteúdo específico da página DataLake
    
>>>>>>> 869feeab9f7c75d60f112684ab7f7fe0b99aa5ad

    arquivo = st.file_uploader("Envie um arquivo Excel", type=["xlsx"])
    if arquivo:
        try:
            df = pd.read_excel(arquivo)
            st.success("Arquivo carregado com sucesso!")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Erro ao ler o arquivo: {e}")
# teste commit