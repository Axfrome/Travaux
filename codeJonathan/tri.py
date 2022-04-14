import random

# tri par selection
def generateRandonList(n, min, max):
    endList = []
    for i in range(n):
        number = random.randint(min, max)
        endList.append(number)
    return endList

listedObject =(generateRandonList(10, 0, 10))



def sortedUnsortedThing(liste):
    for unsorted_index in range(0, len(liste)-1):
        min = liste[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index, len(liste)):
            if liste[i] < min:
                min = liste[i]
                min_index = i
    #in-place
        liste[min_index] = liste[unsorted_index] 
        liste[unsorted_index] = min
    return liste

print(sortedUnsortedThing(listedObject))