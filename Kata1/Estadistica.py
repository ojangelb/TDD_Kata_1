
class Estadistica:
    def calculoEstadistica(cadena):
        arrayResult = []
        arrayString = []
        arrayString = cadena.split(",")

        try:
            arrayString = [int(i) for i in arrayString]

        except:
             return 0

        if not cadena:
            return 0
        else:
            if len(arrayString):

               arrayResult = [arrayString[0],arrayString[0],1,arrayString[0]]

               return arrayResult