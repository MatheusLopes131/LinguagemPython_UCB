print ("Hello World!!!")

print((8).bit_length()) #Printa Tamanho dos bits
print(bin(8))
print(7/2) #Printa divisão inteira que vira float
print(type(7/2)) #Printa tipo da variável
print(7//2) #Arrendonda transformando em inteiro

print(int("20", 16))
print(int("0b1000", 0))
print(int("A", 16))

x = "Universidade Catolica"
print(x[0]) #Printa a posição do Array 
print(x[3])
print(x[3:10]) #Printa a posição do Array do 3 até o 10
print(x[:10]) #Printa a posição do Array antes do 10
print(x[3:]) #Printa a posição do Array depois do 3
print(x[-1]) #Printa a posição do Array ao contrário
print(x[-2])

y = x
print(y.upper()) #Printa em Capslock
print(y[::-1]) #Printa tudo ao contrário
print(x in x [::-1]) #Testa se são iguais
x = "ANNA"
print(x in x [::-1])

nome= input ("Digite o seu nome: ")
print("O nome do usuário é " +nome)
idade= input ("Digite a sua idade: ")
print(type(idade))
idade= int(input ("Digite a sua idade: "))
