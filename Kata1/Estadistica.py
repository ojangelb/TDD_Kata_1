import sys


class Estadistica:
    def calculoEstadistica(self, cadena):
        arrayResult = []

        arrayString = cadena.split(",")

        try:
            arrayString = [int(i) for i in arrayString]

        except:
             return 0

        if not cadena:
            return 0
        else:
            if len(arrayString) == 1:
               arrayResult = [arrayString[0],arrayString[0],1,arrayString[0]]
            elif len(arrayString) > 1:
                arrayResult = self.calculoVariosNumeros(self,arrayString)

        return arrayResult

    def calculoVariosNumeros(self, arrayString):
        minimo = self.calcularMinimo(arrayString)
        maximo = self.calcularMaximo(arrayString)
        promedio = self.calcularPromedio(arrayString) / len(arrayString)
        arrayResult = [maximo, minimo, len(arrayString), promedio]
        return arrayResult

    def calcularPromedio(arrayString):
        auxiliar = 0
        for i in arrayString:
            auxiliar = auxiliar + i
        return auxiliar

    def calcularMaximo(arrayString):
        auxiliar = 0
        for i in arrayString:
            if i > auxiliar:
                auxiliar = i
        return auxiliar

    def calcularMinimo(arrayString):
        auxiliar = sys.maxsize
        for i in arrayString:
            if i < auxiliar:
                auxiliar = i
        return auxiliar