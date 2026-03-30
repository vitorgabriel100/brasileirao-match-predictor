import streamlit as st
import pandas as pd

from src.previsao import prever_resultado


df = pd.read_csv("data/jogos_tratados.csv")

times = sorted(set(df["mandante"]).union(set(df["visitante"])))


st.set_page_config(
    page_title="Previsão Brasileirão",
    page_icon="⚽",
    layout="centered"
)

st.title("⚽ Previsão de Resultado de Partida")
st.write("Escolha dois times e veja as probabilidades do confronto.")

mandante = st.selectbox("🏠 Time mandante", times)
visitante = st.selectbox("🛫 Time visitante", times)

if mandante == visitante:
    st.warning("⚠️ Escolha times diferentes.")
else:
    if st.button("Prever resultado"):
        resultado = prever_resultado(mandante, visitante)

        st.subheader("📊 Probabilidades")
        st.write(f"🏠 Vitória do mandante: {resultado.get('casa', 0):.2%}")
        st.write(f"🤝 Empate: {resultado.get('empate', 0):.2%}")
        st.write(f"🛫 Vitória do visitante: {resultado.get('fora', 0):.2%}")