import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b**2) - (4*a*c)

if delta >= 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    raizes = sorted([raiz1,raiz2])

if delta < 0:
    print("esta equação não possui raízes reais")   
if delta == 0:
    print("a raiz desta equação é",raizes[0])
else: 
    if delta > 0:
        print("as raízes da equação são",raizes[0],"e",raizes[1])        