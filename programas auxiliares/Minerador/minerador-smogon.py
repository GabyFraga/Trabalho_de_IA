import csv

def imprimirPokemon(pokemon, listaPokemon) :
    for i in range(len(listaPokemon)) :
        if (listaPokemon[i][0] == pokemon) :
            print(listaPokemon[i])
            return

def separadorTipo(dado, tiposPokemon, pokemon) :
    for i in range(len(tiposPokemon)) :
        if(dado == tiposPokemon[i][0]) :
            pokemon.append(tiposPokemon[i][1])
            pokemon.append(tiposPokemon[i][2])
            return
    pokemon.append("")
    pokemon.append("")
    return

arq = open('pokemon-smogon', 'r')
texto = arq.read()
database = texto.split('\n')

databaseL = database.count("")
for a in range(databaseL) :
        database.remove("")

arqTipos = open('pokemon_alltipos', 'r')
tipos = arqTipos.read().split('\n')
tipos.pop()

tiposPokemon = []
for a in range(len(tipos)) :
    temp = tipos[a].split(' ')
    tiposPokemon.append(temp)

arqFormatos = open('formatos_smogon', 'r')
formatosJogo = arqFormatos.read().split('\n')
formatosJogo.pop()

arq.close()
arqTipos.close()
arqFormatos.close()

a = 0
contA = 0;
pokemon = []
listaPokemon = []
while a < len(database): #12
    if(contA == 0) : # Nome
        pokemon.append(database[a])
        contA += 1
    elif(contA == 1) : # Tipo 1 e Tipo 2
        contA += 1
        separadorTipo(database[a], tiposPokemon, pokemon)

    elif(contA == 2) : # Habilidade e Formato de jogo
        pokemon.append(database[a]) # 1 ability
        a += 1
        contA += 1

        if database[a] in formatosJogo :
            pokemon.append("") # 2 ability
            pokemon.append("") # 3 ability
            pokemon.append(database[a])

        elif database[a] == "HP" :
            pokemon.append("") # 2 ability
            pokemon.append("") # 3 ability
            pokemon.append("") # Formato do jogo
            a -= 1

        else :
            pokemon.append(database[a]) # 2 ability
            a += 1
            if database[a] in formatosJogo :
                pokemon.append("") # 3 ability
                pokemon.append(database[a])

            elif database[a] == "HP" :
                pokemon.append("") # 3 ability
                pokemon.append("") # Formato do jogo
                a -= 1

            else :
                pokemon.append(database[a]) # 3 ability
                a += 1
                if database[a] == "HP" :
                    pokemon.append("") # Formato do jogo
                    a -= 1
                else :
                    pokemon.append(database[a]) # Formato do jogo

    elif(contA == 3) :
        pokemon.append(database[a + 1])
        if database[a] == "Spe" :
            contA = 0
            listaPokemon.append(pokemon.copy())
            pokemon.clear()
        a += 1
    else :
        print("ERRO")

    a += 1

csvPokemon = open('pokemon.csv', 'w')
for i in range(len(listaPokemon)) :
    for j in range(len(listaPokemon[0])) :
        csvPokemon.write(listaPokemon[i][j])
        csvPokemon.write(",")
    csvPokemon.write("\n")


csvPokemon.close()
