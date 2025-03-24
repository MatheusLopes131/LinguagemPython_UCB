lado = int(input("Digite o lado do quadrado: "))

print("* "*lado)
for _ in range(lado-2): #_ é o defaut
    print("* " + "  "*(lado-2) + "*")
print("* "*lado)