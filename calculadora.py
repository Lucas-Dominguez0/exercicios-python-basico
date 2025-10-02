x = int (input("insira um numero: "))
y =int (input("insira outro numero: "))

soma = x + y
 
print(f"a soma dos numeros é igual a: {soma}")



x = int (input("insira um numero: "))
y = int (input("insira outro numero: "))
z = int(input("insira outro numero: "))

soma = x + y + z 
 
print(f"a soma dos numeros é igual a: {soma}")


x = int(input("insira um numero: "))
y = int(input("insira outro numero: "))

subtr = x - y

print(f"a diferença resultado de {x} - {y} é = {subtr}")


x = int(input("insira um numero: "))
y = int(input("insira outro numero: "))

multi = x * y

print(f"a multiplicação de {x} e {y} é igual a: {multi}")

x = int(input("insira um numerador: "))
y = int(input("insira um denominador(não pode ser 0): "))

while y == 0:
    print("o número 0 não pode, escolha outro!")
    y = int(input("insira um denominador(não pode ser 0): ")) 

divisao = x / y

print(f"a divisao entre {x} e {y} é igual a: {divisao}")