import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

def write(lang):
    lang_data={
        'pt-br':
            {
                'name': 'Douglas Winston',
                'title': 'Gerente de Produto de Dados',
                'competences': {'columns': ['Ano', 'Gestão de Pessoas', 'Entrega de Valor', 'Dados e Analytics', 'Criatividade e Soluções', 'Gestão de Produto'],
                                'values': [{0: 2019, 1: 0.5, 2: 1.5, 3: 2.0, 4: 3.0, 5: 0.5},
                                           {0: 2020, 1: 1.0, 2: 2.5, 3: 3.5, 4: 3.5, 5: 1.5},
                                           {0: 2021, 1: 2.0, 2: 3.5, 3: 4.0, 4: 3.8, 5: 2.5},
                                           {0: 2022, 1: 3.8, 2: 4.1, 3: 4.5, 4: 4.0, 5: 3.0}]},
                'contact': 'Contato',
                'location': 'São Paulo, SP',
                'phone': '+55 62 996990837',
                'email': 'douglas.winston.r@gmail.com',
                'link': '[linkedin.com/in/douglas-winston](https://www.linkedin.com/in/douglas-winston/)'
            },
        'en-us':
            {
                'name': 'Douglas Winston',
                'title': 'Data Product Manager',
                'competences': {'columns': ['Year', 'People Management', "Value Delivery", 'Data and Analytics', 'Solutions and Creativity', 'Product Management'],
                                'values': [{0: 2019, 1: 0.5, 2: 1.5, 3: 2.0, 4: 3.0, 5: 0.5},
                                           {0: 2020, 1: 1.0, 2: 2.5, 3: 3.5, 4: 3.5, 5: 1.5},
                                           {0: 2021, 1: 2.0, 2: 3.5, 3: 4.0, 4: 3.8, 5: 2.5},
                                           {0: 2022, 1: 3.8, 2: 4.1, 3: 4.5, 4: 4.0, 5: 3.0}]},
                'contact': 'Contact',
                'location': 'Sao Paulo, SP',
                'phone': '+55 62 996990837',
                'email': 'douglas.winston.r@gmail.com',
                'link': '[linkedin.com/in/douglas-winston](https://www.linkedin.com/in/douglas-winston/)'
            }
        }
    data = lang_data[lang]


    st.title(data['name'])
    st.markdown('#### {title}'.format(title=data['title']))

    df = pd.DataFrame(data['competences']['values'])
    df.rename(columns=dict(zip(range(df.shape[1]), data['competences']['columns'])), inplace=True)

    df_melted = df.melt(id_vars=data['competences']['columns'][0],
                                value_vars=data['competences']['columns'][1:])


    coluna_header = st.columns((2, 1, 2, 2), gap='small')

    perfil = Image.open('perfil.jpeg')
    personalidade = Image.open('personalidade.png')

    coluna_header[0].image(perfil, width=400)

    fig = px.line_polar(df_melted, r='value', theta='variable', color=data['competences']['columns'][0], color_discrete_sequence=px.colors.qualitative.G10, line_close=True, render_mode='SVG')

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
        )
    )
    coluna_header[2].write(fig)

    with st.expander('**{0}**'.format(data['contact']), True):
        coluna_header = st.columns(4, gap='small')
        coluna_header[0].markdown(data['location'])
        coluna_header[1].markdown(data['phone'])
        coluna_header[2].markdown(data['email'])
        coluna_header[3].markdown(data['link'])

    html_componet = """<div style="text-align: center"> your-text-here </div>"""