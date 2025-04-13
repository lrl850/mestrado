import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px 

# Configuração da página
st.set_page_config(page_title="Navegação com Menu", layout="wide")

# Menu lateral
with st.sidebar:
    pagina = option_menu(
        "Menu",
        ["Home", "Sobre", "Contato", "Projeto", 
         "Curso Integrado em Eletroeletrônica","Curso Integrado em Informática","Curso Integrado em Administração"],
       
        icons=["house", "info", "envelope", "file-earmark-code", "database","database","database"],
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
        

# Página: DataLake Curso Integrado em Eletroeletrônica"
elif pagina == "Curso Integrado em Eletroeletrônica":
    st.title("Página DataLake")
    st.write("Bem-vindo à página DataLake!")
    df = pd.read_excel("geral info.xlsx")
    DataFrame_eltro_resumido = pd.read_excel("Total eletro Resumido .xlsx")
    st.dataframe(df)
# criando  grafico interativo
    # Selecionar colunas para o gráfico
    colunas = df.columns
    x_col = st.selectbox("Selecione a coluna para o eixo X", colunas)
    y_col = st.selectbox("Selecione a coluna para o eixo Y", colunas)
    
    # Gerar o gráfico interativo
    if x_col and y_col:
         fig = px.line(df, x=x_col, y=y_col, title=f"Gráfico de {x_col} vs {y_col}")
         st.plotly_chart(fig)
# criando  grafico  do curso integrado em eletroeletrônica Resumido

    # Gerar gráfico de linhas interativo com Plotly Express (px)
    fig = px.line(df_long, x='Ano', y='Número de Alunos', color='Categoria',
              markers=True, title='Tendência: Total Matriculados, Retenção e Evasão (por Ano)')

    fig.update_layout(xaxis_title='Ano', yaxis_title='Número de Alunos', legend_title='Categoria')

# Salvar o gráfico como imagem usando Kaleido (alternativa: Matplotlib já foi feito)
# Como Kaleido não está disponível, salvamos novamente como imagem usando Matplotlib anteriormente
# Aqui apenas exibiríamos interativamente se possível, mas como isso falha, salvar novamente não é necessário

    fig.show()




# Página: DataLake Curso Integrado em Informática
elif pagina == "Curso Integrado em Informática":
    st.title("Página Curso Integrado em Informática")
    st.write("Bem-vindo à página Curso Integrado Tecnico em Informatica!")

# criando  grafico interativo do curso integrado em informatica
### poem seu codigo aqui
  
        
# Página : DataLake Curso Integrado em Administração
elif pagina == "Curso Integrado em Administração":
    st.title("Página Curso Integrado em Administração")
    st.write("Bem-vindo à página Curso Integrado Tecnico em Administração!")

# criando  grafico interativo do curso integrado em administração
### poem seu codigo aqui


# teste commit