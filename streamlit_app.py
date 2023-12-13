import streamlit as st
import pandas as pd
 
st.write("""
# Helper App
Hallo, Wintersfeer 22/12 komt eraan!
""")

df = pd.DataFrame({
    'taken': ["ik bak pannenkoeken", "ik kom 's namiddags opstellen", "ik help bij verdelen na schooltijd"]    
    })

with st.form("my_form"):

  option = st.selectbox(
    'Hoe wil je helpen?',
     df['taken'])

  name = st.text_input('Uw naam', placeholder= 'Bob')
  st.form_submit_button('Klaar!')

'U koos: ', option
