import subprocess
import os
from datetime import datetime


BUILD_PATH = '/home/project/protheus'  # Allways Full Path
BUILD_BRANCH = 'master'
BUILD_INTERVAL = '10.day'  # see https://git-scm.com/docs/git-log
BUILD_INCLUDES = '/home/Protheus/include'  # Allways Full Path
BUILD_SERVER = '127.0.0.1'
BUILD_PORT = '1234'
BUILD_ENV = 'Tests'
BUILD_USER = 'admin'
BUILD_PASS = ''
BUILD_FILES = ''
BUILD_LOGS = []


def git_pull():
    list_files = ['git', 'pull']
    std_in = subprocess.run(list_files, stdout=subprocess.PIPE,
                            cwd=BUILD_PATH).stdout.decode('UTF-8').__str__().split('\n')
    add_log('GIT', std_in)


def load_changed_files():
    files = ''
    last_update = ['git', 'log', BUILD_BRANCH, '--since=' + BUILD_INTERVAL,
                   '--name-only', '--line-prefix=' + BUILD_PATH + '/']
    std_in = subprocess.run(last_update, stdout=subprocess.PIPE,
                            cwd=BUILD_PATH).stdout.decode('UTF-8').__str__().split('\n')

    for x in std_in:
        if '.prw' in x.lower() and x not in files:
            files += ',' if files.__len__() > 0 else ''
            files += x

    return files


def make_ini():
    f = open("build-bot.ini", "w")

    f.write('showConsoleOutput=true\n')

    f.write('[authentication]\n')
    f.write('action=authentication\n')
    f.write('server=' + BUILD_SERVER + '\n')
    f.write('port=' + BUILD_PORT + '\n')
    f.write('secure=0\n')
    f.write('build=AUTO\n')
    f.write('environment=' + BUILD_ENV + '\n')
    f.write('user=' + BUILD_USER + '\n')
    f.write('psw=' + BUILD_PASS + '\n')

    f.write('[compile]\n')
    f.write('action=compile\n')
    f.write('program=' + BUILD_FILES + '\n')
    f.write('recompile=T\n')
    f.write('includes=' + BUILD_INCLUDES + '\n')

    f.close()


def make_build():
    if BUILD_FILES.strip().__len__() > 0:
        make = [os.getcwd() + '/advpls', '--tdsCli=build-bot.ini']
        std_in = subprocess.run(make, stdout=subprocess.PIPE,
                                cwd=os.getcwd()).stdout.decode('UTF-8').__str__().split('\n')
        add_log('BUILD', std_in)
    else:
        add_log('BUILD', ['No files to compile'])


def add_log(prefix, lines):
    for line in lines:
        if line.strip().__len__() > 0:
            BUILD_LOGS.append('[' + datetime.now().__str__() + ']' + '[' + prefix + '] ' + line + '\n')


def write_log():
    f = open("build-bot.log", "w")
    for x in BUILD_LOGS:
        f.write(x)
    f.close()


if __name__ == '__main__':
    git_pull()
    BUILD_FILES = load_changed_files()
    make_ini()
    make_build()
    write_log()
