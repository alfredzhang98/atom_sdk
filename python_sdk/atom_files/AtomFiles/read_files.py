import os
import yaml
import json
import logging
import shutil
from cryptography.fernet import Fernet
import difflib
import pandas as pd

class ReadFiles:
    """
    A class to read various file types. Currently supports YAML, JSON files.
    """
    @staticmethod
    def print_read_supports():
        print("Supported file types: YAML, JSON, EXCEL")

    class ReadYAML:
        def __init__(self, path=None, encryption_key=None):
            self.path = path
            self.file_path = self._initialize_file_path(path)
            self.encryption_key = encryption_key
            self.fernet = Fernet(self.encryption_key) if encryption_key else None
            self.yaml = self._load_yaml_from_file()
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(__name__)

        def _initialize_file_path(self, path):
            if path is None:
                script_dir = os.path.dirname(__file__)
                file_name = "setting.yaml"
                return os.path.join(script_dir, "settings", file_name)
            else:
                return os.path.abspath(path)

        def _load_yaml_from_file(self):
            self._check_file_exists()
            try:
                with open(self.file_path, 'r') as yaml_file:
                    return yaml.safe_load(yaml_file)
            except Exception as e:
                self.logger.error(f"Error in _load_yaml_from_file: {e}")
                return None

        def _check_file_exists(self):
            if not os.path.isfile(self.file_path):
                raise FileNotFoundError(f"File not found: {self.file_path}")

        def _write_yaml(self):
            try:
                with open(self.file_path, 'w') as yaml_file:
                    yaml.dump(self.yaml, yaml_file, default_flow_style=False)
            except Exception as e:
                self.logger.error(f"Error in _write_yaml: {e}")

        def _recursive_update(self, d, u):
            for k, v in u.items():
                if isinstance(v, dict):
                    d[k] = self._recursive_update(d.get(k, {}), v)
                else:
                    d[k] = v
            return d

        def _recursive_delete(self, d, key):
            if key in d:
                del d[key]
            for k, v in d.items():
                if isinstance(v, dict):
                    self._recursive_delete(v, key)

        @staticmethod
        def generate_encryption_key():
            """
            Generate a secure encryption key.
            :return: A Fernet encryption key.
            """
            return Fernet.generate_key()

        @staticmethod
        def create_yaml_file(path, data=None, overwrite=False):
            if os.path.exists(path) and not overwrite:
                return
            try:
                with open(path, 'w') as yaml_file:
                    yaml.dump(data if data else {}, yaml_file)
            except Exception as e:
                print("Error:" + str(e))

        @staticmethod
        def get_file_content(path):
            """
            Return the complete content of the YAML file.
            """
            with open(path, 'r') as file:
                return file.read()

        def merge_with_file(self, other_file_path):
            with open(other_file_path, 'r') as other_file:
                other_content = yaml.safe_load(other_file)
            self.yaml.update(other_content)
            self._write_yaml()

        def compare_with_file(self, other_file_path):
            with open(other_file_path, 'r') as other_file:
                other_content = yaml.safe_load(other_file)
            diff = difflib.ndiff(json.dumps(self.yaml, indent=4).splitlines(), json.dumps(other_content, indent=4).splitlines())
            return '\n'.join(diff)

        def backup_yaml(self):
            backup_path = self.file_path + '.bak'
            shutil.copyfile(self.file_path, backup_path)

        def restore_yaml(self):
            backup_path = self.file_path + '.bak'
            shutil.copyfile(backup_path, self.file_path)
            # Reload yaml
            self.yaml = self._load_yaml_from_file()

        def encrypt_file(self):
            if not self.fernet:
                raise ValueError("Encryption key is not set.")
            with open(self.file_path, 'rb') as file:
                encrypted_data = self.fernet.encrypt(file.read())
            with open(self.file_path, 'wb') as file:
                file.write(encrypted_data)

        def decrypt_file(self):
            if not self.fernet:
                raise ValueError("Encryption key is not set.")
            with open(self.file_path, 'rb') as file:
                decrypted_data = self.fernet.decrypt(file.read())
            with open(self.file_path, 'wb') as file:
                file.write(decrypted_data)

        def convert_to_json(self, json_path):
            with open(json_path, 'w') as json_file:
                json.dump(self.yaml, json_file, indent=4)

        def update_yaml(self, updates, recursive=False):
            self._check_file_exists()
            try:
                self.yaml = self._load_yaml_from_file() if self.yaml is None else self.yaml
                self._recursive_update(self.yaml, updates) if recursive else self.yaml.update(updates)
                self._write_yaml()
            except Exception as e:
                self.logger.error(f"Error in update_yaml: {e}")

        def delete_key(self, key, recursive=False):
            self._check_file_exists()
            if recursive:
                self._recursive_delete(self.yaml, key)
            elif key in self.yaml:
                del self.yaml[key]
            self._write_yaml()
        
        def get_value(self, key=None):
            self._check_file_exists()
            return self.yaml if key is None else self.yaml.get(key, None)
        
    class ReadJSON:
        def __init__(self, path=None, encryption_key=None):
            self.path = path
            self.file_path = self._initialize_file_path(path)
            self.encryption_key = encryption_key
            self.fernet = Fernet(self.encryption_key) if encryption_key else None
            self.json_data = self._load_json_from_file()
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(__name__)

        def _initialize_file_path(self, path):
            if path is None:
                script_dir = os.path.dirname(__file__)
                file_name = "setting.json"
                return os.path.join(script_dir, "settings", file_name)
            else:
                return os.path.abspath(path)

        def _load_json_from_file(self):
            self._check_file_exists()
            try:
                with open(self.file_path, 'r') as json_file:
                    return json.load(json_file)
            except Exception as e:
                self.logger.error(f"Error in _load_json_from_file: {e}")
                return None

        def _check_file_exists(self):
            if not os.path.isfile(self.file_path):
                raise FileNotFoundError(f"File not found: {self.file_path}")

        def _write_json(self):
            try:
                with open(self.file_path, 'w') as json_file:
                    json.dump(self.json_data, json_file, indent=4)
            except Exception as e:
                self.logger.error(f"Error in _write_json: {e}")

        def _recursive_update(self, d, u):
            for k, v in u.items():
                if isinstance(v, dict):
                    d[k] = self._recursive_update(d.get(k, {}), v)
                else:
                    d[k] = v
            return d

        def _recursive_delete(self, d, key):
            if key in d:
                del d[key]
            for k, v in d.items():
                if isinstance(v, dict):
                    self._recursive_delete(v, key)

        @staticmethod
        def generate_encryption_key():
            return Fernet.generate_key()

        @staticmethod
        def create_json_file(path, data=None, overwrite=False):
            if os.path.exists(path) and not overwrite:
                return
            try:
                with open(path, 'w') as json_file:
                    json.dump(data if data else {}, json_file, indent=4)
            except Exception as e:
                print("Error:" + str(e))

        @staticmethod
        def get_file_content(path):
            """
            Return the complete content of the JSON file.
            """
            with open(path, 'r') as file:
                return file.read()

        def merge_with_file(self, other_file_path):
            with open(other_file_path, 'r') as other_file:
                other_content = json.load(other_file)
            self.json_data.update(other_content)
            self._write_json()

        def compare_with_file(self, other_file_path):
            with open(other_file_path, 'r') as other_file:
                other_content = json.load(other_file)
            diff = difflib.ndiff(json.dumps(self.json_data, indent=4).splitlines(), json.dumps(other_content, indent=4).splitlines())
            return '\n'.join(diff)

        def backup_json(self):
            backup_path = self.file_path + '.bak'
            shutil.copyfile(self.file_path, backup_path)

        def restore_json(self):
            backup_path = self.file_path + '.bak'
            shutil.copyfile(backup_path, self.file_path)
            self.json_data = self._load_json_from_file()

        def encrypt_file(self):
            if not self.fernet:
                raise ValueError("Encryption key is not set.")
            with open(self.file_path, 'rb') as file:
                encrypted_data = self.fernet.encrypt(file.read())
            with open(self.file_path, 'wb') as file:
                file.write(encrypted_data)

        def decrypt_file(self):
            if not self.fernet:
                raise ValueError("Encryption key is not set.")
            with open(self.file_path, 'rb') as file:
                decrypted_data = self.fernet.decrypt(file.read())
            with open(self.file_path, 'wb') as file:
                file.write(decrypted_data)

        def convert_to_yaml(self, yaml_path):
            import yaml
            with open(yaml_path, 'w') as yaml_file:
                yaml.dump(self.json_data, yaml_file)

        def update_json(self, updates, recursive=False):
            self._check_file_exists()
            try:
                self.json_data = self._load_json_from_file() if self.json_data is None else self.json_data
                self._recursive_update(self.json_data, updates) if recursive else self.json_data.update(updates)
                self._write_json()
            except Exception as e:
                self.logger.error(f"Error in update_json: {e}")

        def delete_key(self, key, recursive=False):
            self._check_file_exists()
            if recursive:
                self._recursive_delete(self.json_data, key)
            elif key in self.json_data:
                del self.json_data[key]
            self._write_json()

        def get_value(self, key=None):
            self._check_file_exists()
            return self.json_data if key is None else self.json_data.get(key, None)
        
    class ReadExcel:
        def __init__(self, path):
            self.path = path
            self.df = self._load_excel_file()

        def _load_excel_file(self):
            if os.path.exists(self.path):
                return pd.read_excel(self.path)
            else:
                raise FileNotFoundError(f"File not found: {self.path}")

        def create_filter_conditional(self, condition):
            """
            Filter the DataFrame based on a condition.
            Examples of conditions:
            - "Age > 30" : Filter rows where the Age column is greater than 30.
            - "Department == 'Sales'" : Filter rows where the Department column is 'Sales'.
            - "Salary >= 50000 and Department == 'IT'" : Filter rows where Salary is >= 50000 and Department is 'IT'.
            """
            return self.df.query(condition)

        def create_filter_conditional_formatting(self, column, condition, format_style):
            """
            Apply conditional formatting based on a condition to a specified column.

            Examples of usage:
            - `create_conditional_formatting("Salary", lambda x: x > 50000, 'background-color: yellow')`: 
            This will highlight all cells in the 'Salary' column with a salary greater than 50,000 in yellow.

            - `create_conditional_formatting("Age", lambda x: x < 30, 'color: green')`: 
            This will change the font color to green for all cells in the 'Age' column where age is less than 30.

            - `create_conditional_formatting("Status", lambda x: x == "Active", 'font-weight: bold')`: 
            This will make the font bold for all cells in the 'Status' column where the status is "Active".

            :param column: Column to apply conditional formatting.
            :param condition: Condition for formatting (e.g., lambda x: x > 0).
            :param format_style: Style to apply if condition is True (e.g., 'background-color: yellow').
            """
            return self.df.style.applymap(lambda x: format_style if condition(x) else '', subset=[column])

        def create_sort_column(self, column, ascending=True):
            """
            Sort the DataFrame by a specific column.
            Example: sort_dataframe("Age", ascending=False) - Sorts the DataFrame by Age in descending order.
            """
            return self.df.sort_values(by=column, ascending=ascending)

        def create_column_based_on_formula(self, new_column_name, formula):
            """
            Add a new column based on a formula applied to each row.
            Example: add_column_based_on_formula("Total Compensation", lambda row: row['Salary'] + row['Bonus'])
            """
            self.df[new_column_name] = self.df.apply(formula, axis=1)

        # View datas
        def view_statistics(self, column):
            """
            Calculate basic statistics for a specified column.
            Example: calculate_statistics("Salary") - Returns count, mean, std, min, max for 'Salary' column.
            """
            return self.df[column].describe()

        def view_group_statistics(self, group_column, stat_column):
            """
            Group by a column and calculate statistics for another column.
            Example: group_and_calculate_statistics("Department", "Salary") - Groups by Department and calculates statistics for Salary.
            """
            grouped = self.df.groupby(group_column)[stat_column]
            return grouped.agg(['mean', 'count', 'sum'])

        def view_pivot_table(self, index, columns, values):
            """
            Create a pivot table from the DataFrame.
            Example: create_pivot_table("Department", "Job Title", "Salary") - Creates a pivot table with Department as index, Job Title as columns, and Salary as values.
            """
            return pd.pivot_table(self.df, index=index, columns=columns, values=values)

        # Calculate sth
        def calculate_correlation(self, columns=None):
            """
            Calculate the correlation between columns.
            Example: calculate_correlation(["Salary", "Age"]) - Calculates correlation between Salary and Age columns.
            """
            return self.df[columns].corr() if columns else self.df.corr()

        # Missing
        def missing_data_drop(self, threshold=0.5):
            """
            Drop rows or columns with too many missing values.
            :param threshold: Proportion of missing values to tolerate (default is 0.5).
            """
            self.df.dropna(thresh=int(threshold * len(self.df.columns)), axis=0, inplace=True)
            self.df.dropna(thresh=int(threshold * len(self.df)), axis=1, inplace=True)
                
        def missing_data_fill(self, fill_value=0):
            """
            Fill missing values with a specific value.
            Example: fill_missing_data(0) - Replaces all NaN values with 0.
            """
            self.df.fillna(fill_value, inplace=True)

        @staticmethod
        def export_to_csv(df, output_file, include_index=False):
            """
            Export DataFrame to a CSV file.
            Example: export_to_csv(df, "output.csv", include_index=False)
            """
            df.to_csv(output_file, index=include_index)

        @staticmethod
        def export_to_excel(df, output_file, include_index=False):
            """
            Export DataFrame to an Excel file.
            Example: export_to_excel(df, "output.xlsx", include_index=False)
            """
            df.to_excel(output_file, index=include_index)
    
        # Excels handle
        def excel_compare_and_highlight_differences(self, file1, file2, column_to_compare, output_file):
            """
            Compare two Excel files and highlight differences in a specific column.
            Example: compare_and_highlight_differences("file1.xlsx", "file2.xlsx", "Employee ID", "differences.xlsx")
            """
            df1 = pd.read_excel(file1)
            df2 = pd.read_excel(file2)
            unique_rows = df1[~df1[column_to_compare].isin(df2[column_to_compare])]
            unique_rows = unique_rows.append(df2[~df2[column_to_compare].isin(df1[column_to_compare])])
            unique_rows.to_excel(output_file, index=False)

        def excel_merge_with_other(self, other_file, on, merge_type='inner'):
            """
            Merge this DataFrame with another Excel file.
            Example: merge_with_other_excel("other_file.xlsx", "Employee ID", merge_type='outer')
            """
            other_df = pd.read_excel(other_file)
            self.df = pd.merge(self.df, other_df, on=on, how=merge_type)
