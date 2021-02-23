# from pathlib import Path
# alle files lijsten voor files moeten in de paden naar files gezet worden of een aparten module
#Alleen harde data hier
# formuyles voor harde data  eigen module
#  ophalen van files doormiddel van een functie die gebruik maakt van List comprehensions.

import pandas as pd
import xlrd

import bron.paden_naar_files as from_path
import bron.lijst_functies as from_functies




order_nummer = "202109916 vdp2 rol van 2000"  # wordt in GUI --> filenaam.stem
aantal_per_rol = 2000
begin_rolnummer = 0 # count zero, will fix default = 0 voor rol 1
mes = 6
etiketten_Y = 42
formaat_hoogte = 20
wikkel = from_functies.wikkel(aantal_per_rol,formaat_hoogte,76)  # +3 = 10

print(f'wikkel = {wikkel+1} inclusief sluit etiket')
# formule voor uitrekenen wikkel
# geef keuze


def makenvoorinloop():
    pass



inloop = (etiketten_Y * 10)-(wikkel + etiketten_Y)

# dataframe_from_excel = pd.read_excel(from_path.excel_file)
# print(dataframe_from_excel.head())

dataframe_from_csv_file_in = pd.read_csv(from_path.file_in, ";", dtype="str")

print(dataframe_from_csv_file_in.head())
aantal = len(dataframe_from_csv_file_in)
aantal_rollen = aantal // aantal_per_rol
baan = len(dataframe_from_csv_file_in) // aantal_per_rol
combinaties = aantal_rollen // mes
# wikkel = 20  # +3 = 23
# etiketten_Y = 25
# inloop = (etiketten_Y * 10)-(wikkel + etiketten_Y)

# from_functies.breek_naar_csv(dataframe_from_csv_file_in,
#                from_path.file_tmp,
#                aantal_per_rol,
#                aantal_rollen,
#                "Rol")




list_of_files_to_clean = [from_path.file_tmp_2,
                          from_path.file_tmp,
                          from_path.hor,
                          from_path.vert,
                          from_path.file_sum_hor,
                          from_path.file_sum_vert,
                          from_path.file_sum_vert]
