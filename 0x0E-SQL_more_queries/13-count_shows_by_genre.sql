-- Importing database dump from another DATABASE with SQL:
SELECT gen.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS gen
       INNER JOIN `tv_show_genres` AS tv_s
       ON gen.`id` = tv_s.`genre_id`
 GROUP BY gen.`name`
 ORDER BY `number_of_shows` DESC;
