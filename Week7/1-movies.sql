-- 1
SELECT title
  FROM movies
 WHERE year = 2008;

-- 2
SELECT birth
  FROM people
 WHERE name = "Emma Stone";

-- 3
SELECT title
  FROM movies
 WHERE year >= 2018
 ORDER BY title;

-- 4
SELECT count(rating)
  FROM ratings
 WHERE rating = 10.0;

-- 5
SELECT title, year
  FROM movies
 WHERE title
  LIKE "Harry Potter%"
 ORDER BY year;

-- 6
SELECT avg(rating)
  FROM movies
  JOIN ratings
    ON movies.id = ratings.movie_id
 WHERE year = 2012;

-- 7
SELECT title, rating
  FROM movies
  JOIN ratings
    ON movies.id = ratings.movie_id
 WHERE year = 2010
 ORDER BY rating DESC, title
 LIMIT 10;

-- 8
SELECT name
  FROM movies, stars, people
 WHERE movies.id = stars.movie_id
   AND people.id = stars.person_id
   AND title = "Toy Story";

-- 9
SELECT distinct(name)
  FROM movies, stars, people
 WHERE movies.id = stars.movie_id
   AND people.id = stars.person_id
   AND year = 2004
 ORDER BY birth;

-- 10
SELECT distinct(name)
  FROM ratings, directors, people
 WHERE directors.movie_id = ratings.movie_id
   AND people.id = directors.person_id
   AND rating >= 9.0;

-- 11
SELECT title
  FROM movies, ratings, stars, people
 WHERE movies.id = ratings.movie_id
   AND movies.id = stars.movie_id
   AND people.id = stars.person_id
   AND name = "Chadwick Boseman"
 ORDER BY rating DESC
 LIMIT 5;

-- 12
SELECT title
  FROM movies, stars, people
 WHERE movies.id = stars.movie_id
   AND people.id = stars.person_id
   AND name = "Johnny Depp"
   AND title IN
       (SELECT title
          FROM movies, stars, people
         WHERE movies.id = stars.movie_id
           AND people.id = stars.person_id
           AND name = "Helena Bonham Carter");

-- 13
SELECT distinct(name)
  FROM stars, people
 WHERE people.id = stars.person_id
   AND name != "Kevin Bacon"
   AND movie_id IN
       (SELECT movie_id
          FROM stars, people
         WHERE stars.person_id = people.id
           AND name = "Kevin Bacon"
           AND birth = 1958);
