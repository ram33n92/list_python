#comment acceder aux elements dune liste avec son indice
maliste= [10, 20, 30, 40, 50, 60, 70]
print(maliste[0])
print(maliste[-1])

#acceder aux element par slice(:)
# maliste= list[debut:fin:step]
liste1= maliste[2:5]
print(liste1)
#pour print la liste mais inverser
liste1= maliste[::-1]
print(liste1)