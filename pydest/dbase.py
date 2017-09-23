import sqlite3


class DBase:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()


    def query(self, hash_id, definition):
        sql = """
              SELECT json FROM {}
              WHERE id = {}
              """
        self.cur.execute(sql.format(definition,hash_id))
        return self.cur.fetchall()
