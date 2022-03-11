from datetime import datetime

class Build_Log:
    def __init__(self):
        self.__build_logs = []
    

    def add(self, prefix, lines):
        for line in lines:
            if line.strip().__len__() > 0:
                self.__build_logs.append(f'[{datetime.now().__str__()}] [{prefix}] {line}\n')


    def write_log(self):
        f = open(f"build-bot-{datetime.now().strftime('%Y%m%d-%H%M%S')}.log", "w")
        for x in self.__build_logs:
            f.write(x)
        
        f.close()
