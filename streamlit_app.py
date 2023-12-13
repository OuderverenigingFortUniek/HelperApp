import streamlit as st
import pandas as pd

def get_data():
 df = pd.DataFrame({
    'taken': ["ik bak pannenkoeken", "ik kom 's namiddags opstellen", "ik help bij verdelen na schooltijd"]    
    })
 return df

if 'df' not in st.session_state:
    st.session_state.df = get_data()
df = st.session_state.df

st.write("""
# Helper App
Hallo, Wintersfeer 22/12 komt eraan!
""")

with st.form("my_form"):

  option = st.selectbox('Hoe wil u helpen?',df['taken'], index=None, placeholder="Maak uw keuze")
  name = st.text_input('Uw naam', placeholder= 'Bob')

  if st.form_submit_button('Klaar!'):
    st.session_state.df = get_data()
   
name , ' koos: ', option
