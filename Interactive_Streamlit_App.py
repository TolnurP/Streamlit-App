import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.set_page_config(layout="wide")

st.title('Netflix subscription fee in different countries')

st.sidebar.title("Sidebar")

st.subheader('Dataframe')
netflix_data = pd.read_csv('netflix.csv')
st.write(netflix_data)

st.sidebar.header("Pick two variables for your plot")
x_val=st.sidebar.selectbox("Pick your X-axis",(netflix_data.columns))
y_val=st.sidebar.selectbox("Pick your Y-axis",(netflix_data.columns))

st.subheader('Plot')
graph = alt.Chart(netflix_data,title=f"{x_val} versus {y_val}").interactive().mark_bar().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    tooltip=[x_val,y_val])
st.altair_chart(graph, use_container_width=True) 