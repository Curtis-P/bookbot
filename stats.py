def count_words(text):
    words = text.split()
    print(f"----------- Word Count ---------- \n")
    print(f"Found {len(words)} total words\n")

def get_occurances(text):
    chars = list(text.lower())
    charDict = {}
    for x in range(len(chars)):
        if chars[x] not in charDict:
            charDict[chars[x]] = 1
        else:
            charDict[chars[x]] += 1
    return charDict

def get_report(occurance_dict):
    alphaList=[]

    for x in occurance_dict:
        if x.isalpha():
            alphaList.append({'char': x, 'occurance' : occurance_dict[x]})

    alphaList.sort(reverse=True, key=lambda d: d['occurance'])

    for x in alphaList:
        if x == alphaList[0]:
            print(f"--------- Character Count ------- \n")
            print(f"{x['char']}: {x['occurance']}")
        elif x != alphaList[len(alphaList) -1]:
            print(f"{x['char']}: {x['occurance']}")            
        else:
            print(f"{x['char']}: {x['occurance']}")            
            print(f"\n============= END ===============")