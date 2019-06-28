def son_anagramas(p1,p2):
    number = 0;
    isAnagram = True
    if len(p1) == len(p2):
        for i in range(0, len(p1)):
            for j in range(0, len(p2)):
                if p1[i] == p2[j]:
                    number +=1
        if number != len(p1):
            isAnagram = False
    else:
        isAnagram = False
    return isAnagram.__str__()