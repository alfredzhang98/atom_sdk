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

    def delete_database(self):
        try:
            self.cursor.execute(f"DROP DATABASE {self.database}")
            print(f"Database '{self.database}' deleted successfully.")
        except Exception as e:
            print("Error:", e)
    
    def list_databases(self):
        try:
            self.cursor.execute("SHOW DATABASES")
            databases = self.cursor.fetchall()
            print("List of databases:")
            for db in databases:
                print(db[0])
        except Exception as e:
            print("Error:", e)

    def close_connection(self):
        try:
            if self.cursor:
                self.cursor.close()
                self.cursor = None
            if self.connection:
                self.connection.close()
                self.connection = None
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

    def delete_table(self, table_name):
        try:
            sql = f"DROP TABLE {table_name}"
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Table '{table_name}' dropped successfully.")
        except Exception as e:
            print("Error:", e)

    def list_tables(self):
        try:
            self.cursor.execute("SHOW TABLES")
            tables = self.cursor.fetchall()
            print("List of tables:")
            for table in tables:
                print(table[0])
        except Exception as e:
            print("Error:", e)

    # User free
    # db commend by user
    def user_read_free(self,sql):
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print("Error:", e)
            return None
        
    # 增
    # insert_data_query = "INSERT INTO {table_name}  (name, gender, age, experiment_date, note) VALUES (%s, %s, %s, %s, %s)".format(table_name = tableName)
    # sample_data = [
    #     ("Alice", "Women", 25, "2023-08-19", "Sample note 1"),
    #     ("Bob", "Men", 30, "2023-08-20", "Sample note 2"),
    #     ("Charlie", "Others", 40, "2023-08-21", "Sample note 3"),
    # ]
    # insert_data(insert_data_query, sample_data[2])
    def insert_data(self,data_query,data):
        try:
            self.cursor.execute(data_query,data)
            self.connection.commit()
            print("Success insert:" + data)
        except Exception as e:
            print("Error:", e)

    # 删
    # delete_data("users", "name = 'John'")
    # delete_data("users", "age > 30 AND name LIKE 'J%'")
    def delete_data(self, table_name, condition):
        try:
            sql = f"DELETE FROM {table_name} WHERE {condition}"
            self.cursor.execute(sql)
            self.connection.commit()
            print("Data deleted successfully.")
        except Exception as e:
            print("Error:", e)

    # 改
    # set_data = {"age": 35, "city": "New York"}
    # update_data("users", set_data, "name = 'John'")
    def update_data(self, table_name, set_data, where_clause):
        try:
            set_clause = ', '.join([f"{column} = %s" for column in set_data.keys()])
            query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
            self.cursor.execute(query, tuple(set_data.values()))
            self.connection.commit()
            print("Success update")
        except Exception as e:
            print("Error:", e)


    # 查
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
        
    # 筛选
    # 准确字段
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
        
    def num_content_row(self, field, target):
        try:
            self.cursor.execute(f"SELECT *, ROW_NUMBER() OVER (ORDER BY {field}) AS row_index FROM {self.tableName} WHERE {field} = '{target}'")
            data = self.cursor.fetchall()
            if data is not None:
                return data
            else:
                return None
        except Exception as e:
            print("Error:", e)
            return None
    
    def read_content_row_index(self, field, target, row_index):
        try:
            self.cursor.execute(f"SELECT *, ROW_NUMBER() OVER (ORDER BY {field}) AS row_index FROM {self.tableName} WHERE {field} LIKE '{target}'")
            data = self.cursor.fetchall()
            if data is not None and row_index <= len(data):
                return data[row_index-1]  # Subtract 1 to convert 1-based index to 0-based index
            else:
                return None
        except Exception as e:
            print("Error:", e)
            return None

    
    # 筛选
    # 满足字段
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
        
    def num_content_row_fuzzy(self, field, target):
        try:
            self.cursor.execute(f"SELECT *, ROW_NUMBER() OVER (ORDER BY {field}) AS row_index FROM {self.tableName} WHERE {field} LIKE '%{target}%'")
            data = self.cursor.fetchall()
            if data is not None:
                return data
            else:
                return None
        except Exception as e:
            print("Error:", e)
            return None
    
    def read_content_row_fuzzy_index(self, field, target, row_index):
        try:
            self.cursor.execute(f"SELECT *, ROW_NUMBER() OVER (ORDER BY {field}) AS row_index FROM {self.tableName} WHERE {field} LIKE '%{target}%'")
            data = self.cursor.fetchall()
            if data is not None and row_index <= len(data):
                return data[row_index-1]  # Subtract 1 to convert 1-based index to 0-based index
            else:
                return None
        except Exception as e:
            print("Error:", e)
            return None


    
    # 筛选
    # 时间段
    # read date_column
    # read_data_by_date_range("2023-10-20", "2023-10-22")
    # read_data_by_datetime("2023-10-22 15:30:00", "2023-10-22 21:30:00")
    def read_data_by_date_range(self, date_column, start_date, end_date):
        try:
            query = f"SELECT * FROM {self.tableName} WHERE {date_column} >= %s AND {date_column} <= %s"
            self.cursor.execute(query, (start_date, end_date))
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print("Error:", e)
            return None
        
    # 筛选
    # 数字在某个区间的数据
    def read_content_by_figure_range(self, field, min, max):
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
            
    # 统计
    # 枚举计数
    def count_enum(self, field, type):
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
        

    # 分页
    # read_data_with_pagination_and_sort(2, 10, "id", "DESC")
    # 选择一个稳定的排序列，例如主键或唯一索引列。
    # 这样可以确保每个行的排序值是唯一的，不会出现重复或丢失数据的情况。
    # "ASC"（升序）或"DESC"（降序)
    def read_data_with_pagination_and_sort(self, page_number, page_size, master_key, maste_order, sort_column, sort_order):
        try:
            offset = (page_number - 1) * page_size
            if sort_column == None or sort_order == None:
                query = f"SELECT * FROM {self.tableName} ORDER BY {master_key} {maste_order} LIMIT {page_size} OFFSET {offset}"
            else:
                query = f"SELECT * FROM {self.tableName} ORDER BY {sort_column} {sort_order} {master_key} {maste_order} LIMIT {page_size} OFFSET {offset}"
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print("Error:", e)
            return None

    def close_connection(self):
        try:
            if self.cursor:
                self.cursor.close()
                self.cursor = None
            if self.connection:
                self.connection.close()
                self.connection = None
        except Exception as e:
            print("Error:", e)

    def reconnect(self):
        try:
            self.connection = self._get_connection(self.host, self.port, self.user, self.password, self.database)
            self.cursor = self._get_cursor()
        except Exception as e:
            print("Error:", e)

import os
import sys
from read_files import ReadFiles
sys.path.insert(0, sys.path[0]+"\\..\\")
from encryption.encryption_tool import EncryptionTools

if __name__ == "__main__":

    # 读取yaml文件
    # 拿到Key进行解析
    # 链接数据库
    # 增删改查

    # current_dir = os.path.dirname(__file__)
    # relative_path = os.path.join(current_dir, "settingfiles/mysql_setting_remote.yaml")
    # u_ReadFiles1 = ReadFiles()
    # u_readyaml1 = u_ReadFiles1.ReadYAML(relative_path)

    # aes = EncryptionTools.AES(current_dir, "DBkey")
    # host_remote = aes.decrypt_data(u_readyaml1.get_value("host"), aes.load_key())
    # port_remote = aes.decrypt_data(u_readyaml1.get_value("port"), aes.load_key())
    # user_remote = aes.decrypt_data(u_readyaml1.get_value("user"), aes.load_key())
    # password_remote = aes.decrypt_data(u_readyaml1.get_value("password"), aes.load_key())
    # database_remote = u_readyaml1.get_value("database")
    # tableName_remote = u_readyaml1.get_value("tableName")

    # print(host_remote, port_remote, user_remote, password_remote, database_remote, tableName_remote)

    # relative_path = os.path.join(current_dir, "settingfiles/mysql_setting_local.yaml")
    # u_ReadFiles2 = ReadFiles()
    # u_readyaml2 = u_ReadFiles2.ReadYAML(relative_path)
    
    # host_local = aes.decrypt_data(u_readyaml2.get_value("host"), aes.load_key())
    # port_local = aes.decrypt_data(u_readyaml2.get_value("port"), aes.load_key())
    # user_local = aes.decrypt_data(u_readyaml2.get_value("user"), aes.load_key())
    # password_local = aes.decrypt_data(u_readyaml2.get_value("password"), aes.load_key())
    # database_local = u_readyaml2.get_value("database")
    # tableName_local = u_readyaml2.get_value("tableName")

    # print(host_local, port_local, user_local, password_local, database_local, tableName_local)

    # 都需要先判断数据库
    # dbset =  DBSetting(host, port, user, password, database)
    # if dbset.databse_exists() == False:
    #     dbset.create_database()

    # dbtool = DBTool(host, port, user, password, database, tableName)

    # 都需要先判断数据表
    # if dbtool.table_exists() == False:
    #     dbtool.create_table(create_table_trigger_sql)


    # dbtool.insert_data(insert_data_query, sample_data[2])

    # data = dbtool.read_all_data()
    # print(data)

    # 务必关闭
    # dbtool.close_connection()


    #################################Tips#################################
    # 建表格式
    # create_table_trigger_sql = """
    # CREATE TABLE {table_name} (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     name VARCHAR(100) DEFAULT 'Admin',
    #     gender ENUM ('Men', 'Women', 'Others', 'Prefer no to say') DEFAULT 'Prefer no to say',
    #     age INT DEFAULT 99,
    #     experiment_date DATE NOT NULL,
    #     note VARCHAR(100) DEFAULT NULL
    # );
    # """.format(table_name = tableName)

    # 插入数据参考
    # insert_data_query = "INSERT INTO {table_name}  (name, gender, age, experiment_date, note) VALUES (%s, %s, %s, %s, %s)".format(table_name = tableName)
    # sample_data = [
    #     ("Alice", "Women", 25, "2023-08-19", "Sample note 1"),
    #     ("Bob", "Men", 30, "2023-08-20", "Sample note 2"),
    #     ("Charlie", "Others", 40, "2023-08-21", "Sample note 3"),
    # ]