import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Skills",
    page_icon="🏃🏼",
    layout="wide"
)

st.title("🛠️ Skills")

st.header("🚀 Tecnologias Principais")
tecnologias = [
    "Node.js", "Python", "TypeScript", "SQL (PostgreSQL, MySQL)", "NoSQL (MongoDB, Redis)",
    "GraphQL", "Kafka", "Docker", "Kubernetes", "AWS (Lambda, S3, DynamoDB)", "RabbitMQ",
    "Microservices", "Serverless", "Clean Architecture", "TDD"
]
st.write(" | ".join(tecnologias))

st.header("🔧 Ferramentas")
ferramentas = ["Git", "GitHub Actions", "JIRA", "VSCode", "Postman", "Grafana", "Prometheus", "Terraform"]
st.write(" | ".join(ferramentas))

st.header("🤝 Soft Skills")
soft_skills = [
    "Pensamento Crítico", "Resolução de Problemas", "Trabalho em Equipe", "Liderança Técnica",
    "Comunicação Eficiente", "Autogestão", "Aprendizado Contínuo", "Tomada de Decisão Baseada em Dados"
]
st.write(" | ".join(soft_skills))
