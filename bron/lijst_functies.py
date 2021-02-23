import pandas as pd
from pathlib import Path

from bron.paden_naar_files import *



def breek_naar_csv(dataframe_from_csv_file_in, posix_dir_pad, aantalperrol, aantalrollen, rol_taal):
    """# dit is een functie waard maak een dataframe
    van lijst en maak dan x aantal csv files"""

    begin = 0
    eind = aantalperrol

    for i in range(1, aantalrollen + 1):
        rol = f'{posix_dir_pad}/{rol_taal}_{i:>{0}{4}}.csv'
        dataframe_from_csv_file_in.iloc[begin:eind].to_csv(rol, index=0)
        begin += aantalperrol
        eind += aantalperrol


def wikkel_aan_file_zetten(posixlijst, aantal_per_rol, wikkel, rolnummer):
    """neem de csv file en zet er een sluitetiket en een wikkel aan inclusief rolnummer"""
    kolomnaamlijst=["kolom1", "pdf", "omschrijving", "test_kolom"]
    # kolom naam lijst moet uit de in te lezen file te halen zijn of anders maak zelf file aan

    rol = pd.read_csv(posixlijst, dtype="str")
    print(rol.head(1))

    df_rol = pd.DataFrame(rol, columns=kolomnaamlijst)

    begin = df_rol.iat[0, 0]
    eind_positie_rol = (aantal_per_rol) - 1
    eind = df_rol.iat[eind_positie_rol, 0]

    twee_extra = pd.DataFrame(
        [(".", "stans.pdf", "","") for x in range(2)],
        columns=kolomnaamlijst,
    )

    wikkel_df = pd.DataFrame(
        [(".", "stans.pdf", "","") for x in range(wikkel)],
        columns=kolomnaamlijst,
    )

    sluitstuk = pd.DataFrame(
        [(".", "stans.pdf", f"{rolnummer} | {begin} - {eind} |  {aantal_per_rol} etiketten","")],
        # f"{rolnummer} {begin} t/m {eind}", "stans.pdf"
        columns=kolomnaamlijst,
    )

    naam = f"df_{posixlijst.name:>{0}{4}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([twee_extra, sluitstuk, wikkel_df, df_rol])
    # naam = pd.concat([twee_extra, wikkel_df, df_rol])

    return naam


def files_maken_met_wikkel_en_sluit(posix_rollen_lijst, aantal_per_rol, wikkel, aantalrollen, begin_nummer_rol=0):
    """de totale wikkel functie met de wikkel functie erin"""
    for i in range(aantalrollen):
        csv_naam = f'wikkel_sluit_{i:>{0}{5}}.csv'
        pad = Path(file_tmp_2 / csv_naam)
        # print(csv_naam)
        rol = f'Rol_{begin_nummer_rol + i + 1:>{0}{3}}'
        wikkel_aan_file_zetten(posix_rollen_lijst[i], aantal_per_rol, wikkel, rol).to_csv(pad, index=0)
    return csv_naam


def lijstmaker_uit_posixpad_csv(padnaam):
    rollen_posix_lijst = [rol for rol in padnaam.glob("*.csv") if rol.is_file()]
    return rollen_posix_lijst

def lijst_opbreker(lijst_in, mes_waarde, combi):
    start = 0
    end = mes_waarde
    combinatie_binnen_mes = []


    for combinatie in range(combi):
        # print(combinatie)
        combinatie_binnen_mes.append(lijst_in[start:end])
        start += mes_waarde
        end += mes_waarde
    return combinatie_binnen_mes


def kol_naam_lijst_builder(mes_waarde=1):
    """deze functie geeft me een lijst
    de andere
    bijna identieke geeft me een string"""

    kollomnaamlijst = []

    for count in range(1, mes_waarde + 1):
        # 5 = len (list) of mes
        num = f"kolom_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        #probeer
        test_kolom= f'test_kolom_{count}'

        kollomnaamlijst.append(num)
        kollomnaamlijst.append(pdf)
        kollomnaamlijst.append(omschrijving)
        #probeer
        kollomnaamlijst.append(test_kolom)

    # return ["id"] + kollomnaamlijst
    return kollomnaamlijst


def lees_per_lijst(lijst_met_posix_paden, mes_waarde):
    """1 lijst in len(lijst) namen uit
    input lijst met posix paden"""
    count = 1
    concatlist = []
    for posix_pad_naar_file in lijst_met_posix_paden:
        # print(posix_pad_naar_file)
        naam = f'file{count:>{0}{4}}'
        # print(naam)
        naam = pd.read_csv(posix_pad_naar_file)
        concatlist.append(naam)
        count += 1
    kolomnamen = kol_naam_lijst_builder(mes_waarde)
    lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    lijst_over_axis_1.columns = [kolomnamen]

    # return lijst_over_axis_1.to_csv("test2.csv", index=0)
    return lijst_over_axis_1

def horizontale():
    pass


def horizontaal_samenvoegen(opgebroken_posix_lijst, map_uit, meswaarde):
    count = 1
    for lijst_met_posix in opgebroken_posix_lijst:
        vdp_hor_stap = f'vdp_hor_stap_{count:>{0}{4}}.csv'
        vdp_hor_stap = map_uit / vdp_hor_stap
        # print(vdp_hor_stap)

        dataframe_new = lees_per_lijst(lijst_met_posix, meswaarde)
        print(dataframe_new.tail(5))

        lees_per_lijst(lijst_met_posix, meswaarde).to_csv(vdp_hor_stap, index=0)

        count += 1
    return print("hor")


def stapel_df_baan(naam, lijstin, ordernummer, map_uit):

    stapel_df = []
    for lijst_naam in lijstin:
        # print(lijst_naam)
        to_append_df = pd.read_csv(
            f"{lijst_naam}", ";", dtype="str", index_col=0)
        stapel_df.append(to_append_df)
    pd.concat(stapel_df, axis=0).to_csv(f"{map_uit}/{naam}_{ordernummer}.csv", ";", "str")
    return pd.concat(stapel_df, axis=0)


def kolom_naam_gever_num_pdf_omschrijving(mes=1):
    """supplies a specific string  met de oplopende kolom namen num_1, pdf_1, omschrijving_1 etc"""

    def list_to_string(lijst_met_kolomnamen):
        kolom_namen = ""
        for kolomnamen in lijst_met_kolomnamen:
            kolom_namen += kolomnamen + ","
        return kolom_namen[:-1] + "\n"

    kollomnaamlijst = []

    for count in range(1, mes + 1):
        # 5 = len (list) of mes
        num = f"num_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        kolom4 = f"test_kolom_{count}"

        kollomnaamlijst.append(num)
        kollomnaamlijst.append(pdf)
        kollomnaamlijst.append(omschrijving)
        kollomnaamlijst.append(kolom4)


    namen = list_to_string(kollomnaamlijst)

    return namen


def wikkel_n_baans_tc(input_vdp_posix_lijst, etiketten_Y, in_loop, mes, wikkel):
    """last step voor VDP adding in en uitloop"""

    inlooplijst = (".,stans.pdf,,," * mes)
    inlooplijst = inlooplijst[:-1] + "\n"  # -1 removes empty column in final file

    for file_naam in input_vdp_posix_lijst:
        with open(f"{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        nieuwe_vdp_naam = VDP_Def / file_naam.name
        with open(nieuwe_vdp_naam, "w", encoding="utf-8") as target:
            target.writelines(kolom_naam_gever_num_pdf_omschrijving(mes))

            target.writelines(readline[3:etiketten_Y])
            target.writelines(readline[wikkel+4:wikkel + etiketten_Y])
            # target.writelines(readline[1:etiketten_Y + 1])
            # target.writelines(readline[16:(etikettenY+etikettenY-8)])

            target.writelines(
                (inlooplijst) * in_loop)  # inloop
            print("inloop maken")
            target.writelines(readline[1:])  # bestand

            target.writelines(
                (inlooplijst) * in_loop)  # inloop  # uitloop
            print("uitloop maken")
            target.writelines(readline[-etiketten_Y:])


def map_lezer(foldername_path, file_extension="*.csv"):
    gelezen_map = [rol for rol in foldername_path.glob(file_extension) if rol.is_file()]
    return gelezen_map

# todo x aantal vdps
# todo paden module toevoegen
# todo output waarde in is string en uit is float?



def wikkel(Aantalperrol, formaat_hoogte, kern=76):
    """ importing in a function?"""
    import math

    pi = math.pi
    # kern = 76  # global andere is 40
    materiaal = 145  # global var
    var_1 = int(math.sqrt((4 / pi) * ((Aantalperrol * formaat_hoogte) / 1000) * materiaal + pow(kern, 2)))
    wikkel = int(2 * pi * (var_1 / 2) / formaat_hoogte + 2)
    return wikkel-2


