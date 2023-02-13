import os
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

def get_dataframes():
    directory = 'data'
    dfs = {}
    for filename in os.listdir(directory):
        dfs[filename.removeprefix('serial_killers_').removesuffix('.csv')] = pd.read_csv(directory +'/'+ filename).iloc[: , 1:]
    return dfs

dfs = get_dataframes()

countries = dfs['countries']
education = dfs['education']
mental = dfs['mental_conditions']
victims = dfs['most_victims']
occupation = dfs['occupation']
penalty = dfs['penalty']
demographics = dfs['stats']
demographics = pd.DataFrame(np.vstack([demographics.columns, demographics])).T
demographics.columns=['Demographic', 'Number of people']

"""
# Serial killers
"""

pie = px.pie(demographics, values='Number of people', names='Demographic')
bar = px.bar(demographics.sort_values(by=['Number of people']), y='Number of people', x='Demographic')
fig = px.choropleth(
    countries,
    locations="Country Code",
    color="Total",
    hover_name="Country",
    range_color=[20,80])

if st.checkbox('Show temporary charts'):
    st.plotly_chart(pie, use_container_width=True)
    st.plotly_chart(bar, use_container_width=True)
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Show dataframes'):
    for i, (key, df) in enumerate(dfs.items()):
        f"## {key}"
        st.write(df)



# st.bar_chart()

# if st.checkbox('Show dataframe'):

# with col1:

# with col2:
#     if st.checkbox('Show line chart'):
#         chart_data = pd.DataFrame(
#             np.random.randn(20, 3),
#             columns=['a', 'b', 'c'])

#         st.line_chart(chart_data)

# "# Map example"
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

# "# Widgets"
# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)
