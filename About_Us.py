import streamlit as st
from PIL import Image



# Define the HTML for the centered header
centered_html = '<h1 style="text-align: center;">Sisterhood Restorative Project</h1>'
# Display the centered header using st.markdown
st.markdown(centered_html, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col2:
	image = Image.open('attachments/srp_graphic.png')
	st.image(image)

st.write('---')

st.subheader('Our Misison')
st.markdown('_Empower, uplift, and create lasting bonds among black women._')

st.write('---')

st.subheader('What we\'re offering:')
st.markdown('**Restorative Circles:** Engage in open and honest discussions in a safe space, sharing your experiences, wisdom, and challenges.')
st.markdown('**Workshops & Activities**: Participate in workshops and activities focused on self-care, mindfulness, creativity, and personal growth.')
st.markdown('**Bonding & Networking**: Connect with like-minded women, build meaningful relationships, and expand your circle of sisters.')
st.markdown('**Community Support**: Receive the encouragement and support you deserve as you navigate life\'s journey.')

st.write('---')

st.subheader('What\'s Included:')
st.write('-Coffee on Saturday')
st.write('-Breakfast and coffee on Sunday')
st.write('-Lunch on Saturday and Sunday')
st.write('-Dinner on Saturday')
st.write('-Anything you create throughout the workshop')
st.write('-Oh! and a small surprise :)')