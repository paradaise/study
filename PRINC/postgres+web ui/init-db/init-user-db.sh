#!/usr/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER gogolevvg WITH PASSWORD 'Paradaise1337!';
    CREATE DATABASE princ_db;
    GRANT ALL PRIVILEGES ON DATABASE princ_db TO gogolevvg;
EOSQL
