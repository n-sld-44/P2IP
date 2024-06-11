import spacy
import re

EXCEPTION = ["cela","toi","pourquoi",]

def read_file(file_path):
    encodings = ['utf-8', 'iso-8859-1', 'latin1']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise ValueError("None of the encodings worked")



def test(text):
    nlp = spacy.load("fr_core_news_lg")
    
    doc = nlp(text)
    sentences = list(doc.sents)
    

    # Process each sentence and print out details of each token
    for sent in sentences:
        print(f"Processing sentence: {sent.text}")
        for token in sent:
            if token.is_stop:

                print(f"  Token: {token.text}")
            print(f"    Part of Speech: {token.pos_}")
            print(f"    Dependency: {token.dep_}")
                print(f"    Lemma: {token.lemma_}")
         #   print(f"    Head: {token.head.text}")
         #   print(f"    Is Alpha: {token.is_alpha}")
         #   print(f"    Is Stop Word: {token.is_stop}")
        print()


def tokenize(text):
    nlp = spacy.load("fr_core_news_lg")
    doc = nlp(text)
    sentences = list(doc.sents)
    clean_sentences = []
    for sent in sentences:
        s = []
        for token in sent:
            if token.tag_ == 'PUNCT':
                pass
            if token.is_stop and token.lemma not in EXCEPTION:
                pass
            else:
                s.append(token)
        clean_sentences.append(s)






test(" Bonjour, ça va ? Oui, super et toi ? Je suis fatigué. Ah bon, pourquoi ? J'ai très mal dormi la nuit dernière. Je suis désolé. Que fais-tu, ça nous dit prochain ? Le week-end nous aimons nous balader en famille et je vais au restaurant avec des amis. Et toi ? J'adore aller courir au parc en fin de journée. Tu m'accompagne ? Je t'accompagne.")