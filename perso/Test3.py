liste = [1, 4, 5, 6, 7, 9, 11, 15, 16, 17, 18, 19, 20, 22, 23, 24, 28]
def presente(lst):
    mini, med, maxi = 0, 0, 0
    i1 = 0
    p = 0
    lstTemp = []
    while i1 < len(lst):
        if i1 == 0: mini, med = lst[i1], lst[i1]
        if i1 < len(lst)-1:
            if lst[i1+1] == med+1:
                p, med = 1, lst[i1+1] 
            if lst[i1+1] != med :
                if p == 0:
                    lstTemp.append([lst[i1]])
                    mini = lst[i1+1]
                    med = lst[i1+1]
                if p == 1:
                    maxi = med
                    lstTemp.extend([[mini, maxi]])
                    mini = lst[i1+1]
                    med = lst[i1+1]
                    p = 0
        #dernier élement
        if i1 == len(lst)-1:
            if lst[i1] == lst[i1-1] + 1:
                maxi = med
                lstTemp.extend([[mini, maxi]])
                mini = lst[i1]
                med = lst[i1]
                p = 0
            else:
                lstTemp.append([lst[i1]])
        i1 = i1 + 1
    #--------------------------------------------------

    i1 = 0
    o1 = 0
    for x in lstTemp:
        o1 = o1 +1  
        if o1 == len(lstTemp):
            if len(lstTemp[i1]) == 1:
                coco = str(lstTemp[i1])
                print(coco[1:-1])            
            if len(lstTemp[i1]) == 2:
                parti1 = str([lstTemp[i1][0]])
                parti2 = str([lstTemp[i1][1]])
                print (parti1[1:-1]+'-'+parti2[1:-1])
        
            i1 = i1+1
        if i1 < len(lstTemp)-1:
            if len(lstTemp[i1]) == 2:
                parti1 = str([lstTemp[i1][0]])
                parti2 = str([lstTemp[i1][1]])
                print (parti1[1:-1]+'-'+parti2[1:-1], end=', ')
        
            if len(lstTemp[i1]) == 1:
                coco = str(lstTemp[i1])
                print(coco[1:-1], end=', ')
            i1 = i1+1

presente(liste)