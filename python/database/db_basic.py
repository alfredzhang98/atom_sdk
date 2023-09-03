import pymysql

class DBSetting:
    def __init__(self, host, port, user, password, database):
        self.connection = self._get_connection(host, port, user, password)
        self.cursor = self._get_cursor()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def _get_connection(self, host, port, user, password):
        if port != None:
            conn= pymysql.connect(host=host, 
            port = int(port),
            user=user,
            password=password)
        else:
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
    def __init__(self, host, port, user, password, database, tableName):
        self.connection = self._get_connection(host, port, user, password, database)
        self.cursor = self._get_cursor()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.tableName = tableName

    def _get_connection(self, host, port, user, password, database):
        if port != None:
            conn= pymysql.connect(host=host, 
            port = int(port),
            user=user,
            password=password,
            database = database)
        else:
            conn= pymysql.connect(host=host, 
            user=user,
            password=password,
            database = database)
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
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print("Error:", e)

    def insert_data(self,data_query,data):
        try:
            self.cursor.execute(data_query,data)
            self.connection.commit()
            print("Success insert:" + data)
        except Exception as e:
            print("Error:", e)


    def user_read_free(self,sql):
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print("Error:", e)
            return None

    # read all data
    def read_all_data(self):
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName}")
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print("Error:", e)
            return None
    
    # read lastest line data
    def read_latest_line(self):
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName}")
            data = self.cursor.fetchall()
            return data[-1]
        except Exception as e:
            print("Error:", e)
            return None
    
    # field is the db 字段 准确搜
    def read_content_row(self, field, target):
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName} WHERE {field} = '{target}'")
            data = self.cursor.fetchall()
            if data is not None:
                return data
            else:
                return None
        except Exception as e:
            print("Error:", e)
            return None
        
    # field is the db 字段 模糊搜
    def read_content_row_fuzzy(self, field, target):
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName} WHERE {field} LIKE '%{target}%'")
            data = self.cursor.fetchall()
            if data is not None:
                return data
            else:
                return None
        except Exception as e:
            print("Error:", e)
            return None
        
    # 筛选figure在某个区间
    def screen_figure_content_range(self, field, min, max):
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName} WHERE {field} >= {min} AND {field} <= {max}")
            data = self.cursor.fetchall()
            if data is not None:
                return data
            else:
                return None
        except Exception as e:
            print("Error:", e)
            return None
            
    # 枚举计数
    def read_enum_count(self, field, type):
        try:
            self.cursor.execute(f"SELECT COUNT(*) AS category_count FROM {self.tableName} WHERE {field} = '{type}'")
            data = self.cursor.fetchone()
            if data is not None:
                return data[0]
            else:
                return None
        except Exception as e:
            print("Error:", e)
            return None

    def close_connection(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except Exception as e:
            print("Error:", e)

    def reconnect(self):
        try:
            self.connection = self._get_connection(self.host, self.port, self.user, self.password, self.database)
            self.cursor = self._get_cursor()
        except Exception as e:
            print("Error:", e)

