import streamlit as st
import pandas as pd

df = pd.read_csv("Crain's Sponsorship_House Line Item ends 11_30_2024 (refresh=true).csv")

# Create the cross-tabulation
cross_tab = pd.crosstab([df['Date'], df['Line item'], df['Line item ID']], #Index 
                         df['Total impressions']
                       )

# Print the cross-tabulation
st.write(cross_tab)

subset = df['Line item ID']
subset = subset.fillna(0).astype(int)
# print(subset)
unique_lines = subset.drop_duplicates()[:-1]

new_lines = ",".join(unique_lines.astype(str))
# st.write(df)

bigString = 'var oCrainLineItemIds_ = ['
bigString = bigString + new_lines + ",  "
bigString = bigString + "\n  "
bigString = bigString + '//Airtory Line Item Ids  '
bigString = bigString + '6788162314,6795423809,6795423830,6694763698,6694762555,6694763704,6694762684,6694767241,6692784870,6694771588,6694767253,6694767265,6692784897,6695790602,6694767292,6695823800,6692822538,6692822571,6692822325,6695825693,6692822595,6692822346,6692819007,6695825738,6692822631,6504177064,6504805568,6504177262,6421771327,6421771336,6422439572,6709502360,6708338077,6709502363,6708338089,6411235394,6409685232,6409676544,6694830202,6581785579'
bigString = bigString + ']'

st.text_area("Unique Line Items to exclude for Crain's Refresh", bigString, height=200)

# # Replace 'your_file.csv' with the actual path to your CSV file
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
#     try:
#     except Exception as e:
#         st.error(f"Error reading the file: {e}")
# else:
#     st.info("Please upload a CSV file.")
