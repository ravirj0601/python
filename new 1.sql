SELECT DISTINCT CITY FROM STATION
where city not in(SELECT DISTINCT CITY FROM STATION WHERE REGEXP_LIKE(CITY, '^[aeiou].*[aeiou]$','i')) ;