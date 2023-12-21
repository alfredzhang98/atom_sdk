import os
import yaml
import json

class ReadFiles:
    """
    A class to read various file types. Currently supports YAML, JSON files.
    """
    @staticmethod
    def print_read_supports():
        print("Supported file types: YAML, JSON")

    class ReadYAML:
        '''
        Could read and create yaml files and update keys, delete keys
        '''
        def __init__(self, path=None):
            self.path = path
            if path is None:
                # Get the directory of the script file
                script_dir = os.path.dirname(__file__)
                file_name = "setting.yaml"
                file_path = os.path.join(script_dir, "settings", file_name)
                self.file_path = file_path
            else:
                # Handle both absolute and relative paths
                file_path = os.path.abspath(path)
                self.file_path = file_path
                self.create_yaml_file(self.file_path)
            
            self.yaml = self._load_yaml_from_file()

        def _load_yaml_from_file(self):
            try:
                with open(self.file_path, 'r') as yaml_file:
                    return yaml.safe_load(yaml_file)
            except Exception as e:
                print("Error:" + str(e))

        @staticmethod
        def create_yaml_file(path, data = None, overwrite=False):
            """
            Creates the contents of the YAML file.
            :param path
            :param data
            :type data: dict
            :boolen overwrite
            """
            if os.path.exists(path) and not overwrite:
                # print("Warning: The file already exists. Set overwrite=True to overwrite the file.")
                return
            else:
                try:
                    with open(path, 'w') as yaml_file:
                        yaml.dump(data, yaml_file)
                except Exception as e:
                    print("Error:" + str(e))

        def update_yaml(self, updates):
            """
            Update the contents of a YAML file.
            :param updates: A dictionary containing the key-value pairs to be updated.
                            If the key already exists, the value is updated;
                            If the key does not exist, the key-value pair is added to the YAML.
            :type updates: dict
            :raises ValueError: If any error occurs during the update.
            """
            if self.path is None:
                print("Cannot modify the default setting.yaml file. Please specify a path.")
                return
            try:
                # Load the current YAML content
                self.yaml = self._load_yaml_from_file()
                if self.yaml is None:
                    self.yaml = {}

                # Update or add key-value pairs
                for key, value in updates.items():
                    self.yaml[key] = value

                # Write the updated content back to the file
                self._write_yaml()

            except Exception as e:
                print("Error:", e)

        def _write_yaml(self):
            try:
                with open(self.file_path, 'w') as yaml_file:
                    yaml.dump(self.yaml, yaml_file, default_flow_style=False)
            except Exception as e:
                print("Error:", e)

        def delete_key(self, key):
            if self.path is None:
                print("Cannot modify the default setting.yaml file. Please specify a path.")
                return
            if key in self.yaml:
                del self.yaml[key]
                with open(self.file_path, 'w') as yaml_file:
                    yaml.dump(self.yaml, yaml_file)
            else:
                print("Error:" + "Key not found: " + key)
        
        def get_value(self, key=None):
            if key is None:
                return self.yaml
            elif key in self.yaml:
                return self.yaml[key]
            else:
                print("Error:" + "Key not found: " + key)
            
    class ReadJSON:
        '''
        Could read and create json files/dick/str data and update keys, delete keys
        '''
        def __init__(self, source=None):
            """
            Initialise the ReadJSON class.
            :param source: can be a file path, a JSON format string, or None.
                        If None, load the setting.json file in the default path.
            """
            self.source = source
            self.json_content = {}
            self.file_path = None

            if source is None:
                # Load the default setting.json
                script_dir = os.path.dirname(__file__)
                file_name = "setting.json"
                self.file_path = os.path.join(script_dir, "settings", file_name)
                self.json_content = self._load_json_from_file()
            elif isinstance(source, dict):
                # Directly using dictionary-type JSON data
                self.json_content = source
            elif isinstance(source, str):
                source_upper = os.path.dirname(source)
                if os.path.exists(source_upper):
                    self.file_path = os.path.abspath(source)
                    self.create_json_file(self.file_path)
                    self.json_content = self._load_json_from_file()
                else:
                    try:
                        self.json_content = self.parse_json_string(source)
                    except Exception as e:
                        print("Error:" + str(e))
            else:
                raise ValueError("The source parameter must be a file path or a string in JSON format.")

        def _load_json_from_file(self):
            # Load JSON data from file
            try:
                with open(self.file_path, 'r') as file:
                    return json.load(file)
            except FileNotFoundError:
                return {}
            except json.JSONDecodeError as e:
                raise ValueError(f"Unable to load JSON file: {str(e)}")
            except Exception as e:
                raise ValueError(f"Unable to load JSON file: {str(e)}")

        @staticmethod
        def parse_json_string(json_string):
            # Parsing a JSON string
            try:
                return json.loads(json_string)
            except Exception as e:
                print("Error:" + str(e))

        @staticmethod
        def create_json_file(path, data={}, overwrite=False):
            """
            Create a new JSON file.
            :param path: Path to the file to be created.
            :param data: The data to be written to the file.
            :param overwrite: If or not overwrite the file if it already exists. Default is False.
            """
            if os.path.exists(path) and not overwrite:
                # print("The file already exists. Set overwrite=True to overwrite the file.")
                return
            else:
                try:
                    with open(path, 'w') as file:
                        json.dump(data, file, indent=4) # indent is 4 space
                except Exception as e:
                    print("Error:" + str(e))

        def update_json(self, updates):
            if self.source is None:
                print("Cannot modify the default setting.yaml file. Please specify a path.")
                return
            try:
                if not isinstance(updates, dict):
                    print("Error: Updates must be in dictionary format")
                    return
                self.json_content.update(updates)
                if self.file_path:
                    self._write_json()
            except Exception as e:
                    print("Error:" + str(e))

        def _write_json(self):
            try:
                with open(self.file_path, 'w') as file:
                    json.dump(self.json_content, file, indent=4)
            except Exception as e:
                print("Error:" + str(e))

        def delete_key(self, key):
            """
            Delete the specified key from JSON.
            :param key: The key to delete.
            """
            if self.source is None:
                print("Cannot modify the default setting.yaml file. Please specify a path.")
                return
            try:
                if key in self.json_content:
                    del self.json_content[key]
                    if self.file_path:
                        self._write_json()
                    # print(f"The key '{key}' has been removed from the JSON.")
                else:
                    # print(f"The key '{key}' does not exist in JSON.")
                    pass
            except Exception as e:
                    print("Error:" + str(e))

        def get_value(self, key=None):
            if key is None:
                return self.json_content
            return self.json_content.get(key, None)


if __name__ == "__main__":

    u_ReadFiles = ReadFiles()

    # Yaml Test
    yaml_data = {
    "key1": "new_value1",
    "key2": "new_value2"
    }

    u_readyaml = u_ReadFiles.ReadYAML()
    print(u_readyaml.get_value())
    u_readyaml.update_yaml(yaml_data)
    u_readyaml.delete_key('version')

    path = os.path.dirname(__file__)
    path = os.path.join(path, "test.yaml")
    u_readyaml1 = u_ReadFiles.ReadYAML(path)
    print(u_readyaml1.get_value())
    u_readyaml1.update_yaml(yaml_data)
    print(u_readyaml1.get_value())
    u_readyaml1.delete_key('key1')
    print(u_readyaml1.get_value())

    #Json Test

    json_data_update = {"git" : "Test"}
    json_data = {"name": "John", "age": 30}
    json_str_data = '{"name": "John", "age": 30}'
    u_readjson = u_ReadFiles.ReadJSON()
    print(u_readjson.get_value())
    u_readjson.update_json(json_data)
    u_readjson.delete_key('version')

    test = u_ReadFiles.ReadJSON.parse_json_string(json_str_data)
    print(type(test))

    source = os.path.dirname(__file__)
    source = os.path.join(source, "test.json")

    u_readjson1 = u_ReadFiles.ReadJSON(source)
    print(u_readjson1.get_value())
    u_readjson1.update_json(json_data)
    print(u_readjson1.get_value())
    u_readjson1.delete_key('name')
    print(u_readjson1.get_value())

    u_readjson2 = u_ReadFiles.ReadJSON(json_data)
    u_readjson2 = u_ReadFiles.ReadJSON(json_str_data)
    print(u_readjson2.get_value())
    u_readjson2.update_json(json_data_update)
    print(u_readjson2.get_value())
    u_readjson2.delete_key('name')
    print(u_readjson2.get_value())