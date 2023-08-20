import pymysql

class DBSetting:
    def __init__(self, host, user, password, database):
        self.connection = self._get_connection(host, user, password)
        self.cursor = self._get_cursor()
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def _get_connection(self, host, user, password):
        conn= pymysql.connect(host=host, 
                    user=user,
                    password=password)
        return conn
    
    def _get_cursor(self):
        cursor = self.connection.cursor()
        return cursor

    def databse_exists(self):
        try:
            self.cursor.execute("SHOW DATABASES")
            databases = self.cursor.fetchall()
            database = [db[0] for db in databases]
            return self.database in database
        except Exception as e:
            print("Error:", e)
            return False
    
    def create_database(self):
        try:
            self.cursor.execute(f"CREATE DATABASE {self.database}")
            print(f"Database '{self.database}' created successfully.")
        except Exception as e:
            print("Error:", e)


class DBTool:
    def __init__(self, host, user, password, database, tableName):
        self.connection = self._get_connection(host, user, password, database)
        self.cursor = self._get_cursor()
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.tableName = tableName

    def _get_connection(self, host, user, password, database):
        conn= pymysql.connect(host=host, 
                    user=user,
                    password=password,
                    database=database)
        return conn
    
    def _get_cursor(self):
        cursor = self.connection.cursor()
        return cursor
            

    def table_exists(self):
        try:
            self.cursor.execute(f"SHOW TABLES LIKE '{self.tableName}'")
            result = self.cursor.fetchone()
            return result is not None
        except Exception as e:
            print("Error:", e)
            return False

    def create_table(self,sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def insert_data(self,data_query,data):
        self.cursor.execute(data_query,data)
        self.connection.commit()

    def read_all_data(self):
        self.cursor.execute(f"SELECT * FROM {self.tableName}")
        data = self.cursor.fetchall()
        return data
    
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def reconnect(self):
        self.connection = self._get_connection(self.host, self.user, self.password, self.database)
        self.cursor = self._get_cursor()
