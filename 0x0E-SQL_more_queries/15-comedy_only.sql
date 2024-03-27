-- Import the database dump from DATABASE 2.0 with SQL:
SELECT tv_s.`title`
  FROM `tv_shows` AS tv_s
       INNER JOIN `tv_show_genres` AS ser
       ON tv_s.`id` = ser.`show_id`

       INNER JOIN `tv_genres` AS gen
       ON gen.`id` = ser.`genre_id`
       WHERE gen.`name` = "Comedy"
 ORDER BY tv_s.`title`;
