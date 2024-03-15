-- show and all genres linked to it
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres AS tsg ON tv_shows.id = tsg.show_id
LEFT JOIN tv_genres ON tsg.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name;
