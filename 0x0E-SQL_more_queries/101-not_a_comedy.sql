-- Importing the database dump from DB with SQL:
SELECT DISTINCT `title`
  FROM `tv_shows` AS tv_s
       LEFT JOIN `tv_show_genres` AS ser
       ON ser.`show_id` = tv_s.`id`

       LEFT JOIN `tv_genres` AS gen
       ON gen.`id` = ser.`genre_id`
       WHERE tv_s.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS tv_s
	             INNER JOIN `tv_show_genres` AS ser
		     ON ser.`show_id` = tv_s.`id`

		     INNER JOIN `tv_genres` AS gen
		     ON gen.`id` = ser.`genre_id`
		     WHERE gen.`name` = "Comedy")
 ORDER BY `title`;
