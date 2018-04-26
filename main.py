import random
import math
from LectorDescriptores import LectorDescriptores
from DataPoint import DataPoint
from Centroid import Centroid
NUM_CLUSTERS = 3
TOTAL_DATA = 7
A_SEED = 0 
B_SEED = 71
C_SEED = 141
BIG_NUMBER = math.pow(10, 10)

# SAMPLES = [[1.0, 1.0], [1.5, 2.0], [3.0, 4.0], [5.0, 7.0], [3.5, 5.0], [4.5, 5.0], [3.5, 4.5], [6.0, 8.0]]

data = []
# centroids = [200]
centroid_A = list()
centroid_B = list()
centroid_C = list()
lector = LectorDescriptores()
#dataSet = list()
dataSet = lector.cargarDatos()


def initialize_centroids():
    
    centroids_A = Centroid(dataSet[A_SEED].getNombreImagen(), dataSet[A_SEED].getVectorMomentosHu())
    centroids_B = Centroid(dataSet[B_SEED].getNombreImagen(), dataSet[B_SEED].getVectorMomentosHu())
    centroids_C = Centroid(dataSet[C_SEED].getNombreImagen(), dataSet[C_SEED].getVectorMomentosHu())
    

    
    print("Centroides inicializados en:")
    print("(", centroids_A.getNombreImagen() , ", ", centroids_A.getVectorMomentosHu() , ")")
    print("(", centroids_B.getNombreImagen() , ", ", centroids_B.getVectorMomentosHu() , ")")
    print("(", centroids_C.getNombreImagen() , ", ", centroids_C.getVectorMomentosHu() , ")")
    print()
    return
    
initialize_centroids()
"""
def initialize_centroids():
    
    centroids.append(Centroid(SAMPLES[LOWEST_SAMPLE_POINT][0], SAMPLES[LOWEST_SAMPLE_POINT][1]))
    centroids.append(Centroid(SAMPLES[HIGHEST_SAMPLE_POINT][0], SAMPLES[HIGHEST_SAMPLE_POINT][1]))
    
    print("Centroids initialized at:")
    print("(", centroids[0].get_x(), ", ", centroids[0].get_y(), ")")
    print("(", centroids[1].get_x(), ", ", centroids[1].get_y(), ")")
    print()
    return

def initialize_datapoints():
   
    for i in range(TOTAL_DATA):
        newPoint = DataPoint(SAMPLES[i][0], SAMPLES[i][1])
        
        if(i == LOWEST_SAMPLE_POINT):
            newPoint.set_cluster(0)
        elif(i == HIGHEST_SAMPLE_POINT):
            newPoint.set_cluster(1)
        else:
            newPoint.set_cluster(None)
            
        data.append(newPoint)
    
    return

def get_distance(dataPointX, dataPointY, centroidX, centroidY):
 
    return math.sqrt(math.pow((centroidY - dataPointY), 2) + math.pow((centroidX - dataPointX), 2))

def recalculate_centroids():
    totalX = 0
    totalY = 0
    totalInCluster = 0
    
    for j in range(NUM_CLUSTERS):
        for k in range(len(data)):
            if(data[k].get_cluster() == j):
                totalX += data[k].get_x()
                totalY += data[k].get_y()
                totalInCluster += 1
        
        if(totalInCluster > 0):
            centroids[j].set_x(totalX / totalInCluster)
            centroids[j].set_y(totalY / totalInCluster)
    
    return

def update_clusters():
    isStillMoving = 0
    
    for i in range(TOTAL_DATA):
        bestMinimum = BIG_NUMBER
        currentCluster = 0
        
        for j in range(NUM_CLUSTERS):
            distance = get_distance(data[i].get_x(), data[i].get_y(), centroids[j].get_x(), centroids[j].get_y())
            if(distance < bestMinimum):
                bestMinimum = distance
                currentCluster = j
        
        data[i].set_cluster(currentCluster)
        
        if(data[i].get_cluster() is None or data[i].get_cluster() != currentCluster):
            data[i].set_cluster(currentCluster)
            isStillMoving = 1
    
    return isStillMoving

def perform_kmeans():
    isStillMoving = 1
    
    initialize_centroids()
    
    initialize_datapoints()
    
    while(isStillMoving):
        recalculate_centroids()
        isStillMoving = update_clusters()
    
    return

def print_results():
    for i in range(NUM_CLUSTERS):
        print("Cluster ", i, " includes:")
        for j in range(TOTAL_DATA):
            if(data[j].get_cluster() == i):
                print("(", data[j].get_x(), ", ", data[j].get_y(), ")")
        print()   
    return

perform_kmeans()
print_results()
"""