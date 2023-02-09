import streamlit as st
import pandas as pd
import numpy as np

"""
# My first app
Here's our first attempt at using data to create a table:
"""

col1, col2 = st.columns(2)


with col1:
    if st.checkbox('Show dataframe'):
        dataframe = pd.DataFrame(
            np.random.randn(10, 20),
            columns=('col %d' % i for i in range(20)))

        st.dataframe(dataframe.style.highlight_max(axis=0))

with col2:
    if st.checkbox('Show line chart'):
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])

        st.line_chart(chart_data)

"# Map example"
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

"# Widgets"
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)