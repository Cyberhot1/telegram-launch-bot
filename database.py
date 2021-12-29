import sqlite3

class DBHelper:
	name = "data.sqlite"
	def __init__(self):
		self.conn = sqlite3.connect(DBHelper.name, check_same_thread = False)
		self.cur = self.conn.cursor()

	def setup(self):
		stmt = "CREATE TABLE IF NOT EXISTS data (id BIGINT NOT NULL PRIMARY KEY, types TEXT, files TEXT, texts TEXT)"
		self.cur.execute(stmt)
		self.conn.commit()

	def add_data(self, ids, type, file, text):
		stmt = "INSERT INTO data (id, types, files, texts) VALUES (?, ?, ?, ?)"
		args = (ids, type, file, text, )
		self.cur.execute(stmt, args)
		self.conn.commit()

	def del_data(self, ids):
		stmt = "DELETE FROM data WHERE id = (?)"
		args = (ids, )
		self.cur.execute(stmt, args)
		self.conn.commit()

	def get_data(self, ids):
		stmt = "SELECT types, files, texts FROM data WHERE id = (?)"
		args = (ids, )
		self.cur.execute(stmt, args)
		return self.cur.fetchall()

	def check_data(self, ids):
		stmt = "SELECT id FROM data WHERE id = (?)"
		args = (ids, )
		self.cur.execute(stmt, args)
		return self.cur.fetchall()
		
	def check_all(self):
		stmt = "SELECT * FROM data"
		self.cur.execute(stmt)
		return self.cur.fetchall()
		
	def del_all_data(self):
		stmt = "DELETE FROM data"
		self.cur.execute(stmt)
		self.conn.commit()
