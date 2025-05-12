echo "=== MariaDB Проверка ===" && \
docker exec lab_mariadb mariadb -u root -prootpassword -e "
SELECT 
  'max_connections' AS 'Параметр',
  @@max_connections AS 'Значение'
UNION SELECT
  'wait_timeout',
  @@wait_timeout
UNION SELECT
  'character_set_server',
  @@character_set_server
UNION SELECT
  'bind_address',
  @@bind_address
UNION SELECT
  'testuser_exists',
  IF(EXISTS(SELECT 1 FROM mysql.user WHERE User='testuser'), 'Да', 'Нет')
UNION SELECT
  'testdb_exists',
  IF(EXISTS(SELECT 1 FROM information_schema.SCHEMATA WHERE SCHEMA_NAME='testdb'), 'Да', 'Нет');"


echo -e "\n\n\n=== PostgreSQL Проверка ===" && \
docker exec lab_postgres psql -U postgres -c "
SELECT 'max_connections' AS \"Параметр\", 
       setting AS \"Значение\" 
FROM pg_settings 
WHERE name='max_connections'
UNION ALL
SELECT 'idle_in_transaction_session_timeout', 
       setting 
FROM pg_settings 
WHERE name='idle_in_transaction_session_timeout'
UNION ALL
SELECT 'server_encoding', 
       setting 
FROM pg_settings 
WHERE name='server_encoding'
UNION ALL
SELECT 'listen_addresses', 
       setting 
FROM pg_settings 
WHERE name='listen_addresses'
UNION ALL
SELECT 'testdb_exists', 
       CASE WHEN EXISTS(SELECT 1 FROM pg_database WHERE datname='testdb') 
            THEN 'Да' ELSE 'Нет' END
UNION ALL
SELECT 'postgres_user_exists', 
       CASE WHEN EXISTS(SELECT 1 FROM pg_roles WHERE rolname='postgres') 
            THEN 'Да' ELSE 'Нет' END;"