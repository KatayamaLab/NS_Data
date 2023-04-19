import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


class Show_graph:
    def __init__(self):
        st.title('graph app')
        self.fig = plt.figure(figsize = (12,8))
        self.sidebar()
        # self.uploaded_file = st.sidebar.file_uploader("aplode file", type='csv', accept_multiple_files=True)
        for f in self.uploaded_file:
            df = self.seiri(f)
            plt.scatter(df.loc[:,self.x],df.loc[:,self.y])

        plt.xlabel(self.x_label,fontsize = 25)
        plt.xlim(self.limmin,self.limmax)
        plt.ylabel(self.y_label,fontsize = 25)
        plt.title(self.graph_title,fontsize= 25)

        st.pyplot(self.fig)

    def sidebar(self):
        self.uploaded_file = st.sidebar.file_uploader("aplode file", type='csv', accept_multiple_files=True)

        self.x = st.sidebar.selectbox(
        'x axis',
        ['number of line','time','input 1','input 2','input 1+2','output','absorved','filter 1','filter 2','filter3','temp','set temp','uncertain','total value','nothing']
        )
        self.y = st.sidebar.selectbox(
        'y axis',
        ['number of line','time','input 1','input 2','input 1+2','output','absorved','filter 1','filter 2','filter3','temp','set temp','uncertain','total value','nothing']
        )
        self.limmax = st.sidebar.number_input("Display range（max）", -10000, 100000, 1000)
        self.limmin = st.sidebar.number_input("Display range（min）", -10000, 100000, 0)   

        self.graph_title  = st.sidebar.text_input('graph title',' ')
        self.x_label = st.sidebar.text_input('name of x_value axis',' ')
        self.y_label = st.sidebar.text_input('name of y_value axis',' ')

    def seiri(self, file):
        df = pd.read_csv(file, encoding="Shift-JIS")
        df = df.set_axis(['number of line','time','input 1','input 2','input 1+2','output','absorved','filter 1','filter 2','filter3','temp','set temp','uncertain','total value','nothing'],axis=1)
        return df

if __name__ == "__main__":
    Show_graph()
    


"""st.title('graph app')

#ファイルのアップロードとデータの整頓
self.uploaded_file = st.sidebar.file_uploader("aplode file", type='csv', accept_multiple_files=True)

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
limmax = st.sidebar.number_input("Display range（max）", -10000, 100000, 1000)
limmin = st.sidebar.number_input("Display range（min）", -10000, 100000, 0)   

graph_title  = st.sidebar.text_input('graph title',' ')
x_label = st.sidebar.text_input('name of x_value axis',' ')
y_label = st.sidebar.text_input('name of y_value axis',' ')

for file in self.uploaded_file:
    df = pd.read_csv(file, encoding="Shift-JIS")
    df = df.set_axis(['number of line','time','input 1','input 2','input 1+2','output','absorved','filter 1','filter 2','filter3','temp','set temp','uncertain','total value','nothing'],axis=1)


    #matplotlibで可視化
    plt.scatter(df.loc[:,x],df.loc[:,y])
plt.xlabel(x_label,fontsize = 25)
plt.xlim(limmin,limmax)
plt.ylabel(y_label,fontsize = 25)
plt.title(graph_title,fontsize= 25)

st.pyplot(fig)
"""