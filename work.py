import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
from datetime import datetime
import numpy as np

def write(lang):
    lang_data={
        "pt-br": {
            "title": "Trabalhos e Publicações",
            "works": [
                (2021, 'PulseRL: Permitindo Aprendizado por Reforço Offline para Sistemas de Marketing Digital via ConservativeQ-Learning'),
                (2020, 'Um Estudo de Mapeamento Sistemático em Teste de Software para Sistemas de Sistemas'),
                (2020, 'Selecionando Interações de Recursos Importantes em uma Aplicação de Taxa de Cliques Usando Algoritmos Genéticos'),
                (2020, 'Perceptron de Múltiplas Camadas Adaptativo'),
                (2019, 'Uma Abordagem Evolutiva Multiobjetivo para Otimização de Locais de Coleta e Entrega em um Serviço de Transporte Responsivo à Demanda'),
                (2019, 'GAEEII: Um Extrator de Endmembers com Algoritmo Genético Otimizado para Mistura Espectral'),
                (2018, 'Comparação dos Algoritmos VCA e GAEE para Extração de Endmembers'),
                (2018, 'TensorNet: Classificação de Protozoários'),
                (2013, 'Estudo de um Ambiente Virtual para Simulação Multiagente de Usuários de uma Aplicação Web')
            ]
            },
        "en-us": {
            "title": "Works and Publications",
            "works": [
                (2021, 'PulseRL: Enabling Offline Reinforcement Learning for Digital Marketing Systems via ConservativeQ-Learning'),
                (2020, 'A Systematic Mapping Study on Software Testing for Systems-of-Systems'),
                (2020, 'Selecting Important Features Interactions In A Click-Through-Rate Application Using Genetic Algorithms'),
                (2020, 'Adaptive Multilayer Perceptron'),
                (2019, 'A Multi-Objective Evolutionary Approach For Optimizing Pickup and Delivery Locations In A Demand Responsive Transport Service'),
                (2019, 'GAEEII: An Optimised Genetic Algorithm Endmember Extractor for Hyperspectral Unmixing'),
                (2018, 'Comparison of VCA and GAEE algorithms for Endmember Extraction'),
                (2018, 'TensorNet: Protozoa Classification'),
                (2013, 'Study of a Virtual Environment for Multi-Agent Simulation of Users of a Web Application')
            ]
        }
    }

    data = lang_data[lang]
    st.markdown('### {title}'.format(title=data['title']))

    for exp in data['works']:
        st.markdown(' {0}, *{1}*'.format(exp[0],
                                                exp[1]))