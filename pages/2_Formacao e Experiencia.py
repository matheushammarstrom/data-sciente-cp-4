import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Formação e Experiência",
    page_icon="🏃🏼",
    layout="wide"
)

st.title("📌 Formação e Experiência")

st.header("🎓 Formação Acadêmica")
st.write("**Bacharelado em Engenharia de Software**")
st.write("FIAP - [2027]")
st.write("Principais disciplinas: Estruturas de Dados, Algoritmos, Inteligência Artificial, Sistemas Distribuídos")

st.header("💼 Experiência Profissional")
experiencia = [
    {"Cargo": "Engenheiro de Software", "Empresa": "Operanex", "Período": "2024 - Presente", "Descrição": "Desenvolvimento de APIs escaláveis usando Node.js."},
    {"Cargo": "Desenvolvedor Backend", "Empresa": "Poliedro", "Período": "2022 - 2024", "Descrição": "Implementação de sistemas distribuídos e microservices."}
]

exp_df = pd.DataFrame(experiencia)
st.dataframe(exp_df, hide_index=True)


st.header("🗣️ Idiomas")
st.write("Fluente em **Português** e **Inglês**")

st.header("📬 Contato")
st.write("📧 Email: matheusfelippeh@gmail.com")
st.write("🔗 LinkedIn: [linkedin.com/in/matheushammarstrom](#)")
st.write("💻 GitHub: [github.com/matheushammarstrom](#)")