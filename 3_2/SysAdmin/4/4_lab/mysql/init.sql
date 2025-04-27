CREATE DATABASE testdb;
CREATE USER 'testuser'@'%' IDENTIFIED BY 'testpass';
GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%';
ALTER USER 'testuser'@'%' IDENTIFIED BY 'newpassword';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'newrootpass';
FLUSH PRIVILEGES;