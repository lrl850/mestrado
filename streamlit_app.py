import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
#pip install openpyxl




### Configuração da página
with st.sidebar:
    pagina = option_menu("Menu", ["Home", "Sobre", "Contato","pagina do projeto"], 
                         icons=["house", "info", "envelope"],
                         menu_icon="cast", default_index=0)

if pagina == "Home":
    st.title("Página Iniccial")
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
# teste o2 committtt