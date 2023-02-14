import streamlit as st

anita, alina, lars = st.columns(3, gap="medium")

st.markdown("""
# Anita Vishinskaite
### Masters degree student in Digital Humanities and Digital Knowledge at the University of Bologna
Responsible for **data collection** and **data manipulation**

[Contact](mailto:anita.vishinskaite@studio.unibo.it)
""")

st.markdown("""
# Alina Stroyeva
### Bachelors degree student in Media and Communication at the European Humanities University
Responsible for **data analysis** and **storytelling**

[Contact](mailto:alina.stroyeva@studio.unibo.it)
""")

st.markdown("""
# Lars Tønder
### Masters degree student in Computer Science at the Norwegian university of Technology and Science
Responsible for **data visualization** and **web development**

[Contact](mailto:lars.tonder@studio.unibo.it)
""")

# with anita:
#     st.markdown("""
#     ### Anita Vishinskaite
#     **Masters degree student**

#     in **X** at the **University of Bologna**

#     ### Responsible for
#     **data collection** and **data manipulation**

#     ### [Contact](mailto:anita.vishinskaite@studio.unibo.it)
#     """)

# with alina:
#     st.markdown("""
#     ### Alina Stroyeva
#     **Masters degree student**

#     in **X** at **X**
#     ### Responsible for
#     **data analysis** and **storytelling**

#     ### [Contact](mailto:alina.stroyeva@studio.unibo.it)
#     """)

# with lars:
#     st.markdown("""
#     ### Lars Tønder
#     **Masters degree student**

#     in **Computer Science** at the **Norwegian university of Technology and Science**
#     ### Responsible for
#     **data visualization** and **web development**

#     ### [Contact](mailto:lars.tonder@studio.unibo.it)
#     """)