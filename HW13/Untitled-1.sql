\c dvdrental

\dt

\d customer


SELECT 
	first_name, 
	last_name
FROM 
	customer 
WHERE 
	first_name LIKE 'R%' OR 
	first_name LIKE '%n';






SELECT
    actor_id,
	last_name,
	first_name
FROM
	actor
WHERE
	first_name = 'Nick' OR
    first_name = 'Bette' OR
    first_name = 'Ed' ;    


SELECT
first_name,
last_name
from actor WHERE first_name in 
(SELECT first_name 
               FROM actor
               GROUP BY first_name HAVING COUNT(*) = 1)
               order BY
               first_name;