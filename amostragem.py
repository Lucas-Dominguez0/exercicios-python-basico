nome = input("Digite seu nome: ")
idade = int(input("Digite sua Idade: "))
altura_str = (input("Digite sua altura: "))
altura = float(altura_str.replace(",","."))

print(f"Olá, %s, voce tem %d e mede %.2f metros!" %(nome, idade, altura) ) 
