import os
import yaml

class ReadFiles:
    """
    A class to read various file types. Currently supports YAML files.
    """

    @staticmethod
    def print_read_supports():
        print("Supported file types: YAML")

    class ReadYAML:
        """
        Class for reading YAML files.
        """

        def __init__(self, path=None):
            if path is None:
                # Get the directory of the script file
                script_dir = os.path.dirname(__file__)
                file_name = "setting.yaml"
                file_path = os.path.join(script_dir, "settings", file_name)
            else:
                # Handle both absolute and relative paths
                file_path = os.path.abspath(path)

            self.file_path = file_path
            self.config = self._load_config()

        def _load_config(self):
            try:
                with open(self.file_path, 'r') as yaml_file:
                    return yaml.safe_load(yaml_file)
            except FileNotFoundError:
                raise FileNotFoundError(f"YAML file not found: {self.file_path}")
            except yaml.YAMLError as e:
                raise ValueError(f"Error parsing YAML file: {str(e)}")

        def get_value(self, key=None):
            if key is None:
                return self.config
            elif key in self.config:
                return self.config[key]
            else:
                raise KeyError(f"Key not found: {key}")

if __name__ == "__main__":
    u_ReadFiles = ReadFiles()
    u_readyaml = u_ReadFiles.ReadYAML()
    print(u_readyaml.get_value())
