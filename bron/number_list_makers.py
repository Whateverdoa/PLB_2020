import pandas as pd

def maak_simpele_lijst(begin_nummer,vlg,posities,totaal, pdf):
    '''list comp voor maken nummer lijst, 3 kolommen
    kijk voor benamingen in project lijst bewerken'''
    eind = begin_nummer + totaal
    nummers = [[f'{x:>{vlg}{posities}}',f'{pdf}'," ",""] for x in range(begin_nummer,eind)]


    return nummers

standaard_input_lijst=maak_simpele_lijst(1,0,5,100,"leeg.pdf")

df = pd.DataFrame(standaard_input_lijst, columns=["kolom1", "pdf", "omschrijving","barcode"], dtype="str" )
print(df.head(2))
# df.to_csv("standaard_lijst.csv",  sep=";", encoding="utf-8",index=0)

def teken_op_meerdere_posities(positie_lijst, begin_nummer, teken, posities):
    """check if number in list exceeds posities"""
    input_string = str(begin_nummer)
    string_list = []

    start = 0
    for pos in positie_lijst:
        a = input_string[start:pos]
        # print(start, pos)
        start = pos
        string_list.append(a)
    string_list.append(input_string[pos:])
    return teken.join(str(x) for x in string_list)



def maak_dataframe(begin_nummer, posities, totaal, pdf="leeg.pdf"):
    '''list comp voor maken nummer lijst, 3 kolommen
    kijk voor benamingen in project lijst bewerken'''
    vlg=0
    eind = begin_nummer + totaal
    nummers = [(f'{x:>{vlg}{posities}}', f'{pdf}', '', f'{teken_op_meerdere_posities([3],x," ",6)}') for x in range(begin_nummer, eind)]
    nummers_df = pd.DataFrame(nummers, columns=["kolom1", "pdf", "omschrijving", "onder_barcode"], dtype="str")
    return nummers_df


maak_dataframe(700001,6, 100000, "leeg.pdf").to_csv("file_out/42981a.csv",sep=";", encoding="utf-8",index=0)







begin = 700001
nummer_hoza = teken_op_meerdere_posities([3],begin," ",6)


