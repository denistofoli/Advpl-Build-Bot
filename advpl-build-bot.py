from build_log import Build_Log
from build_system import Build_System
from build_git import Build_Git
from build_advpl import Build_Advpl
from build_config import Build_Config

config = Build_Config
objConfig  = config.read_json("build-bot-config.json")

# Allways Full Path
BUILD_PATH = objConfig["configs"][0]["totvsServer"]["path"]  # (For Windows use '\\' like c:\\totvs\\sources)
BUILD_INCLUDES = objConfig["configs"][0]["totvsServer"]["includes"] 

# Git
BUILD_BRANCH = objConfig["configs"][0]["git"]["branch"] 
BUILD_INTERVAL = objConfig["configs"][0]["git"]["interval"] # see https://git-scm.com/docs/git-log

# AppServer
BUILD_SERVER = objConfig["configs"][0]["totvsServer"]["server"] 
BUILD_PORT = objConfig["configs"][0]["totvsServer"]["port"] 
BUILD_ENV = objConfig["configs"][0]["totvsServer"]["env"] 
BUILD_USER = objConfig["configs"][0]["totvsServer"]["user"] 
BUILD_PASS = objConfig["configs"][0]["totvsServer"]["pass"] 


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

