import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import norm, poisson

st.title("Distribuições Probabilísticas Aplicadas aos Dados da NFL")

st.write("""
Neste dashboard, aplicamos duas distribuições probabilísticas aos dados:
- **Distribuição Normal para WTS (pontuação do time vencedor):**  
  *Justificativa:* Em virtude do Teorema Central do Limite, quando lidamos com um grande número de jogos, a distribuição dos pontos tende a se aproximar de uma distribuição normal. Assim, a variável WTS pode ser bem modelada por uma normal, permitindo a estimação de intervalos de confiança e a realização de testes estatísticos.
- **Distribuição de Poisson para LTS (pontuação do time perdedor):**  
  *Justificativa:* Como LTS representa um dado discreto (contagem de pontos) e muitos jogos podem ter pontuações baixas ou até nulas para o time perdedor, a distribuição de Poisson é adequada para modelar a frequência desses eventos discretos em intervalos fixos.
""")

df = pd.read_csv("nfl.csv")
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

st.header("Distribuição Normal aplicada a WTS (Time Vencedor)")
wts = df['WTS']
wts_mean = wts.mean()
wts_std = wts.std()

st.write(f"**Média (μ):** {wts_mean:.2f}")
st.write(f"**Desvio Padrão (σ):** {wts_std:.2f}")

nbins_normal = 30
fig_norm = px.histogram(wts, nbins=nbins_normal, title="Histograma de WTS com Curva Normal Ajustada",
                        labels={'value': 'WTS', 'count': 'Frequência'})

x_vals = np.linspace(wts.min(), wts.max(), 100)
pdf_vals = norm.pdf(x_vals, loc=wts_mean, scale=wts_std)

bin_width = (wts.max() - wts.min()) / nbins_normal
pdf_scaled = pdf_vals * len(wts) * bin_width

fig_norm.add_scatter(x=x_vals, y=pdf_scaled, mode='lines', name='Distribuição Normal Ajustada')
st.plotly_chart(fig_norm)

st.header("Distribuição de Poisson aplicada a LTS (Time Perdedor)")
lts = df['LTS']
lambda_lts = lts.mean()
st.write(f"**Parâmetro λ (média):** {lambda_lts:.2f}")

nbins_poisson = int(lts.max() - lts.min() + 1)
fig_pois = px.histogram(lts, nbins=nbins_poisson,
                        title="Histograma de LTS com Distribuição de Poisson Ajustada",
                        labels={'value': 'LTS', 'count': 'Frequência'})

x_vals_pois = np.arange(int(lts.min()), int(lts.max())+1)
pmf_vals = poisson.pmf(x_vals_pois, mu=lambda_lts)

pmf_scaled = pmf_vals * len(lts)

fig_pois.add_scatter(x=x_vals_pois, y=pmf_scaled, mode='markers+lines', name='Poisson Ajustada')
st.plotly_chart(fig_pois)

st.header("Interpretação dos Resultados")
st.write("""
- **Distribuição Normal (WTS):**  
  A pontuação do time vencedor (WTS) apresenta uma distribuição aproximadamente normal, com média de 26.58 e desvio padrão de 9.59. O histograma mostra a frequência das pontuações, e a curva normal ajustada reforça que os dados seguem uma distribuição simétrica em torno da média. Esse comportamento permite aplicar métodos estatísticos baseados na normalidade para inferências e previsões sobre a pontuação dos times vencedores

- **Distribuição de Poisson (LTS):**  
  A pontuação do time perdedor (LTS) se ajusta bem a uma distribuição de Poisson, com parâmetro λ = 14.54, que representa sua média. O histograma evidencia a natureza discreta da pontuação, e a curva ajustada indica que a distribuição de Poisson é adequada para modelar esses dados. Essa modelagem permite entender a frequência de jogos com determinadas pontuações e avaliar a probabilidade de eventos raros, como pontuações muito baixas ou altas.
""")
