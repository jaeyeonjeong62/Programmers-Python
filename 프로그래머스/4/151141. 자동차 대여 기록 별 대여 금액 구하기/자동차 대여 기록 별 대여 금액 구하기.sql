-- 코드를 입력하세요
SELECT T.HISTORY_ID,
       FLOOR(
           T.DAYS * T.DAILY_FEE
           * (1 - IFNULL((
               SELECT D.DISCOUNT_RATE
               FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS D
               WHERE D.CAR_TYPE = '트럭'
                 AND D.DURATION_TYPE = CASE
                     WHEN T.DAYS >= 90 THEN '90일 이상'
                     WHEN T.DAYS >= 30 THEN '30일 이상'
                     WHEN T.DAYS >= 7 THEN '7일 이상'
                     ELSE NULL
                 END
           ), 0) / 100)
       ) AS FEE
FROM (
    SELECT H.HISTORY_ID,
           DATEDIFF(H.END_DATE, H.START_DATE) + 1 AS DAYS,
           (
               SELECT C.DAILY_FEE
               FROM CAR_RENTAL_COMPANY_CAR AS C
               WHERE C.CAR_ID = H.CAR_ID
           ) AS DAILY_FEE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
    WHERE H.CAR_ID IN (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_CAR
        WHERE CAR_TYPE = '트럭'
    )
) AS T
ORDER BY FEE DESC, HISTORY_ID DESC;