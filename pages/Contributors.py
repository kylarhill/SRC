import streamlit as st
from PIL import Image

centered_html = '<h1 style="text-align: center;">Contributors</h1>'
st.markdown(centered_html, unsafe_allow_html=True)
st.write('---')

col1, col2 = st.columns(2)

with col1:
    image = Image.open('attachments/srp_headshot.png')
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
    image = Image.open('attachments/arel_headshot.png')
    st.image(image)
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
    image = Image.open('attachments/bridges_pic.png')
    st.image(image)
    st.write('''Christine K. Bridges is an ordained Itinerant Elder of the African Methodist Episcopal Church. 
              While serving in the women’s ministry at the Greater Allen A.M.E. Cathedral (GAC), 
             pastored by Reverend Drs. Floyd H. and Elaine M. Flake, she was introduced to Womanist Theology.''')
    st.write('''She received a Master of Divinity from New Brunswick Theological Seminary.  
             She completed the clinical pastoral education training and certification as a 
             Board-Certified Clinical Chaplain and Pastoral Counselor (BCCC/PC) with the College of Pastoral 
             Supervision and Psychotherapy, Inc. (CPSP).  She is a Registered Nurse with a Bachelor of Science in Nursing 
             from S.U.N.Y., Stony Brook and has clinical / managerial community health experience with Visiting Nurse 
             Serve of New York.  ''')
    st.write('''Her approach to ministry embraces womanism (“…Loves struggle. Loves the Folk. Loves herself. Regardless.” 
             Alice Walker, In Search of Our Mother’s Gardens: Womanist Prose, Jovanovich,1984).''')
    st.write('''As Chaplain of the Cancer Center and Palliative Care Team at NYC Health + Hospitals/ Queens 
             (2015-2022) she provided spiritual care to persons diagnosed with life limiting illnesses or who 
             are dying and offered grief counseling for caregivers and staff.''')
    st.write('''Her prophetic passion is to embark upon an “Inspired Journey,” embodying God’s
              compassion and the creative power of contemplative practices of breathing, and centering 
             prayers for persons coping with anxiety, embodied trauma and grief.''')
    st.write('''She designed and facilitated small group workshops focused on sharing personal sacred narratives for,
              “I’m Just Saying” Women’s Retreats presented by Rev. Dr. Francine Hernandez of L&F Consultants, Inc. 
             before relocating to Delaware.''')
    st.write('''She is Co-Facilitator for “Sisters Believing In Wellness” (SBW) Womanist 
             Gathering Project which affirms the full humanity of ALL women reading sacred texts with
              the intention of receiving the life, love and liberty of God.''')
    
st.write('---')

st.markdown('And a special thanks to our sponsors **Dean Parmach** and **CECL**!')