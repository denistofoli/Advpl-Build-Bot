from build_log import Build_Log
from build_system import Build_System
from build_git import Build_Git
from build_advpl import Build_Advpl


# Allways Full Path
BUILD_PATH = '/home/project/protheus' # (For Windows use '\\' like c:\\totvs\\sources)
BUILD_INCLUDES = '/home/Protheus/include'

# Git
BUILD_BRANCH = 'master'
BUILD_INTERVAL = '10.day'  # see https://git-scm.com/docs/git-log

# AppServer
BUILD_SERVER = '127.0.0.1'
BUILD_PORT = '1234'
BUILD_ENV = 'Tests'
BUILD_USER = 'admin'
BUILD_PASS = ''


# Internal script usage
log = Build_Log()
system = Build_System(BUILD_PATH)
git = Build_Git(system, BUILD_BRANCH, BUILD_INTERVAL)
advpl = Build_Advpl(system,  BUILD_SERVER, BUILD_PORT, BUILD_ENV, BUILD_INCLUDES, BUILD_USER, BUILD_PASS)


if __name__ == '__main__':
    log.add(system.os, ['Starting Advpl Build Bot'])
    log.add('GIT', git.pull())
    log.add('BUILD',advpl.build(git.get_changed_files()))
    log.add(system.os, ['Finish job'])
    log.write_log()

