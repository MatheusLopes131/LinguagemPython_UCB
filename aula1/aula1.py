#Algoritmo para formulario de usuario

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
massa = float(input("Digite seu peso: "))
est_civil = input("""Digite seu estado civil: 
                     S - Solteiro
                     C- Casado
                     D - Divorciado
                     SE - Separado
                     V - Viúvo """).upper() #Transforma em maiúsculo

imc = massa/altura**2

if imc < 17:
    pimc = "Muito abaixo do peso!"
elif imc >= 17 and imc < 18.5:
    pimc = "Abaixo do peso!"
elif imc >= 18.5 and imc < 25:
    pimc = "Peso normal!"
elif imc >= 25 and imc < 30:
    pimc = "Acima do peso!"
elif imc >= 30 and imc < 35:
    pimc = "Obesidade I!"
elif imc >= 35 and imc < 40:
    pimc = "Obesidade II!"
else:
    pimc = "Obesidade III!"

match est_civil:
    case 'S':
        pcivil = "Solteiro"
    case 'C':
        pcivil = "Casado"
    case 'SE' | 'D': #Testa  o ou com |
        pcivil = "Divorciado"
    case 'V':
        pcivil = "Viúvo"
    case _: #Caso Defaut
        pcivil = "Estado Civil Não Identificado!"

print(f"""\nFormulário do Usuário
Nome: {nome}
Idade: {idade}
IMC: {imc:.2f}
{pimc}
{pcivil}""") #Usa o f antes para pode usar essas {}