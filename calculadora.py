# soma simples

x = int (input("insira um numero: "))
y =int (input("insira outro numero: "))

soma = x + y
 
print(f"a soma dos numeros é igual a: {soma}")

#soma com três valores

x = int (input("insira um numero: "))
y = int (input("insira outro numero: "))
z = int(input("insira outro numero: "))

soma = x + y + z 
 
print(f"a soma dos numeros é igual a: {soma}")

#subtração entre valores

x = int(input("insira um numero: "))
y = int(input("insira outro numero: "))

subtr = x - y

print(f"a diferença resultado de {x} - {y} é = {subtr}")

#multiplicação entre valores

x = int(input("insira um numero: "))
y = int(input("insira outro numero: "))

multi = x * y

print(f"a multiplicação de {x} e {y} é igual a: {multi}")

#divisão entre valores

x = int(input("insira um numerador: "))
y = int(input("insira um denominador(não pode ser 0): "))

while y == 0:
    print("o número 0 não pode, escolha outro!")
    y = int(input("insira um denominador(não pode ser 0): ")) 

divisao = x / y

print(f"a divisao entre {x} e {y} é igual a: {divisao}")

#exponenciação entre valores

x = int(input("insira um operador: "))
y = int(input("insira uma potência:  "))


exponen = x ** y 

print(f"a exponenciação entre {x} e {y} é igual a: {exponen}")


#média entre valores

x = int(input('primeira nota do aluno: '))
y = int(input('segunda nota do aluno: '))
z = int(input('terceira nota do aluno: '))

media = (x + y + z) / 3

print(f'a média de notas do aluno é = {media}')

#média ponderada entre valores ja pré-definidos

x = 5
peso1 = 1

y = 12
peso2 = 2

z = 20
peso3 = 3

xy = 15
peso4 = 4

media_ponderada = (x * peso1 + y * peso2 + z * peso3 + xy * peso4) / (peso1 + peso2 + peso3 + peso4)

print(f'a média ponderada é : {media_ponderada}')
