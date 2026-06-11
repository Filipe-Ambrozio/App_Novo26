import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

st.title("🏠 Home")
st.markdown("### 📌 Atualizações da Aplicação")
st.success("📅 Atualização: data registrada e atualizada com sucesso.")
st.error("🚨 Erro previsto: correção futura em andamento. Observação em vermelho.")
st.warning("⚠️ Nova modificação/atualização: ver observação em amarelo.")
st.markdown(
    "[🔗 Acessar gráfico em BI](https://app.powerbi.com/view?r=eyJrIjoiOWQ0ZjBjZTMtZTYzNy00OTcyLWIwNjUtZWViZGQ0MWM0NjU2IiwidCI6ImU1MzA4M2Y2LTYwOWItNDQzMi05NmVkLWJjZGM2NmM1MjI2YSJ9)"
)
