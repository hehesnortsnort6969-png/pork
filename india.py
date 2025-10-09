import streamlit as st
import pandas as pd
st.title("top 10 reasons why John is retarded")
names = ("John","Nathan","Moe")
selectbox = st.selectbox("names",names)
st.write(selectbox)
