

import speach_to_text
text = speach_to_text.speach_to_text()
print(text)
import lemmma
liste_signe = lemmma.parse(text)
print(liste_signe)
import movie_clip
movie_clip.parsed_to_clip(liste_signe)