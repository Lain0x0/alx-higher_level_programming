-- Import the database dump from DB 2.0 with SQL:
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS gen
       INNER JOIN `tv_show_genres` AS ser
       ON ser.`genre_id` = gen.`id`

       INNER JOIN `tv_show_ratings` AS rat
       ON rat.`show_id` = ser.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;-- Lists all genres in the database:
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS gen
       INNER JOIN `tv_show_genres` AS ser
       ON ser.`genre_id` = gen.`id`

       INNER JOIN `tv_show_ratings` AS rat
       ON rat.`show_id` = ser.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
