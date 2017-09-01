import asyncio
import sqlite3


class Manifest:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()


    def query(self, table, item_id):
        sql = """
              SELECT json FROM {}
              WHERE id = {}
              """
        self.cur.execute(sql.format(table, item_id))
        return self.cur.fetchall()
