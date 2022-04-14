"""
def Question(question, reponse1, reponse2, reponse3, reponse4, bonneReponse):
    global score
    print()
    print(str(question))
    print('a - '+str(reponse1))
    print('b - '+str(reponse2))
    print('c - '+str(reponse3))
    print('d - '+str(reponse4))
    reponse = input("votre réponse ")
    if bonneReponse.lower() == reponse.lower(): 
        print("bonne réponse")
        score += 1
    else: print("mauvaise réponse")
    print()

def integrationQuestionnaire(listeQuestionReponse):
    Question(listeQuestionReponse[0],listeQuestionReponse[1],
    listeQuestionReponse[2],listeQuestionReponse[3],listeQuestionReponse[4],listeQuestionReponse[5])
score = 0
questionnaire = ["Quel est mon prénom ?", "toto", "titi", "tuncay", "papou", "c"]
questionnaire2 = ["Capital de la france ?", "Paris", "Istambul", "Madrid", "Berlin", "a"]
questionnaire3 = ["Ce programme est écrit en quel language ?", "C++", "Java", "JavaScript", "Python", "d"]
questionnaire4 = ["Comment nomme t'on un professionnel de l'informatique ?", "gynécologue", "informaticien", "proctologue", "paripatétitienne", "b"]
integrationQuestionnaire(questionnaire)
integrationQuestionnaire(questionnaire2)
integrationQuestionnaire(questionnaire3)
integrationQuestionnaire(questionnaire4)
print("vous avez", score, "points")
"""
#fonction récursif
"""def a(n, limit):
    if n > 100000: return
    print(n)
    a(n*n, limit)

a(2, 100000)"""

def demanderchoixutilisateur(min, max):
    reponseStr = input('Quel est le choix entre ' + str(min) + " et " + str(max)+ " : ")
    try:
        reponseInt = int(reponseStr)
        if not min <= reponseInt <= max:
            print("ERREUR : Vous devez rentrer un nombre entre", min, " et ", max)
            return demanderchoixutilisateur(min, max)
        return reponseInt
    except:
        print("ERREUR: Rentrez un nombre")
        return demanderchoixutilisateur(min, max)

choix = demanderchoixutilisateur(1, 4)
print("Choix de l'utilisateur : ", choix)