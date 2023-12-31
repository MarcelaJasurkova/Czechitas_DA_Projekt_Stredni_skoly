CREATE TABLE TEMP_KONALI AS
SELECT 
    ROK, 
    ID_KRAJ,
    SUM(CAST(KONALI AS INTEGER)) AS SUM_KONALI
FROM 
    PJZ_KOMPLET
WHERE ROK != '2021' AND PREDMET = 'CJ'
GROUP BY 
    ROK, ID_KRAJ;

CREATE TABLE TEMP_NAROZENI AS
SELECT 
    ROK_JPZ, 
    ID_KRAJ,
    KRAJ,
    SUM(CAST(NAROZENI AS INTEGER)) AS SUM_NAROZENI
FROM 
    NAROZENI_2002_2009
WHERE ROK_JPZ != '2021'
GROUP BY 
    ROK_JPZ, ID_KRAJ, KRAJ;

CREATE TABLE DATA_K_TESTU AS
SELECT 
    T1.ROK_JPZ, 
    T1.KRAJ, 
    T1.ID_KRAJ,
    T2.ROK,
    T1.SUM_NAROZENI,
    T2.SUM_KONALI
FROM 
    TEMP_NAROZENI AS T1
INNER JOIN 
    TEMP_KONALI AS T2
ON 
    T1.ID_KRAJ = T2.ID_KRAJ AND T1.ROK_JPZ = T2.ROK;