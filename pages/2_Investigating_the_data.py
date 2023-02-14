import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

px.set_mapbox_access_token(open(".mapbox_token").read())

def get_dataframes():
    directory = 'Data'
    dfs = {}
    for filename in os.listdir(directory):
        dfs[filename.removeprefix('serial_killers_').removesuffix('.csv')] = pd.read_csv(directory +'/'+ filename).iloc[: , 1:]
    return dfs

dfs = get_dataframes()

countries = dfs['countries']

education = dfs['education']
education = pd.DataFrame(np.vstack([education.columns, education])).T
education.columns=['Education', 'Percent']

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

elif st.session_state.page == 3: # Genders
    st.markdown("""
        # Divison between genders
        Say something about the fact that there is one intersex and two trans women?
    """)
    fig = px.bar(
        demographics,
        x='Demographic',
        y='Number of people')
    st.plotly_chart(fig, use_container_width=True)
    st.write("Divison between just males and females")
    fig = px.pie(
        demographics.loc[demographics['Demographic'].isin(['Males', 'Females'])],
        values='Number of people',
        names='Demographic')
    st.plotly_chart(fig, use_container_width=True)

elif st.session_state.page == 4: # Education
    st.markdown("""
        # Education
    """)
    # st.write(education)
    fig = px.pie(
        education,
        values='Percent'
    )
    st.plotly_chart(fig, use_container_width=True)

elif st.session_state.page == 5: # 
    st.markdown("""
        # Occupations
        Here we can see the 10 most common occupations in total. Etc.
    """)
    fig = px.bar(
        occupation[:10],
        x="Occupation",
        y=["Male", "Female"])
    st.plotly_chart(fig, use_container_width=True)

    st.write("Here we can see the 10 most common occupations for males. Etc.")
    fig = px.bar(
        occupation.iloc[:, [0,1]].sort_values(by="Male", ascending=False)[:10],
        x="Occupation",
        y="Male")
    st.plotly_chart(fig, use_container_width=True)

    st.write("Here we can see the 10 most common occupations for femals. Etc.")
    fig = px.bar(
        occupation.iloc[:, [0,2]].sort_values(by="Female", ascending=False)[:10],
        x="Occupation",
        y="Female")
    st.plotly_chart(fig, use_container_width=True)


elif st.session_state.page == 6: # Mental conditions
    st.markdown("""
        # Mental conditions
    """)

    # st.write(mental)

    # st.write("Here we can see the 10 most common mental conditions")
    # fig = px.bar(
    #     occupation.iloc[:, [0,1]].sort_values(by="Male", ascending=False)[:10],
    #     x="Occupation",
    #     y="Male")
    # st.plotly_chart(fig, use_container_width=True)

elif st.session_state.page == 7: # Victims
    st.markdown("""
        # Number of victims
    """)
    options = st.selectbox(
        'What gender do you wish to view?',
        ('Total', 'Female', 'Male')
        )
    
    victims['Rank'] = range(1, len(victims)+1)
    victims.set_index('Rank', drop=True, inplace=True)

    victims_female = victims.loc[victims['Gender'] == 'female']
    victims_female['Rank'] = range(1, len(victims_female)+1)
    victims_female.set_index('Rank', drop=True, inplace=True)

    victims_male = victims.loc[victims['Gender'] == 'male']
    victims_male['Rank'] = range(1, len(victims_male)+1)
    victims_male.set_index('Rank', drop=True, inplace=True)

    if options == 'Total':
        st.write("Total")
        st.dataframe(victims.iloc[:,[0,1,2,3]][:10], use_container_width=True)
    elif options == 'Male':
        st.write("Males")
       
        st.dataframe(victims_male.iloc[:,[0,2,3]][:10], use_container_width=True)
    else:
        st.write("Females")
        st.dataframe(victims_female.iloc[:,[0,2,3]], use_container_width=True)

    st.write("How do the genders compare?")
    division = pd.DataFrame({
        'Gender': ['Male', 'Female'],
        'Victims': [victims_male['Victims'].sum(), victims_female['Victims'].sum()]}
        )
    # st.write(division)
    fig = px.pie(division, values='Victims', names='Gender')
    st.plotly_chart(fig)

elif st.session_state.page == 8:
    st.markdown("""
        # Penalties
    """)

else:
    st.markdown("""
        # To conclude
        From what we've seen, most of the serial killers listed above originated from the USA,
        however the biggest concentration of serial killers was in Estonia
        (approximately 0,3 person per 100.000).
        Men become serial killers 7.6 times more often than women.
        Most of the killers were nurses (9,5%), military personnel (7,6%) and physicians (5,5%).
        51% of serial killers got capital punishment, while 38,6% get life imprisonment.
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