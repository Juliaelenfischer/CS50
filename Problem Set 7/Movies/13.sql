SELECT distinct(name) FROM people
JOIN movies ON stars.movie_id = movies.id
JOIN stars ON people.id = stars.person_id
WHERE movies.title IN(
    SELECT distinct(movies.title) FROM people
    JOIN movies ON stars.movie_id = movies.id
    JOIN stars ON people.id = stars.person_id
    WHERE people.name = "Kevin Bacon" AND people.birth = 1958) AND people.name != "Kevin Bacon";
