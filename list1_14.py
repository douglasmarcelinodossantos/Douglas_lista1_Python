""" 14. Escreva um programa que verifica se todas as letras do alfabeto constam no mínimo uma
vez do parágrafo fornecido pelo usuário. """

paragrafo = input("Digite um parágrafo que você deseja comparar com as letras do alfabeto: ")

paragrafo = paragrafo.lower()
paragrafo = paragrafo.replace(" ","")
paragrafo = paragrafo.replace("\n","")
paragrafo = paragrafo.replace(".","")
paragrafo = paragrafo.replace("!","")
paragrafo = paragrafo.replace("?","")
paragrafo = paragrafo.replace(",","")
paragrafo = paragrafo.replace(";","")
paragrafo = paragrafo.replace("á","a")
paragrafo = paragrafo.replace("à","a")
paragrafo = paragrafo.replace("ã","a")
paragrafo = paragrafo.replace("é","e")
paragrafo = paragrafo.replace("ê","e")
paragrafo = paragrafo.replace("í","i")
paragrafo = paragrafo.replace("ó","o")
paragrafo = paragrafo.replace("ô","o")
paragrafo = paragrafo.replace("ú","u")
paragrafo = paragrafo.replace("ç","c")

letras = 0

for caracter in paragrafo:
    if caracter in 'abcdefghijklmnopqrstuvwxyz':
        letras = letras + 1

print("letras: %d" %letras)
