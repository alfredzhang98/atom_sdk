import pymysql
import logging
import csv

class MysqlBaseHandler:
    def __init__(self, host, port, user, password, database):
        '''
        Initialize the database handler with connection details.
        Parameters:
        - host: Database server host
        - port: Database server port
        - user: Username for the database
        - password: Password for the database
        - database: Name of the database
        '''
        self.connection = self._get_connection(host, port, user, password)
        self.cursor = self._get_cursor()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def _get_connection(self, host, port, user, password):
        if port is not None:
            conn = pymysql.connect(
                host=host, 
                port=int(port),
                user=user,
                password=password
            )
        else:
            conn = pymysql.connect(
                host=host, 
                user=user,
                password=password
            )
        return conn
    
    def _get_cursor(self):
        cursor = self.connection.cursor()
        return cursor

    def database_exists(self):
        '''
        Check if the specified database exists.
        Returns True if the database exists, False otherwise.
        '''
        try:
            self.cursor.execute("SHOW DATABASES")
            databases = self.cursor.fetchall()
            database_list = [db[0] for db in databases]
            return self.database in database_list
        except Exception as e:
            self.logger.error(f"Error in database_exists: {e}")
            return False
    
    def create_database(self):
        '''
        Create a new database with the name specified in the class constructor.
        '''
        try:
            self.cursor.execute(f"CREATE DATABASE {self.database}")
            print(f"Database '{self.database}' created successfully.")
        except Exception as e:
            self.logger.error(f"Error in create_database: {e}")

    def delete_database(self):
        '''
        Delete the database specified in the class constructor.
        '''
        try:
            self.cursor.execute(f"DROP DATABASE {self.database}")
            print(f"Database '{self.database}' deleted successfully.")
        except Exception as e:
            self.logger.error(f"Error in delete_database: {e}")
    
    def list_databases(self):
        '''
        List all databases in the MySQL server.
        '''
        try:
            self.cursor.execute("SHOW DATABASES")
            databases = self.cursor.fetchall()
            print("List of databases:")
            for db in databases:
                print(db[0])
        except Exception as e:
            self.logger.error(f"Error in list_databases: {e}")

    def close_connection(self):
        '''
        Close the database connection and cursor.
        '''
        try:
            if self.cursor:
                self.cursor.close()
                self.cursor = None
            if self.connection:
                self.connection.close()
                self.connection = None
        except Exception as e:
            self.logger.error(f"Error in close_connection: {e}")

class MysqlTableHandler:
    def __init__(self, host, port, user, password, database, tableName):
        '''
        Initialize the table handler with connection details and table name.
        Inherits from MysqlBaseHandler.
        Parameters:
        - host: Database server host
        - port: Database server port
        - user: Username for the database
        - password: Password for the database
        - database: Name of the database
        - tableName: Name of the table to be handled
        '''
        self.connection = self._get_connection(host, port, user, password, database)
        self.cursor = self._get_cursor()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.tableName = tableName
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

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
        '''
        Check if the specified table exists in the database.
        Returns True if the table exists, False otherwise.
        '''
        try:
            self.cursor.execute(f"SHOW TABLES LIKE '{self.tableName}'")
            result = self.cursor.fetchone()
            return result is not None
        except Exception as e:
            self.logger.error(f"Error in table_exists: {e}")
            return False

    def create_table(self,sql):
        '''
        Create a table in the database using the provided SQL command.
        Parameter:
        - sql: A string containing the SQL command to create the table.
        '''
        try:
            self._start_transaction()
            self.cursor.execute(sql)
            self._commit_transaction()
        except Exception as e:
            self._rollback_transaction() 
            self.logger.error(f"Error in create_table: {e}")

    def delete_table(self, table_name):
        '''
        Delete a table from the database.
        Parameter:
        - table_name: Name of the table to be deleted.
        '''
        try:
            sql = f"DROP TABLE {table_name}"
            self._start_transaction()
            self.cursor.execute(sql)
            self._commit_transaction()
            print(f"Table '{table_name}' dropped successfully.")
        except Exception as e:
            self._rollback_transaction() 
            self.logger.error(f"Error in delete_table: {e}")

    def list_tables(self):
        '''
        List all tables in the current database.
        '''
        try:
            self.cursor.execute("SHOW TABLES")
            tables = self.cursor.fetchall()
            print("List of tables:")
            for table in tables:
                print(table[0])
        except Exception as e:
            self.logger.error(f"Error in list_tables: {e}")
  
    def close_connection(self):
        '''
        Close the database connection and cursor.
        Overrides the method from MysqlBaseHandler.
        '''
        try:
            if self.cursor:
                self.cursor.close()
                self.cursor = None
            if self.connection:
                self.connection.close()
                self.connection = None
        except Exception as e:
            self.logger.error(f"Error in close_connection: {e}")

    def reconnect(self):
        '''
        Reconnect to the database. Useful if the connection was lost.
        '''
        try:
            self.connection = self._get_connection(self.host, self.port, self.user, self.password, self.database)
            self.cursor = self._get_cursor()
        except Exception as e:
            self.logger.error(f"Error in reconnect: {e}")

    # Transaction processing function
    def _start_transaction(self):
        try:
            self.connection.begin()
        except Exception as e:
            print("Error:", e)

    def _commit_transaction(self):
        try:
            self.connection.commit()
        except Exception as e:
            print("Error:", e)

    def _rollback_transaction(self):
        try:
            self.connection.rollback()
        except Exception as e:
            print("Error:", e)

    # basic sql
    def user_execute_free(self, sql, is_select=False):
        '''
        Execute a free-form SQL query. The method can handle both read and write operations.
        Parameters:
        - sql: A string containing the SQL query.
        - is_select: A boolean indicating if the query is a SELECT operation (default is False).
        '''
        try:
            if not is_select:
                self._start_transaction()

            self.cursor.execute(sql)

            if is_select:
                data = self.cursor.fetchall()
                return data
            else:
                self._commit_transaction()
                return f"Query executed successfully: {sql}"

        except Exception as e:
            if not is_select:
                self._rollback_transaction()
            self.logger.error(f"Error in user_execute_free: {e}")
            return None

    def insert_data(self, data):
        '''
        Insert data into the table.
        Parameters:
        - data: A dictionary where keys are column names and values are the corresponding data to be inserted.
        Example:
        data = {
            "name": "Alice",
            "gender": "Women",
            "age": 25,
            "experiment_date": "2023-08-19",
            "note": "Sample note 1"
        }
        '''
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {self.tableName} ({columns}) VALUES ({placeholders})"
        
        try:
            self._start_transaction()
            self.cursor.execute(sql, tuple(data.values()))
            self._commit_transaction()
            print(f"Success insert: {data}")
        except Exception as e:
            self._rollback_transaction() 
            self.logger.error(f"Error in insert_data: {e}")

    def bulk_insert_data(self, data_query, data_list):
        '''
        Bulk insert data into a table.
        Parameters:
        - data_query: A string containing the SQL insert query.
        - data_list: A list of tuples containing the data to be inserted.

        Example:
        Suppose you have a table 'employees' with columns 'name', 'age', 'position'.
        Your SQL insert query would be:
        insert_query = "INSERT INTO employees (name, age, position) VALUES (%s, %s, %s)"

        And the data to be inserted could be a list of tuples like:
        data_to_insert = [
            ("Alice", 30, "Manager"),
            ("Bob", 25, "Developer"),
            ("Charlie", 28, "Analyst")
        ]

        You would call the method like this:
        bulk_insert_data(insert_query, data_to_insert)
        '''
        try:
            self.cursor.executemany(data_query, data_list)
            self.connection.commit()
            print(f"Successfully inserted {len(data_list)} records.")
        except Exception as e:
            self.logger.error(f"Error in bulk_insert_data: {e}")

    def delete_data(self, row_condition, column=None, data=None):
        '''
        Delete data from a table based on a condition.
        Parameters:
        - row_condition: The condition for selecting the row(s) to be deleted.
        - column: Optional. The column to check for additional data.
        - data: Optional. The data to check for in the column.
        Tips: row_condition = "position = 'Senior Developer' AND years_of_experience > 5"
        '''
        try:
            if row_condition is None and (column is None or data is None):
                raise ValueError("No conditions provided for deletion.")
            
            if row_condition is None:
                raise ValueError("No conditions provided for delete. Refusing to delete all rows.")

            sql = "DELETE FROM {self.tableName}"
            params = ()

            if row_condition is not None:
                sql += f" WHERE {row_condition}"
            if column is not None and data is not None:
                sql += f" AND {column} = %s" if 'WHERE' in sql else f" WHERE {column} = %s"
                params = (data,)

            self._start_transaction()
            self.cursor.execute(sql, params)
            self._commit_transaction()
            print("Data deleted successfully.")
        except Exception as e:
            self._rollback_transaction()
            self.logger.error(f"Error in delete_data: {e}")

    def update_data(self, row_condition, update_column, update_data):
        '''
        Update data in a table.
        Parameters:
        - row_condition: The condition for selecting the row(s) to be updated.
        - update_column: The column to be updated.
        - update_data: The new data for the update_column.
        Tips: row_condition = "position = 'Senior Developer' AND years_of_experience > 5"
        '''
        try:
            if update_column is None or update_data is None:
                raise ValueError("Update column and data must be provided.")

            if row_condition is None:
                raise ValueError("No conditions provided for update. Refusing to update all rows.")

            sql = f"UPDATE {self.tableName} SET {update_column} = %s WHERE {row_condition}"
            self._start_transaction()
            self.cursor.execute(sql, (update_data,))
            self._commit_transaction()
            print("Data updated successfully.")
        except Exception as e:
            self._rollback_transaction()
            self.logger.error(f"Error in update_data: {e}")

    # accurate read
    def read_latest_line(self):
        '''
        Read the latest line (most recent entry) from the table.
        Returns the latest row from the table.
        '''
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName} ORDER BY id DESC LIMIT 1")
            data = self.cursor.fetchone()
            return data
        except Exception as e:
            self.logger.error(f"Error in read_latest_line: {e}")
            return None

    def read_content_row(self, field, target):
        '''
        Read rows from the table where a specific field matches a target value.
        Parameters:
        - field: The column to match.
        - target: The value to match in the field.
        '''
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName} WHERE {field} = '{target}'")
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            self.logger.error(f"Error in read_content_row: {e}")
            return None

    def num_content_row(self, field, target):
        '''
        Count the number of rows where a specific field matches a target value.
        Parameters:
        - field: The column to match.
        - target: The value to match in the field.
        '''
        try:
            self.cursor.execute(f"SELECT COUNT(*) FROM {self.tableName} WHERE {field} = '{target}'")
            count = self.cursor.fetchone()[0]
            return count
        except Exception as e:
            self.logger.error(f"Error in num_content_row: {e}")
            return None

    def read_content_row_index(self, field, target, row_index):
        '''
        Read a specific row based on a field match and row index.
        Parameters:
        - field: The column to match.
        - target: The value to match in the field.
        - row_index: The index of the row to return.
        '''
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName} WHERE {field} = '{target}'")
            data = self.cursor.fetchall()
            if data is not None and row_index < len(data):
                return data[row_index]
            else:
                return None
        except Exception as e:
            self.logger.error(f"Error in read_content_row_index: {e}")
            return None
    
    # fuzzy read
    def read_content_row_fuzzy(self, field, target):
        '''
        Read rows from the table where a specific field contains a target value (fuzzy search).
        Parameters:
        - field: The column to perform the search on.
        - target: The substring to search for in the field.
        '''
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName} WHERE {field} LIKE '%{target}%'")
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            self.logger.error(f"Error in read_content_row_fuzzy: {e}")
            return None

    def num_content_row_fuzzy(self, field, target):
        '''
        Count the number of rows where a specific field contains a target value (fuzzy search).
        Parameters:
        - field: The column to perform the search on.
        - target: The substring to search for in the field.
        '''
        try:
            self.cursor.execute(f"SELECT COUNT(*) FROM {self.tableName} WHERE {field} LIKE '%{target}%'")
            count = self.cursor.fetchone()[0]
            return count
        except Exception as e:
            self.logger.error(f"Error in num_content_row_fuzzy: {e}")
            return None

    def read_content_row_index_fuzzy(self, field, target, row_index):
        '''
        Read a specific row based on a field fuzzy match and row index.
        Parameters:
        - field: The column to perform the fuzzy search on.
        - target: The substring to search for in the field.
        - row_index: The index of the row to return.
        '''
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName} WHERE {field} LIKE '%{target}%'")
            data = self.cursor.fetchall()
            if data is not None and row_index < len(data):
                return data[row_index]
            else:
                return None
        except Exception as e:
            self.logger.error(f"Error in read_content_row_index_fuzzy: {e}")
            return None

    # complex read
    def read_complex_query_builder(self, select_columns, conditions, join=None, group_by=None, having=None, order_by=None, limit=None):
        '''
        Build and execute a complex SQL query.
        Parameters:
        - select_columns: Columns to select in the query. Example: ['column1', 'column2']
        - conditions: Conditions for the WHERE clause. Example: ['column1 > 5', 'column2 = "value"']
        - join: JOIN clause for the query. Example: 'JOIN another_table ON table.column = another_table.column'
        - group_by: GROUP BY clause. Example: 'column1'
        - having: HAVING clause for GROUP BY. Example: 'COUNT(column1) > 1'
        - order_by: ORDER BY clause. Example: 'column1 DESC'
        - limit: LIMIT clause. Example: '10'

        Example usage:
        results = handler.complex_query_builder(
            select_columns=["table.column1", "another_table.column2"],
            conditions=["table.column1 > 5", "another_table.column2 = 'value'"],
            join="JOIN another_table ON table.column = another_table.column",
            group_by="table.column1",
            having="COUNT(table.column1) > 1",
            order_by="table.column1 DESC",
            limit="10"
        )
        '''
        query = f"SELECT {', '.join(select_columns)} FROM {self.tableName}"
        if join:
            query += f" {join}"
        if conditions:
            query += f" WHERE {' AND '.join(conditions)}"
        if group_by:
            query += f" GROUP BY {group_by}"
        if having:
            query += f" HAVING {having}"
        if order_by:
            query += f" ORDER BY {order_by}"
        if limit:
            query += f" LIMIT {limit}"

        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            self.logger.error(f"Error in complex_query_builder: {e}")
            return None

    # time figure and other range
    def read_data_by_date_range(self, date_column, start_date, end_date):
        '''
        Read data from the table within a specified date range.
        Parameters:
        - date_column: The column containing date values.
        - start_date: The start date of the range.
        - end_date: The end date of the range.
        '''
        try:
            query = f"SELECT * FROM {self.tableName} WHERE {date_column} BETWEEN %s AND %s"
            self.cursor.execute(query, (start_date, end_date))
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            self.logger.error(f"Error in read_data_by_date_range: {e}")
            return None

    def read_content_by_figure_range(self, field, min_value, max_value):
        '''
        Read data from the table where a numeric field is within a specified range.
        Parameters:
        - field: The numeric column to be checked.
        - min_value: The minimum value of the range.
        - max_value: The maximum value of the range.
        '''
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName} WHERE {field} BETWEEN {min_value} AND {max_value}")
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            self.logger.error(f"Error in read_content_by_figure_range: {e}")
            return None

    # enum return num
    def count_enum(self, field, value):
        '''
        Count the number of occurrences of a specific value in an ENUM type column.
        Parameters:
        - field: The ENUM column to be checked.
        - value: The specific value to count.
        '''
        try:
            self.cursor.execute(f"SELECT COUNT(*) FROM {self.tableName} WHERE {field} = '{value}'")
            count = self.cursor.fetchone()[0]
            return count
        except Exception as e:
            self.logger.error(f"Error in count_enum: {e}")
            return None

    # page
    def get_total_pages(self, page_size):
        '''
        Calculate the total number of pages.
        Parameters:
        - page_size: The number of records per page.
        '''
        try:
            self.cursor.execute(f"SELECT COUNT(*) FROM {self.tableName}")
            total_records = self.cursor.fetchone()[0]
            total_pages = -(-total_records // page_size)  # Ceiling division
            return total_pages
        except Exception as e:
            self.logger.error(f"Error in get_total_pages: {e}")
            return None

    def read_data_with_pagination_and_sort(self, page_number, page_size, sort_column, sort_order):
        '''
        Read data from the table with pagination and sorting.
        Parameters:
        - page_number: The page number to retrieve.
        - page_size: The number of records per page.
        - sort_column: The column to sort by.
        - sort_order: The order of sorting ('ASC' or 'DESC').
        '''
        try:
            offset = (page_number - 1) * page_size
            query = f"SELECT * FROM {self.tableName} ORDER BY {sort_column} {sort_order} LIMIT {page_size} OFFSET {offset}"
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            self.logger.error(f"Error in read_data_with_pagination_and_sort: {e}")
            return None
        
    def read_data_with_conditions_pagination_and_sort(self, condition, page_number, page_size, sort_column, sort_order):
        '''
        Read data from the table with pagination, sorting, and conditions.
        Parameters:
        - condition: A SQL condition string.
        - page_number: The page number to retrieve.
        - page_size: The number of records per page.
        - sort_column: The column to sort by.
        - sort_order: The order of sorting ('ASC' or 'DESC').
        '''
        try:
            offset = (page_number - 1) * page_size
            query = f"SELECT * FROM {self.tableName} WHERE {condition} ORDER BY {sort_column} {sort_order} LIMIT {page_size} OFFSET {offset}"
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            self.logger.error(f"Error in read_data_with_conditions_pagination_and_sort: {e}")
            return None

    def read_specific_columns_with_pagination_and_sort(self, columns, page_number, page_size, sort_column, sort_order):
        '''
        Read specific columns from the table with pagination and sorting.
        Parameters:
        - columns: A list of column names to be selected.
        - page_number: The page number to retrieve.
        - page_size: The number of records per page.
        - sort_column: The column to sort by.
        - sort_order: The order of sorting ('ASC' or 'DESC').
        '''
        try:
            selected_columns = ', '.join(columns)
            offset = (page_number - 1) * page_size
            query = f"SELECT {selected_columns} FROM {self.tableName} ORDER BY {sort_column} {sort_order} LIMIT {page_size} OFFSET {offset}"
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            self.logger.error(f"Error in read_specific_columns_with_pagination_and_sort: {e}")
            return None

    # csv storage
    def export_table_to_csv(self, file_path):
        '''
        Export the entire table to a CSV file.
        Parameters:
        - file_path: The path of the file where the data will be saved.
        '''
        try:
            self.cursor.execute(f"SELECT * FROM {self.tableName}")
            with open(file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([i[0] for i in self.cursor.description])  # Write headers
                writer.writerows(self.cursor)
            print(f"Data exported successfully to {file_path}")
        except Exception as e:
            self.logger.error(f"Error in export_table_to_csv: {e}")

    # stored procedure
    def create_stored_procedure(self, procedure_name, procedure_definition):
        '''
        Create a stored procedure in the database.
        Parameters:
        - procedure_name: The name of the stored procedure.
        - procedure_definition: The SQL definition of the procedure.

        Example usage:
        Suppose you want to create a stored procedure named 'calculate_statistics'
        that takes two dates as input and returns some statistics. The SQL definition
        might look like this:
        procedure_definition = """
        IN start_date DATE, IN end_date DATE
        BEGIN
            SELECT COUNT(*), AVG(some_column)
            FROM your_table
            WHERE date_column BETWEEN start_date AND end_date;
        END
        """
        create_stored_procedure('calculate_statistics', procedure_definition)
        '''
        try:
            self.cursor.execute(f"DROP PROCEDURE IF EXISTS {procedure_name}")
            self.cursor.execute(f"CREATE PROCEDURE {procedure_name} {procedure_definition}")
            self.connection.commit()
            print(f"Stored procedure '{procedure_name}' created successfully.")
        except Exception as e:
            self.logger.error(f"Error in create_stored_procedure: {e}")

    def delete_stored_procedure(self, procedure_name):
        '''
        Delete a stored procedure from the database.
        Parameters:
        - procedure_name: The name of the stored procedure to be deleted.

        Example usage:
        Suppose you want to delete a stored procedure named 'calculate_statistics':
        delete_stored_procedure('calculate_statistics')
        '''
        try:
            self.cursor.execute(f"DROP PROCEDURE IF EXISTS {procedure_name}")
            self.connection.commit()
            print(f"Stored procedure '{procedure_name}' deleted successfully.")
        except Exception as e:
            self.logger.error(f"Error in delete_stored_procedure: {e}")

    def list_stored_procedures(self):
        '''
        List all stored procedures in the current database.
        
        Returns a list of stored procedure names.
        '''
        try:
            self.cursor.execute("SHOW PROCEDURE STATUS WHERE Db = %s", (self.database,))
            procedures = self.cursor.fetchall()
            return [proc[1] for proc in procedures if proc[1]]  # Extracting procedure names
        except Exception as e:
            self.logger.error(f"Error in list_stored_procedures: {e}")
            return None

    def execute_stored_procedure(self, procedure_name, args=()):
        '''
        Execute a stored procedure.
        Parameters:
        - procedure_name: The name of the stored procedure.
        - args: A tuple of arguments to pass to the procedure.

        Example usage:
        Suppose there is a stored procedure named 'calculate_statistics'
        in the database that takes two dates as input and returns statistics data.
        It can be called as follows:
        results, output_params = execute_stored_procedure('calculate_statistics', ('2023-01-01', '2023-01-31'))
        This will execute the 'calculate_statistics' stored procedure with the provided dates
        and return the results and any output parameters.
        '''
        try:
            self.cursor.callproc(procedure_name, args)
            self.connection.commit()
            results = [self.cursor.fetchall()]
            # Retrieve output parameters if any
            self.cursor.nextset()
            output_params = self.cursor.fetchone()
            return results, output_params
        except Exception as e:
            self.logger.error(f"Error in execute_stored_procedure: {e}")
            return None, None
