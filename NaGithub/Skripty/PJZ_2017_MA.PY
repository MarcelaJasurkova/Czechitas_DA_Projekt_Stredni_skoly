import openpyxl
import csv

wb = openpyxl.load_workbook(
    r"pjz_2017.xlsx",
    read_only=True,
)
# první list
sh = wb.worksheets[0]
zaznamy = []
# Začínáme od 60.řádku
for row in sh.iter_rows(min_row=59, values_only=True):
    zaznamy.append(
        {
            "REDIZO": row[0],
            "ROK": "2017",
            "ID_OBOR": row[1],
            "ID_KRAJ": row[5],
            "NAZEV_SKOLY": row[3],
            "PREDMET": "MA",
            "KONALI": row[14],
            "PRUMERNY_PERCENTIL": row[16],
            "SMERODATNA_ODCHYLKA": row[17],
        }
    )
if not zaznamy:
    exit()

with open("PJZ_2017_MA.CSV", "w", newline="", encoding="utf8") as csvfile:
    fieldnames = zaznamy[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # zapisuje první řádek s názvy sloupců, tzn. RedIzo,Oborova_skupina,bla atd.
    writer.writeheader()
    writer.writerows(zaznamy)
