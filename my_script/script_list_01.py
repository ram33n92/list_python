#creer une liste vide(on ignore le nombre d'elements d'avance)
#maliste=[]
#print(maliste)
#print(type(maliste))

#liste avec elements connus
#monautreliste=[1, 2, 3, 'test']
#print(monautreliste)
#print(type(monautreliste))

#creer une liste qui va etre peuplee a partir du clavier d'utilisateur
#list1=[]
#nbr_delement=int(input("combien d'element avez vous : "))
#for i in range(nbr_delement):
#    element = input("saisir les elements: ")
#    list1.append(element)
#print(list1)

#creer une liste qui sera peuplee par l'ulitisateur sur une ligne de code
#on utilise la "eval"
#list2 = eval(input("saisir une liste: "))
#print(list2)
#print(type(list2))

#creer une liste avec la fonction list()
liste3= list(range(0, 11, 2))
print(liste3)

#la fonction split() pour creer des liste
machaine= "le college bois de boulogne"
list4= machaine.split()
print(list4)

nom= "hassan"
list5= list(nom)
print(list5)
