import streamlit as st

def display_intro():
    return st.markdown("""
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