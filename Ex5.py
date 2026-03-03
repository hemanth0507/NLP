import spacy
base=spacy.load("en_core_web_sm")

input='''Wow! Yesterday,Dr.Arun Kumar, the chief scientist of India,
        announced that he will quickly launch three innovative AI-based projects
        in Chennai, becasuse they can significantly imporve public safety.
        It may not only reduce accidencts but also save livves.
        there are over 50 experts working on the project'''
doc=base(input)
for token in doc:
    Print(token.text,"->",token.pos_)
  
