

arquivo_excel = "geral info.xlsx

# Lê o arquivo
df = pd.read_excel(arquivo_excel)

# Mostra os dados
st.dataframe(df)

if arquivo_excel is not None:
    df = pd.read_excel(arquivo_excel)
    st.write("📊 Dados do Excel:")
    st.dataframe(df)