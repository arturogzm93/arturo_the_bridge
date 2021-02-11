

import pandas as pd
from clases import Estacion, ComunidadMadrid

df = pd.read_excel("2018_Julio_Bases_Bicimad_EMT.xlsx")


tot_est = []

for index, row in df.iterrows():

    estacion = Estacion(row[0], row[3], row[1], row[6], row[4], row[5])
    tot_est.append(estacion)
