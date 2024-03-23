import os

class lectorArchivo:

    #constructor
    def __init__(self, rutaArchivo):
        self.rutaArchivo = rutaArchivo
        

    #metodo que verifica si un archivo existe y retorna un booleano
    def validar_archivo_existente(self):
        existencia = os.path.exists(self.rutaArchivo)
        if not existencia:
            print("El archivo no existe")
        else:
            print("El archivo existe")
        return existencia
    

    #metodo que verifica si el contenido de el archivo son numeros separados por comas y retorna un booleano
    def validar_contenido_numerico(self):
        with open(self.rutaArchivo, 'r') as archivo:
            for linea in archivo:
                numeros = linea.strip().split(",")
                for numero in numeros:
                    try:
                        float(numero)
                        
                    except ValueError:
                        print("El archivo no contiene numeros")
                        return False
        print("El archivo contiene numeros")            
        return True
 


    #metodo que lee el archivo de texto y retorna una lista de numeros y separa los numeros por lineas separados por ,
    def leer_archivo(self):
        listaNumeros = []
        with open(self.rutaArchivo, 'r') as archivo:
            for linea in archivo:
                numeros = linea.strip().split(",")
                for numero in numeros:
                    listaNumeros.append(float(numero))
        return listaNumeros


