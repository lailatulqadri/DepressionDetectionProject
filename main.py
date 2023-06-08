import streamlit as st
import pandas as pd

from empath import Empath
lexicon = Empath()

from LeXmo import LeXmo

from nltk.tokenize import word_tokenize

import string

import contractions


#list - important text features for depression identification:
# 1) absolute words - source: https://speakai.co/absolutist-words/
absolutist_word =['absolutely','all','always','complete','completely','constant','constantly','definitely','entire','ever','every','everyone','everything','full','must','never','nothing','totally','whole']
# 2) first person singular & plurl (sometimes we use plural to refer to ourselve)
first_person_singular = ['me','myself', 'i', 'mine', 'my', 'ourself']
first_person_plural = ['we', 'us', 'our', 'ours', 'ourselves']

st.title("Extracting Depression Linguistic Features by using Natural Language Processing")
