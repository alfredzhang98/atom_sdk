import pymysql
from db_tool import DBTool,DBSetting


host='localhost'
user='root'
password='ZQY201613886f-'
database='test1'

tableName = 'psy_exp_01'

create_table_trigger_sql = """
CREATE TABLE {table_name} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) DEFAULT 'Admin',
    gender ENUM ('Men', 'Women', 'Others', 'Prefer no to say') DEFAULT 'Prefer no to say',
    age INT DEFAULT 99,
    experiment_date DATE NOT NULL,
    note VARCHAR(100) DEFAULT NULL
);
""".format(table_name = tableName)

insert_data_query = "INSERT INTO {table_name}  (name, gender, age, experiment_date, note) VALUES (%s, %s, %s, %s, %s)".format(table_name = tableName)
sample_data = [
    ("Alice", "Women", 25, "2023-08-19", "Sample note 1"),
    ("Bob", "Men", 30, "2023-08-20", "Sample note 2"),
    ("Charlie", "Others", 40, "2023-08-21", "Sample note 3"),
]



if __name__ == "__main__":

    dbset =  DBSetting(host, user, password, database)
    if dbset.databse_exists() == False:
        dbset.create_database()


    dbtool = DBTool(host, user, password, database, tableName)

    if dbtool.table_exists() == False:
        dbtool.create_table(create_table_trigger_sql)
    dbtool.insert_data(insert_data_query, sample_data[1])
    data = dbtool.read_all_data()
    print(data)
    dbtool.close_connection()
