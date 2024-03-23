
class calculadoraEstadistica:

    #metodo que recibe una lista de numeros y calcula la media
    def calcular_media(self, listaNumeros):
        suma = sum(listaNumeros)
        cantidad_numeros = len(listaNumeros)
        if cantidad_numeros == 0:
            return 0  # Devuelve 0 si la lista está vacía para evitar divisiones por cero
        return suma / cantidad_numeros


    #metodo que recibe una lista de numeros y calcula la varianza
    def calcular_varianza(self, listaNumeros):
        media = self.calcular_media(listaNumeros)
        suma = 0
        for numero in listaNumeros:
            suma += (numero - media) ** 2
        return suma / len(listaNumeros)
