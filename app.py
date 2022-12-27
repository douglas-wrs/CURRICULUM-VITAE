import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title('Douglas Winston')

data = [
        {'Ano': 2019, 'Gestão de Pessoas': 0.0, 'Entrega de Valor': 2.0, 'Dados e Analytics': 3.0, 'Criatividade e Soluções': 3.0, 'Gestão de Produto': 1.0},
        {'Ano': 2020, 'Gestão de Pessoas': 1.0, 'Entrega de Valor': 2.5, 'Dados e Analytics': 3.5, 'Criatividade e Soluções': 3.5, 'Gestão de Produto': 2.5},
        {'Ano': 2021, 'Gestão de Pessoas': 2.0, 'Entrega de Valor': 3.5, 'Dados e Analytics': 4.0, 'Criatividade e Soluções': 3.8, 'Gestão de Produto': 2.8},
        {'Ano': 2022, 'Gestão de Pessoas': 3.8, 'Entrega de Valor': 4.1, 'Dados e Analytics': 4.2, 'Criatividade e Soluções': 4.0, 'Gestão de Produto': 3.0},
        ]

df = pd.DataFrame(data)

df_melted = df.melt(id_vars=['Ano'],
                            value_vars=['Gestão de Pessoas',
                                        'Entrega de Valor',
                                        'Dados e Analytics',
                                        'Criatividade e Soluções',
                                        'Gestão de Produto'])


coluna_header = st.columns(3, gap='small')

perfil = Image.open('perfil.jpeg')
personalidade = Image.open('personalidade.png')

coluna_header[0].image(perfil)

fig = px.line_polar(df_melted, r='value', theta='variable', color='Ano', color_discrete_sequence=px.colors.qualitative.G10, line_close=True, render_mode='SVG')

fig.update_layout(legend=dict(
    orientation="h",
    yanchor='middle',
    xanchor="center",
    x=0.5
))

coluna_header[1].write(fig)
colunas = st.columns(5, gap='small')
colunas[0].markdown('São Paulo, SP')
colunas[1].markdown('+55 62 996990837')
colunas[2].markdown('douglas.winston.r@gmail.com')
colunas[3].markdown('[linkedin.com/in/douglas-winston](https://www.linkedin.com/in/douglas-winston/)')
colunas[4].markdown('[github.com/douglaswinstonr](https://github.com/douglaswinstonr)')

st.markdown('### Experiência')
st.markdown("""
##### 2022, **Coordenador de Dados**, Recovery, São Paulo, SP (***1 ano e 3 meses)***

- Ajudo um time excepcional a construir ferramentas baseadas em **dados** e **inteligência artificial** para a **precificação de carteiras de créditos** corporativos **inadimplidos**.
- Aplico diariamente técnicas de **descoberta de produto**, **testes de funcionalidade** com usuários especialistas e avaliações constantes da **proposta de valor** de cada feature e entrega.
- Utilizamos o máximo de **processamento e tratamento de dados** internos e de mercado para o treinamento de **modelos estatísticos e computacionais** robustos.
- Conseguimos com cada melhoria nas **métricas dos modelos** e **usabilidade do produto**, reduzir o **risco de investimento de centenas de milhões de reais**.
- Tenho orgulho de dizer que construimos uma das **ferramentas mais avançadas** do pais no que diz respeito a **recuperação de crédito**.

**Habilidades**: Product Management · Agile · Scrum  · Python · PySpark · Power BI · Classification · Regression · Survival · Boosting · Neural Networks · Azure · Databricks · Streamlit
""")
st.markdown("""
##### 2021, **Cientista de Dados,** Carajás, Maceió, AL, (***1 ano***)

- Como consultor ajudei a mapear as **etapas da jornada do cliente** nas **lojas online** e de lojas **físicas** de produtos relacionados a **construção, decoração e utensílios**.
- Identifiquei e implementei **soluções de dados** para guiar **ações de CRM** e comunicação com o cliente usando a base de dados de 10 lojas virtuais e físicas.
- Construí **modelos de segmentação** e **classificação** da base de clientes para identificar o tempo e fase certa em que o cliente se encontra.
- Definição de **fluxos de tranformações de dados** brutos em **visões simples e ricas** com todas as definições de negócio.
- Elaborei **paíneis de acompanhamento** com filtros **interativos** para que a gestão de vendas consiga segmentar listas de clientes de acordo com critérios de uma campanha específica.

**Habilidades**: Business Strategy · SQL · Qlik Sense · CRM · Customer Segmentation · Product Vision · Data Analysis
""")
st.markdown("""
##### 2021, Cientista de Dados, Grupo Saga, Goiânia, GO, (1 ano)

- X
- Y
- Z

**Habilidades**: 
""")
st.markdown("""
##### 2020, Cientista de Dados, Acordo Certo, São Paulo, SP,  (1 ano e 2 meses)

- X
- Y
- Z

**Habilidades**: 
""")
st.markdown("""
##### 2019, Cientista de Dados, HP Transportes, Goiânia, GO, (1 ano e 4 meses)

- X
- Y
- Z

**Habilidades**: 
""")
st.markdown("""
##### 2018, Analista de Dados, Grupo Jaime Câmera, Goiânia, GO, (1 ano e 4 meses)

- X
- Y
- Z

**Habilidades**: 
""")
st.markdown("""
##### 2015, Pesquisador, Jacobs School of Engineering, San Diego, CA, (3 meses)

- X
- Y
- Z

**Habilidades**: 
""")

st.markdown('### Educação')
st.markdown(""" 
##### 2022, **Doutorado em Ciências da Computação,** Universidade Federal de Goiás, UFG, (**disciplinas concluídas**)
*SEO-RL: A Supervised Evolutionary Offline Reinforcement Learning Approach*

**Tópicos**: Aprendizado de Máquina, Aprendizado por Reforço, Redes Neurais e Computação Evolutiva
""")
st.markdown(""" 
##### 2020, **Mestrado em Ciências da Computação**, Universidade Federal de Goiás, UFG
*Evolutionary Approaches for Endmember Extraction in Hyperspectral Unmixing using Genetic Algorithms*

**Tópicos**: Processamento de Imagens, Computação Evolutiva, Aprendizado Supervisionado e Meta-heurísticas
""")
st.markdown(""" 
##### 2019, **Especialização em Desenvolvimento Web**, Universidade Federal de Goiás, UFG, (**disciplinas concluídas**)
*Aplicação Web e Mobile de serviço de sugestões de mobilidade direcionados as necessidades dos usuários focado em economia tempo e dinheiro*

**Tópicos**: Raspagem de Dados Web, Aplicação Web e Mobile, Visualização de Dados
""")
st.markdown(""" 
##### 2018, **Especialização em Business Intelligence**, Universidade Federal de Goiás, UFG
*Categorização Automática de Textos Não Supervisionada Aplicada a um Site de Notícias*

**Tópicos**: Categorização de Textos, Processamento de Linguagem Natural e Aprendizado Não Supervisionado
""")
st.markdown(""" 
##### 2016, **Bacharelado em Ciência da Computação,** Universidade Federal de Goiás, UFG
*Estudo e implementação do método de calibração de câmeras de Zhengyou Zhang*

**Tópicos**: Geometria Computacional, Calibração de Câmeras, Processamento de Imagens
""")
st.markdown(""" 
##### 2015, **Intercâmbio**, University of California San Diego, UCSD
*Hospital Patient Monitoring System*

**Tópicos**: Construção de Software, Processamento de Imagens
""")
st.markdown('### Trabalhos e Publicações')
st.markdown("""
- 2021, PulseRL: Enabling Offline Reinforcement Learning for Digital Marketing Systems via ConservativeQ-Learning
- 2020, A Systematic Mapping Study on Software Testing for Systems-of-Systems
- 2020, Selecting Important Features Interactions In A Click-Through-Rate Application Using Genetic Algorithms
- 2020, Adaptive Multilayer Perceptron
- 2019 A Multi-Objective Evolutionary Approach For Optimizing Pickup and Delivery Locations In A Demand Responsive Transport Service
- 2019, GAEEII: An Optimised Genetic Algorithm Endmember Extractor for Hyperspectral Unmixing
- 2018, Comparison of VCA and GAEE algorithms for Endmember Extraction
- 2018, TensorNet: Classificação de Protozoários
- 2013, Estudo de Ambiente Virtual para Simulação Multiagente de Usuários de Aplicativo Web
"""
)