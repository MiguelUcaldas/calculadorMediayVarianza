import os
from lectorArchivo import lectorArchivo
from calculadoraEstadistica import calculadoraEstadistica

class gestorEstadistico:

    #constructor con parametros rutadelarchivo una lista de numeros de tipo float y varianza y media
    def __init__(self, rutaArchivo):
        self.rutaArchivo = rutaArchivo
        self.listaNumeros = []
        self.varianza = 0
        self.media = 0
        self.archivo_valido = False
    
#metodo de lector de archivo
    def leer_archivo(self):
        print("Buscando Archivo...")
        lector = lectorArchivo(self.rutaArchivo)
         #if que verifica si el archivo existe y si el contenido es numerico
  

        if lector.validar_archivo_existente() and lector.validar_contenido_numerico():
            self.listaNumeros = lector.leer_archivo()
            self.archivo_valido = True
            print("Archivo leido con exito")
        else:
            print("Error al leer el archivo")


#metodo de que calcula la media y varianza mediante la calculadoraEstadistica
    def calcular_estadisticas(self):
        calculadora = calculadoraEstadistica()
        self.media = calculadora.calcular_media(self.listaNumeros)
        self.varianza = calculadora.calcular_varianza(self.listaNumeros)
        print("Estadisticas calculadas con exito")

#override del metodo str para mostrar la lista de numeros, media y varianza
    def __str__(self):
        return f"Lista de numeros: {self.listaNumeros}\nMedia: {self.media}\nVarianza: {self.varianza}"
