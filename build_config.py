import json
import os.path

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
    
    def read_json(arq_json):
        control = os.path.isfile(arq_json)    
        if control:
            with open(arq_json, 'r', encoding='utf8') as f:
                return json.load(f)
