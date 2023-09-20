import streamlit as st

centered_html = '<h1 style="text-align: center;">Register Below</h1>'
# Display the centered header using st.markdown
st.markdown(centered_html, unsafe_allow_html=True)	
st.write('---')


url = 'https://docs.google.com/forms/d/e/1FAIpQLSceenpAtEpVHO0rGEUscBRVER26WRZ9MDMXQKnnGf8DR2btXQ/viewform?usp=sf_link'
button_label = 'Register Here'

centered_text = '''
<div style="color: red; text-align: center;">
    Registration is Limited to 20 spots!
</div>
'''

st.markdown(centered_text, unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)
with col2:
	st.markdown(f"[{button_label}]({url})", unsafe_allow_html=True, )
