class Model_Config:
    def __init__(self, name, path, includes, branch, interval, server, port, env, user, passwd):
        self.__name = name
        self.__path = path
        self.__includes = includes
        self.__branch = branch
        self.__interval = interval
        self.__server = server
        self.__port = port
        self.__env = env
        self.__user = user
        self.__passwd = passwd

    @property
    def name(self): return self.__name

    @property
    def path(self): return self.__path

    @property
    def includes(self): return self.__includes

    @property
    def branch(self): return self.__branch

    @property
    def interval(self): return self.__interval

    @property
    def server(self): return self.__server

    @property
    def port(self): return self.__port

    @property
    def env(self): return self.__env

    @property
    def user(self): return self.__user

    @property
    def passwd(self): return self.__passwd
