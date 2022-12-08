import spacy

text = 'Allerdings glaubt fast die Hälfte der Chief Executives, daß Perot durchaus Chancen habe, die Wahl im November zu gewinnen, wenn er denn kandidiert.'

nlp = spacy.load('de_core_news_sm')      # deutsches Modell laden (muss installiert sein)
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)