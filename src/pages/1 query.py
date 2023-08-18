# Imports first:
from pathlib import Path
import streamlit as st
import sys
import os

# Grab the filepath:
filepath = os.path.join(Path(__file__).parents[1])
print(filepath)

# Insert the filepath into the system:
sys.path.insert(0, filepath)

# Import the ToMongo Class now:
from to_mongo import ToMongo

# Instantiate the class:
c = ToMongo()
st.header('Query Page')
st.write('This page will search our database for top grades by subject')
# Now we query the database
# '''
# This is to return information about a card from our database to a user in a friendly format.

# Query the database based off a user input, then display that information back to them.

# Why is this important?

# When a user wants to query(or search) information, and we don't have a local file to reference, we will want to be able to
# plug and play into a database. 

# Also, when build dashboards and applications, knowing how to allow a user to retreive information is critical.

# How will we go about this?
# First, we will use the texct_input function to allow a user to input a card name:
# When we find a match, we will return all info about the card to the user
# The .find() function will give us everythin we need!
queries={
"Best 10 Final Math Grades": c.students.find({"course":"math"}).sort("g3",-1).limit(10),
"Best 10 Sem 2 Math Grades": c.students.find({"course":"math"}).sort("g2",-1).limit(10),
"Best 10 Sem 1 Math Grades": c.students.find({"course":"math"}).sort("g1",-1).limit(10),
"Best 10 Final Portuguese Grades": c.students.find({"course":"portuguese"}).sort("g3",-1).limit(10),
"Best 10 Sem 2 Portuguese Grades": c.students.find({"course":"portuguese"}).sort("g2",-1).limit(10),
"Best 10 Sem 1 Portuguese Grades": c.students.find({"course":"portuguese"}).sort("g1",-1).limit(10)
}
# '''
answer = st.selectbox('select a search criteria',options=queries.keys())
cursor = queries[answer]
try:
    st.write(list(cursor))
except BaseException:
    st.error('invalid query option')


#"course":"portuguese"
