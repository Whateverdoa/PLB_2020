# import pandas as pd
from pathlib import Path

file = r"file_in/202109916 r v 2000.csv"

# excel_file= r"file_in/202011034/202011034samen.xlsx"
wdir = Path.cwd()
file_in = wdir / file




print(wdir)
print(file_in.is_file())

file_out = wdir / "file_out"
file_tmp = wdir / "file_out/tmp"
file_tmp_2 = wdir / "file_out/tmp2"

hor = wdir / "file_out/hor"
vert = wdir / "file_out/vert"

VDP_Def = wdir / "VDP_Def/"

file_sum = wdir / "summary"
file_sum_hor = wdir / "summary/hor"
file_sum_vert = wdir / "summary/vert"


#
# print(vert.is_dir())
file_concat = Path(r"C:\Users\mike\PycharmProjects\Projekt_lijstbewerken\source\file_out\concat")

file_tmp_2.mkdir(parents=True, exist_ok=True)
file_tmp.mkdir(parents=True, exist_ok=True)
vert.mkdir(parents=True, exist_ok=True)
hor.mkdir(parents=True, exist_ok=True)
VDP_Def.mkdir(parents=True, exist_ok=True)
file_sum.mkdir(parents=True, exist_ok=True)
file_sum_hor.mkdir(parents=True, exist_ok=True)
file_sum_vert.mkdir(parents=True, exist_ok=True)




def cleaner(pad):

    dir_to_empty = sorted(Path(pad).glob('*.csv'))

    for file in dir_to_empty:
        file.unlink()



