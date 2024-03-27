-- Listing all shows from an imported DATABASE with SQL:
SELECT ser.`title`, gen.`genre_id`
  FROM `tv_shows` AS ser
        INNER JOIN `tv_show_genres` AS gen
	ON ser.`id` = gen.`show_id`
 ORDER BY ser.`title`, gen.`genre_id`;
