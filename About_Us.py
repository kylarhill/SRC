import streamlit as st
from PIL import Image


def add_logo(my_logo, width, height):
    """Read and return a resized logo"""
    logo = Image.open(my_logo)
    modified_logo = logo.resize((width, height))
    return modified_logo

my_logo = add_logo('club_siren.png', width=50, height=60)
st.sidebar.image(my_logo)

# Define the HTML for the centered header
centered_html = '<h1 style="text-align: center;">Sisterhood Restorative Project</h1>'
# Display the centered header using st.markdown
st.markdown(centered_html, unsafe_allow_html=True)
		#	==	end	code	from ==
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
st.write('-Lunch and Dinner on Saturday and Sunday')
st.write('-Anything you create throughout the workshop')
st.write('-Oh! and a small surprise :)')