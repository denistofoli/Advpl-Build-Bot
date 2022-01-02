import json
import os.path
from model_config import Model_Config

class Build_Config:
    schema = {                
                "type": "object",
                "properties": {
                    "configs": {
                    "type": "array",
                    "items": [
                        {
                        "type": "object",
                        "properties": {
                            "totvsServer": {
                            "type": "object",
                            "properties": {
                                "name": {
                                "type": "string"
                                },
                                "path": {
                                "type": "string"
                                },
                                "includes": {
                                "type": "string"
                                },
                                "server": {
                                "type": "string"
                                },
                                "port": {
                                "type": "string"
                                },
                                "env": {
                                "type": "string"
                                },
                                "user": {
                                "type": "string"
                                },
                                "pass": {
                                "type": "string"
                                }
                            },
                            "required": [
                                "name"
                                "path",
                                "includes",
                                "server",
                                "port",
                                "env",
                                "user",
                                "pass"
                            ]
                            },
                            "git": {
                            "type": "object",
                            "properties": {
                                "branch": {
                                "type": "string"
                                },
                                "internal": {
                                "type": "string"
                                }
                            },
                            "required": [
                                "branch",
                                "internal"
                            ]
                            }
                        },
                        "required": [
                            "totvsServer",
                            "git"
                        ]
                        }
                    ]
                    }
                },
                "required": [
                    "configs"
                ]
            }
    

    def __init__(self, json_file):
        self.__json_file = json_file
        self.__message = ''
        self.__configs = self.__read_json()


    def __read_json(self):
        if os.path.isfile(self.__json_file):
            configs = []
            with open(self.__json_file, 'r', encoding='utf8') as f:
                configs_json = json.load(f)
                for c in configs_json["configs"]:
                    configs.append(Model_Config(c["totvsServer"]["name"],
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
            return configs
        else:
            self.__message = "Error loading config file!"
            return []


    @property
    def configs(self): return self.__configs

    @property
    def message(self): return self.__message