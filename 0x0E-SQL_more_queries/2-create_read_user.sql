-- Creating a new DATABASE for a user with SQL:
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2;
GRANTS ALL PRIVILEGS ON hbtn_0d_2 TO "user_0d_2"@"localhost" IDENTIFIED BY "user_0d_2_pwd";
