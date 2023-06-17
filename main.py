import streamlit as st

import json
import contractions

st.title("Extracting Depression Linguistic Features by using Natural Language Processing")



#read input from user
input_text = st.text_input("Please add a sentence that you want to analyse.")
analyse_button = st.button("Analyse")

if analyse_button:
  st.write("i got you!")

          



