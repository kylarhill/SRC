import streamlit as st
from PIL import Image
# Define the HTML for the centered header
centered_html = '<h1 style="text-align: center;">Event Schedule</h1>'

	
# Display the centered header using st.markdown
st.markdown(centered_html, unsafe_allow_html=True)

st.write('---')

image = Image.open('attachments/workshop_schedule.png')

st.image(image)

st.write('---')

st.markdown('**Meditation:** Through meditation, we will enhance mind-body connection, foster emotional regulation, build resilience, create a safe space for processing, promote empowerment, and nurture self-compassion.')
st.markdown('**Narrative Group Work:** Confront familiar narratives and stereotypes about black women through discussion')
st.markdown('**Restorative Yoga:** Gentle and therapeutic style of yoga that focuses on relaxation, deep rest, and rejuvenation; beneficial for reducing stress, calming the nervous system, and promoting overall well-being.')
st.markdown('**Speaker/Q&A:** With Professor Stephanie Arel (see contributors page for more information about her)')
st.markdown('**Dinner:** With Dean Parmach')
st.markdown('**Podcast & Group Discussion:** A conversation between Dr. Joy Harden Bradford and  Dr. Yaba Blay,  licensed psychologists. It discusses the "system of white supremacy, skin color politics, and the role of the media in shaping our ideas about who we" (black women) are')
st.markdown('**Art Group Work:** Confront perceptions of Black women as invisible, undesirable, and a challenge through art')
st.markdown('**Celebratory Service:** A Christian religious service where we will celebrate ourselves with Reverend Christine Bridges.')
st.markdown('**Poetry Group Work:** Write poetry to your "younger self" to foster healing')