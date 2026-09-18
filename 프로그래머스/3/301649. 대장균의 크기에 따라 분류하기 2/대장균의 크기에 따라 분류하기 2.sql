-- 코드를 작성해주세요
SELECT E.ID,
       CASE
           WHEN (
               SELECT COUNT(*)
               FROM ECOLI_DATA AS B
               WHERE B.SIZE_OF_COLONY > E.SIZE_OF_COLONY
           ) < (SELECT COUNT(*) FROM ECOLI_DATA) * 0.25
           THEN 'CRITICAL'

           WHEN (
               SELECT COUNT(*)
               FROM ECOLI_DATA AS B
               WHERE B.SIZE_OF_COLONY > E.SIZE_OF_COLONY
           ) < (SELECT COUNT(*) FROM ECOLI_DATA) * 0.50
           THEN 'HIGH'

           WHEN (
               SELECT COUNT(*)
               FROM ECOLI_DATA AS B
               WHERE B.SIZE_OF_COLONY > E.SIZE_OF_COLONY
           ) < (SELECT COUNT(*) FROM ECOLI_DATA) * 0.75
           THEN 'MEDIUM'

           ELSE 'LOW'
       END AS COLONY_NAME
FROM ECOLI_DATA AS E
ORDER BY E.ID;