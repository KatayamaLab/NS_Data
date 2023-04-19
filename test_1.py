import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('graph app')

#ファイルのアップロードとデータの整頓
uploaded_file = st.sidebar.file_uploader("aplode file", type='csv', accept_multiple_files=True)

fig = plt.figure(figsize = (12,8))

name_list = ['number of line','time','input 1','input 2','input 1+2','output','absorved','filter 1','filter 2','filter3','temp','set temp','uncertain','total value','nothing']



def make_selectbox(x):
    return st.sidebar.selectbox(x + " " + 'axis', name_list )
def make_sidebar(z,j):
    return st.sidebar.number_input("Display range" + "("+ str(j) + ")"  , -10000, 100000, z)
def make_text_input(i):
    return st.sidebar.text_input('name of ' +  i )

#セレクトボックスの作成
x_value = make_selectbox("x")
y_value =make_selectbox("y")

#選択範囲の作成
limmax = make_sidebar(1000,"max")
limmin = make_sidebar(0,"min")

#グラフの書式の設定
graph_title  = make_text_input("graph title")
x_label = make_text_input("x_value axis")
y_label = make_text_input("y_value axis")



for i,file in enumerate(uploaded_file):
    df = pd.read_csv(file, encoding="UTF-8")
    df = df.set_axis(name_list,axis=1)

    
    limmin_i= st.sidebar.number_input("下から" + str(i+1) + "番目のファイルの始点", -10000, 100000, 0)   
    #matplotlibで可視化
    
    
    plt.scatter(df.loc[:,x_value] - limmin_i , df.loc[:,y_value], alpha=0.7)
plt.xlabel(x_label,fontsize = 25)
plt.xlim(limmin,limmax)
plt.ylabel(y_label,fontsize = 25)
plt.title(graph_title,fontsize= 25, fontname="MS Gothic")

st.pyplot(fig)



