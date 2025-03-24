i=0
while(i<=100):
    if(i==15):
        i+=1
        continue #continue pula uma interação
    print(i, end=" ")
    i+=1

print("\n")

for i in (0,1,2,3,4):
    print(i, end=" ")

print("\n")

for i in ("Algoritmo","Novas Tecnologias", "POO", "ED"):
    print(i)

print("\n")

i=0
for materia in ("Algoritmo","Novas Tecnologias", "POO", "ED"):
    print(f"Materias{[i]} = {materia}")
    i+=1

print("\n")

for i,materia in enumerate(("Algoritmo","Novas Tecnologias", "POO", "ED")): #enumerate recebe a iteração e retorna um lista 1 por 1
    print(f"Materias[{i}] = {materia}")

print("\n")

for materia,i in enumerate(("Algoritmo","Novas Tecnologias", "POO", "ED")): #primeiro é o valor da lista e depois os valores a serem impressos i,materia
    print(f"Materias[{i}] = {materia}")

print("\n")

for i in range(20): #range faz um sequencia de execuções de acordo com o número dentro dele
    print(i, end=" ")

print("\n")

for i in range(1,20,2): #range 1/2/3 1- onde o numero começa 2- quantidade de vezes que executa 3- de quantos em quantos ele conta
    print(i, end=" ")

print("\n")

for i,j in enumerate(range(0,21,2)):
    print(f"pares[{i}] = {j}")

print("\n")

lista = [e**2 for e in range(0,11)]
print(lista)