import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('graph app')

#ファイルのアップロードとデータの整頓
uploaded_file = st.sidebar.file_uploader("aplode file", type='csv', accept_multiple_files=True)

fig = plt.figure(figsize = (12,8))



#セレクトボックスの作成
x = st.sidebar.selectbox(
'x axis',
['number of line','time','input 1','input 2','input 1+2','output','absorved','filter 1','filter 2','filter3','temp','set temp','uncertain','total value','nothing']
)
y = st.sidebar.selectbox(
'y axis',
['number of line','time','input 1','input 2','input 1+2','output','absorved','filter 1','filter 2','filter3','temp','set temp','uncertain','total value','nothing']
)

limmax = st.sidebar.number_input("Display range（max)"  , -10000, 100000, 1000)
limmin = st.sidebar.number_input("Display range（min)" , -10000, 100000, 0)   

graph_title  = st.sidebar.text_input('graph title',' ')
x_label = st.sidebar.text_input('name of x_value axis',' ',)
y_label = st.sidebar.text_input('name of y_value axis',' ')



for i,file in enumerate(uploaded_file):
    df = pd.read_csv(file, encoding="UTF-8")
    df = df.set_axis(['number of line','time','input 1','input 2','input 1+2','output','absorved','filter 1','filter 2','filter3','temp','set temp','uncertain','total value','nothing'],axis=1)

    
    limmin_i= st.sidebar.number_input("下から" + str(i+1) + "番目のファイルの始点", -10000, 100000, 0)   
    #matplotlibで可視化
    x_value = df.loc[:,x]
    y_value = df.loc[:,y]
    plt.scatter(x_value - limmin_i,y_value,alpha=0.7)
plt.xlabel(x_label,fontsize = 25)
plt.xlim(limmin,limmax)
plt.ylabel(y_label,fontsize = 25)
plt.title(graph_title,fontsize= 25, fontname="MS Gothic")

st.pyplot(fig)
