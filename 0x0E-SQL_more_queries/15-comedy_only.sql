-- list all shows in genre comedy in database
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres AS tsg ON tv_shows.id = tsg.show_id
INNER JOIN tv_genres ON tsg.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
