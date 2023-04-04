import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
from datetime import datetime
import numpy as np

def write(lang):
    lang_data={
        "pt-br": {
            "title": "Educação",
            "education": [
                {
                    "header": (
                        2022,
                        "Doutorado em Ciências da Computação",
                        "Universidade Federal de Goiás, UFG",
                        "somente disciplinas",
                    ),
                    "title": "SEO-RL: A Supervised Evolutionary Offline Reinforcement Learning Approach",
                    "topic": [
                        "Tópicos",
                        "Aprendizado de Máquina",
                        "Aprendizado por Reforço",
                        "Redes Neurais",
                        "Computação Evolutiva",
                    ],
                },
                {
                    "header": (
                        2020,
                        "Mestrado em Ciências da Computação",
                        "Universidade Federal de Goiás, UFG",
                        "",
                    ),
                    "title": "Evolutionary Approaches for Endmember Extraction in Hyperspectral Unmixing using Genetic Algorithms",
                    "topic": [
                        "Tópicos",
                        "Processamento de Imagens",
                        "Computação Evolutiva",
                        "Aprendizado Supervisionado",
                        "Meta-heurísticas",
                    ],
                },
                {
                    "header": (
                        2019,
                        "Especialização em Desenvolvimento Web",
                        "Universidade Federal de Goiás",
                        "UFG",
                        "somente disciplinas",
                    ),
                    "title": "Aplicação Web e Mobile de serviço de sugestões de mobilidade direcionados as necessidades dos usuários focado em economia tempo e dinheiro",
                    "topic": [
                        "Tópicos",
                        "Raspagem de Dados Web",
                        "Aplicação Web e Mobile",
                        "Visualização de Dados",
                    ],
                },
                {
                    "header": (
                        2018,
                        "Especialização em Business Intelligence",
                        "Universidade Federal de Goiás",
                        "UFG",
                        "",
                    ),
                    "title": "Categorização Automática de Textos Não Supervisionada Aplicada a um Site de Notícias",
                    "topic": [
                        "Tópicos",
                        "Categorização de Textos",
                        "Processamento de Linguagem Natural",
                        "Aprendizado Não Supervisionado",
                    ],
                },
                {
                    "header": (
                        2016,
                        "Bacharelado em Ciência da Computação",
                        "Universidade Federal de Goiás, UFG",
                        "",
                    ),
                    "title": "Estudo e implementação do método de calibração de câmeras de Zhengyou Zhang",
                    "topic": [
                        "Tópicos",
                        "Geometria Computacional",
                        "Calibração de Câmeras",
                        "Processamento de Imagens",
                    ],
                },
                {
                    "header": (
                        2015,
                        "Intercâmbio",
                        "University of California San Diego, UCSD",
                        "",
                    ),
                    "title": "Hospital Patient Monitoring System",
                    "topic": [
                        "Tópicos",
                        "Microsoft Kinect",
                        "Processamento de Imagens",
                        "Construção de Software",
                    ],
                },
            ],
        },
        "en-us": {
            "title": "Education",
            "education": [
                {
                    "header": (
                        2022,
                        "PhD in Computer Science",
                        "Federal University of Goiás, UFG",
                        "Coursework only",
                    ),
                    "title": "SEO-RL: A Supervised Evolutionary Offline Reinforcement Learning Approach",
                    "topic": [
                        "Topics",
                        "Machine Learning",
                        "Reinforcement Learning",
                        "Neural Networks",
                        "Evolutionary Computing",
                    ],
                },
                {
                    "header": (
                        2020,
                        "Master's Degree in Computer Science",
                        "Federal University of Goiás, UFG",
                        "",
                    ),
                    "title": "Evolutionary Approaches for Endmember Extraction in Hyperspectral Unmixing using Genetic Algorithms",
                    "topic": [
                        "Topics",
                        "Image Processing",
                        "Evolutionary Computing",
                        "Supervised Learning",
                        "Meta-heuristics",
                    ],
                },
                {
                    "header": (
                        2019,
                        "Specialization in Web Development",
                        "Federal University of Goiás, UFG",
                        "Coursework only",
                    ),
                    "title": "Web and Mobile Application for Mobility Suggestions Directed at Users' Needs Focused on Time and Money Saving",
                    "topic": [
                        "Topics",
                        "Web Scraping",
                        "Web and Mobile Application",
                        "Data Visualization",
                    ],
                },
                {
                    "header": (
                        2018,
                        "Specialization in Business Intelligence",
                        "Federal University of Goiás, UFG",
                        "",
                    ),
                    "title": "Unsupervised Automatic Text Categorization Applied to a News Website",
                    "topic": [
                        "Topics",
                        "Text Categorization",
                        "Natural Language Processing",
                        "Unsupervised Learning",
                    ],
                },
                {
                    "header": (
                        2016,
                        "Bachelor's Degree in Computer Science",
                        "Federal University of Goiás, UFG",
                        "",
                    ),
                    "title": "Study and Implementation of Zhengyou Zhang's Camera Calibration Method",
                    "topic": [
                        "Topics",
                        "Computational Geometry",
                        "Camera Calibration",
                        "Image Processing",
                    ],
                },
                {
                    "header": (
                        2015,
                        "Exchange Program",
                        "University of California San Diego, UCSD",
                        "",
                    ),
                    "title": "Hospital Patient Monitoring System",
                    "topic": [
                        "Topics",
                        "Microsoft Kinect",
                        "Image Processing",
                        "Software Development",
                    ],
                },
            ],
        },
    }

    
    data = lang_data[lang]
    st.markdown('### {title}'.format(title=data['title']))

    for exp in data['education']:
        if exp['header'][3]:
            st.markdown('##### {0}, **{1}**, {2}, (**{3}**)'.format(exp['header'][0],
                                                            exp['header'][1],
                                                            exp['header'][2],
                                                            exp['header'][3]))
        else:
            st.markdown('##### {0}, **{1}**, {2}'.format(exp['header'][0],
                                                        exp['header'][1],
                                                        exp['header'][2]))
        
        st.markdown('- {0}'.format(exp['title']))

        st.markdown('###### {0}: *{1}*'.format(exp['topic'][0], ' · '.join(exp['topic'][1:])))
        st.markdown(' ')