# #les fonctions importantes de list
#
# #len() nous retourne la taille d'une liste ou la taille d'une chaine de caractere
# s= "test"
# print(len(s))
#
# x= [1,2,3,4]
# print(len(x))
#
# #count() nous retourne le nombre d'apparition d'un element dans une liste
# y = [3,5,3,3,6,7,7,9,9,8,10]
# print(y.count(3))
# print(y.count(7))
#
# #index() retourne l'indice de la premiere apparition d'un element
# malist= [1,2,3,3,3,3,5]
# print(malist.index(3))
# print(malist.index(5))
# #tu peux meme demander si il est dans ta liste
# print(0 in malist)
# print(1 in malist)
#
# #append() ajoute un element a la fin de la liste
# maliste=[]
# maliste.append(3)
# maliste.append(90)
# maliste.append("test")
# print(maliste)
#
# #EXERCICE 05 (POUR APPEND): 1- creer une liste vide
# #             2- ajouter tous les nombre divisible par 10 dans cette liste jusqu'a 100
#
# maliste1= []
#
# for nombre in range(0, 101):
#     if nombre % 10 == 0:
#         maliste1.append(nombre)
# print("les nombre divisible par par 10 sont: ", maliste1)
#
# #insert() ajouter un element dans une liste a un indice specifique
# #append () insert l'element a la fin de la liste et insert() insert dans l'indice que vous voulez
# maliste2= [1,2,3,4]
# #la premiere valeur la () est l'indice et la deuxieme est l'element que vous voulez inserer
# maliste2.insert(1 , 'test')
# print(maliste2)
#
# maliste2.insert(0, 'javascript')
# print(maliste2)
#
# #extend() elle ajoute un enssemble d'element(d'un coup) a la fin de la liste
# list01= ['java', 'C#', 'python']
# list02= ['PHP', 'C++', 'javascript']
#
# list01.extend(list02)
# print(list01)

# #fonction pop() elle supprime le dernier element dans une liste et le retourne
# list03=[10,20,30,40,50]
# print(list03)
# print(list03.pop())
# print(list03)
# print(list03.pop())
# print(list03)
# #vous pouvez specifier une indice que vous voulez supprimer
# print(list03.pop(0))
# print(list03)
#
# a= list03.pop(0)
# print(a*10)


#fonction remove cest pour supprimer un element specifique
list04=[10,20,30,40,50]
list04.remove(40)
print(list04)
list04.remove(60)
print(list04)

