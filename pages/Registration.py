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
<br>

'''

st.markdown(centered_text, unsafe_allow_html=True)

centered_button = f'''
<div style="text-align: center;">
    [{button_label}]({url})
</div>
'''

st.markdown(centered_button, unsafe_allow_html=True)



