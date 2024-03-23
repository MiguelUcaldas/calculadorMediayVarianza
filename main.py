from gestorEstadistico import gestorEstadistico
import os

print("  / \\")
print(" (   @\\___")
print("  /         O")
print(" /   (_____/")
print("/_____/ U")

#venta de bienvenida para usuario
print("BIENVENIDO AL CALCULADOR DE MEDIA Y VARIANZA EN ARCHIVOS")
print("Este programa calcula la media y varianza de un archivo de texto que contenga numeros separados por comas")
print("eje: 1,2,3,4,5,6,7,8,9,10")
print(" ")


#Recibe ruta
ruta = input("Ingrese la ruta deL archivo donde buscara: ")
#ruta = "C:\pruebas\pruebasNumericas\ejemplo3.txt"


#crea objeto de gestorEstadistico
gestor = gestorEstadistico(ruta)

gestor.leer_archivo()

if gestor.archivo_valido:
     gestor.calcular_estadisticas()

     print(gestor)

else:
    exit()
    pass



print(" ")
print("GRACIAS POR USAR EL CALCULADOR DE MEDIA Y VARIANZA EN ARCHIVOS")

#C:\pruebas\pruebasNumericas\ejemplo.txt