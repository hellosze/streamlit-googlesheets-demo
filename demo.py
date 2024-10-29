import streamlit as st
import pandas as pd

df = pd.read_csv("Crain's Sponsorship_House Line Item ends 11_30_2024 (refresh=true).csv")
# st.write(df)


st.write('var oCrainLineItemIds_ = [')
st.write(']')
  
# # Replace 'your_file.csv' with the actual path to your CSV file
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
#     try:
#     except Exception as e:
#         st.error(f"Error reading the file: {e}")
# else:
#     st.info("Please upload a CSV file.")
