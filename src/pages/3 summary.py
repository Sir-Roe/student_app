import streamlit as st


st.title("Summary Page for MTG Tracer")
st.text('''
        This application was designed to show my ability to connect to mongodb and present
        the data via streamlit in my own application.
''')

st.image('https://logos-download.com/wp-content/uploads/2016/09/MongoDB_logo_Mongo_DB.png')

st.write('''
        I do not believe the data particularly needing to be within a no sql data base due to how incredibly
        small and tabular it is. But this was a requirement of the assignment.
        ''')

st.write('Technologies used: Streamlit, Python, Pandas, Plotlyexpress')