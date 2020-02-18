dicionario = {1:'domingo', 2:'segunda', 3:'terca', 4:'quarta', 5:'quinta', 6:'sexta', 7:'sabado'}
numero=int(input("Digite um número: "))
if numero >=1 and numero <= 7 :
    print ("O dia da semana é:", dicionario[numero])
else:
    print("Escolha um número entre 1 e 7")