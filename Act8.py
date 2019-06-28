def es_vocal(s):
    list = ["a", "e", "i", "o", "u"]
    isVocal = False
    for i in list:
        if (s.lower() == i):
            isVocal = True
    return isVocal.__str__()

def es_consonante(s):
    list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    isVocal = True
    for i in list:
        if (s == i):
            isVocal = False
    return isVocal.__str__()
