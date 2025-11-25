import sqlite3
import psycopg2
# path / url de conexão
<<<<<<< HEAD
DB_PATH = "postgresql://neondb_owner:npg_O5dEQGbiSjA4@ep-polished-hill-ahfdsdqk-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
    return psycopg2.connect(DB_PATH)

=======
DB_PATH = "postgresql://neondb_owner:npg_5utNwhLvEel4@ep-lively-mud-acbp5jaw-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
    return psycopg2.connect(DB_PATH)
>>>>>>> 70f4be88010779fb5bbb05e41146c3575fc2d540
