import random


def obtenerNumeroAleatorio():
    """
    Devolvemos una palabra de la lista apartir de un random de la longitud
    :return:
    """
    arrayPalabras =["marco", "pablo", "lucas", "miguel"]
    #numero = random.randint(0, len(arrayPalabras)-1)
    #print ("Numero Generado " + str(numero))
    #palabra = arrayPalabras[numero]
    #print ("Palabra escogida " + palabra)
    #return palabra
    return arrayPalabras[random.randint(0, len(arrayPalabras)-1)]


def comparar(palabraUsuario, palabraGenerada):

    palabraUsuarioN = list(palabraUsuario)
    palabraGeneradaN = list(palabraGenerada)

    if (palabraUsuarioN == palabraGeneradaN):
        return "Acertaste"
    else:
        for i in range(0,len(palabraUsuario)):
            if (palabraUsuario[i] == palabraGenerada[i]):
                return "Acercate una letra en una posicion"
            if (palabraUsuario[i] in palabraGenerada):
                return "Acertaste una letra pero no es la posicion que toca"
    return "Fallaste"

def game():
    acertado = False
    palabraGenerada = obtenerNumeroAleatorio()

    while not (acertado):
        #try:
            palabraUsuario = raw_input("Di un palabra de cinco letras \n")
            respuesta = comparar(palabraUsuario, palabraGenerada)
            if respuesta == "Acertaste":
                acertado = True
            print respuesta
        #except:
            #print "No se puede introducir un valor que sea distinto a un numero"
game()