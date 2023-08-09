import streamlit as st
# Define the HTML for the centered header
centered_html = '<h1 style="text-align: center;">Register Below</h1>'
# Display the centered header using st.markdown
st.markdown(centered_html, unsafe_allow_html=True)
		#	==	end	code	from ==
st.write('---')
url = 'https://docs.google.com/forms/d/e/1FAIpQLSceenpAtEpVHO0rGEUscBRVER26WRZ9MDMXQKnnGf8DR2btXQ/viewform?usp=sf_link'
button_label = 'Register Here'

st.markdown(f"[{button_label}]({url})", unsafe_allow_html=True, )
