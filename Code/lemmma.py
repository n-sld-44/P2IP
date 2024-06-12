import simplemma
import re
from dictionnaire import FIXED_EXPRESSION, STOP_WORDS, DICTIONNAIRE 


def replace_expressions(text, expressions):
    for i, expr in enumerate(expressions):
        text = text.replace(expr, f"EXPR{i}")
    return text, {f"EXPR{i}": expr for i, expr in enumerate(expressions)}

def split(text):
    sentence = re.split(r"[.!?,]| et",text)
    sentence = [sentence.strip() for sentence in sentence if sentence.strip()]
    return sentence

def lemmatize(text):
    
    text_with_tokens, token_dict = replace_expressions(text.lower(), FIXED_EXPRESSION)
    sents = split(text_with_tokens)
    clean = list()
    for sent in sents:
        s = list()
        i = sent.split()
        for j in i :
            if j in token_dict:
                s.append(token_dict[j].lower())
            else:
                a = simplemma.lemmatize(j.lower(),'fr')
                if a not in STOP_WORDS:
                    s.append(a)

        clean.append(s)
    
    
    return clean



def parse(text):
    sentences_tokenized = lemmatize(text)
    sentences_parsed = list()
    for i in sentences_tokenized:
        sent = sorted(i,key=lambda x: DICTIONNAIRE[x])
        sentences_parsed.append(sent)
    return sentences_parsed
