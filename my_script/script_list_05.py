# # tri des elements d'une liste
# # inversion
# list01=[10,20,30,40]
# list01.reverse()
# print(list01)
#
# #sort pour trier en ordre croissant des nombres
# list02=[40,30,20,15,60,70,2]
# list02.sort()
# print(list02)
# # avec les chaines de caractere il va en ordre alphabetique
# list03=["test02", "test01", "test03"]
# list03.sort()
# print(list03)
#
# list04=["mohammed", "iurie", "hassan", "Rameen", "rameen", "Rameez"]
# list04.sort()
# print(list04)
# #on ne peut pas melanger int et str
# list05=[20,10,5, "test"]
# list05.sort()
# print(list05)

#list comprehension : creer une liste a partir de donnée itérable
#syntaxe : [expression for item in list if condition]
malist= [n * n for n in range(1, 11)]
print(malist)

malist1= [n + n for n in range(1, 11)]
print(malist1)

#### EXERCICE  ####
# creer une liste comprehension de nombre entier pair a partir du range (1,101)

malist2= [n for n in range(1,101) if n % 2 == 0]
print(malist2)
