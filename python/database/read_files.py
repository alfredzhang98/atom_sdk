import yaml

class ReadFiles:

    def print_read_supports():
        print("YAML")

    class ReadYAML:
        def __init__(self, file_path):
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
    u_readyaml = u_ReadFiles.ReadYAML("/Users/alfred/project/atom_sdk/python/crawler/slot_config.yaml")
    print(type(u_readyaml.get_value("CENTER1")))
    print(u_readyaml.get_value("CENTER1"))
    print(u_readyaml.get_value())