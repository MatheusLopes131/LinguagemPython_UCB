msg = input("Digite a mensagem: ")

dig1 = (int(msg[0])+7)%10
dig2 = (int(msg[1])+7)%10
dig3 = (int(msg[2])+7)%10
dig4 = (int(msg[3])+7)%10

dig1,dig2,dig3,dig4 = dig3,dig4,dig1,dig2

print(f"Msg criptografada: {dig1}{dig2}{dig3}{dig4}")

msg = input("Digite a mensagem: ")

dig1 = (int(msg[0])+7)%10
dig2 = (int(msg[1])+7)%10
dig3 = (int(msg[2])+7)%10
dig4 = (int(msg[3])+7)%10

dig1,dig2,dig3,dig4 = dig3,dig4,dig1,dig2

print(f"Msg descriptografada: {dig1}{dig2}{dig3}{dig4}")

#corrigir no notion