# Quick Start

#### 1. Download and install [Python3](https://www.python.org/) interpreter.

#### 2. Download and install [Git](https://git-scm.com/)

#### 3. Clone this project
```git clone https://github.com/denistofoli/Advpl-Build-Bot.git```

#### 4. Install Python Requeriments
```pip install requirement.txt```

#### 5. Download Totvs Binary Compiler [tds-cli](https://github.com/totvs/tds-ls)
Download version for your operating system, and put into script folder (only binary)

#### 6. Configure build-bot-config.json
**Important:** For Windows use ```\\``` like ```c:\\totvs\\sources```

Exemple
```json
{
   "configs" : [
       {"totvsServer":{
        "name": "Server Name",
        "path":"/home/project/protheus",
        "includes":"/home/Protheus/include",
        "server":"127.0.0.1",
        "port":"1234",
        "env":"Tests",
        "user":"admin",
        "pass":""
    },
    "git":{
      "branch":"master",
      "interval":"10.day"  
    }}
]}
```

To skip git steps, leave branch empty ```"branch":""```


#### 7. Run script
```python3 advpl-build-bot.py```

For automatic builds, schedule this instruction
