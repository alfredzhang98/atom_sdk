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
            self.yaml = self._load_yaml()

        def _load_yaml(self):
            try:
                with open(self.file_path, 'r') as yaml_file:
                    return yaml.safe_load(yaml_file)
            except Exception as e:
                raise ValueError(f"Error : {str(e)}")

        def get_value(self, key=None):
            if key is None:
                return self.yaml
            elif key in self.yaml:
                return self.yaml[key]
            else:
                raise KeyError(f"Key not found: {key}")
            
        def create_yaml(self, data, overwrite=False):
            if os.path.exists(self.file_path) and not overwrite:
                raise FileExistsError("YAML file already exists. Set overwrite=True to overwrite.")
            try:
                with open(self.file_path, 'w') as yaml_file:
                    yaml.dump(data, yaml_file)
            except Exception as e:
                raise ValueError(f"Error while creating YAML file: {str(e)}")


        def update_yaml(self, updates):
            """
            更新 YAML 文件的内容。
            :param updates: 一个包含要更新的键值对的字典。
                            如果键已存在，则更新其值；
                            如果键不存在，则在 YAML 中添加该键值对。
            :type updates: dict
            :raises ValueError: 如果更新过程中出现任何错误。
            """
            try:
                # 加载当前 YAML 文件的内容
                self.yaml = self._load_yaml()
                # 更新或添加键值对
                for key, value in updates.items():
                    self.yaml[key] = value
                # 将更新后的内容写回文件
                with open(self.file_path, 'w') as yaml_file:
                    yaml.dump(self.yaml, yaml_file, default_flow_style=False)
            except Exception as e:
                raise ValueError(f"Error while updating YAML file: {str(e)}")
            
        def delete_key(self, key):
            if key in self.yaml:
                del self.yaml[key]
                with open(self.file_path, 'w') as yaml_file:
                    yaml.dump(self.yaml, yaml_file)
            else:
                raise KeyError(f"Key not found: {key}")



if __name__ == "__main__":
    u_ReadFiles = ReadFiles()
    u_readyaml = u_ReadFiles.ReadYAML()
    print(u_readyaml.get_value('version'))
