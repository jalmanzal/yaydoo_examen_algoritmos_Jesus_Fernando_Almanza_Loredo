def capturar():
    palabra = input("Dame cualquier texto (Pulsa enter para terminar):\n").lower()
    palabra = palabra.replace("—", ",").replace(".", ",").replace(",", "")
    return contar(palabra.split(" "))


def contar(lista):
    conjuntoPalabras = list(set(lista))
    diccionarioFinal = dict()
    contador = 0
    for i in conjuntoPalabras:
        for j in lista:
            if i == j:
                contador += 1
        diccionarioFinal[i] = contador
        contador = 0
    return diccionarioFinal
