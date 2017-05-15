arqTipos = open('pokemon_types', 'r')
tipos = arqTipos.read().split('\n')
tipos.pop()

arqTipos.close()
allTipos = open('pokemon_alltipos', 'w')
for i in range(len(tipos)) :
    allTipos.write(tipos[i])
    allTipos.write(" ")
    allTipos.write(tipos[i])
    allTipos.write(" ")
    allTipos.write(tipos[i])
    allTipos.write("\n")

for i in range(len(tipos)) :
    for j in range(len(tipos)) :
        if i != j :
            allTipos.write(tipos[i])
            allTipos.write(tipos[j])
            allTipos.write(" ")
            allTipos.write(tipos[i])
            allTipos.write(" ")
            allTipos.write(tipos[j])
            allTipos.write("\n")

allTipos.close()
