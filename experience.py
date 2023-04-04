import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
from datetime import datetime
import numpy as np

def write(lang):
    lang_data= {
        "pt-br": {
            "title": "Experiência",
            "experiences": [
                {
                    "header": (
                        2022,
                        "Coordenador de Dados",
                        "Recovery",
                        "São Paulo, SP",
                        "2021-10-01",
                        (datetime.now()).strftime("%Y-%m-%d"),
                        "Anos",
                    ),
                    "content": (
                        "Liderei um time excepcional a construir ferramentas baseadas em dados e inteligência artificial para a precificação de carteiras de créditos inadimplidos.",
                        "A cada Sprint fizemos descoberta de produto, testes de funcionalidade com usuários especialistas e avaliações constantes da proposta de valor de cada funcionalidade.",
                        "Utilizamos o máximo de processamento e tratamento de dados internos e de mercado para o treinamento de modelos estatísticos e computacionais robustos.",
                        "Conseguimos com cada melhoria nas métricas dos modelos e usabilidade do produto, reduzir o risco de investimento de centenas de milhões de reais.",
                        "Tenho orgulho de dizer que construímos uma das ferramentas mais avançadas do pais no que diz respeito a recuperação de crédito.",
                    ),
                    "skills": [
                        "Habilidades",
                        "People Management",
                        "Product Management",
                        "Agile",
                        "Python",
                        "PySpark",
                        "Power BI",
                        "Databricks",
                        "Azure Cloud",
                        "Regression Models",
                        "Survival Analysis",
                    ],
                },
                {
                    "header": (
                        2021,
                        "Cientista de Dados",
                        "Carajás",
                        "Maceió, AL",
                        "2021-05-01",
                        "2022-06-01",
                        "Anos",
                    ),
                    "content": (
                        "Como consultor ajudei a mapear as etapas da jornada do cliente nas lojas online e físicas de produtos relacionados a construção, decoração e utensílios domésticos.",
                        "Em reuniões semanais identifiquei e propus soluções de dados para guiar ações de comunicação com o cliente (CRM) usando a base de dados de 10 lojas online e físicas.",
                        "Desenvolvi modelos de segmentação e classificação de clientes para identificar o tempo e a fase da construção na obra ou reforma do cliente.",
                        "Elaborei painéis de acompanhamento com filtros interativos para que a gestão de vendas conseguisse segmentar os clientes de acordo com critérios de cada campanha de marketing.",
                    ),
                    "skills": [
                        "Habilidades",
                        "Business Strategy",
                        "SQL",
                        "Qlik Sense",
                        "CRM",
                        "Customer Segmentation",
                        "Product Vision",
                        "Data Analysis",
                        "Python",
                    ],
                },
                {
                    "header": (
                        2021,
                        "Cientista de Dados",
                        "Grupo Saga",
                        "Goiânia, GO",
                        "2020-12-01",
                        "2022-02-01",
                        "Anos",
                    ),
                    "content": (
                        "Construí e disseminei produtos de dados para as concessionárias automobilísticas de diversas marcas do Grupo Saga (Toyota, BMW, Volkswagen, entre outras).",
                        "Realizei análises de evasão de clientes em revisões programadas, análises de recompra de veículos novos e propus uma segmentação da base de clientes por critérios do negócio.",
                        "Construí também um processo de extração e recomendação de precificação de assinaturas de carros da concessionária com base nos preços concorrentes do mercado (Localiza, Movida, Porto Seguro).",
                    ),
                    "skills": [
                        "Habilidades",
                        "Gestão de projetos",
                        "SQL",
                        "Google Cloud",
                        "CRM",
                        "Data Scrapping",
                        "Amazon Athena",
                        "S3",
                        "PySpark",
                        "Python",
                    ],
                },
                {
                    "header": (
                        2020,
                        "Cientista de Dados",
                        "Acordo Certo",
                        "São Paulo, SP",
                        "2020-08-01",
                        "2021-09-01",
                        "Anos",
                    ),
                    "content": (
                        "Liderei tecnicamente uma equipe de cientistas de dados com foco na construção de um processo de tomada de decisão de acionamentos de consumidores com inadimplência no mercado de crédito.",
                        "Desenvolvi modelos de propensão de cadastro e de pagamento/acordo em um site estilo marketplace para a negociação de dívidas.",
                        "Construí modelos de LTV para estimar o valor de recuperação de cada consumidor/cliente otimizando os custos com acionamentos nos canais de sms e e-mail.",
                        "Avaliei métricas relevantes para o negócio como taxa de clique, quantidade de cadastros, quantidade de acordos, entre outros, correlacionando com o resultado dos modelos.",
                    ),
                    "skills": [
                        "Habilidades",
                        "SQL",
                        "Google Cloud",
                        "Big Query",
                        "Modelos de Propensão",
                        "Data Studio",
                        "Python",
                    ],
                },
                {
                    "header": (
                        2019,
                        "Cientista de Dados",
                        "HP Transportes",
                        "Goiânia, GO",
                        "2019-06-01",
                        "2020-08-01",
                        "Anos",
                    ),
                    "content": (
                        "Extrai dados para processos de inteligência competitiva com objetivo de otimizar estratégias de marketing de serviço de MAAS (Mobility As A Service).",
                        "Realizei diversas modelagens de dados geográficos para soluções de mobilidade urbana com foco na resolução de problemas relacionados ao transporte compartilhado na região metropolitana.",
                        "Desenvolvi estudos de conceitos de centralidades urbanas no âmbito do transporte público.",
                        "Construí um produto de dados para acompanhar e recomendar preços de viagens de serviços de aplicativos de transporte em toda região metropolitana (Uber e 99).",
                    ),
                    "skills": [
                        "Habilidades",
                        "Qlik Sense",
                        "Google Earth",
                        "QGis",
                        "Data Scrappig",
                        "Automação de Processos (RPA)",
                        "Python",
                    ],
                },
                {
                    "header": (
                        2018,
                        "Analista de Dados",
                        "Grupo Jaime Câmera",
                        "Goiânia, GO",
                        "2018-02-01",
                        "2019-05-01",
                        "Anos",
                    ),
                    "content": (
                        "Desenvolvi relatórios de SEO para os produtos importantes da filial da TV Globo em Goiânia, como o site de notícias Jornal O Popular e o site de classificados Classi.",
                        "Construí visualizações e monitorei indicadores-chave de desempenho relacionadas ao tráfego de audiência orgânico e pago dos sites do grupo.",
                        "Realizei extrações e modelagem de dados de audiência de TV fornecidos pelo IBOPE.",
                    ),
                    "skills": [
                        "Habilidades",
                        "SEO",
                        "Web Development",
                        "React",
                        "Java Script",
                        "Microsoft Azure",
                        "Kantar Media",
                        "Python",
                    ],
                },
                {
                    "header": (
                        2015,
                        "Pesquisador",
                        "Jacobs School of Engineering",
                        "San Diego, CA",
                        "2015-06-01",
                        "2015-08-01",
                        "Anos",
                    ),
                    "content": (
                        "Ajudei a construir uma plataforma de coleta de imagens em tempo real usando o Microsoft Kinect com o objetivo de monitorar ambientes hospitalares.",
                        "Realizei estudos para o processamento de imagens de profundida usadas em algoritmos de detecção de movimento e queda para alertas sobre o estado do paciente.",
                    ),
                    "skills": [
                        "Habilidades",
                        "C#",
                        " Microsoft Kinect SDK",
                        "Image Processing",
                    ],
                },
            ],
        },
        "en-us": {
            "title": "Experiences",
            "experiences": [
                {
                    "header": (
                        2022,
                        "Data Coordinator",
                        "Recovery",
                        "São Paulo, SP",
                        "2021-10-01",
                        (datetime.now()).strftime("%Y-%m-%d"),
                        "Years",
                    ),
                    "content": (
                        "I led an exceptional team to build data and artificial intelligence-based tools for pricing debt portfolios.",
                        "With each Sprint we made product discovery, functionality testing with expert users and constant evaluations of the value proposition of each functionality.",
                        "We used the maximum internal and market data processing and treatment for training robust statistical and computational models.",
                        "With each improvement in model metrics and product usability, we were able to reduce the investment risk of hundreds of millions of reais.",
                        "I'm proud to say that we built one of the most advanced tools in the country when it comes to credit recovery.",
                    ),
                    "skills": [
                        "Skills",
                        "People Management",
                        "Product Management",
                        "Agile",
                        "Python",
                        "PySpark",
                        "Power BI",
                        "Databricks",
                        "Azure Cloud",
                        "Regression Models",
                        "Survival Analysis",
                    ],
                },
                {
                    "header": (
                        2021,
                        "Data Scientist",
                        "Carajás",
                        "Maceió, AL",
                        "2021-05-01",
                        "2022-06-01",
                        "Years",
                    ),
                    "content": (
                        "As a consultant, I helped map the customer journey stages in online and physical stores selling construction, decoration, and household items.",
                        "In weekly meetings, I identified and proposed data solutions to guide customer communication actions (CRM) using the databases of 10 online and physical stores.",
                        "I developed customer segmentation and classification models to identify the customer's construction or renovation time and phase.",
                        "I created monitoring dashboards with interactive filters so that sales management could segment customers according to the criteria of each marketing campaign.",
                    ),
                    "skills": [
                        "Skills",
                        "Business Strategy",
                        "SQL",
                        "Qlik Sense",
                        "CRM",
                        "Customer Segmentation",
                        "Product Vision",
                        "Data Analysis",
                        "Python",
                    ],
                },
                {
                    "header": (
                        2021,
                        "Data Scientist",
                        "Saga Group",
                        "Goiânia, GO",
                        "2020-12-01",
                        "2022-02-01",
                        "Years",
                    ),
                    "content": (
                        "I built and disseminated data products for automotive dealerships of various brands within the Saga Group (Toyota, BMW, Volkswagen, among others).",
                        "I conducted analyses of customer attrition in scheduled revisions, analyses of new vehicle repurchase, and proposed customer segmentation based on business criteria.",
                        "I also built a process for extracting and recommending pricing for car subscriptions based on market competitors' prices (Localiza, Movida, Porto Seguro).",
                    ),
                    "skills": [
                        "Skills",
                        "Project Management",
                        "SQL",
                        "Google Cloud",
                        "CRM",
                        "Data Scraping",
                        "Amazon Athena",
                        "S3",
                        "PySpark",
                        "Python",
                    ],
                },
                {
                    "header": (
                        2020,
                        "Data Scientist",
                        "Acordo Certo",
                        "São Paulo, SP",
                        "2020-08-01",
                        "2021-09-01",
                        "Years",
                    ),
                    "content": (
                        "I technically led a team of data scientists with a focus on building a decision-making process for consumer activation with delinquency in the credit market.",
                        "I developed registration and payment/agreement propensity models on a marketplace-style website for debt negotiation.",
                        "I built LTV models to estimate the recovery value of each consumer/client by optimizing costs with activations in SMS and email channels.",
                        "I evaluated relevant business metrics such as click-through rate, number of registrations, number of agreements, among others, correlating with the models' results.",
                    ),
                    "skills": [
                        "Skills",
                        "SQL",
                        "Google Cloud",
                        "Big Query",
                        "Propensity Models",
                        "Data Studio",
                        "Python",
                    ],
                },
                {
                    "header": (
                        2019,
                        "Data Scientist",
                        "HP Transportes",
                        "Goiânia, GO",
                        "2019-06-01",
                        "2020-08-01",
                        "Years",
                    ),
                    "content": (
                        "Extracted data for competitive intelligence processes with the aim of optimizing marketing strategies for MAAS (Mobility As A Service) service.",
                        "Carried out several geographical data modeling for urban mobility solutions focused on solving problems related to shared transportation in the metropolitan region.",
                        "Developed studies on urban centrality concepts in public transportation.",
                        "Built a data product to track and recommend travel prices for transportation application services throughout the metropolitan region (Uber and 99).",
                    ),
                    "skills": [
                        "Skills",
                        "Qlik Sense",
                        "Google Earth",
                        "QGis",
                        "Data Scraping",
                        "Process Automation (RPA)",
                        "Python",
                    ],
                },
                {
                    "header": (
                        2018,
                        "Data Analyst",
                        "Grupo Jaime Câmera",
                        "Goiânia, GO",
                        "2018-02-01",
                        "2019-05-01",
                        "Years",
                    ),
                    "content": (
                        "Developed SEO reports for important products of the TV Globo affiliate in Goiânia, such as the news website Jornal O Popular and the classifieds website Classi.",
                        "Built visualizations and monitored key performance indicators related to organic and paid audience traffic for the group's websites.",
                        "Performed data extraction and modeling of TV audience data provided by IBOPE.",
                    ),
                    "skills": [
                        "Skills",
                        "SEO",
                        "Web Development",
                        "React",
                        "Java Script",
                        "Microsoft Azure",
                        "Kantar Media",
                        "Python",
                    ],
                },
                {
                    "header": (
                        2015,
                        "Researcher",
                        "Jacobs School of Engineering",
                        "San Diego, CA",
                        "2015-06-01",
                        "2015-08-01",
                        "Years",
                    ),
                    "content": (
                        "Helped to build a real-time image collection platform using Microsoft Kinect with the goal of monitoring hospital environments.",
                        "Performed studies for depth image processing used in motion and fall detection algorithms for patient status alerts.",
                    ),
                    "skills": ["Skills", "C#", "Microsoft Kinect SDK", "Image Processing"],
                },
            ],
        },
    }

    data = lang_data[lang]
    st.markdown('### {title}'.format(title=data['title']))

    for exp in data['experiences']:
        start_dt = datetime.strptime(exp['header'][4], '%Y-%m-%d')
        now_dt = datetime.strptime(exp['header'][5], '%Y-%m-%d')
        years = round((now_dt-start_dt).days/360, 1)

        st.markdown('##### {0}, **{1}**, {2}, {3} ({4} {5})'.format(exp['header'][0],
                                                          exp['header'][1],
                                                          exp['header'][2],
                                                          exp['header'][3],
                                                          years,
                                                          exp['header'][6]))
        for desc in exp['content']:
            st.markdown('- {0}'.format(desc))

        st.markdown('###### {0}: *{1}*'.format(exp['skills'][0], ' · '.join(exp['skills'][1:])))
        st.markdown(' ')