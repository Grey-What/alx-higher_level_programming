-- list all genres of the show 'Dexter'
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres AS tsg ON tv_genres.id = tsg.genre_id
INNER JOIN tv_shows ON tsg.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
