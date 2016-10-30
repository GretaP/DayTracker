import psycopg2


def connect():
    conn = psycopg2.connect('database super secret authentication info like passwords and stoopid stuff.')
    conn.cursor