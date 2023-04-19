import streamlit as st

def get_range():
    limmax = st.sidebar.number_input("Display range（max)"  , 0.0000000001, 1000, 1000)
    limmin = st.sidebar.number_input("Display range（min)" , 0.0000000001, 1000, 0.0000000001)   
    return limmax, limmin

def another_func():
    pass