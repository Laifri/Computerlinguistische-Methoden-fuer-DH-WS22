import nltk

#nltk.download('punkt')		# Kommentarzeichen beim ersten Durchlauf entfernen

text = '''Ich habe gerade Frau Dr. Meier getroffen.  Das Buch erscheint in dritter Aufl.
       Am Mittwoch fliege ich nach New York. Ich mag z.B. Enten.'''

sent_tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
sentences = sent_tokenizer.tokenize(text)

for sentence in sentences:
    words = nltk.word_tokenize(sentence, language='german')
    for word in words:
        print(word)
    print('\n')