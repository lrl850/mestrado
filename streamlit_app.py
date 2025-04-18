import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Navegação com Menu", layout="wide")

# Menu lateral
with st.sidebar:
    pagina = option_menu(
        "Menu",
        ["Home", "Sobre", "Contato", "Projeto", 
         "Curso Integrado em Eletroeletrônica",
         "Curso Integrado em Informática",
         "Curso Integrado em Administração"],
        icons=["house", "info", "envelope", "file-earmark-code", "database", "database", "database"],
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

# Página: Curso Integrado em Eletroeletrônica
elif pagina == "Curso Integrado em Eletroeletrônica":
    st.title("Análise do Curso Integrado em Eletroeletrônica")
    st.write("Bem-vindo à análise de tendências do curso!")

    # Corrigido: nomes dos arquivos sem espaços desnecessários
    df = pd.read_excel("eletro geral 2a.xlsx")
    df_resumido = pd.read_excel("total_eletro_resumido.xlsx")

    # Exibir dados
    st.subheader("Dados completos")
    st.dataframe(df)

    st.subheader("Dados resumidos")
    st.dataframe(df_resumido)

    # Gráfico interativo com escolha de colunas
    colunas = df.columns
    x_col = st.selectbox("Selecione a coluna para o eixo X", colunas)
    y_col = st.selectbox("Selecione a coluna para o eixo Y", colunas)

    if x_col and y_col:
        fig = px.line(df, x=x_col, y=y_col, title=f"Gráfico de {x_col} vs {y_col}")
        st.plotly_chart(fig)

    # Gráfico de tendência com dados resumidos
    st.subheader("Tendência: Matrículas, Retenção e Evasão")
    fig_tendencia = px.line(
        df_resumido,
        x='Ano/Período',
        y=['Alunos matriculado 1 ano', 'Alunos Total retido', 'Alunos Evadido'],
        title='Tendência no Curso de Eletroeletrônica',
        labels={'value': 'Número de Alunos', 'variable': 'Categoria'},
        color_discrete_map={
            'Alunos matriculado 1 ano': 'blue',
            'Alunos Total retido': 'orange',
            'Alunos Evadido': 'red'
        }
    )
    fig_tendencia.update_layout(
        xaxis_title='Ano/Período',
        yaxis_title='Quantidade de Alunos',
        hovermode='x unified',
        legend_title='Categorias'
    )
    st.plotly_chart(fig_tendencia)

    # Gráfico com Matplotlib
    anos = df_resumido['Ano/Período']
    entrada = df_resumido['Alunos matriculado 1 ano']
    retencao = df_resumido['Alunos Total retido']
    evasao = df_resumido['Alunos Evadido']
    total_matriculados = entrada + retencao

    plt.figure(figsize=(12, 6))
    plt.plot(anos, total_matriculados, marker='o', label='Total Matriculados')
    plt.plot(anos, retencao, marker='s', label='Retidos')
    plt.plot(anos, evasao, marker='^', label='Evadidos')

    plt.xlabel('Ano')
    plt.ylabel('Número de Alunos')
    plt.title('Tendência: Total Matriculados, Retenção e Evasão')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)

# Página: Curso Integrado em Informática
elif pagina == "Curso Integrado em Informática":
    st.title("Curso Integrado em Informática")
    st.write("Bem-vindo à página do curso técnico em Informática!")
    # Você pode adicionar gráficos e dados aqui

# Página: Curso Integrado em Administração
elif pagina == "Curso Integrado em Administração":
    st.title("Curso Integrado em Administração")
    st.write("Bem-vindo à página do curso técnico em Administração!")
    # Você pode adicionar gráficos e dados aqui
