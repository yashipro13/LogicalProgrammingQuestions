all_letters = [chr(i) for i in range(97,123)]
def isPangram (string1):
    charFound = []
    letters_found = 0
    string1 = string1.lower()
    for eachChar in string1:
        if eachChar not in charFound and eachChar in all_letters:
            letters_found += 1
            charFound.append(eachChar)
    if letters_found == 26:
        return True
    return False

print(isPangram("Pack my box with five dozen liquor jugs."))
print(isPangram("Old brother fox jumps over the lazy dog."))

def getImpurity(string1):
    vowels = ['a' , 'e' , 'i', 'o', 'u']
    consonants = list(set(all_letters) - set(vowels))
    string1 = string1.lower()
    impurity = 0
    countIncremented = []
    char_found = []
    for eachChar in string1:
        if eachChar in all_letters:
            if string1.count(eachChar) > 3 and eachChar not in countIncremented:
                impurity += 3
                countIncremented.append(eachChar)
            elif string1.count(eachChar) > 2 and eachChar not in countIncremented:
                impurity += 1
                countIncremented.append(eachChar)
            if eachChar in char_found:
                if eachChar in vowels:
                    impurity += 0.5
                else:
                    impurity += 0.7
            char_found.append(eachChar)
    return impurity
            
print(getImpurity("Pack my box with five dozen liquor jugs."))       