import os

class Build_Advpl:
    def __init__(self, system, server, port, env, includes, user, passwd):
        self.__system = system
        self.__server = server
        self.__port = port
        self.__env = env
        self.__includes = includes
        self.__user = user
        self.__passwd = passwd
        self.__ini_file = 'build-bot.ini'


    def build(self, files):
        log_return = []

        if os.path.isfile(self.__system.compiler):
            if files.strip().__len__() > 0:
                self.__make_ini(files)

                make = [self.__system.compiler, f'--tdsCli={self.__ini_file}']
                log_return = self.__system.run(make)

                os.remove(self.__ini_file)
            else:
                log_return = ['No files to compile']
        else:
            log_return = [f'Totvs Binary not found {self.__system.compiler}']
    
        return log_return


    def __make_ini(self, files):
        f = open(self.__ini_file, "w")

        f.write('showConsoleOutput=true\n')

        f.write('[authentication]\n')
        f.write('action=authentication\n')
        f.write(f'server={self.__server}\n')
        f.write(f'port={self.__port}\n')
        f.write('secure=0\n')
        f.write('build=AUTO\n')
        f.write(f'environment={self.__env}\n')
        f.write(f'user={self.__user}\n')
        f.write(f'psw={self.__passwd}\n')

        f.write('[compile]\n')
        f.write('action=compile\n')
        f.write(f'program={files}\n')
        f.write('recompile=T\n')
        f.write(f'includes={self.__includes}\n')

        f.close()
