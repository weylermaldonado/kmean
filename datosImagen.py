
class datosImagen:


    def __init__(self, nombreImagen, vectorDescriptores):
        self.nombreImagen = nombreImagen
        self.vectorDescriptores = vectorDescriptores


    def getNombreImagen(self):
        return self.nombreImagen


    def getVectorMomentosHu(self):
        return self.vectorDescriptores


    def imprimirDatos(self):
        print("\n" ,self.nombreImagen)
        for i in self.vectorDescriptores:
            print("\n", i)