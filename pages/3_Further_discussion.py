import streamlit as st

if 'page_d' not in st.session_state:
    st.session_state.page_d = 0

def decrement_page():
    st.session_state.page_d -= 1

def increment_page():
    st.session_state.page_d += 1

def restart():
    st.session_state.page_d = 0

if st.session_state.page_d == 0: # Intro
    st.markdown("""
    # Further discussion

    We will now delve deeper and look at some of the facts on two topics:
    * The three serial killers with the most victims
    * Common motives
    """)

elif st.session_state.page_d == 1: # Top 3
    st.markdown("""
    # The three serial killers with the most victims
    ## Samuel Little (June 7, 1940 - December 30, 2020)
    Samuel Little was an American serial killer and serial rapist.
    In his youth Little attracted the attention of the authorities being arrested
    in eight states for crimes that included driving under the influence,
    fraud, shoplifting, solicitation, armed robbery, aggravated assault, and rape.
    In 2012  he was convicted of the murders of 93 people in California between 1987 and 1989,
    and in 2018 of the murder of one woman in Texas in 1994. 
    The Federal Bureau of Investigation (FBI) has confirmed Little's involvement in at least fifty murders,
    the largest number of proven cases for any serial killer in United States history.
    He allegedly murdered women across nineteen states over a third of a century ending around 2005.



    ## Gary Ridgway (February 18, 1949 - )
    Gary Ridgway, better known as the Green River Killer is an American criminal
    who was the country's deadliest convicted serial killer.
    He claimed to have killed as many as 80 women—many of whom were prostitutes—in Washington
    during the 1980s and '90s, although he pleaded guilty (2003) to only 48 murders.
    
    Gary alleged that after wetting the bed his mother would wash his genitals. 
    He began fantasizing about killing her, and in the mid-1960s he stabbed a young boy.
    Over the next 30 years, he married three times and had a son.
    In 1980 Ridgway was arrested for allegedly choking a prostitute,
    but no charges were filed after he claimed that the woman had bit him.
    Two years later he was arrested for solicitation.
    Ridgway was believed to have begun his killing spree shortly thereafter.
    His first victim was thought to have been a 16-year-old girl.
    Over the next two years, Ridgway raped and killed more than 40 women,
    many of whom were prostitutes or runaways.
    
    Although he initially proclaimed his innocence,
    Ridgway soon confessed to the crimes,
    stating that he wanted to kill as many prostitutes as possible.
    In 2003 he accepted a plea deal in which he was sentenced to 48
    consecutive life sentences without the possibility of parole. 

    ## Salvatore Riina (16 November 1930 - 17 November 2017)
    Salvatore Riina became head of the Corleonesi criminal organization in the mid 1970s.
    Riina had been a fugitive since the late 1960s after he was indicted on a murder charge.
    In violation of established Mafia codes, Riina advocated the killing of women and children,
    and killed blameless members of the public solely to distract law enforcement agencies.
    Hitman Giovanni Brusca estimated he murdered between 100 and 200 people on behalf of Riina.
    As part of the Maxi Trial of 1986,
    Riina was sentenced to life imprisonment in absentia for Mafia association and multiple murder.
    After 23 years living as a fugitive, he was captured in 1993,
    provoking a series of indiscriminate bombings by his organization.
    His lack of repentance subjected him to the stringent Article 41-bis prison regime until
    his death on 17 November 2017.
    """)

elif st.session_state.page_d == 2: # Motives
    st.markdown("""
    # Common motives amongst serial killers

    Serial killers are commonly divided several categories, some of which we will now discuss.
    It should be said that we will now discuss more psycographic divisions,
    but one can also differentiate based on the territory where murderers commit crimes,
    which we can also divide maniacs into "local" and "wandering",
    that is, those who kill in the same region, and those who prefer to move from place to place.

    Serial killers can rarely be attributed to any one type,
    more often they manifest themselves as carriers of mixed characteristics.

    ### Power lovers
    The main motive for the crimes of such people is the assertion of their superiority over the helpless victim,
    the desire to compensate for the feeling of their own inferiority (Bob Berdella, David Berkowitz);
    
    ### Sensualists
    They commit crimes for sexual pleasure (Jeffrey Dahmer, Andrei Chikatilo);
    
    ### Visionaries
    Murderers which suffer from clinical delusions and hallucinations
    (Herbert Mallin, who killed 13 people in order to "prevent an earthquake");
    
    ### Missionaries
    They consider themselves judges, they kill in order to rid society of what they consider "dirt",
    such as prostitutes, homosexuals, people of another race, etc. (Jack the Ripper, Sergei Ryakhovsky);
    
    ### Cannibals
    They commit crimes in order to eat the body of the murdered (Alexander Spesivtsev, Nikolai Dzhumagaliev).

    """)
else:
    st.markdown("""
        # Thank you for joining our journey!
    """)

but1, but2, _ = st.columns((2,2,8))

if st.session_state.page_d == 0:
    but1, but2, _ = st.columns((10,1,1))
    with but1: st.button('Start journey', on_click=increment_page)
elif st.session_state.page_d > 2:
    but1, but2, _ = st.columns((2,3,7))
    with but1: st.button('Previous', on_click=decrement_page)
    with but2: st.button('Restart journey', on_click=restart)
else:
    with but1: st.button('Previous', on_click=decrement_page)
    with but2: st.button('Next', on_click=increment_page)