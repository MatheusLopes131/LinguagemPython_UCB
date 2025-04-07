expressao = input("Digite a sequencia de parenteses: ")

pilha =[]

erro= False
for char in expressao:
    if char =='(':
        pilha.append(') ')
    else:
        if len(pilha) == 0:
            erro = True
            break
        pilha.pop()

if erro or len(pilha) !=0:
    print("Erro!")
else:
    print("Correta!")