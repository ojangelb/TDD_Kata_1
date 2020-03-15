import sys


class Estadistica:
    def calculoEstadistica(cadena):
        arrayResult = []
        arrayString = []
        arrayString = cadena.split(",")
        minimo = 0
        maximo = 0
        promedio = 0

        try:
            arrayString = [int(i) for i in arrayString]

        except:
             return 0


        if not cadena:
            return 0
        else:
            if len(arrayString) == 1:

               arrayResult = [arrayString[0],arrayString[0],1,arrayString[0]]
            elif len(arrayString) == 2:
                auxiliar = sys.maxsize
                for i in arrayString:
                    if i < auxiliar:
                        auxiliar = i
                minimo = auxiliar
                auxiliar = 0
                for i in arrayString:
                    if i > auxiliar:
                        auxiliar = i
                maximo = auxiliar
                auxiliar = 0
                for i in arrayString:
                    auxiliar = auxiliar + i
                promedio = auxiliar/len(arrayString)
                arrayResult = [maximo, minimo, 2, promedio]
        return arrayResult