#comment parcourir une liste
maliste= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#avec la boucle for
for i in maliste:
    print(i, end=", ")

#boucle while
i = 0
while(i < len(maliste)):
    print(maliste[i], end=" ")
    i =i+1
print()
#exercice01: afficher uniquement les nombres pair entre0 et 11
#exercice 02: afficher uniquement les nomnres impaires

#ex01
list1= list(range(0,11,2))
print(list1)
#ex02
list2= list(range(1,12,2))
print(list2)

#exercice03: ecrire un programme qui affiche un element d'une liste
#ainsi que ses indices positif et negatif

list3= ["mohssen", "mohammed", "iurie"]
taille= len(list3)
print(taille)

for i in range(taille):
    print(list3[i] , "est disponible a l'indice positif: ", i , " et a l'indice negatif: " , i-taille)
