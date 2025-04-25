def enc(text, key):
    from random import choice
    from math import fabs
    encText = ""
    for f in text:
        def main(encList, key, f):
            for c in key:
                for x in key:
                    cIndex = key.index(c)
                    xIndex = key.index(x)
                    if fabs(cIndex-xIndex) == key.index(f):
                        var = key[cIndex] + key[xIndex]
                        encList.append(var)
            encLet = choice(encList)
            return encLet
        key = key.lower()
        encList = []
        if f.isalpha() == False:
            encText = encText + f
        elif f.isupper() == True:
            key = key.upper()
            encText = encText + main(encList, key, f)
        else:
            encText = encText + main(encList, key, f)
    return encText

def dec(text, key):
    from math import fabs
    decText = ""
    let = []
    for f in text:
        def main(let, key):
            pos1 = key.index(let[0])
            pos2 = key.index(let[1])
            index = int(fabs(pos2 - pos1))
            decLet = key[index]
            return decLet
        if f.isalpha() == True:
            let.append(f)
            if f.isupper() == True:
                key = key.upper()
            else:
                key = key.lower()
        else:
            let = []
            decText = decText + f
        if len(let) == 2:
            decText = decText + main(let, key)
            let = []
    return decText

def genkey(key):
    from random import sample
    x = sample(key,len(key))
    newKey = "".join(x)
    return newKey
