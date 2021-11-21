import streamlit as st
import pdfplumber
import nltk
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import wordcloud
nltk.download('punkt')
nltk.download('stopwords')

st.set_page_config(page_title = 'WCloud - Powered by Daiene Fortunato',  
				   layout = 'centered', 
				   initial_sidebar_state = 'auto')


st.markdown('# :cloud: WCloud :cloud:')
st.markdown('#### Gere sua nuvem de palavras de maneira simples')
st.markdown('---')
st.markdown('## Carregue o PDF que deseja utilizar')

PDFs = st.file_uploader('O arquivo deve ter no máximo 10mb e ter a extenção ".pdf"',
				 type = ['pdf'],
				 accept_multiple_files = False)

if st.button('Carregar'):

    palavras = pdfplumber.open(PDFs)
    primeira_pagina = palavras.pages[0]
    textoCRU = primeira_pagina.extract_text()
    lista_de_palavras = nltk.tokenize.word_tokenize(textoCRU) 
    lista_de_palavras = [palavra.lower() for palavra in lista_de_palavras]
    pontuacao = ['(',')',';',':','[',']',',','–','(',')','/','|','-','%','@']
    stop_words = nltk.corpus.stopwords.words('portuguese')
    keywords = [palavra for palavra in lista_de_palavras if not palavra in stop_words and not palavra in pontuacao]
    textocv = " ".join(s for s in keywords)
    wordcloud = WordCloud(background_color = '#0f54c9', 
                        max_font_size = 150, 
                        width = 1280, 
                        height = 720, 
                        colormap= 'Blues').generate(textocv) 

    fig, ax = plt.subplots(figsize=(16, 9))
    ax.imshow(wordcloud)
    ax.set_axis_off()
    plt.imshow(wordcloud)
    salvar = True
    if salvar:
        wordcloud.to_file("mywordcloud.png")
    
    st.image('./mywordcloud.png')
    