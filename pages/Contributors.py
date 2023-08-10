import streamlit as st
from PIL import Image

centered_html = '<h1 style="text-align: center;">Contributors</h1>'
st.markdown(centered_html, unsafe_allow_html=True)
st.write('---')

col1, col2 = st.columns(2)

with col1:
    image = Image.open('src_headshot.png')
    st.image(image)
    st.write('''Kyla Hill graduated from FCRH in 2023 with a BA in Economics and International Political Economy. She is now pursuing an MS in Management from Fordham's Gabelli School of Business.
                Born and raised in Springfield, Massachusetts, she spent much of her childhood performing on
                stages and participating in competitive sports. She also spent much of her youth songwriting and
                making music. She is an accomplished sprinter on Fordham's Women's T&F team and has one more year left to keep breaking records.'''
             )
    st.write('''While taking a theology course at Fordham University called Scripture and Trauma, for a project, Kyla created the framework for a
                retreat aimed at building a space for black women to confront transgenerational trauma and
                damaging stereotypes. She has decided to repurpose her work to fit the Fordham environment.'''
             )
    
with col2:
    #image - Image.open('arel_headshot.png')
    st.write('''Stephanie Arel has taught theology at Fordham since 2019. She designed the sacred texts course
            Scripture and the Human Response to Trauma in 2021. Before coming to Fordham, she won an
            Andrew W. Mellon Fellowship that funded research at the National September 11 Memorial &amp;
            Museum exploring the effects of commemorating mass trauma. The inquiry extended into
            multiple countries including Bosnia Herzegovina, South Africa, and Cambodia and comes to
            fruition in Bearing Witness: The Wounds of Mass Trauma at Memorial Museums (Fortress Press,
            2023). During that time, she also held a position as a visiting researcher at New York University
            (2017-2019). ''')
             
    st.write('''She is the author of Affect Theory, Shame and Christian Formation (Palgrave
            Macmillan 2016) and co-editor of Post-Traumatic Public Theology (Palgrave Macmillan 2016)
            and Ideology and Utopia in the Twenty-First Century: The Surplus of Meaning in Ricoeur&#39;s
            Dialectical Concept (Lexington 2018). Her involvement in trauma studies stems from three years
            of work at an Eating Disorder Hospital and in-depth training in treatment for trauma in the
            clinical setting from the New York Institute of Psychoanalysis.''')
