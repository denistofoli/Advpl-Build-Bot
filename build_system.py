import subprocess
import platform
import os


class Build_System:
    def __init__(self, path = os.getcwd()):
        self.__os = platform.system()
        self.__build_path = self.__path_check(path)
        self.__compiler = os.getcwd() + ('/advpls' if self.os == 'Linux' or self.os == 'Darwin' else '\\advpls.exe')


    def run(self, command, path=os.getcwd()):
        std_out = subprocess.run(command,
                                stdout=subprocess.PIPE,
                                cwd=path).stdout.decode('UTF-8').__str__().split('\n')
        return std_out


    def __path_check(self, path):
        if self.os == 'Linux' or self.os == 'Darwin':
            if path[-1] != '/':
                path += '/'

        elif self.os == 'Windows':
            if path[-2] != '\\':
                path += '\\'

        return path


    @property
    def os(self): return self.__os

    @property
    def build_path(self): return self.__build_path

    @property
    def compiler(self): return self.__compiler
