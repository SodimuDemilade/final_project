import psycopg2

conn = psycopg2.connect(
    database="MOODLE_CRAWLER", user="postgres", password="demi1234", host='127.0.0.1'
)

cursor = conn.cursor()

# cursor.execute("DROP TABLE IF EXISTS USER_INFO")
#
# sql = '''CREATE TABLE USER_INFO(
#     USERNAME CHAR(20) NOT NULL,
#     PASSWORD CHAR(30) NOT NULL
# )'''
# cursor.execute(sql)

cursor.execute('''INSERT INTO USER_INFO(USERNAME, PASSWORD)
    VALUES('19CG026486', 'demi1234')
''')

conn.commit()
print("Records inserted.......")

conn.close()