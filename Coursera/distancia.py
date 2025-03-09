import math

X = int(input("Digite um número:"))
Y = int(input("Digite um número:"))
x = int(input("Digite um número:"))
y = int(input("Digite um número:"))

D = (X - x)**2 + (Y - y)**2
d = math.sqrt(D)

if d >= 10:
    print("longe")
else:
    print("perto")