CREATE OR REPLACE TABLE REJSTRIK_SKOL AS (
SELECT 
  REDIZO,
  IZO,
  NAZEV_SKOLY,
  ADRESA_1,
  ADRESA_2,
  ADRESA_3,
  ADRESA_KOMPLET,
  OKRES AS ID_OKRES,
  ZRIZOVATEL AS ID_ZRIZOVATEL,
  KAPACITA_SKOLA,
  LAT AS LATITUDE,
  LON AS LONGITUDE
FROM REJSTRIK_SKOL_SOURADNICE
);