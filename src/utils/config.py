import yaml

class Config:
    """
    Reads the specific config file and create the dictionary of the yaml
    """
    def __init__(self, config_path: str):
        self.conf = None
        with open(config_path, 'r') as file:
            self.conf = yaml.safe_load(file)
    def to_dict(self):
        return self.conf


# Example Test Usage
# config = Config("./config/model_config.yaml")
# print(config.to_dict())

