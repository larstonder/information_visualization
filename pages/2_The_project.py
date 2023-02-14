import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

def get_dataframes():
    directory = 'Data'
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

if 'page' not in st.session_state:
    st.session_state.page = 0

def decrement_page():
    st.session_state.page -= 1

def increment_page():
    st.session_state.page += 1

def restart():
    st.session_state.page = 0

# --- Page start ---

if st.session_state.page == 0: # INTRO
    st.markdown("""
        # Murder history
        The project “Murder History” is dedicated to serial killers, their histories, motives,
        and analysis related to origin, sex, occupation of murders.
        Referring to the datasets made publicly available by the wikidata,
        we are aiming to understand which criteria have been decisive in committing murders.

        **The investigation tries to answer some question to better cover the topic:**

        * Which countries do the most serial killers originate from? 
        * How many percent is the number of serial killers per 100 thousand of the population of these countries? 
        * How many of them are men and women?
        * How many of them had higher education? 
        * What was their occupation? 
        * How many of them had mental conditions? 
        * Who had the biggest number of victims? 
        * What penalties did they receive? 
    """)

elif st.session_state.page == 1: # ORIGINS
    st.markdown("""
        # Origins
        As shown in the map below, ... 
    """)
    fig = px.choropleth(
        countries,
        locations="Country Code",
        color="Total",
        hover_name="Country",
        labels={'Total':'Total serial killers'},
        color_continuous_scale=px.colors.sequential.Plasma)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, geo_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("The US has many more ...")
    bar = px.bar(countries, y='Total', x='Country')
    st.plotly_chart(bar, use_container_width=True)

elif st.session_state.page == 2:
    st.markdown("""
        # Serial killers per capita
    """)

elif st.session_state.page == 3:
    st.markdown("""
        # Divison between genders
    """)

elif st.session_state.page == 4:
    st.markdown("""
        # Education
    """)

elif st.session_state.page == 5:
    st.markdown("""
        # Occupations
    """)

elif st.session_state.page == 6:
    st.markdown("""
        # Mental conditions
    """)

elif st.session_state.page == 7:
    st.markdown("""
        # Victims
    """)

elif st.session_state.page == 8:
    st.markdown("""
        # Penalties
    """)

else:
    st.markdown("""
        # Thank you for joining us on this journey!
    """)

# --- Buttons ---

but1, but2, _ = st.columns((2,2,8))

if st.session_state.page == 0:
    but1, but2, _ = st.columns((10,1,1))
    with but1: st.button('Start journey', on_click=increment_page)
elif st.session_state.page > 8:
    but1, but2, _ = st.columns((2,3,7))
    with but1: st.button('Previous', on_click=decrement_page)
    with but2: st.button('Restart journey', on_click=restart)
else:
    with but1: st.button('Previous', on_click=decrement_page)
    with but2: st.button('Next', on_click=increment_page)