import spacy

text = 'Ich habe gerade Frau Dr. Meier getroffen. Das Buch erscheint in dritter Aufl. Ich mag z. B. Enten.'

nlp = spacy.load('de_core_news_sm')      # deutsches Modell ladenuss installiert sein)
doc = nlp(text)

for sentence in doc.sents:
    tokens = [i for i in sentence]
    print(tokens)
