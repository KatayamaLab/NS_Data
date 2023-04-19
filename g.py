import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#ファイルのアップロードとデータの整頓
uploaded_file = st.sidebar.file_uploader("aplode file")#, accept_multiple_files=True)

if uploaded_file:
    df = pd.read_csv(uploaded_file, header=None, sep="\t")
    freq = df[0][:1000]
    amp = df[1][:1000]
    a = amp[50]
    amp *= 100 / a

    fig = plt.figure(figsize = (12,8))

    # xlim = st.sidebar(0, 1000, 400)

    plt.bar(freq, amp, width=3.0)
    plt.yscale("log")
    plt.ylim(10**(-4), 10**2)
    plt.xlim(0, 400)

    st.pyplot(fig)