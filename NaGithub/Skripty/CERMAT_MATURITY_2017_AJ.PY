import openpyxl
import csv

wb = openpyxl.load_workbook(
    r"CERMAT_MATURITY_2017.xlsx",
    read_only=True,
)
# první list
sh = wb.worksheets[0]
zaznamy = []
# Začínáme od 1171.řádku
for row in sh.iter_rows(min_row=1171, values_only=True):
    zaznamy.append(
        {
            "ID": str(row[1]) + "2017",
            "REDIZO": row[1],
            "ROK": "2017",
            "OBOROVA_SKUPINA": row[2],
            "KRAJ": row[3],
            "PREDMET": "AJ",
            "KONALI": row[7],
            "NEUSPELI": row[8],
            "USPELI": row[9],
            "PRUMERNY_PERCENTIL": row[10],
            "MEDIAN": row[11],
        }
    )
if not zaznamy:
    exit()

with open("CERMAT_MATURITY_2017_AJ.CSV", "w", newline="", encoding="utf8") as csvfile:
    fieldnames = zaznamy[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # zapisuje první řádek s názvy sloupců
    writer.writeheader()
    writer.writerows(zaznamy)
