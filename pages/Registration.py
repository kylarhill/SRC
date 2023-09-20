import streamlit as st

st.header('Register Below')
	
st.write('---')
url = 'https://docs.google.com/forms/d/e/1FAIpQLSceenpAtEpVHO0rGEUscBRVER26WRZ9MDMXQKnnGf8DR2btXQ/viewform?usp=sf_link'
button_label = 'Register Here'

col1, col2, col3 = st.columns(3)
with col2:
	st.markdown(':red[Registration is Limited to 20 spots!]')
	st.markdown(f"[{button_label}]({url})", unsafe_allow_html=True, )
