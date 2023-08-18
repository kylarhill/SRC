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
    image = Image.open('no_user.png')
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
    
st.write('---')

ccol1, ccol2 = st.columns(2)

with ccol1:
    image = Image.open('cecl_image.png')
    st.write('''The Center for Community Engaged Learning (CECL) aims to “bridge Fordham University with our neighboring communities and 
             global partners through experiential learning, research, and civic engagement.” The CECL’s vision to 
             accomplish its mission involves engaging “every member of the University as active citizens in the alleviation of 
             poverty, the promotion of justice, the protection of human rights, and respect for the environment.''')
    st.write('''The values the CECL strive to uphold include experiential learning for social justice, asset-based community development, anti-racist pedagogies,
              Ignatian Pedagogical Paradigm, Catholic Social Teaching, and Student success. As a sponsor for the Sisterhood Restorative Project, the CECL exemplifies
              its unwavering commitment to uplifting individuals and communities through education.
              The project, aligned with CECL's ethos, fulfills its mission by facilitating participants'
              comprehension of the impact of community engagement on personal and spiritual growth and interpersonal relationships.''')
    st.write('Thank you for your sponsorship')

    

with ccol2:
    image = Image.open('parmach_headshot.png')
    st.write('''Robert Parmach, Ph.D., for over two decades, has dedicated a significant portion of his career to incorporating
              Jesuit values, teachings, and practices into various aspects of the Fordham University community.
              He has held several roles, including first-year class dean, professor, and leader of the Manresa program. ''')
    
    st.write('''Parmach's emphasis on "instigating our head, our heart, and our hands" is a compelling message that encourages 
            individuals to engage fully on intellectual, emotional, and practical levels. This message suggests a holistic
             approach to personal and professional growth, aligning well with Jesuit education ideals encompassing academic learning, 
            personal development, and engagement with the community.''' )
    st.write('''In addition to his contributions hosting events where the university community can learn about the Ignatian values and
              mission, Parmach is a sponsor for the upcoming Black Women Restorative Workshop. This workshop aligns with his long-standing
              commitment to incorporating Jesuit values, teachings, and practices into various aspects of his work and the university community.''')
    st.write('Thank you for your sponsorship')
    
