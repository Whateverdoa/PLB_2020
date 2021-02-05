import pandas as pd
from pathlib import Path
from bron.paden_naar_files import file_sum


def summary_maken(posixlijst, aantal_per_rol, rolnummer):
    """haal uit de csv file het begin, eind en rolnummer"""
    kolomnaamlijst = ["kolom1", "pdf", "omschrijving", "test_kolom"]
    rol = pd.read_csv(posixlijst, dtype="str")
    # print(rol.head(1))

    df_rol = pd.DataFrame(rol, columns=kolomnaamlijst,)

    begin = df_rol.iat[0, 0]
    eind_positie_rol = (aantal_per_rol) - 1
    eind = df_rol.iat[eind_positie_rol, 0]
    # data_uit_kolom4 = df_rol.loc[0:1]

    rol_nummer = pd.DataFrame(
        [(".", "rol nummer", f"{rolnummer}","") for x in range(1)],
        columns=kolomnaamlijst,)


    begin_nummer = pd.DataFrame(
        [(".", "begin nummer", f"{begin}", "") for x in range(1)],
        columns=kolomnaamlijst,)


    eind_nummer = pd.DataFrame(
        [(".", "eind nummer",f"{eind}","") for x in range(1)],
        columns=kolomnaamlijst,)


    sluitstuk = pd.DataFrame(
        [[".", "stans.pdf", f"{aantal_per_rol} etiketten",""]],
        # f"{rolnummer} {begin} t/m {eind}", "stans.pdf"
        columns=kolomnaamlijst,
    )

    naam = f"df_{posixlijst.name:>{0}{4}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([rol_nummer, begin_nummer, eind_nummer])

    return naam

def Summary_files_maken_met_wikkel_en_sluit(posix_rollen_lijst,
                                            aantal_per_rol,
                                            wikkel,
                                            aantalrollen,
                                            begin_nummer_rol=0):
    """de totale wikkel functie met de wikkel functie erin"""
    for i in range(aantalrollen):
        csv_naam = f'summary_{i:>{0}{5}}.csv'
        pad = Path(file_sum / csv_naam)
        # print(csv_naam)
        rol = f'rol_{begin_nummer_rol + i + 1:>{0}{3}}'
        summary_maken(posix_rollen_lijst[i], aantal_per_rol, rol).to_csv(pad, index=0)
    return