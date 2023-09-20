import streamlit as st

col1, col2, col3 = st.columns(3)
# Define the HTML for the centered header
with col2:
	st.header('Register Below')
	st.markdown(':red[Registration is Limited to 20 spots!]')
	
st.write('---')
url = 'https://docs.google.com/forms/d/e/1FAIpQLSceenpAtEpVHO0rGEUscBRVER26WRZ9MDMXQKnnGf8DR2btXQ/viewform?usp=sf_link'
button_label = 'Register Here'

with col2:
	st.markdown(f"[{button_label}]({url})", unsafe_allow_html=True, )
