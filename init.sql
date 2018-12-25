create database radioszpieg;
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON radioszpieg.* TO 'user'@'localhost';
flush priviliges;

use radioszpieg;
create table historia(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, reg_date TIMESTAMP, radio VARCHAR(40), song VARCHAR(80), song_id INT(6) UNSIGNED, listeners INT(6));
create table lastfm(id INT(6) UNSIGNED, artist VARCHAR(80), title VARCHAR(80), listeners INT(6) UNSIGNED, album VARCHAR(80), coverurl VARCHAR(200), url VARCHAR(200),duration INT(6) UNSIGNED, mbid VARCHAR(200));

