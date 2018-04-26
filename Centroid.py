class Centroid:

    def __init__(self, nombreImagen, vectorDescriptores):
        self.nombreImagen = nombreImagen
        self.vectorDescriptores = vectorDescriptores


    def getNombreImagen(self):
        return self.nombreImagen


    def getVectorMomentosHu(self):
        return self.vectorDescriptores

    