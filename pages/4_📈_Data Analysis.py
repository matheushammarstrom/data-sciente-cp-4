import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("nfl.csv")
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

tab1, tab2, tab3 = st.tabs(["Dados e Variáveis", "Perguntas de Análise", "Análise Estatística"])

with tab1:
  st.header("Explicação do Conjunto de Dados")
  st.write(
    "O dataset escolhido contém registros históricos de jogos da NFL, abrangendo temporadas de 1924 até 2025. "
    "Cada linha representa um jogo e inclui informações essenciais, tais como:"
  )
  st.markdown("""
  - **Data do jogo:** Indica quando o jogo ocorreu.
  - **Dia da semana (DOW):** Mostra o dia em que o jogo foi realizado (ex.: "Sun" para domingo).
  - **Times envolvidos:**  
    - **WT:** Time vencedor.  
    - **LT:** Time perdedor.
  - **Pontuações:**  
    - **WTS:** Pontuação do time vencedor.  
    - **LTS:** Pontuação do time perdedor.
  - **Tipo de jogo:** Ex.: "Regular Season" ou "Play-off".
  """)

  st.header("Identificação dos Tipos de Variáveis")
  st.markdown("""
### **Variáveis Categóricas (Nominais)**  
- **DOW:** Dia da semana do jogo (ex.: "Sun", "Mon").  
- **WT:** Time vencedor.  
- **LT:** Time perdedor.  
- **Type:** Tipo do jogo (ex.: "Regular Season").  

### **Variáveis Numéricas Discretas**  
- **WTS:** Pontuação do time vencedor.  
- **LTS:** Pontuação do time perdedor.  
- **Season:** Ano da temporada.  

### **Variaveis Numéricas Continuas**
- **Date:** Data do jogo.  
""")

  st.header("Visualização dos Dados")
  st.dataframe(df.head())

with tab2:
  st.header("Perguntas de Análise")
  st.markdown("""
  - **Distribuição Temporal:**  
    - Como os jogos se distribuem ao longo das temporadas? Há aumento ou diminuição no número de jogos ao longo dos anos?
  - **Análise de Performance dos Times:**  
    - Quais times possuem maiores taxas de vitória?  
    - Existe uma relação entre os times e a pontuação obtida?
  - **Estatísticas Descritivas das Pontuações:**  
    - Qual é a média, mediana e moda das pontuações dos jogos?  
    - Como se comportam a variância e o desvio padrão dos resultados?
  - **Impacto do Tipo de Jogo:**  
    - Os jogos de Regular Season apresentam comportamentos estatísticos diferentes quando comparados a outros tipos de jogos (caso existam)?
  - **Influência do Dia da Semana:**  
    - Existe alguma tendência ou padrão nos resultados dos jogos que varia conforme o dia da semana em que foram disputados?
  """)

with tab3:
  st.header("Análise Estatística dos Dados")
  
  st.subheader("1. Distribuição Temporal")
  st.write("Analisando a distribuição dos jogos ao longo das temporadas:")
  season_counts = df.groupby('Season').size().reset_index(name='Number of Games')
  fig_season = px.line(season_counts, x='Season', y='Number of Games', markers=True, 
             title="Número de Jogos por Temporada")
  st.plotly_chart(fig_season)
  st.write("Observa-se que, nos primeiros anos, o número de jogos era menor, e houve um crescimento gradual à medida que a NFL se expandiu. "
       "Em determinados períodos, variações podem ocorrer devido a mudanças no formato da temporada ou fatores históricos. Também conclui-se que nunca houveram tantos jogos na NFL como há hoje")

  st.subheader("2. Performance dos Times")
  st.write("Contagem de vitórias por time:")
  win_counts = df['WT'].value_counts().reset_index()
  win_counts.columns = ['Time', 'Vitórias']
  fig_wins = px.bar(win_counts, x='Time', y='Vitórias', title="Vitórias por Time", height=500)
  st.plotly_chart(fig_wins)
  st.write("Os times que aparecem com maior número de vitórias sugerem uma performance consistente ao longo dos anos. Porém, existem alguns times que nao existem mais, portanto possuem um número de vitórias muito baixo. Outro fator interessante é que o time com maior número de vitórias, é na verdade o 5º time em ranking de campeonatos vencidos.")
  
  team_scores = df.groupby('WT')['WTS'].mean().reset_index().sort_values(by='WTS', ascending=False)
  fig_team_scores = px.bar(team_scores, x='WT', y='WTS', title="Pontuação Média dos Times Vencedores", height=500)
  st.plotly_chart(fig_team_scores)
  st.write("O gráfico exibe a pontuação média dos times vencedores na NFL entre 1924 e 2025, destacando equipes com maior desempenho ofensivo ao longo do tempo. O New York Yanks se sobressai com a maior média de pontos entre os vencedores, enquanto o Canton Bulldogs possui a menor. Essa métrica complementa o número de vitórias ao indicar times com ataques historicamente mais produtivos.")

  st.subheader("3. Estatísticas Descritivas das Pontuações")
  if 'WTS' in df.columns and 'LTS' in df.columns:
    wts_mean = df['WTS'].mean()
    wts_median = df['WTS'].median()
    wts_mode = df['WTS'].mode()[0] if not df['WTS'].mode().empty else None
    wts_std = df['WTS'].std()
    wts_var = df['WTS'].var()
    
    lts_mean = df['LTS'].mean()
    lts_median = df['LTS'].median()
    lts_mode = df['LTS'].mode()[0] if not df['LTS'].mode().empty else None
    lts_std = df['LTS'].std()
    lts_var = df['LTS'].var()
    
    st.write("**Pontuações do Time Vencedor (WTS):**")
    st.write(f"Média: {wts_mean:.2f}, Mediana: {wts_median}, Moda: {wts_mode}, "
         f"Desvio Padrão: {wts_std:.2f}, Variância: {wts_var:.2f}")
    
    st.write("**Pontuações do Time Perdedor (LTS):**")
    st.write(f"Média: {lts_mean:.2f}, Mediana: {lts_median}, Moda: {lts_mode}, "
         f"Desvio Padrão: {lts_std:.2f}, Variância: {lts_var:.2f}")
    
    st.write("As estatísticas descritivas mostram que os times vencedores (WTS) têm uma média de 26.58 pontos, enquanto os perdedores (LTS) registram 14.54, evidenciando uma diferença significativa no desempenho ofensivo. A mediana das pontuações dos vencedores (27.0) está próxima da média, sugerindo uma distribuição relativamente simétrica, enquanto a dos perdedores (14.0) confirma uma tendência semelhante. O desvio padrão maior nos vencedores (9.59 vs. 8.37) indica maior variabilidade nas pontuações das equipes que triunfam, reforçando que algumas vitórias ocorrem com margens expressivas. Outro fator notável é que a média de pontos dos times vencedores é quase o dobro da média de pontos dos times perdedores")
  else:
    st.error("Colunas 'WTS' ou 'LTS' não encontradas no dataset.")
  
  st.subheader("4. Impacto do Tipo de Jogo")
  st.write("Comparando as pontuações para diferentes tipos de jogo:")
  if 'Type' in df.columns:
    fig_type = px.box(df, x='Type', y='WTS', title="Distribuição de Pontuações (WTS) por Tipo de Jogo")
    st.plotly_chart(fig_type)
    st.write("A análise da distribuição das pontuações (WTS) por tipo de jogo indica que a Regular Season apresenta uma maior variabilidade nas pontuações dos times vencedores em comparação aos Playoffs. Isso é evidenciado por uma amplitude interquartil ligeiramente maior e um número significativamente maior de outliers, sugerindo que há partidas com pontuações extremas mais frequentes na temporada regular. Já nos Playoffs, a pontuação tende a ser mais concentrada, possivelmente devido ao equilíbrio competitivo entre as equipes classificadas.")
  else:
    st.error("Coluna 'Type' não encontrada no dataset.")
  
  st.subheader("5. Influência do Dia da Semana")
  st.write("Analisando a distribuição dos jogos por dia da semana:")
  dow_counts = df['DOW'].value_counts().reset_index()
  dow_counts.columns = ['DOW', 'Número de Jogos']
  fig_dow = px.bar(dow_counts, x='DOW', y='Número de Jogos', title="Número de Jogos por Dia da Semana")
  st.plotly_chart(fig_dow)
  st.write("De acordo com o gráfico, podemos observar que Domingo(Sunday), é disparado o dia com maior quantidade de jogos, com mais de 14000 jogos disputados. Já segunda(monday), fica em segundo lugar, com menos de 1000 jogos disputados. O dia com a menor quantidade de jogos é Terca-feira(Tuesday)")
  dow_scores = df.groupby('DOW')['WTS'].mean().reset_index()
  fig_dow_scores = px.bar(dow_scores, x='DOW', y='WTS', title="Pontuação Média (WTS) por Dia da Semana")
  st.plotly_chart(fig_dow_scores)
  st.write("Esta análise permite identificar que a pontuacao média dos times vencedores na sexta e na segunda, sao superiores aos outros dias da semana. O dia com a menor média de pontuacao para o time vencedor é quarta-feira")
