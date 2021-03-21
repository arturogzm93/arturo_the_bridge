from scipy.spatial import distance
import numpy as np

points = [[1, 1, 2], [2, 1, 2], [2, 3, 4], [1, 1, 1], [2, 3, 4], [10, 10 , 10], [9, 9, 9]]
y = [2, 2, 2, 1, 1, 4, 4]

class Knn:

    def __init__(self, k):

        # Construye tu predictor, debes indicarle definir la k
        self.k = k
        

    def fit(self, x, y):

        # verifica que los datos que has introducido tienen sentido
        # Almacena los puntos y las etiquetas con las que haremos la prediccion
        self.x = x
        self.y = y


    def predict(self, punto):

        # Calcula la distancia del nuevo punto a los demas puntos
       
        # Evalua los 'votos' de los k vecinos más cercanos

        # Predice

        mas_cercanos = np.argsort(list(map(lambda una_x: distance.euclidean(una_x, punto), self.x)))[:self.k]
        
        votos = np.take(self.y, mas_cercanos)

        counts = np.bincount(votos)

        np.argmax(counts)