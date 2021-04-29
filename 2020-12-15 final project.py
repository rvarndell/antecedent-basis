#!/usr/bin/env python
# coding: utf-8

# Useful links:
# * https://www.youtube.com/watch?v=THduWAnG97k 
# * https://spacy.io/usage/spacy-101

# Claim Text I Made Up:
# ***
# **A vehicle** containing:
# **a first passenger** and **a second passenger**,
# where <font color='red'>the passenger</font>  jumps out <font color='blue'>the window</font> of <font color='green'>the vehicle</font>.
# ***
# * **bold** are words that may have another words that rely on it for antecedent basis
# * <font color='red'>red</font> are words that have incorrect 112 2nd antecedent basis and should have a 112 2nd rejection
# * <font color='blue'>blue</font> are words that have incorrect 112 2nd antecedent basis and should be objected to
# * <font color='green'>green</font> are words that have correct 112 2nd antecedent basis

# Claim Text for an Automobile:<br>
# from: https://www.nolo.com/legal-encyclopedia/sample-patent-claims-common-inventions.html
# 
# ***
# **A  vehicle**, comprising:
# **a body carriage** having **rotatable wheels** mounted thereunder for enabling <font color='green'> said body carriage </font> to roll along **a surface**
# **an engine** mounted in <font color='green'>said carriage</font> for producing rotational energy, and
# means for controllably coupling rotational energy from <font color='green'> said engine </font> to at least one of <font color='green'> said wheels </font> ,
# whereby <font color='green'> said carriage</font> can be propelled along <font color='green'> said surface</font>.
# ***
# * **bold** are words that may have another words that rely on it for antecedent basis
# * <font color='red'>red</font> are words that have incorrect 112 2nd antecedent basis and should have a 112 2nd rejection
# * <font color='blue'>blue</font> are words that have incorrect 112 2nd antecedent basis and should be objected to
# * <font color='green'>green</font> are words that have correct 112 2nd antecedent basis

# Claim for the Process of Sewing:<br>
# from: https://www.nolo.com/legal-encyclopedia/sample-patent-claims-common-inventions.html
# 
# ***
# **A method** for joining **a cloth** together, comprising the steps of:
# providing  <font color='green'> said cloth </font> and positioning **the cloth** together so that **an edge portion of one piece** overlaps **an adjacent edge portion** of <font color='green'> the other piece </font>, and
# passing **a thread** repeatedly through and along <font color='green'>the overlapping portions </font> in sequentially opposite directions and through sequentially spaced holes in <font color='green'>said overlapping adjacent portions </font>,
# whereby <font color='red'>said two pieces of cloth</font> will be attached along <font color='green'>said edge portions</font>.
# ***
# * **bold** are words that may have another words that rely on it for antecedent basis
# * <font color='red'>red</font> are words that have incorrect 112 2nd antecedent basis and should have a 112 2nd rejection
# * <font color='blue'>blue</font> are words that have incorrect 112 2nd antecedent basis and should be objected to
# * <font color='green'>green</font> are words that have correct 112 2nd antecedent basis

# Claim for a Pencil:<br>
# from: https://www.nolo.com/legal-encyclopedia/sample-patent-claims-common-inventions.html
# 
# ***
# **A hand-held writing instrument** comprising:
# **an elongated core-element means** that will leave **a marking line** if moved 
# across **a paper or other similar surface**, and
# **an elongated holder** surrounding and encasing said <font color='green'> elongated core element means</font>, one portion of <font color='green'> said holder </font> being removable from **an end** thereof to expose **an end** of <font color='green'>said core-element means </font> so as to enable <font color='red'> said core-element means </font>to be exposed for writing,
# whereby <font color='red'>said holder </font> protects <font color='red'> said core element means</font> from breakage and provides **an enlarged means** for holding <font color='red'>  said core-element means </font> conveniently.
# ***
# * **bold** are words that may have another words that rely on it for antecedent basis
# * <font color='red'>red</font> are words that have incorrect 112 2nd antecedent basis and should have a 112 2nd rejection
# * <font color='blue'>blue</font> are words that have incorrect 112 2nd antecedent basis and should be objected to
# * <font color='green'>green</font> are words that have correct 112 2nd antecedent basis

# Claim for Concrete:<br>
# from: https://www.nolo.com/legal-encyclopedia/sample-patent-claims-common-inventions.html
# 
# ***
# **A rigid building and paving material** comprising **a mixture of: a sand and stones**, and **a hardened cement binder filling** <font color='blue'> the interstices</font> between and adhering to <font color='green'>the sand and stones</font>, whereby **a hardened, rigid, and strong matrix** for building and paving will be provided.
# ***
# * **bold** are words that may have another words that rely on it for antecedent basis
# * <font color='red'>red</font> are words that have incorrect 112 2nd antecedent basis and should have a 112 2nd rejection
# * <font color='blue'>blue</font> are words that have incorrect 112 2nd antecedent basis and should be objected to
# * <font color='green'>green</font> are words that have correct 112 2nd antecedent basis

# In[1]:


# https://spacy.io/usage/spacy-101
import spacy
import en_core_web_sm

# import the matcher
from spacy.matcher import Matcher

# load a model and create teh nlp objet
nlp = en_core_web_sm.load()


# In[6]:


text = input("Please input your claim.\n")

text = text.lower()

# process some text
doc = nlp(text)

# for token in doc:
#     print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}}")

################################# Matching Patterns #########################################    

# intialize the matcher with the shared vocab 
matcher_a = Matcher(nlp.vocab)
matcher_b = Matcher(nlp.vocab)

# add patterns to matcher_a
pattern = [{"TEXT": "a"}, # pattern starts with 'a'
           {"POS":"ADJ", "OP":"*"}, # 0 or more  adjectives
           {"POS":"NOUN"}] # pattern ends with a noun
matcher_a.add("A_ADJ_PATTERN", None, pattern)

pattern = [{"TEXT": "an"}, # pattern starts with 'an'
           {"POS":"ADJ", "OP":"*"}, # 0 or more  adjectives
           {"POS":"NOUN"}] # pattern ends with a noun
matcher_a.add("AN_ADJ_PATTERN", None, pattern)

# run matcher_a on our claims
matches_a = matcher_a(doc)

# iterate over the matches found with matcher_a to print the match from the doc 
for match_id, start, end in matches_a: 
    matched_span = doc[start:end] # get the matched span
#     print(matched_span.text)

# add patterns to matcher_b
pattern =[{"TEXT": "the"},# pattern starts with 'the'
          {"POS":"ADJ", "OP":"*"}, # 0 or more  adjectives
          {"POS":"NOUN"}]# pattern ends with a noun
matcher_b.add("THE_ADJ_PATTERN", None, pattern) # 

pattern =[{"TEXT": "said"}, # pattern starts with 'the'
          {"POS":"ADJ", "OP":"*"},  # 0 or more  adjectives
          {"POS":"NOUN"}]# pattern ends with a noun
matcher_b.add("SAID_ADJ_PATTERN", None, pattern)

# run matcher_b on our claims
matches_b = matcher_b(doc)

# iterate over the matches found with matcher_b to print the match from the doc 
for match_id, start, end in matches_b:
#     get the matched span
    matched_span = doc[start:end]
    
################################# Filter Noun Chunks #########################################      

filter_noun_chunks_a = []
filter_noun_chunks_b = []
filter_noun_chunks_a_roots = []
filter_noun_chunks_b_roots = []
 

def filter_noun_chunk(noun_chunks):
    for i in noun_chunks:
        if ("a " in i.text) or ("an " in i.text):
            filter_noun_chunks_a.append(i)
            filter_noun_chunks_a_roots.append(i.root.text)
#             print(i)
        elif ("the " in i.text) or ("said " in i.text):
            filter_noun_chunks_b.append(i)
            filter_noun_chunks_b_roots.append(i.root.text)
#             print(i)
#     print(filter_noun_chunks_a)
#     print(filter_noun_chunks_b)
    return(filter_noun_chunks_a_roots, filter_noun_chunks_b_roots)  
#     print("-- a or an --")
#     print("-- the or said --")

################################# Find and Print 112 2nd issues #########################################     

for match_a, start_a, end_a in matches_a:
    for match_b, start_b, end_b in matches_b:
#         print("end match a: ", end_a)
#         print("start match b: ", start_b)
#         if end_a < start_b:
        match_a_span = doc[start_a:end_a]
        match_a_noun = doc[end_a-1]
        match_b_span = doc[start_b:end_b]
        match_b_noun = doc[end_b-1]
        match_a_other = doc[start_a+1:end_a-1]
        match_b_other = doc[start_b+1:end_b-1]
        if match_a_noun.text == match_b_noun.text:
            if match_a_other.text == match_b_other.text:
                pass  #print(match_a_span.text, "<->", match_b_span.text, "-- All good!") 
            else:
                print("\n",match_a_span.text, "<->", match_b_span.text, "-- Possible 112 2nd issue!")
                
################################# Find and Print Claim Objections #########################################         

noun_chunks = list(doc.noun_chunks)
# print(noun_chunks)

filter_noun_chunk(noun_chunks)

for match_b, start_b, end_b in matches_b:
    match_b_noun = doc[end_b-1]
    match_b_span = doc[start_b:end_b]
#     print("match_b_noun:", match_b_noun)
#     print("roots:", filter_noun_chunks_a_roots)
    if match_b_noun.text not in filter_noun_chunks_a_roots:
         print("\n? <->", match_b_span.text, "-- claim objection -- 'the/said' should be 'a/an'")


# In[ ]:




