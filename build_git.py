from os.path import exists

class Build_Git:
    def __init__(self, system, branch, exp_interval, show_type):
        self.__system = system
        self.__branch = branch
        self.__show_type = show_type
        self.__exp_interval = exp_interval
        self.__changed_files = self.__system.build_path


    def checkout(self): 
        log_return = []
        
        if self.__branch:
            log_return = self.__system.run(['git', 'checkout', self.__branch], self.__system.build_path)
        else:
            log_return = ['Checkout Skipped']
        
        return log_return


    def pull(self): 
        log_return = []
        
        if self.__branch:
            log_return = self.__system.run(['git', 'pull'], self.__system.build_path)
        else:
            log_return = ['Pull Skipped']
        
        return log_return


    def get_changed_files(self):


        if self.__branch:
            last_update = []

            last_update.append('git')
            last_update.append('log')
            last_update.append(self.__branch)
            if "m" in self.__show_type:
                last_update.append('-m')
            last_update.append(f'--since={self.__exp_interval}')
            last_update.append('--name-only')
            last_update.append(f'--line-prefix={self.__system.build_path}')

            out = self.__system.run(last_update, self.__system.build_path)

            self.__changed_files = ''

            for x in out:
                if ('.prw' in x.lower() or '.aph' in x.lower()) and x not in self.__changed_files and exists(x):
                    self.__changed_files += ',' if self.__changed_files.__len__() > 0 else ''
                    self.__changed_files += x

        return self.__changed_files
