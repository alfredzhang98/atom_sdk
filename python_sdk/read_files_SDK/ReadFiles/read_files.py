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
                self.__create_yaml()
            
            self.yaml = self.__load_yaml()

        def __load_yaml(self):
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
            
        def __create_yaml(self, data = None, overwrite=False):
            """
            创建 YAML 文件的内容。
            :param data: 一个包含要更新的键值对的字典。
                            如果键已存在，则更新其值；
                            如果键不存在，则在 YAML 中添加该键值对。
            :type data: dict
            data = {
                "key1": "new_value1",
                "key2": "new_value2"
            }
            :boolen overwrite
            :raises ValueError: 如果更新过程中出现任何错误。
            """
            if self.path is None:
                print("Cannot modify the default setting.yaml file. Please specify a path.")
                return
            if os.path.exists(self.file_path) and not overwrite:
                pass
            else:
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
            updates = {
                "key1": "new_value1",
                "key2": "new_value2"
            }
            :raises ValueError: 如果更新过程中出现任何错误。
            """
            if self.path is None:
                print("Cannot modify the default setting.yaml file. Please specify a path.")
                return
            try:
                # 加载当前 YAML 文件的内容
                self.yaml = self.__load_yaml()
                # 如果 self.yaml 是 None，则初始化为空字典
                if self.yaml is None:
                    self.yaml = {}

                # 更新或添加键值对
                for key, value in updates.items():
                    self.yaml[key] = value

                # 将更新后的内容写回文件
                with open(self.file_path, 'w') as yaml_file:
                    yaml.dump(self.yaml, yaml_file, default_flow_style=False)
            except Exception as e:
                raise ValueError(f"Error while updating YAML file: {str(e)}")

        def delete_key(self, key):
            if self.path is None:
                print("Cannot modify the default setting.yaml file. Please specify a path.")
                return
            if key in self.yaml:
                del self.yaml[key]
                with open(self.file_path, 'w') as yaml_file:
                    yaml.dump(self.yaml, yaml_file)
            else:
                raise KeyError(f"Key not found: {key}")

if __name__ == "__main__":
    updates = {
    "key1": "new_value1",
    "key2": "new_value2"
    }

    u_ReadFiles = ReadFiles()
    u_readyaml = u_ReadFiles.ReadYAML()
    print(u_readyaml.get_value())
    u_readyaml.update_yaml(updates)
    u_readyaml.delete_key('version')

    path = os.path.dirname(__file__)
    path = os.path.join(path, "test.yaml")
    u_readyaml1 = u_ReadFiles.ReadYAML(path)
    print(u_readyaml1.get_value())

    u_readyaml1.update_yaml(updates)
    print(u_readyaml1.get_value())
    u_readyaml1.delete_key('key1')
    print(u_readyaml1.get_value())
