import psycopg
 
DATABASE = {
    'NAME': 'apidata',
    'USER': 'postgres',
    'PASSWORD': 'root',
    'HOST': 'localhost',
    'PORT': '5432',
}

class Database():
    def __init__(self):
        self.conn = psycopg.connect(
            "postgres://postgres:root@localhost:5432/apidata",row_factory=psycopg.rows.dict_row,autocommit=True
            
        )
        self.cur = self.conn.cursor()
    
    def get_user(self):
        self.cur.execute('select * from utilisateur')
        user = self.cur.fetchall()
        return user

    