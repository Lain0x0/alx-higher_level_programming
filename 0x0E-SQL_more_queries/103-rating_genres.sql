-- Importing database to dump from DB 2.0 with SQL:
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rat
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
JOIN tv_show_rat ON tv_show_rat.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY rat DESC;
