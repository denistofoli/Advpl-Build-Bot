from build_log import Build_Log
from build_system import Build_System
from build_git import Build_Git
from build_advpl import Build_Advpl
from build_config import Build_Config


configs = Build_Config("build-bot-config.json")

# Allways Full Path
BUILD_PATH = configs.configs[0].path  # (For Windows use '\\' like c:\\totvs\\sources)
BUILD_INCLUDES = configs.configs[0].includes 

# Git
BUILD_BRANCH = configs.configs[0].branch
BUILD_INTERVAL = configs.configs[0].interval # see https://git-scm.com/docs/git-log

# AppServer
BUILD_SERVER = configs.configs[0].server 
BUILD_PORT = configs.configs[0].port 
BUILD_ENV = configs.configs[0].env 
BUILD_USER = configs.configs[0].user 
BUILD_PASS = configs.configs[0].passwd 


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
