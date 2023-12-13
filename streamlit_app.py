import streamlit as st
import pandas as pd
 
st.write("""
# Helper App
Hallo, wie wil er meewerken aan...

""")

df = pd.DataFrame({
    'taken': ["ik bak pannenkoeken", "ik kom 's namiddags opstellen", "ik help bij verdelen na schooltijd"]    
    })

with st.form("my_form"):

 option = st.selectbox(
    'Hoe wil je helpen?',
     df['taken'])

'U koos: ', option
