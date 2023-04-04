import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import me
import experience
import education
import work

st.set_page_config(layout="wide", page_title="Douglas Winston")

tab_eng, tab_ptbr  = st.tabs(["English", "Português"])

with tab_ptbr:
    me.write('pt-br')
    experience.write('pt-br')
    education.write('pt-br')
    work.write('en-us')

with tab_eng:
    me.write('en-us')
    experience.write('en-us')
    education.write('en-us')
    work.write('en-us')

    # st.markdown('### Trabalhos e Publicações')
    # st.markdown("""
    # - 2021, PulseRL: Enabling Offline Reinforcement Learning for Digital Marketing Systems via ConservativeQ-Learning
    # - 2020, A Systematic Mapping Study on Software Testing for Systems-of-Systems
    # - 2020, Selecting Important Features Interactions In A Click-Through-Rate Application Using Genetic Algorithms
    # - 2020, Adaptive Multilayer Perceptron
    # - 2019, A Multi-Objective Evolutionary Approach For Optimizing Pickup and Delivery Locations In A Demand Responsive Transport Service
    # - 2019, GAEEII: An Optimised Genetic Algorithm Endmember Extractor for Hyperspectral Unmixing
    # - 2018, Comparison of VCA and GAEE algorithms for Endmember Extraction
    # - 2018, TensorNet: Classificação de Protozoários
    # - 2013, Estudo de Ambiente Virtual para Simulação Multiagente de Usuários de Aplicativo Web
    # """
    # )
