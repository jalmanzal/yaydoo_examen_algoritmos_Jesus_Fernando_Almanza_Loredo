
# Se obtiene los puntajes para devolver un array
def obtener_puntaje():
    a = [calificar('Claridad del problema', False), calificar('Originalidad', False), calificar('Dificultad', False)]
    b = [calificar('Claridad del problema', True), calificar('Originalidad', True), calificar('Dificultad', True)]
    final = [0, 0]
    for i in range(0, 3):
        if a[i] > b[i]:
            final[0] += 1
        elif a[i] < b[i]:
            final[1] += 1

    return final


def calificar(category, i):
    salida = int(input(f"Dame la calificación de {'Alice' if not i else 'Bob'} ({category})[1-100]: "))
    if salida > 100 or salida < 1:
        print("No se puede evaluar con esa calificación")
        calificar(category, i)
    return salida
