
from clases import Estacion

def dist_estaciones(est1, est2, comunidad):

    estacion1 = comunidad.busca_estacion(id.est1, 'id')
    estacion2 = comunidad.busca_estacion(id.est2, 'id')

    if estacion1 != None and estacion2 != None:

        return estacion1.distancia(longitude = estacion2.longitude, latitude = estacion2.latitude)

    else:

        return 'Alguna de las estaciones no esta en la base de datos'