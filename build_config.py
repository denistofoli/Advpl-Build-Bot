import json
import os.path
from model_config import Model_Config
from jsonschema.validators import validate
from jsonschema.exceptions import ValidationError, FormatError, SchemaError

class Build_Config:
    def __init__(self, json_file):
        self.__config_file = json_file
        self.__schema_file = "schema.json"
        self.__message = ''
        self.__schema = self.__read_json(self.__schema_file)
        self.__config = self.__read_json(self.__config_file)
        self.__configs = []

        if not self.__message:
            self.__load_config()


    def __read_json(self, file):
        json_load = {}

        if os.path.isfile(file):
            with open(file, 'r', encoding='utf8') as f:
                json_load = json.load(f)
        else:
            self.__message = f'Erro loading {file}'

        return json_load


    def __load_config(self):
        try:
            validate(self.__config, self.__schema)

            for c in self.__config["configs"]:
                self.__configs.append(Model_Config(c["totvsServer"]["name"],
                                                   c["totvsServer"]["path"],
                                                   c["totvsServer"]["includes"],
                                                   c["git"]["branch"],
                                                   c["git"]["interval"],
                                                   c["totvsServer"]["server"],
                                                   c["totvsServer"]["port"],
                                                   c["totvsServer"]["env"],
                                                   c["totvsServer"]["user"],
                                                   c["totvsServer"]["pass"]))
            self.__message = "Config file loaded!"
        except ValidationError as e:
            self.__message = f"Validation: {e.message}"
        except FormatError as e:
            self.__message = f"Format: {e.message}"
        except SchemaError as e:
            self.__message = f"Schema: {e.message}"


    @property
    def configs(self): return self.__configs

    @property
    def message(self): return self.__message