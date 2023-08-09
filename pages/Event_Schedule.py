import streamlit as st
from PIL import Image
# Define the HTML for the centered header
centered_html = '<h1 style="text-align: center;">Event Schedule</h1>'

centered_html2 = '<h2 style="text-align: center;">October 20-22</h2>'
	
# Display the centered header using st.markdown
st.markdown(centered_html, unsafe_allow_html=True)
		
st.write('---')

image = Image.open('workshop_schedule.png')

st.image(image)