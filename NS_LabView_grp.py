import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from getrange import get_range, another_func

st.title('graph app')

#ファイルのアップロードとデータの整頓
uploaded_file = st.sidebar.file_uploader("aplode file", type='csv', accept_multiple_files=True)

fig = plt.figure(figsize = (12,8))

name_list = ['frequency','ampretured']

#セレクトボックスの作成
x = st.sidebar.selectbox('x axis', name_list)
y = st.sidebar.selectbox('y axis', name_list)



limmax, limmin = get_range()

graph_title  = st.sidebar.text_input('graph title',' ')
x_label = st.sidebar.text_input('name of x_value axis',' ',)
y_label = st.sidebar.text_input('name of y_value axis',' ')


for i,file in enumerate(uploaded_file):
    df = pd.read_csv(file, encoding="UTF-8")
    df = df.set_axis(name_list,axis=1)

    
    limmin_i= st.sidebar.number_input("下から" + str(i+1) + "番目のファイルの始点", 0.0000000001, 10000, 0.0000000001)   
    #matplotlibで可視化
    x_value = df.loc[:,x]
    y_value = df.loc[:,y]
    plt.bar(x_value ,y_value)
plt.xlabel(x_label,fontsize = 25)
plt.xlim(limmin,limmax)
plt.ylabel(y_label,fontsize = 25)
plt.yscale("log")
plt.title(graph_title,fontsize= 25, fontname="MS Gothic")

st.pyplot(fig)
