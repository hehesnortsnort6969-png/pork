import streamlit as st
import pandas as pd
st.title("top 10 reasons why John is retarded")
data = pd.read_csv("india.csv")
selectbox = st.selectbox("data",names)
st.write(selectbox)
