import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title('Douglas Winston')

data = [
        {'Ano': 2019, 'Gestão de Pessoas': 0.5, 'Entrega de Valor': 1.5, 'Dados e Analytics': 2.0, 'Criatividade e Soluções': 3.0, 'Gestão de Produto': 0.5},
        {'Ano': 2020, 'Gestão de Pessoas': 1.0, 'Entrega de Valor': 2.5, 'Dados e Analytics': 3.5, 'Criatividade e Soluções': 3.5, 'Gestão de Produto': 1.5},
        {'Ano': 2021, 'Gestão de Pessoas': 2.0, 'Entrega de Valor': 3.5, 'Dados e Analytics': 4.0, 'Criatividade e Soluções': 3.8, 'Gestão de Produto': 2.5},
        {'Ano': 2022, 'Gestão de Pessoas': 3.8, 'Entrega de Valor': 4.1, 'Dados e Analytics': 4.5, 'Criatividade e Soluções': 4.0, 'Gestão de Produto': 3.0},
        ]

df = pd.DataFrame(data)

df_melted = df.melt(id_vars=['Ano'],
                            value_vars=['Gestão de Pessoas',
                                        'Entrega de Valor',
                                        'Dados e Analytics',
                                        'Criatividade e Soluções',
                                        'Gestão de Produto'])


coluna_header = st.columns((2, 1, 2, 5), gap='small')

perfil = Image.open('perfil.jpeg')
personalidade = Image.open('personalidade.png')

coluna_header[0].image(perfil, width=350)

fig = px.line_polar(df_melted, r='value', theta='variable', color='Ano', color_discrete_sequence=px.colors.qualitative.G10, line_close=True, render_mode='SVG')

fig.update_layout(legend=dict(
    orientation="h",
    yanchor='middle',
    xanchor="center",
    x=0.5
))

fig.update_layout(
    template=None,
    polar = dict(
        radialaxis = dict(range=[0, 5], showticklabels=False, ticks=''),
        # angularaxis = dict(showticklabels=False, ticks='')
    )
)

# coluna_header[1].markdown(' ')
# coluna_header[1].markdown(' ')
# coluna_header[1].markdown(' ')
coluna_header[2].markdown('São Paulo, SP')
coluna_header[2].markdown('+55 62 996990837')
coluna_header[2].markdown('douglas.winston.r@gmail.com')
coluna_header[2].markdown('[linkedin.com/in/douglas-winston](https://www.linkedin.com/in/douglas-winston/)')
coluna_header[2].markdown('[github.com/douglaswinstonr](https://github.com/douglaswinstonr)')

html_componet = """<div style="text-align: center"> your-text-here </div>"""

# coluna_header[1].markdown(' ')
# coluna_header[1].markdown(' ')
# coluna_header[1].markdown(' ')
# coluna_header[1].markdown(' ')
# coluna_header[1].markdown(' ')
# coluna_header[1].markdown(' ')
# coluna_header[1].markdown("<p style='text-align: right;'>São Paulo, SP</p>", unsafe_allow_html=True)
# coluna_header[1].markdown("<p style='text-align: right;'>+55 62 996990837</p>", unsafe_allow_html=True)
# coluna_header[1].markdown("<p style='text-align: right;'>douglas.winston.r@gmail.com</p>", unsafe_allow_html=True)
# coluna_header[1].markdown("<p style='text-align: right;'>linkedin.com/in/douglas-winston</p>", unsafe_allow_html=True)
# coluna_header[1].markdown("<p style='text-align: right;'>github.com/douglaswinstonr</p>", unsafe_allow_html=True)


coluna_header[3].write(fig)
st.markdown('### Experiência')
st.markdown("""
##### 2022, **Coordenador de Dados**, Recovery, São Paulo, SP (***1 ano e 3 meses)***

- Junto com um time excepcional ajudei a construir ferramentas baseadas em **dados** e **inteligência artificial** para a **precificação de carteiras de créditos** corporativos **inadimplidos**.
- A cada sprint fazemos **descoberta de produto**, **testes de funcionalidade** com usuários especialistas e avaliações constantes da **proposta de valor** de cada funcionalidade.
- Utilizamos o máximo de **processamento e tratamento de dados** internos e de mercado para o treinamento de **modelos estatísticos e computacionais** robustos.
- Conseguimos com cada melhoria nas **métricas dos modelos** e **usabilidade do produto**, reduzir o **risco de investimento de centenas de milhões de reais**.
- Tenho orgulho de dizer que construimos uma das **ferramentas mais avançadas** do pais no que diz respeito a **recuperação de crédito**.

**Habilidades**: Product Management · Agile · Scrum  · Python · PySpark · Power BI · Classification · Regression · Survival · Boosting · Neural Networks · Azure · Databricks · Streamlit
""")
st.markdown("""
##### 2021, **Cientista de Dados,** Carajás, Maceió, AL, (***1 ano***)

- Como consultor ajudei a mapear as **etapas da jornada do cliente** nas **lojas online** e de lojas **físicas** de produtos relacionados a **construção, decoração e utensílios domésticos**.
- Em reuniões semanais indificamos e propomos **soluções de dados** para guiar **ações de comunicação** com o cliente (CRM) usando a base de dados de 10 lojas virtuais e físicas.
- Foram construidos **modelos de segmentação** e **classificação** da base de clientes para identificar o tempo e a fase da construção do cliente.
- Foi elaborado **paíneis de acompanhamento** com filtros **interativos** para que a gestão de vendas consiga segmentar clientes de acordo com critérios de uma campanha de marketing.

**Habilidades**: Business Strategy · SQL · Qlik Sense · CRM · Customer Segmentation · Product Vision · Data Analysis
""")
st.markdown("""
##### 2021, Cientista de Dados, Grupo Saga, Goiânia, GO, (1 ano)

- Construção e disseminação de produtos de dados para as concessionárias automobilísticas de diversas marcas do Grupo Saga (Toyota, BMW, Volkswagen, entre outras).
- Realizamos a análise de evasão de clientes em revisões programadas, análise de recompra de veículos novos e a segmentação da base de clientes por critérios do negócio.
- Construímos também o processo de extração e recomendação de precificação de assinaturas de carros da concessionária.

**Habilidades**: Gestão de projetos · SQL · Google Cloud · Dataform · Data Scrapping · Amazon Athena · S3 · PySpark
""")
st.markdown("""
##### 2020, Cientista de Dados, Acordo Certo, São Paulo, SP,  (1 ano e 2 meses)

- Parte de uma equipe de cientistas de dados com foco na construção de um processo de tomada de decisão para acionamentos de consumidores com inadimplência.
- Foram desenvolvidos modelos de propensão de cadastro e de pagamento de acordo em site de marketplace de créditos inadimplidos.
- Foi implementado modelos de LTV para estimar o valor de recuperação para cada consumidor/cliente otimizando os custos com acionamentos nos canais de sms e e-mail.
- Diariamente alivamos as métricas relevantes para o negócio como taxa de clique, quantidade de cadastros e acordos, e entre outros.

**Habilidades**: Google Cloud · Big Query · SQL · DataForm · Modelos de Propensão · Data Studio
""")
st.markdown("""
##### 2019, Cientista de Dados, HP Transportes, Goiânia, GO, (1 ano e 4 meses)

- Extrações de dados para processos de inteligência competitiva com objetivo de otimizar estratégias de marketing de serviço de MAAS (Mobility As A Service).
- Modelagem de dados geográficos para soluções de mobilidade urbana com foco na resolução de problemas relacionados ao transporte compartilhado na região metropolitana.
- Estudo de conceitos de centralidades urbanas no âmbito do transporte público.
- Construção de um produto de dados para acompanhar os preços de viagens dos serviços concorrentes (Uber e 99).

**Habilidades**: Qlik Sense · Google Earth · QGis · Data Scrappig 
""")
st.markdown("""
##### 2018, Analista de Dados, Grupo Jaime Câmera, Goiânia, GO, (1 ano e 4 meses)

- Forneci insights e soluções de SEO para produtos importantes do grupo, como o site de notícias Jornal O Popular
- Visualização e monitoramente de indicadores-chave de desempenho relacionadas ao tráfego orgânico e pago dos sites do Grupo.
- Modelagem e extração de dados de audiência de TV fornecidos pelo IBOPE

**Habilidades**: SEO · Web Development · React · Java Script · Microsoft Azure · Kantar Media
""")
st.markdown("""
##### 2015, Pesquisador, Jacobs School of Engineering, San Diego, CA, (3 meses)

- Ajudei construção de uma plataforma de coleta de imagens em tempo real usando o Microsoft Kinect e C# com o objetivo de monitorar ambientes hospitalares.
- Processamento de imagens de profundidae usadas para insumos para algoritmos de detecção de movimento e queda alertando equipes médicas sobre o estado do paciente.

**Habilidades**: C#, Microsoft Kinect SDK, Image Processing
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
- 2019, A Multi-Objective Evolutionary Approach For Optimizing Pickup and Delivery Locations In A Demand Responsive Transport Service
- 2019, GAEEII: An Optimised Genetic Algorithm Endmember Extractor for Hyperspectral Unmixing
- 2018, Comparison of VCA and GAEE algorithms for Endmember Extraction
- 2018, TensorNet: Classificação de Protozoários
- 2013, Estudo de Ambiente Virtual para Simulação Multiagente de Usuários de Aplicativo Web
"""
)
