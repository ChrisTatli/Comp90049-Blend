import editdistance
from pyjarowinkler import distance as jwSimilarity


def populateDictionary():
    with open("../data/dict.txt") as f:
        dictionary = f.read().splitlines()
    return dictionary

def populateCandidates():
    with open("../data/candidates.txt") as f:
        candidates = f.read().splitlines()
    return candidates

def populateBlends():
    with open("../data/blends.txt") as f:
        blendLines = f.read().splitlines()
    blends = []
    for blendLine in blendLines:
        blends.append(blendLine.split("\t")[0])
    return blends
    
def printList(elements):
    for e in elements:
        print(e)
    print("*"*20)

def initialise(debug):
    dictionary = populateDictionary()
    candidates = populateCandidates()
    blends = populateBlends()
    if debug:
        printList(dictionary)
        printList(candidates)
        printList(blends)
    return



def calcJWPrefix(word1, word2):
    return jwSimilarity.get_jaro_distance(word1, word2)

def calcJWSuffix(word1, word2):
    word1reversed = reverseWord(word1)
    word2reversed = reverseWord(word2)
    return jwSimilarity.get_jaro_distance(word1reversed, word2reversed)

def calcEditDistance(word1, word2):
    return editdistance.eval(word1, word2)

def reverseWord(word):
    return word[::-1]


def main():
    debug = True
    initialise(debug)


if __name__ == "__main__": main()