from build_log import Build_Log
from build_system import Build_System
from build_git import Build_Git
from build_advpl import Build_Advpl
from build_config import Build_Config


def main():
    log = Build_Log()

    configs = Build_Config("build-bot-config.json")
    log.add('CONFIG', [configs.message])

    for config in configs.configs:
        system = Build_System(config.path)
        git = Build_Git(system, config.branch, config.interval)
        advpl = Build_Advpl(system,
                            config.server,
                            config.port,
                            config.env,
                            config.includes,
                            config.user,
                            config.passwd)

        log.add('PROJECT', [config.name])
        log.add(system.os, ['Starting Advpl Build Bot'])
        log.add('GIT CHECKOUT', git.checkout())
        log.add('GIT PULL', git.pull())
        log.add('BUILD',advpl.build(git.get_changed_files()))
        log.add(system.os, ['Finish'])

    log.write_log()


if __name__ == '__main__':
    main()