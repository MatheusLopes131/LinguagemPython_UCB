palavras = ["amor", "roma", "mora", "carro", "orça", "orca", "arco"]

anagramas={}

for palavra in palavras:
    chave = tuple(sorted(palavra))
    if chave in anagramas:
        anagramas[chave].append(palavra)
    else:
        anagramas[chave] = [palavra]

for chave, valor in anagramas.items():
    print(f"{chave}:{valor}")