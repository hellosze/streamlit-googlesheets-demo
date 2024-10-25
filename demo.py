# # streamlit_app.py

# import streamlit as st
# from streamlit_gsheets import GSheetsConnection

# # Create a connection object.
# conn = st.connection("gsheets", type=GSheetsConnection)

# df = conn.read(
#     worksheet="Sheet1",
#     ttl="10m",
#     usecols=[0, 1],
#     nrows=3,
# )

# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1cpwK088ub8LCVNTo6hQYsBTZstJX026h9zZiS-tLg1U/edit?gid=71029213#gid=71029213"
# url = "https://docs.google.com/spreadsheets/d/1LZ4bPm1lVFfSTc8GOj98Nzo1uWgDbb2QaB451vohtT8/edit?gid=0#gid=0"
conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)
