import streamlit as st
import pandas as pd
import os
from streamlit_pandas_profiling import st_profile_report
import pandas_profiling
import openpyxl

st.set_page_config(page_title='Data Science Profiling',
                   page_icon=':bar_chart:',
                   layout='wide'
)



with st.sidebar:
    st.title('Análises Automáticas do seu DataSet')
    choice = st.radio('Navegação', ('Upload', 'Profiling', 'Download'))
    st.info('Este aplicativo permite você criar sua análise automática e ajuda você a ganhar tempo')

if os.path.exists('filedata.csv'):
    df = pd.read_csv('filedata.csv', index_col=None)

elif os.path.exists('filedata.xlsx'):
     df = pd.read_excel('filedata.xlsx', index_col=None)

if choice == 'Upload':
    st.title('Carregue seu Dataset')
    file = st.file_uploader('Carregue aqui')
    if file:
        if file.type == 'text/csv':
            df = pd.read_csv(file, sep=';', encoding='ISO-8859-1', index_col=None)
            df.to_csv('filedata.csv', index=False)
            st.dataframe(df)
        else:
           df = pd.read_excel(file)
           df.to_excel('filedata.xlsx', index=False)
           st.dataframe(df)

if choice == 'Profiling':
    st.title('')
    pr = df.profile_report()
    st_profile_report(pr)
    pr.to_file('meu_relatorio.html')
if choice == 'Download':
    with open('meu_relatorio.html', 'rb') as f:
          st.download_button('Download_file', f, 'relatorio.html')























