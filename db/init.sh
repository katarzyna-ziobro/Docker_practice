#!/bin/bash
# init.sh
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER ${APP_DB_NPTA} WITH PASSWORD '${APP_DB_NPTA_PASS}';
    CREATE DATABASE ${APP_DB_NAME} OWNER ${APP_DB_NPTA};
EOSQL

psql -v ON_ERROR_STOP=1 --username "$APP_DB_NPTA" --dbname "$APP_DB_NAME" <<-EOSQL
    CREATE TABLE IF NOT EXISTS ${APP_DB_TABLE} (
        created_at TIMESTAMP DEFAULT NOW(),
        number INT
    );
EOSQL