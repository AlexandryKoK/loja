import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import random
import string

st.write("""
# Dany Conveniência!
""")

#vendas = pd.read_table("vendas.csv",sep=',',names=['data','item','pagamento','valor'])
#vendas = vendas[vendas["data"].str.contains("data") == False]
#vendas.sort_values(by='data',ascending=True)
#st.write(vendas['data'].value_counts())
#indice = vendas['data'].value_counts()[-1]-vendas['data'].value_counts()[-2]
#st.metric(label="Vendas", value=float(vendas['data'].value_counts()[-1]), delta=float(indice))



produtos = pd.read_table("pag6.csv", sep = ',',names=['item','produto','unidade','ifood','categoria'])
st.write(produtos)
col = []
st.title("Adicionar Venda!")
#st.text("Produto:")
data = st.date_input("Data:")
lista_itens = produtos['item']
nome = st.multiselect("Produtos",lista_itens)
n = len(nome)
col = []
for i in range(0,n):
     a = str(nome[i])
     b = str(st.number_input(nome[i],key=i,step=1))
     #a = st.write(str(nome[i]) + ' ' + str(st.number_input(nome[i],key=i,step=1)))
     col.insert(i,a + ' (' + b+ '), ')
     #st.write(col[i])

vendidos = ' '.join(str(e) for e in col)
#st.write(vendidos)
pagamento = st.radio("Forma de pagamento:",('PIX','Cartão','Dinheiro'))
#st.write(len(nome))
#st.write(produtos.loc[produtos['item'] == nome[0]]['produto'])
total = st.number_input('Total: R$',step=1.0)
vendas = pd.read_table("vendas.csv",sep=',',names=['data','item','pagamento','valor'])
vendas.loc[len(vendas.index)] = [(data).strftime('%d/%m/%Y'),str(vendidos), str(pagamento), float(total)]


if st.button('Salvar!'):
    st.write('Salvo!')
    vendas = vendas[vendas.data != "data"]
    vendas.to_csv('vendas.csv',header=False)
    vendas = pd.read_table("vendas.csv",sep=',',names=['data','item','pagamento','valor'])
    vendas['Mes'] = vendas['data'].str[3:5]
    vendas = vendas[vendas["data"].str.contains("data") == False]
    st.write(vendas)
    #vendas['data'].hist()
    fig, ax = plt.subplots()
    ax.hist(vendas['data'])
    st.pyplot(fig)



