-- Importing the database with SQL:
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS tv_s
       INNER JOIN `tv_show_ratings` AS rat
       ON tv_s.`id` = rat.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
