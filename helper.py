import psycopg2

conn = psycopg2.connect('postgres://avnadmin:d4x37goj4y8m71a1@pg-13e4cc60-nikithbhee-1d6c.aivencloud.com:24570/defaultdb?sslmode=require')

cur = conn.cursor()
cur.execute('''
CREATE TABLE test (
    key VARCHAR(24) NOT NULL,
    value VARCHAR(24) NOT NULL
);
''')

cur.close()
conn.close()