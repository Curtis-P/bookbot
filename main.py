def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()
    chars = list(file_contents.lower())
    charDict = {}
    for x in range(len(chars)):
        if chars[x] not in charDict:
            charDict[chars[x]] = 1
        else:
            charDict[chars[x]] += 1
    alphaList=[]

    for x in charDict:
        if x.isalpha():
            alphaList.append({'char': x, 'occurance' : charDict[x]})

    alphaList.sort(reverse=True, key=lambda d: d['occurance'])

    for x in alphaList:
        if x == alphaList[0]:
            print("--- Begin report of books/frankenstein.txt ---\n")
            print(f"{len(words)} words found in the document \n")
            print(f"The '{x['char']}' character was found {x['occurance']} times")
        elif x != alphaList[len(alphaList) -1]:
            print(f"The '{x['char']}' character was found {x['occurance']} times")
        else:
            print(f"The '{x['char']}' character was found {x['occurance']} times")
            print("--- End report ---")
    

main()