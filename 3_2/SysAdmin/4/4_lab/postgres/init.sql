CREATE DATABASE testdb;
CREATE USER testuser WITH PASSWORD 'testpass';
ALTER DATABASE testdb OWNER TO testuser;
ALTER USER testuser PASSWORD 'newpassword';
ALTER USER postgres PASSWORD 'newpostgrespass';