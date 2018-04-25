from datosImagen import datosImagen
import re
import sys
from math import sqrt

#Para hacer uso de esta clase generar un objeto a traves del constructor nulo (sin argumentos)
#y llamar a la funcion cargarDatos.

class LectorDescriptores:

    def __init__(self):
        pass


    def etiquetarImagen(self, tipoImagen):
        if tipoImagen == '1':
            return 'A'
        elif tipoImagen == '2':
            return 'B'
        elif tipoImagen == '3':
            return 'C'


    def separarVectores(self, datos):
        datosEntrenamiento = list()
        for i in range(len(datos)):
            descriptoresImagen = datos[i].split()
            tipoImagen = ''
            vectorDescriptores = list()
            for i in range(0,8):
                if i == 7:
                    tipoImagen = self.etiquetarImagen(descriptoresImagen[i])
                else:
                    vectorDescriptores.append(float(descriptoresImagen[i]))
            imagen = datosImagen(tipoImagen, vectorDescriptores)
            datosEntrenamiento.append(imagen)
        return datosEntrenamiento


#Carga datos automaticamente del archivo Banco_descriptores.txt, notar que es importante que el archivo este colocado
#en el mismo directorio en el que el archivo con el codigo esta ubicado.
    def cargarDatos(self):
        trimDatos = list()
        listaVectoresDatos = list()
        archivo = open('seeds_dataset.txt', 'r')
        cadenaDatos = archivo.read()
        archivo.close()
        datos = cadenaDatos.splitlines()
        return self.separarVectores(datos)