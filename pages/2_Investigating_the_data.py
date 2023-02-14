import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os


# --------- Setup ---------

def get_dataframes():
    directory = 'Data'
    dfs = {}
    for filename in os.listdir(directory):
        dfs[filename.removeprefix('serial_killers_').removesuffix('.csv')] = pd.read_csv(directory +'/'+ filename).iloc[: , 1:]
    return dfs

dfs = get_dataframes()

countries = dfs['countries']

education = dfs['education_stats']
education = pd.DataFrame(np.vstack([education.columns, education])).T
education.columns=['Education', 'Number of people']

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

# --------- Page start ---------

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
        As shown in the map below, there doesn't seem to be many other countries that the US that struggle
        with many serial killers.
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

    st.markdown("""
        The following chart confirms our supsicions that were discussed earlier.
        The US has almost ***five times*** as many serial killers than the next country on the list, which is
        Russia (we also have the Soviet Union, but we only discuss current countries).
    """)
    bar = px.bar(countries, y='Total', x='Country')
    st.plotly_chart(bar, use_container_width=True)

    st.markdown("""
        ## Serial killers per 100, 000 people
        While the US still ranks highly when counting the number of serial killers per 100, 000 people,
        we now have some interesting outliers that we coulnd't see before. As an example,
        countries such as Australia actually ranks higher, with approximately 0.02 more serial killers
        per 100, 000 than the US. Surprisingly, the two highest ranking countries are Iceland and Estonia,
        with respectively 0.27 and 0.29 serial killers per 100, 000 people.
    """)
    fig = px.choropleth(
        countries,
        locations="Country Code",
        color='Rate per 100,000',
        hover_name="Country",
        labels={'Rate per 100,000':'Rate per 100,000'},
        color_continuous_scale=px.colors.sequential.Plasma)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, geo_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

elif st.session_state.page == 2: # Genders
    st.markdown("""
        # Divison between genders
        There are in total 1099 people in the world that can be categorized as serial killers.
        Of these, there are **946 males**, **134 females**, **two trans females** and **one intersex**.
        """)
    demographics = demographics[demographics['Demographic'] != 'Total']
    fig = px.bar(
        demographics.sort_values(by='Number of people', ascending=False),
        x='Demographic',
        y='Number of people')
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
        That means that males account for a staggering **87.3%** of all serial killers.
        Women, on the other hand, account for almost all the rest, with **12.4%**.
    """)
    fig = px.pie(
        demographics,
        # demographics.loc[demographics['Demographic'].isin(['Males', 'Females'])],
        values='Number of people',
        names='Demographic')
    st.plotly_chart(fig, use_container_width=True)

elif st.session_state.page == 3: # Education
    st.markdown("""
        # Education
        We might have thought that serial killers must be really smart and savvy.
        As listed below, only 30% of the total amount had higher education.
        While quite a few who initially enrolled in college didn't make it all the way to a degree,some did.
        A few went even further. The degrees at tend to cluster in certain areas:
        medicine, education, the social sciences, or a practical discipline.
    """)
    # st.write(education)
    fig = px.pie(
        education,
        values='Number of people',
        names='Education'
    )
    st.plotly_chart(fig, use_container_width=True)

elif st.session_state.page == 4: #
    st.markdown("# Occupations")
    options = st.selectbox(
        'What gender do you wish to view data for?',
        ('Total', 'Female', 'Male'))
    
    if options == 'Total':
        st.markdown("""
            Here we can see the 10 most common occupations in total.
        """)
        fig = px.bar(
            occupation[:10],
            x="Occupation",
            y=["Male", "Female"])
        st.plotly_chart(fig, use_container_width=True)
    elif options == 'Male':
        st.write("Here we can see the 10 most common occupations for males.")
        fig = px.bar(
            occupation.iloc[:, [0,1]].sort_values(by="Male", ascending=False)[:10],
            x="Occupation",
            y="Male")
        st.plotly_chart(fig, use_container_width=True)
    elif options == 'Female':
        st.write("Here we can see the 10 most common occupations for females.")
        fig = px.bar(
            occupation.iloc[:, [0,2]].sort_values(by="Female", ascending=False)[:10],
            x="Occupation",
            y="Female")
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
        Taken as a whole, certain patterns emerge in the occupations chosen by serial killers,
        with some full-time and part-time jobs over-represented.
        So much so, in fact, that over the last 50 years, some dominant patterns have emerged.
        Obviously, not everyone occupying these jobs is a serial killer,
        nor are they likely to become one.
        But there's something about these jobs that is inherently appealing to offenders,
        or that otherwise cultivates the impulses of serial killers-in-waiting and causes
        them to be curiously over-represented among this rare breed of murderer.
    """)

elif st.session_state.page == 5: # Mental conditions
    st.markdown("""
        # Mental illnesses
    """)

    options = st.selectbox(
        'What gender do you wish to view data for?',
        ('Total', 'Female', 'Male')
        )
    
    st.markdown("""
        In the wake of a violent murder forensic psychologists typically examine the mental
        correlates of criminality. In order to get to the root of a behavior,
        these justice system professionals will often ask such questions as:

        * Did the accused have a troubled childhood?
        * Does (s)he exhibit empathy for others?
        * Does (s)he self-medicate with drugs or alcohol?

        Not surprisingly, many criminals have been diagnosed with mental illnesses
        and may be suffering from co-occurring substance abuse.
        So what are some of the most common psychological disorders associated with serial killers?
    """)
    
    mental = mental[mental['Total'] != 0]
    mental['Rank'] = range(1, len(mental)+1)
    mental.set_index('Rank', drop=True, inplace=True)

    mental_female = mental.loc[:, mental.columns != 'Male']
    mental_female = mental_female[mental_female['Female'] != 0]
    mental_female['Rank'] = range(1, len(mental_female)+1)
    mental_female.set_index('Rank', drop=True, inplace=True)

    mental_male = mental.loc[:, mental.columns != 'Female']
    mental_male['Rank'] = range(1, len(mental_male)+1)
    mental_male.set_index('Rank', drop=True, inplace=True)

    if options == 'Total':
        # st.dataframe(penalty.iloc[:,[0,1,2,3]][:10], use_container_width=True)
        st.markdown("""
            Here we can see the ten most common mental illnesses across all genders.
        """)
        fig = px.bar(mental[:10], x='Mental Illness', y=['Male', 'Female'])
        st.plotly_chart(fig, use_container_width=True)
    elif options == 'Male':
        # st.dataframe(penalty_male.iloc[:, [0,1]], use_container_width=True)
        st.markdown("""
            For the males, most of the diagnosed serial killers was diagnosed with
            antisocial personality disorder.
        """)
        fig = px.bar(mental_male[:10], x='Mental Illness', y='Male')
        st.plotly_chart(fig, use_container_width=True)
    elif options == 'Female':
        st.markdown("""
            Interestingly, of all the female serial killers, only one has been diagnosed with
            a mental illness.
        """)
        # st.dataframe(penalty_female.iloc[:, [0,1]], use_container_width=True)
        fig = px.bar(mental_female[:10], x='Mental Illness', y='Female')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
        Mental illnesses have been found in some of the serial killers,
        but it's important to note that most people suffering from these
        illnesses do not commit any violent offenses.
        These instances of mental disorders represent only a small fraction
        of people diagnosed and the majority of people afflicted do not
        engage in criminal activity, especially if given proper treatment and social support.
    """)

elif st.session_state.page == 6: # Victims
    st.markdown("""
        # Number of victims
    """)
    options = st.selectbox(
        'What gender do you wish to view data for?',
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
        st.markdown("""
            This is the ten serial killers with the most victims.
            We can see from the data that all in the top 10 are male. In fact,
            the first female on the list is all the way down in nr. 17,
            which is Irina Gaidamachuk from Russia with 17 victims.
        """)
        fig = px.bar(
            victims[:10],
            x='Serial Killer',
            y='Victims',
            hover_data=['Serial Killer', 'Victims', 'Gender'])
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("""
            We can seem to see a trend forming:
            Again, males account for most victims. Now at an all time high, a staggering
            **91.1%** of all victims are killed by males. Since the number of male serial killers
            were at 87.3%, that means that each male serial killer in average has more
            victims than the females, who now account for **8.92%** of the victims.
        """)
        division = pd.DataFrame({
            'Gender': ['Male', 'Female'],
            'Victims': [victims_male['Victims'].sum(), victims_female['Victims'].sum()]}
            )
        fig = px.pie(division, values='Victims', names='Gender')
        st.plotly_chart(fig)
    elif options == 'Male':
        st.write("This is the ten male serial killers with the most victims...")
        fig = px.bar(
            victims_male[:10],
            x='Serial Killer',
            y='Victims',
            hover_data=['Serial Killer', 'Victims'])
        st.plotly_chart(fig, use_container_width=True)
    elif options == 'Female':
        st.write("This is the ten female serial killers with the most victims...")
        fig = px.bar(
            victims_female[:10],
            x='Serial Killer',
            y='Victims',
            hover_data=['Serial Killer', 'Victims'])
        st.plotly_chart(fig, use_container_width=True)

elif st.session_state.page == 7:
    st.markdown("""
        # Penalties
    """)

    options = st.selectbox(
        'What gender do you wish to view data for?',
        ('Total', 'Female', 'Male')
        )
    
    penalty = penalty[penalty['Total'] != 0]
    penalty['Rank'] = range(1, len(penalty)+1)
    penalty.set_index('Rank', drop=True, inplace=True)

    penalty_female = penalty.loc[:, penalty.columns != 'Male']
    penalty_female = penalty_female[penalty_female['Female'] != 0]
    penalty_female['Rank'] = range(1, len(penalty_female)+1)
    penalty_female.set_index('Rank', drop=True, inplace=True)

    penalty_male = penalty.loc[:, penalty.columns != 'Female']
    penalty_male['Rank'] = range(1, len(penalty_male)+1)
    penalty_male.set_index('Rank', drop=True, inplace=True)

    if options == 'Total':
        # st.dataframe(penalty.iloc[:,[0,1,2,3]][:10], use_container_width=True)
        st.markdown("""
            Here we can see the ten most common penalties. As one would assume,
            most serial killers are given either capital punishment or life imprisonment.
            What may be surprising to some is the fact that capital punishment,
            or the death penalty, is the most common out of all punishments.
            This is probably due to the fact that the country with the most serial killers is the US,
            where death penalties are still allowed and widely practiced.
        """)
        fig = px.bar(penalty[:10], x='Penalty', y=['Male', 'Female'])
        st.plotly_chart(fig, use_container_width=True)
    elif options == 'Male':
        # st.dataframe(penalty_male.iloc[:, [0,1]], use_container_width=True)
        st.write("What can we see from this data?")
        fig = px.bar(penalty_male[:10], x='Penalty', y='Male')
        st.plotly_chart(fig, use_container_width=True)
    elif options == 'Female':
        st.write("What can we see from this data?")
        # st.dataframe(penalty_female.iloc[:, [0,1]], use_container_width=True)
        fig = px.bar(penalty_female[:10], x='Penalty', y='Female')
        st.plotly_chart(fig, use_container_width=True)

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

# --------- Buttons ---------

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