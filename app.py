import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# Titulo da pagina e faviicon
st.set_page_config(
    page_title="Monitoramente CodepipeLine",
    # page_icon=":bar_chart:",
    page_icon=":world_map:",
    layout="wide"
)

# Chamada dos dados geral 
df = pd.read_csv('./data/data.csv')
#print(df)

# Chamada dos dados geral 
df_list = pd.read_csv('./data/data2.csv')
#print(df_list)

# ---- SIDEBAR ----
st.sidebar.header("Filtros:")
status_select = st.sidebar.multiselect(
    "Selecione o Status:",
    options=df["status"].unique(),
    default=df["status"].unique()
)


df_selection = df.query(
    "status == @status_select"
)
df_selection["num_conta"] = df_selection['num_conta'].astype(str)
# ---- Titudo da pagina principal  ----
st.title(":world_map: Monitorameto CodepipeLine")
st.markdown("##")


# checando se o dataframe com o filtro esta vazio:
if df_selection.empty:
    st.warning("Nenhum dado encontrado na busca!")
    st.stop()  # realizar stop no caso de alguma execução.
df_fail = df[(df['status'] == 'FAILED')]
df_suces = df[(df['status'] == 'SUCCEEDED')]


# Resumo geral das informacoes do dataframe
total_accounts = len(df["num_conta"].unique())
total_fail = df_fail['status'].count()
total_suces = df_suces['status'].count()


check_icon = ":warning:" * int(1)
error_icon = ":warning:" * int(1)
warni_icon = ":warning:" * int(1)


left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Contas Consumer:")
    st.subheader(f"{total_accounts} {check_icon}")
with middle_column:
    st.subheader("Contas c/ Falhas:")
    st.subheader(f"{total_fail} {error_icon}")
with right_column:
    st.subheader("Contas c/ Sucesso:")
    st.subheader(f"{total_suces}{warni_icon}")

st.markdown("""---""")


# plot do dataframe
st.dataframe(df_selection)

df1 = df["num_conta"].copy()
df2 = df_list["num_conta"].copy()
df_new = pd.concat([df1, df2]).drop_duplicates(keep=False)

st.title(":warning: Contas não iniciadas")
st.dataframe(df_new)
