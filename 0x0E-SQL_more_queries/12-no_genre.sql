-- Importing the database dump from DATABASE with SQL:
SELECT ser.`title`, gen.`genre_id`
  FROM `tv_shows` AS ser
       LEFT JOIN `tv_show_genres` AS gen
       ON ser.`id` = gen.`show_id`
       WHERE gen.`genre_id` IS NULL
 ORDER BY ser.`title`, gen.`genre_id`;
