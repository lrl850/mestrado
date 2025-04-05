

arquivo_excel = "general.xlsx"

arquivo_excel = st.file_uploader("Escolha um arquivo Excel", type=["xlsx", "xls"])

if arquivo_excel is not None:
    df = pd.read_excel(arquivo_excel)
    st.write("📊 Dados do Excel:")
    st.dataframe(df)