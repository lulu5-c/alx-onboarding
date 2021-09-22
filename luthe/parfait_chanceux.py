from parfait_chanceux_n import  estChanceux, estParfait
#fonction principale
parfait = []
chanceux = []
  
for n in range(2,1000):
    nParfait = estParfait(n)
    nchanceux = estChanceux(n)
    if(nParfait):
        parfait.append(n)
    elif(nchanceux):
        chanceux.append(n)
        
resultat = "nombre speciaux contenu dans l'intervalle [2, 1000] sont:".center(70, '-')
resultat = "\n Nombre parfait :\t() \n Nombre chanceux :\t()".format(parfait, chanceux)
print(resultat)