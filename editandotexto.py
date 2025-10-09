#atribuindo strings em variaveis

frase = input("digite uma frase de sua escolha: ")

print( frase )

#transformando frase em letras maiúsculas

frase = input("digite uma frase de sua escolha: ")

print( frase.upper() )

#transformando frase em letras minúsculas

frase = input("digite uma frase de sua escolha: ")

print( frase.lower() )

#removendo espaços em branco no inicio e no fim da string

frase =  "  Ola, bem vindo ao mundo da programação  "

print(frase.strip())

#removendo espaços em branco no inicio e no fim da string que for escrita

frase = input("escreva uma frase com espaços no inicio e no fim: ")

print(frase.strip())

#usando mais de um metodo string na mesma variavel

frase = input("escreva uma frase com espaços no inicio e no fim: ")

print(frase.strip().upper())

#trocando as vogais "e" pela letra "f"

frase = input("escreva uma frase que tenha a letra 'e' e veja oque acontece")

print(frase.replace("e","f").replace("E","F"))

#trocando as vogais "a" pelo caractere "@"

frase = input("escreva uma frase que tenha a letra 'a' e veja oque acontece")

print(frase.replace("a","@").replace("A","@"))

