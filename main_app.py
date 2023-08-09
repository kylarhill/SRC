import streamlit as st

# Define the HTML for the centered header
centered_html = '<h1 style="text-align: center;">Sisterhood restorative Project</h1>'
# Display the centered header using st.markdown
st.markdown(centered_html, unsafe_allow_html=True)
		#	==	end	code	from ==
st.write('---')

st.subheader('Our Misison')
st.caption('Empower, uplift, and create lasting bonds among black women.')

st.write('---')

st.subheader('What we\'re offering:')
st.caption('Restorative Circles: Engage in open and honest discussions in a safe space, sharing your experiences, wisdom, and challenges.')
st.caption('Workshops & Activities: Participate in workshops and activities focused on self-care, mindfulness, creativity, and personal growth.')
st.caption('Bonding & Networking: Connect with like-minded women, build meaningful relationships, and expand your circle of sisters.')
st.caption('Community Support: Receive the encouragement and support you deserve as you navigate life\'s journey.')