
class Estadistica:
    def calculoEstadistica(cadena):
        arrayResult = []
        if not cadena:
            return 0
        else:
            if len(cadena)==1:

               arrayResult = [int(cadena),int(cadena),1,int(cadena)]

               return arrayResult