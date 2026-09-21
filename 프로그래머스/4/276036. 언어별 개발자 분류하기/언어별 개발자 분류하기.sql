-- 코드를 작성해주세요
SELECT GRADE, ID, EMAIL
FROM (
    SELECT D.ID, D.EMAIL,
           CASE
               WHEN EXISTS (
                   SELECT 1
                   FROM SKILLCODES AS S
                   WHERE S.CATEGORY = 'Front End'
                     AND (D.SKILL_CODE & S.CODE) > 0
               )
               AND EXISTS (
                   SELECT 1
                   FROM SKILLCODES AS S
                   WHERE S.NAME = 'Python'
                     AND (D.SKILL_CODE & S.CODE) > 0
               ) THEN 'A'

               WHEN EXISTS (
                   SELECT 1
                   FROM SKILLCODES AS S
                   WHERE S.NAME = 'C#'
                     AND (D.SKILL_CODE & S.CODE) > 0
               ) THEN 'B'

               WHEN EXISTS (
                   SELECT 1
                   FROM SKILLCODES AS S
                   WHERE S.CATEGORY = 'Front End'
                     AND (D.SKILL_CODE & S.CODE) > 0
               ) THEN 'C'
           END AS GRADE
    FROM DEVELOPERS AS D
) AS T
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID;