import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt 

@st.cache_data
def load_data(nrows=500):
    return pd.read_csv("https://raw.githubusercontent.com/softbytavz/Bici_data/refs/heads/main/citibike-tripdata.csv")

bici_data = load_data()

st.header("Biclas")
st.dataframe(bici_data)