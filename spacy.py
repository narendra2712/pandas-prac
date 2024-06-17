import spacy
nlp = spacy.load('en_core_web_sm')
doc=nlp(u' "I have 10/- for our\'s expenses" ')
for t in doc:
    print(t.text)
