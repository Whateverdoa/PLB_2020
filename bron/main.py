import pandas as pd
import bron.paden_naar_files as from_path
import bron.data as from_data
from bron.lijst_functies import *
from bron.summary import summary_maken, Summary_files_maken_met_wikkel_en_sluit

# de file word in een gui opgezocht die de lijst omzet in data
# hoe ga ik met de kolommen werken. Ik wil minimaal 4 kolommen
# Ik wil gewoon werken met de opgegeven kolommen in een lijst.

# in eerste instantie gebeurt er hier nog niks met de kolommen.

breek_naar_csv(from_data.dataframe_from_csv_file_in,
               from_path.file_tmp,
               from_data.aantal_per_rol,
               from_data.aantal_rollen,
               "Rol")

# bij het toevoegen van de wikkel is het wel belangrijk dat het op de goede plek komt,
# daar begint het kolom naam geving probleem.
# misschien is de oplossing om een stramien voor de lijst te maken.
# de vraag wat is een veel voorkomende aantal kolommen.
# Ik denk min 4 max 6 voor een lijst
# print(aantal_rollen)
# for pad in list_of_files_to_clean:
#     cleaner(pad)

# print(len(from_data.tmp_rollen_posix_lijst))
# tmp_rollen_posix_lijst = [rol for rol in from_path.file_tmp.glob("*.csv") if rol.is_file()]
tmp_rollen_posix_lijst= map_lezer(from_path.file_tmp)
print(f'lokaal {tmp_rollen_posix_lijst}')

files_maken_met_wikkel_en_sluit(tmp_rollen_posix_lijst,
                                from_data.aantal_per_rol,
                                from_data.wikkel,
                                from_data.aantal_rollen,
                                from_data.begin_rolnummer)

# tmp_rollen_posix_lijst_met_wikkel = [rol for rol in from_path.file_tmp_2.glob("*.csv") if rol.is_file()]
tmp_rollen_posix_lijst_met_wikkel= map_lezer(from_path.file_tmp_2)

lijst_tmp2 = lijst_opbreker(tmp_rollen_posix_lijst_met_wikkel, from_data.mes, from_data.combinaties)

horizontaal_samenvoegen(lijst_tmp2,from_path.hor,from_data.mes)


hor_lijst = map_lezer(from_path.hor)
# print(hor_lijst)

stapel_df_baan("VDP", hor_lijst, from_data.order_nummer, from_path.vert)

print("in en uitloop")

vert_lijst = [rol for rol in from_path.vert.glob("*.csv") if rol.is_file()]


wikkel_n_baans_tc(vert_lijst,
                  from_data.etiketten_Y,
                  from_data.inloop,
                  from_data.mes,
                  from_data.wikkel)

print(f'maplezer test {map_lezer(from_path.vert)}')

# todo in en uitloop data
# todo summary


####summary test

Summary_files_maken_met_wikkel_en_sluit(tmp_rollen_posix_lijst,from_data.aantal_per_rol,
                                        1,
                                        from_data.aantal_rollen,
                                        from_data.begin_rolnummer)

opgebroken_lijst = lijst_opbreker(lijstmaker_uit_posixpad_csv(file_sum),from_data.mes,from_data.combinaties)

horizontaal_samenvoegen(opgebroken_lijst,file_sum_hor,from_data.mes)

stapel_df_baan("Summary",lijstmaker_uit_posixpad_csv(file_sum_hor), from_data.order_nummer, VDP_Def)

##########################################

for dir in from_data.list_of_files_to_clean:
    from_path.cleaner(dir)
#
