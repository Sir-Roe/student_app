import plotly.express as px
from pathlib import Path
import streamlit as st
import pandas as pd
import os
import sys

#establish a filepath to the orcale_cards.csv file
filepath=os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)

from to_mongo import ToMongo

c=ToMongo()

#grab my collection
cursor=c.students.find()

#list into a dataframe
df =  pd.DataFrame(list(cursor))

# Delete the _id
del df['_id']

#take in an User input
answer=st.selectbox('select a column to visualize',options=list(df.columns))
if answer:
    try:
        st.plotly_chart(px.histogram(df,answer))
    except BaseException:
        st.error(f'''
                 {answer.title()} could not be plotted into a histogram!
                 ''')
