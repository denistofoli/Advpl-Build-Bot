# Quick Start

#### 1. Faça o download e instale o interpretador [Python3](https://www.python.org/).

#### 2. Faça o download e instale o [Git](https://git-scm.com/)

#### 3. Clone o projeto
```git clone https://github.com/denistofoli/Advpl-Build-Bot.git```

#### 4. Faça o download do binario de compilação da Totvs [tds-cli](https://github.com/totvs/tds-ls)
Faça o download do binário referente ao seu sistema operacional, e coloque na mesma pasta do script (apenas o binário)

#### 5. Configure build-bot-config.json
**Importante:** Para Windows use ```\\``` dessa forma ```c:\\totvs\\sources```

Exemplo
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

Para pular as etapas do git, deixe branch vazio ```"branch":""```


#### 6. Execute o script
```python3 advpl-build-bot.py```

Para builds automatizadas, deixe essa instrução agendada
