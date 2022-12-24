from shlama_db import get_db

#to fetch all data
def get_data():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM meters"
    cursor.execute(query)
    return cursor.fetchall()

#to get data by id
def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM meter_data WHERE meter_id = ? "
    cursor.execute(statement, [id])
    return cursor.fetchone()    