import streamlit as st

import json
import contractions

st.title("Extracting Depression Linguistic Features by using Natural Language Processing")


  
# Opening JSON file
f = open('depression_lexicon.json',r)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
signal_1 = []
for i in data['signal_1']:
    i = i.replace("_", " ")
    i = contractions.fix(i)
    #print(i)
    signal_1.append(i)

signal_2 = []
for i in data['signal_2']:
    i = i.replace("_", " ")
    i = contractions.fix(i)
    #print(i)
    signal_2.append(i)

signal_3 = []
for i in data['signal_3']:
    i = i.replace("_", " ")
    i = contractions.fix(i)
    #print(i)
    signal_3.append(i)

signal_4 = []
for i in data['signal_4']:
    i = i.replace("_", " ")
    i = contractions.fix(i)
    #print(i)
    signal_4.append(i)

signal_5 = []
for i in data['signal_5']:
    i = i.replace("_", " ")
    i = contractions.fix(i)
    #print(i)
    signal_5.append(i)

signal_6 = []
for i in data['signal_6']:
    i = i.replace("_", " ")
    i = contractions.fix(i)
    #print(i)
    signal_6.append(i)

signal_7 = []
for i in data['signal_7']:
    i = i.replace("_", " ")
    i = contractions.fix(i)
    #print(i)
    signal_7.append(i)

signal_8 = []
for i in data['signal_1']:
    i = i.replace("_", " ")
    i = contractions.fix(i)
    #print(i)
    signal_8.append(i)

signal_9 = []
for i in data['signal_9']:
    i = i.replace("_", " ")
    i = contractions.fix(i)
    #print(i)
    signal_9.append(i)

signal_10 = []
for i in data['signal_10']:
    i = i.replace("_", " ")
    i = contractions.fix(i)
    #print(i)
    signal_10.append(i)

st.write(signal_1,"\n", signal_2,"\n", signal_3)

# Closing file
f.close()

#read input from user
input_text = st.text_input("Please add a sentence that you want to analyse.")

list_symptoms =[signal_1, signal_2, signal_3, signal_4, signal_5, signal_6, signal_7, signal_8, signal_9, signal_10] 

#check if depression signal 1 in input sentence
for s_list in list_symptoms:
  for s in s_list:
      if s in inp:
          st.write(s,' signal detected')
          



