-- Import the database dump from DATABASE with SQL:
SELECT gen.`name`
  FROM `tv_genres` AS gen
       INNER JOIN `tv_show_genres` AS ser
       ON gen.`id` = ser.`genre_id`

       INNER JOIN `tv_shows` AS tv_s
       ON tv_s.`id` = ser.`show_id`
       WHERE tv_S.`title` = "Dexter"
 ORDER BY gen.`name`;
