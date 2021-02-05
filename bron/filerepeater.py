import pandas as pd
from pathlib import Path

filecsv = r"file_in/bunch 1_PL_002.csv"
wdir = Path.cwd()
file_csv = wdir / filecsv
file_out = wdir / r"file_out/file_1.csv"

with open(file_csv, "r", encoding="utf-8") as readf:
    readline = readf.readlines()

with open(file_out, "w", encoding="utf-8") as fwrite:

    fwrite.writelines(readline[0:1])

    for i in range(2):
        fwrite.writelines(readline[1:])


    # for i in range(2):
    #
    #     for line in readline:
    #         regel = line.strip()
    #         # print(line.strip())
    #         fwrite.write(line)
