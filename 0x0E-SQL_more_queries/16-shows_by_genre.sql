-- Importing the database dump from DATABASE 3.0 with SQL:
SELECT tv_s.`title`, gen.`name`
  FROM `tv_shows` AS tv_s
         LEFT JOIN `tv_show_genres` AS ser
	        ON tv_s.`id` = ser.`show_id`

       LEFT JOIN `tv_genres` AS gen
              ON ser.`genre_id` = gen.`id`
	       ORDER BY tv_s.`title`, gen.`name`;
