from app import db, app
import psycopg2

conn = psycopg2.connect(
    dbname="projeto",
    user="postgres",
    password="rodomastwr",
    host="localhost",
    port="5433"
)

cur = conn.cursor()


with app.app_context():
    db.create_all()