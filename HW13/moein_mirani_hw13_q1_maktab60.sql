\c dvdrental


#part a
\dt

#part b

SELECT 
	first_name, 
	last_name
FROM 
	customer 
WHERE 
	first_name LIKE 'R%' OR 
	first_name LIKE '%n';

#part c

SELECT
count(*)
FROM
	customer
	WHERE
	address_id>20;


#part d

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


#part e


SELECT first_name 
               FROM actor
               GROUP BY first_name HAVING COUNT(*) = 1
               order BY
               first_name;

#part f

SELECT
	AVG(rental_duration)  average_duration,
	MIN(rental_duration)  minimom_duration,
	MAX(rental_duration) maximum_duration,
	SUM(rental_duration) sumation_duration
	FROM
	film;

#part g

SELECT
	c.customer_id,
	c.first_name customer_first_name,
	c.last_name customer_last_name,
	p.payment_id,
	r.return_date
FROM
	customer c
INNER JOIN payment p 
    ON p.customer_id = c.customer_id
INNER JOIN rental r 
    ON r.customer_id = p.customer_id
ORDER BY payment_date;


#part h


select 
	first_name,
	last_name,
	address,
	city_id,
	city,
	country
FROM
	customer
	left JOIN address
	using(address_id)
	INNER JOIN city
	using(city_id)
	INNER JOIN country
	using(country_id)
	ORDER BY country; 







