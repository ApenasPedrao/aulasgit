import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
def calc_primeiro_grau(a,b):
    print(f"A equação do primeiro grau é: {a}x + {b} = 0 e 'a' é diferente de zero.")
    if a== 0:
        print("A equação não é do primeiro grau, pois 'a' deve ser diferente de zero.")
    else:
        print(f"A sua equação é: {a}x + {b} = 0")
        x = -b / a
        print(f"O valor de x é: {x}")
calc_primeiro_grau(a, b)