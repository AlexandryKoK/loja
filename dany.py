import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import random
import string
from datetime import datetime


st.write("""
# Dany Conveniência!
""")

vendas = pd.read_table("vendas.csv",sep=',',names=['data','item','Dinheiro','Cartao','PIX'])
vendas['Mes'] = vendas['data'].str[4:5]
vendas = vendas[vendas["data"].str.contains("data") == False]


Total_PIX = vendas['PIX'].sum()
Total_cartao = vendas['Cartao'].sum()
Total_dinheiro = vendas['Dinheiro'].sum()

col1, col2, col3 = st.columns(3)
col1.metric(label="PIX", value=('R$ %.2f'% Total_PIX))
col2.metric(label="Cartão", value=('R$ %.2f'% Total_cartao))
col3.metric(label="Dinheiro", value=('R$ %.2f'% Total_dinheiro))



#st.metric(label="PIX", value=('R$ %.2f'% Total_PIX), delta="1.2 °F")
#st.metric(label="Cartão", value=('R$ %.2f'% Total_cartao), delta="1.2 °F")
#st.metric(label="Dinheiro", value=('R$ %.2f'% Total_dinheiro), delta="1.2 °F")

#vendas = pd.read_table("vendas.csv",sep=',',names=['data','item','pagamento','valor'])
#vendas = vendas[vendas["data"].str.contains("data") == False]
#vendas.sort_values(by='data',ascending=True)
#st.write(vendas['data'].value_counts())
#indice = vendas['data'].value_counts()[-1]-vendas['data'].value_counts()[-2]
#st.metric(label="Vendas", value=float(vendas['data'].value_counts()[-1]), delta=float(indice))

sheet_id = "1Q-DzfuwRTqLni1doeQH3gY2Lhw9fcyQdImUi3qisseA"
sheet_name = "Tudo(Atualizado)"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

produtos = pd.read_table(url, sep = ',',names=['item','produto','unidade','ifood','categoria'])
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
     b = str(st.number_input(nome[i],key=i,step=1,min_value=1))
     #a = st.write(str(nome[i]) + ' ' + str(st.number_input(nome[i],key=i,step=1)))
     col.insert(i,a + ' (' + b+ '), ')
     #st.write(col[i])

vendidos = ' '.join(str(e) for e in col)
#st.write(vendidos)
#pagamento = st.radio("Forma de pagamento:",('PIX','Cartão','Dinheiro'))
#st.write(len(nome))
#st.write(produtos.loc[produtos['item'] == nome[0]]['produto'])
dinheiro = st.checkbox('Dinheiro',key=2)
cartao = st.checkbox('Cartão',key=3)
pix = st.checkbox('Pix',key=1)
if dinheiro:
     dinheiro = st.number_input('Total Dinheiro: R$',step=1.0,key=2,min_value =0.0)
if cartao:
     cartao = st.number_input('Total Cartão: R$',step=1.0,key=3,min_value =0.0)
if pix:
     pix = st.number_input('Total PIX: R$',step=1.0,key=1,min_value =0.0)



vendas = pd.read_table("vendas.csv",sep=',',names=['data','item','Dinheiro','Cartao','PIX'])
vendas.loc[len(vendas.index)] = [(data).strftime('%d/%m/%Y'),str(vendidos), float(dinheiro), float(cartao), float(pix)]


if st.button('Salvar!'):
    st.write('Salvo!')
    vendas = vendas[vendas.data != "data"]
    vendas.to_csv('vendas.csv',header=False)
    vendas = pd.read_table("vendas.csv",sep=',',names=['data','item','Dinheiro','Cartao','PIX'])
    vendas['Mes'] = vendas['data'].str[3:5]
    vendas = vendas[vendas["data"].str.contains("data") == False]
    #st.write(vendas)
    #vendas['data'].hist()
    #fig, ax = plt.subplots()
    #ax.hist(vendas['data'])
    #st.pyplot(fig)



st.title("Vendas até o momento!")
#if st.button('Ver vendas'):
    #st.write('Vendas até o momento:')
    #vendas = vendas[vendas.data != "data"]
    #vendas.to_csv('vendas.csv',header=False)
vendas = pd.read_table("vendas.csv",sep=',',names=['data','item','Dinheiro','Cartao','PIX'])
vendas['Mes'] = vendas['data'].str[3:5]
vendas = vendas[vendas["data"].str.contains("data") == False]
st.write(vendas)