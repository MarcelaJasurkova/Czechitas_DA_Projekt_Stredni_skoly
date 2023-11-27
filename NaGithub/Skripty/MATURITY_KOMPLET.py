import pandas as pd

soubor = [
    "CERMAT_MATURITY_2017_AJ.CSV",
    "CERMAT_MATURITY_2017_CJ.CSV",
    "CERMAT_MATURITY_2017_MA.CSV",
    "CERMAT_MATURITY_2018_AJ.CSV",
    "CERMAT_MATURITY_2018_CJ.CSV",
    "CERMAT_MATURITY_2018_MA.CSV",
    "CERMAT_MATURITY_2019_AJ.CSV",
    "CERMAT_MATURITY_2019_CJ.CSV",
    "CERMAT_MATURITY_2019_MA.CSV",
    "CERMAT_MATURITY_2020_AJ.CSV",
    "CERMAT_MATURITY_2020_CJ.CSV",
    "CERMAT_MATURITY_2020_MA.CSV",
    "CERMAT_MATURITY_2021_AJ.CSV",
    "CERMAT_MATURITY_2021_CJ.CSV",
    "CERMAT_MATURITY_2021_MA.CSV",
    "CERMAT_MATURITY_2022_AJ.CSV",
    "CERMAT_MATURITY_2022_CJ.CSV",
    "CERMAT_MATURITY_2022_MA.CSV",
    "CERMAT_MATURITY_2023_AJ.CSV",
    "CERMAT_MATURITY_2023_CJ.CSV",
    "CERMAT_MATURITY_2023_MA.CSV",
]
vysledny_soubor = []

for file in soubor:
    data = pd.read_csv(file)
    vysledny_soubor.append(data)

kombinovana_data = pd.concat(vysledny_soubor, ignore_index=True)
kombinovana_data.to_csv("MATURITY_KOMPLET.CSV", index=False)
