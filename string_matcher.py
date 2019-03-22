"""
Ce fichier traite les ambiguités (fuzzy logic) pour permettre une tolérance de reconnaissance de certains mots
"""

from reconnaissance import get_names
possibilities=["bonjour","merci","stop","c'est bon"," au revoir","arrête","téléphone","smartphone","voiture",
               "maison","médicaments","portefeuille","clés"]

def match_word(phrase, treshold):
    from fuzzywuzzy import process
    fetch=process.extractOne(phrase,possibilities)
    if fetch[1]>=treshold :
        if fetch[0] in ["merci","stop","c'est bon","arrête","au revoir"] :
            return "merci"
        elif fetch[0] in ["téléphone", "smartphone"] :
            return "téléphone"
        elif fetch[0] == "bonjour" :
            return "bonjour"
        else :
            return fetch[0]
    else :
        return False

def match_number(num):
    poss=[str(i) for i in range(1,32)]
    from fuzzywuzzy import process, fuzz
    fetch = process.extractOne(str(num), poss,scorer=fuzz.token_set_ratio)
    if fetch[1] >= 80 :
        return fetch[0]
    else :
        return False

def match_month(m):
    poss=["janvier","février","mars","avril","mai","juin","juillet","août","septembre",
          "octobre","novembre","décembre"]
    from fuzzywuzzy import process, fuzz
    fetch = process.extractOne(m, poss,scorer=fuzz.token_set_ratio)
    if fetch[1] >= 92:
        return fetch[0]
    else:
        return False

def match_names(name):
    names=get_names()
    from fuzzywuzzy import process, fuzz
    fetch = process.extractOne(name, names, scorer=fuzz.token_set_ratio)
    if fetch[1] >= 80:
        return fetch[0]
    else:
        return False

def match_motif(motif):
    #Pour normaliser les entrées dans la base de données
    poss={"café":"prendre un café",
          "thé":"prendre un thé",
          "consultation":"faire une consultation",
          "promener":"aller se promener",
          "film":"regarder un film",
          "série":"regarder une série",
          "marathon séries":"se faire un marathon séries",
          "anniversaire":"fête d'anniversaire",
          "sport":"faire du sport",
          "footing":"faire un footing",
          "courir":"aller courir",
          "discuter":"discuter",
          "déjeuner":"déjeuner ensemble",
          "dîner":"dîner ensemble",
          "manger":"manger ensemble",
          "cinéma":"aller au cinéma",
          "ciné":"aller au cinéma",
          "théâtre":"aller au théâtre",
          "concert":"se faire un concert",
          "shopping":"faire du shopping",
          "courses":"faire les courses",
          "parler":"parler"}
    from fuzzywuzzy import process, fuzz
    fetch = process.extractOne(motif, poss.keys())
    return poss[fetch[0]]