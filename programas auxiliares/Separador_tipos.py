
def main():
    arq = open('pokemon.arff', 'r')
    salva = open('pokemonNew.arff', 'w')
    texto = arq.read()
    database = texto.split('\n')

    i = 0;
    while(database[i] != '@DATA'):
        database.pop(0)
    database.pop(0)
    database.pop()


    # separadorTipos(texto)
    texto = criarTabelaTipos(database)

    salva.write(texto)
    arq.close()
    salva.close()

def criarTabelaTipos(database):
    listaNova = ""
    for i in range(len(database)):
        pokemonIndividual = database[i].split(',')
        pokemonNovo = []

        pokemonNovo.append(pokemonIndividual[0]) # Nome
        pokemonNovo.append(pokemonIndividual[6]) # Tier

        # Tipos
        for i in range(18):
            pokemonNovo.append(0)
        pokemonNovo[int(pokemonIndividual[1]) + 1] = 1
        pokemonNovo[int(pokemonIndividual[2]) + 1] = 1

        # Status
        total  = int(pokemonIndividual[ 7])
        total += int(pokemonIndividual[ 8])
        total += int(pokemonIndividual[ 9])
        total += int(pokemonIndividual[10])
        total += int(pokemonIndividual[11])
        total += int(pokemonIndividual[12])

        pokemonNovo.append(pokemonIndividual[ 7])
        pokemonNovo.append(pokemonIndividual[ 8])
        pokemonNovo.append(pokemonIndividual[ 9])
        pokemonNovo.append(pokemonIndividual[10])
        pokemonNovo.append(pokemonIndividual[11])
        pokemonNovo.append(pokemonIndividual[12])
        pokemonNovo.append(total)
        pokemonNovo.append(pokemonIndividual[3])
        pokemonNovo.append(pokemonIndividual[4])
        pokemonNovo.append(pokemonIndividual[5])

        for j in range(len(pokemonNovo) -1):
            listaNova += str(pokemonNovo[j]) + ','
        listaNova += str(pokemonIndividual[5])
        listaNova += '\n'

    print(listaNova)

    return listaNova


def separadorTipos(texto):
    print(texto)
    texto = texto.replace(',Grass,', ',1,')
    texto = texto.replace(',Fire,', ',2,')
    texto = texto.replace(',Water,', ',3,')
    texto = texto.replace(',Bug,', ',4,')
    texto = texto.replace(',Normal,', ',5,')
    texto = texto.replace(',Poison,', ',6,')
    texto = texto.replace(',Electric,', ',7,')
    texto = texto.replace(',Ground,', ',8,')
    texto = texto.replace(',Fighting,', ',9,')
    texto = texto.replace(',Psychic,', ',10,')
    texto = texto.replace(',Rock,', ',11,')
    texto = texto.replace(',Flying,', ',12,')
    texto = texto.replace(',Ghost,', ',13,')
    texto = texto.replace(',Ice,', ',14,')
    texto = texto.replace(',Dragon,', ',15,')
    texto = texto.replace(',Steel,', ',16,')
    texto = texto.replace(',Dark,', ',17,')
    texto = texto.replace(',Fairy,', ',18,')

    texto = texto.replace(',Grass,', ',1,')
    texto = texto.replace(',Fire,', ',2,')
    texto = texto.replace(',Water,', ',3,')
    texto = texto.replace(',Bug,', ',4,')
    texto = texto.replace(',Normal,', ',5,')
    texto = texto.replace(',Poison,', ',6,')
    texto = texto.replace(',Electric,', ',7,')
    texto = texto.replace(',Ground,', ',8,')
    texto = texto.replace(',Fighting,', ',9,')
    texto = texto.replace(',Psychic,', ',10,')
    texto = texto.replace(',Rock,', ',11,')
    texto = texto.replace(',Flying,', ',12,')
    texto = texto.replace(',Ghost,', ',13,')
    texto = texto.replace(',Ice,', ',14,')
    texto = texto.replace(',Dragon,', ',15,')
    texto = texto.replace(',Steel,', ',16,')
    texto = texto.replace(',Dark,', ',17,')
    texto = texto.replace(',Fairy,', ',18,')

    texto = texto.replace(',AG,', ',1,')
    texto = texto.replace(',BL,', ',2,')
    texto = texto.replace(',BL2,', ',3,')
    texto = texto.replace(',LC,', ',4,')
    texto = texto.replace(',Limbo,', ',5,')
    texto = texto.replace(',NU,', ',6,')
    texto = texto.replace(',OU,', ',7,')
    texto = texto.replace(',PU,', ',8,')
    texto = texto.replace(',RU,', ',9,')
    texto = texto.replace(',Uber,', ',10,')
    texto = texto.replace(',UU,', ',11,')
    texto = texto.replace(',-,', ',12,')

    print(texto)




main()
