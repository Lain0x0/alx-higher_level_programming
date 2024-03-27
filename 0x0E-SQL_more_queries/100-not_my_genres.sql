-- Importing the database dump from DATABASE with SQL:
SELECT DISTINCT `name`
  FROM `tv_genres` AS gen
       INNER JOIN `tv_show_genres` AS ser
       ON gen.`id` = ser.`genre_id`

       INNER JOIN `tv_shows` AS tv_s
       ON ser.`show_id` = tv_s.`id`
       WHERE gen.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS gen
	             INNER JOIN `tv_show_genres` AS ser
		     ON gen.`id` = ser.`genre_id`

		     INNER JOIN `tv_shows` AS tv_s
		     ON ser.`show_id` = tv_s.`id`
		     WHERE tv_s.`title` = "Dexter")
 ORDER BY gen.`name`;
