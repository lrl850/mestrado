try:
    import streamlit as st
    import pandas as pd
    import numpy as np
except ModuleNotFoundError as e:
    print("Erro: O módulo necessário não está instalado. Tente instalar com `pip install streamlit pandas numpy`.")
    raise e

# Configuração da página
st.set_page_config(page_title="Meu App Streamlit", layout="wide")

# Título
st.title("Bem-vindo ao Meu App Streamlit!")

# Entrada de texto
nome = st.text_input("Digite seu nome:")
if nome:
    st.write(f"Olá, {nome}!")

# Botão
if st.button("Clique aqui"):
    st.write("Você clicou no botão!")

# Gerando dados fictícios
dados = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

# Exibindo o dataframe
st.write("### Dados Aleatórios")
st.dataframe(dados)

# Gráfico
st.line_chart(dados)

# Rodando no Streamlit
# Para rodar este script, salve como app.py e execute no terminal:
# pip install streamlit pandas numpy
# streamlit run app.py
