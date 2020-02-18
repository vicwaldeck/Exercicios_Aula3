import random as rd

contador = 1
lista = []

item = int(input("Quantos itens na lista? "))

while contador <= item:
    lista.append(rd.randrange(0,1000))
    contador+=1

print("lista =", lista)
print("Valor máximo: ", max(lista))
print("Valor mínimo: ", min(lista))