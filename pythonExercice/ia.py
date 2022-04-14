# -*- code:latin1 -*-

from tkinter import Label
import numpy
import pandas as pd
from scipy.sparse import data
from sklearn.model_selection import train_test_split
from sklearn import svm, tree
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score



dataset = pd.read_csv("F:/dev/Web/Projet/test/pythonExercice/diabetes.csv", header=None)
dataset = dataset.dropna()

dataset.head()
dataset = numpy.loadtxt("F:/dev/Web/Projet/test/pythonExercice/diabetes.csv", delimiter=',')
features=dataset[:,0:8]
labels=dataset[:,8]
print(features,labels)

# Data repartition (X = features / y = classe)
feature_train, feature_test, label_train, label_test = train_test_split (features, labels, test_size = 0.30, random_state = 42)

#création de modele
svm = svm.SVC()

arbre = tree.DecisionTreeClassifier()

kmeans = KMeans(n_clusters=2, random_state=0)

#training
svm.fit(feature_train, label_train)
kmeans.fit(feature_train, label_train)
arbre.fit(feature_train, label_train)

# Prediction

predictionSVM = [svm.predict([element]) for element in feature_test]
predictionArbre = [arbre.predict([element]) for element in feature_test] 
PredictionKmean = [kmeans.predict([element]) for element in feature_test]

# Evaluer les modeles
accSvm = accuracy_score(predictionSVM, label_test)
predictionSvm = precision_score(predictionSVM, label_test)
recallSvm = recall_score(predictionSVM, label_test)
f1ScoreSvm = f1_score(predictionSVM, label_test)

print("acc", accSvm, "precision", predictionSvm, "recall", recallSvm, "f1", f1ScoreSvm)


accKmean = accuracy_score(PredictionKmean, label_test)
predictionKmean = precision_score(PredictionKmean, label_test)
recallKmean = recall_score(PredictionKmean, label_test)
f1ScoreKmean = f1_score(PredictionKmean, label_test)

print("acc", accKmean, "precision", predictionKmean, "recall", recallKmean, "f1", f1ScoreKmean)



accArbre = accuracy_score(predictionArbre, label_test)
predictionArbre = precision_score(predictionArbre, label_test)
#recallAb = recall_score(predictionArbre, label_test)
#f1ScoreArbre = f1_score(predictionArbre, label_test)

print("acc", accArbre, "precision", predictionArbre) # "recall", recallAb, "f1", f1ScoreArbre)
 