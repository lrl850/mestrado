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
    if st.button("Ir para DataLake"):
        st.session_state.pagina = "DataLake"
        

# Página: DataLake
elif pagina == "DataLake":
    st.title("Página DataLake")
    st.write("Bem-vindo à página DataLake!")
    df = pd.read_excel("geral info.xlsx")
    st.dataframe(df)

    
# teste commit