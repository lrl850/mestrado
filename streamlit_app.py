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
    df = pd.read_excel("eletro  Geral - 2 a.xlsx")
    DataFrame_eltro_resumido = pd.read_excel("Total eletro Resumido .xlsx")
    st.dataframe(df)
    st.dataframe(DataFrame_eltro_resumido)
# import streamlit as st
import plotly.express as px

# Criando gráfico interativo
colunas = df.columns
x_col = st.selectbox("Selecione a coluna para o eixo X", colunas)
y_col = st.selectbox("Selecione a coluna para o eixo Y", colunas)

# Gerar o gráfico interativo
if x_col and y_col:
    fig = px.line(df, x=x_col, y=y_col, title=f"Gráfico de {x_col} vs {y_col}")
    st.plotly_chart(fig)

# Criando gráfico de tendência para o curso integrado em eletroeletrônica
st.subheader("Análise do Curso Integrado import streamlit as st em Eletroeletrônica")
import pandas as pd
import plotly.express as px

# Página: DataLake Curso Integrado em Eletroeletrônica
elif pagina == "Curso Integrado em Eletroeletrônica":
    st.title("Análise do Curso Integrado em Eletroeletrônica")
    st.write("Bem-vindo à análise de tendências do curso!")

    # Carregar os dados do Excel
    df = pd.read_excel("eletro  Geral - 2 a.xlsx")
    DataFrame_eltro_resumido = pd.read_excel("Total eletro Resumido .xlsx")

    # Exibir os dados carregados
    st.dataframe(DataFrame_eltro_resumido)

    # Criar gráfico de tendência com Plotly Express
    fig_tendencia = px.line(
        DataFrame_eltro_resumido,
        x='Ano/Período',
        y=['Alunos matriculado 1 ano', 'Alunos Total retido', 'Alunos Evadido'],
        title='Tendência: Matrículas, Retenção e Evasão no Curso de Eletroeletrônica',
        labels={'value': 'Número de Alunos', 'variable': 'Categoria'},
        color_discrete_map={
            'Alunos matriculado 1 ano': 'blue',
            'Alunos Total retido': 'orange',
            'Alunos Evadido': 'red'
        }
    )

    # Melhorar a formatação do gráfico
    fig_tendencia.update_layout(
        xaxis_title='Ano/Período',
        yaxis_title='Quantidade de Alunos',
        hovermode='x unified',
        legend_title='Categorias'
    )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig_tendencia)
# Dados para o gráfico de linhas
anos = DataFrame_eltro_resumido['Ano/Período']
entrada = DataFrame_eltro_resumido['Alunos matriculado 1 ano']
retencao = DataFrame_eltro_resumido['Alunos Total retido']
evasao = DataFrame_eltro_resumido['Alunos Evadido']

# Criar gráfico de linhas interativo
fig_curso = px.line(
    DataFrame_eltro_resumido,
    x='Ano/Período',
    y=['Alunos matriculado 1 ano', 'Alunos Total retido', 'Alunos Evadido'],
    title='Tendência: Matrículas, Retenção e Evasão no Curso de Eletroeletrônica',
    labels={'value': 'Número de Alunos', 'variable': 'Categoria'},
    color_discrete_map={
        'Alunos matriculado 1 ano': 'blue',
        'Alunos Total retido': 'orange',
        'Alunos Evadido': 'red'
    }
)

# Melhorar formatação do gráfico
fig_curso.update_layout(
    xaxis_title='Ano/Período',
    yaxis_title='Quantidade de Alunos',
    hovermode='x unified',
    legend_title='Categorias'
)

# Exibir gráfico
st.plotly_chart(fig_curso)


        # Criar gráfico de linhas para visualizar a tendência de cada grupo ao longo dos anos
        plt.figure(figsize=(12, 6))
        # Definir total_matriculados como a soma das colunas relevantes
        total_matriculados = DataFrame_eltro_resumido['Alunos matriculado 1 ano'] + DataFrame_eltro_resumido['Alunos Total retido']
        
        plt.plot(anos, total_matriculados, marker='o', label='Total Matriculados')
        plt.plot(anos, retencao, marker='s', label='Retidos')
        plt.plot(anos, evasao, marker='^', label='Evadidos')

        plt.xlabel('Ano')
        plt.ylabel('Número de Alunos')
        plt.title('Tendência: Total Matriculados, Retenção e Evasão (por Ano)')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)  # Exibir o gráfico no Streamlit
        # Salvar o gráfico como imagem usando Matplotlib
    

# Salvar o gráfico como imagem usando Kaleido (alternativa: Matplotlib já foi feito)
# Como Kaleido não está disponível, salvamos novamente como imagem usando Matplotlib anteriormente
#Aqui apenas exibiríamos interativamente se possível, mas como isso falha, salvar novamente não é necessário

   # fig.show()
    # Gerar gráfico com Matplotlib e salvar como imagem
    plt.figure(figsize=(12, 6))
    plt.plot(anos, total_matriculados, marker='o', label='Total Matriculados')
    plt.plot(anos, retencao, marker='s', label='Retidos')
    plt.plot(anos, evasao, marker='^', label='Evadidos')

    plt.xlabel('Ano')
    plt.ylabel('Número de Alunos')
    plt.title('Tendência: Total Matriculados, Retenção e Evasão (por Ano)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()

    # Salvar imagem
    #image_path = '/mnt/data/grafico_linhas_matriculados_retencao_evasao.png'
    #plt.savefig(image_path)
    plt.show()

    #image_path



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