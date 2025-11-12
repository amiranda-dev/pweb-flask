import sqlite3
import psycopg2
# path / url de conexão
DB_PATH = "postgresql://neondb_owner:npg_5utNwhLvEel4@ep-lively-mud-acbp5jaw-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
    return psycopg2.connect(DB_PATH)