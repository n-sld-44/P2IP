import simplemma

lang = 'fr'

# Exemple de texte à lemmatiser
text = "Ça va bien les chats chassent les souris"

# Liste des expressions fixes
fixed_expressions = ["ça va"]

# Fonction pour remplacer les expressions fixes par des tokens uniques
def replace_expressions(text, expressions):
    for i, expr in enumerate(expressions):
        text = text.replace(expr, f"EXPR{i}")
    return text, {f"EXPR{i}": expr for i, expr in enumerate(expressions)}

# Remplacer les expressions fixes par des tokens uniques
text_with_tokens, token_dict = replace_expressions(text.lower(), fixed_expressions)

# Tokeniser le texte (en séparant sur les espaces)
words = text_with_tokens.split()

# Lemmatization de chaque mot (en ignorant les tokens uniques)
lemmas = [simplemma.lemmatize(word, lang) if word not in token_dict else token_dict[word] for word in words]

# Affichage du résultat
print(lemmas)
