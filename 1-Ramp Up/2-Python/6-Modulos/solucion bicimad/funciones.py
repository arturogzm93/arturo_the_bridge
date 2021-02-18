

def dist_estaciones(id_est1, id_est2, comunidad):

    estacion1 = comunidad.busca_estacion(id_est1, "id")
    estacion2 = comunidad.busca_estacion(id_est2, "id")

    if estacion1 != None and estacion2 != None:
        return estacion1.distancia(longitude = estacion2.longitude, latitude = estacion2.latitude)
    else:
        return "Alguna de las estaciones no está en la BD"