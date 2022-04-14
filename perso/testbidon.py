def afficherTableMultiplication(n , min = 0, max = 10):
    print()   
    if min == max : 
        print(str(n)+ " X " + str(max)+" = " + str(n*max) ) 
        return
    if min > max: 
        print("Annulation de fonction et fin du programme car min > max") 
        return
    
    for x in range(min, max+1): print (str(n) +" X "+ str(x) +" = " + str(n*x))

afficherTableMultiplication(5, 5, 20)
afficherTableMultiplication(5, 100, 100)
afficherTableMultiplication(1)