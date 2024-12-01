import subprocess
from src.logging import log
import src.vars as vars

def execute(command):
    def run_and_log(command_str):
        log(command_str, command=True)
        try:
            result = subprocess.run(
                command_str,
                shell=True,
                text=True,
                check=True,
                stdin=None,
                stdout=None,
                stderr=None
            )
            log("executed with no errors", output=True)
            log(result, output=True)
        except subprocess.CalledProcessError as e:
            log(f"command caused an error: {str(e)}", error=True)
        except Exception as e:
            log({str(e)}, error=True)
            raise e

    not_available_msg = f"'{command}'-command not available for current package manager."
    match command:
        case 'update':
            if not False in vars.update_command:
                if vars.args.packages:
                    print("No arguments expected after 'update'")
                    exit()
                else:
                    for i in vars.update_command:
                        print(f"---executing '{i}'---")
                        run_and_log(i)
                        print()
            else:
                print(not_available_msg)

        case 'upgrade':
            if not False in vars.upgrade_all_command:
                if not vars.args.packages:
                    for i in vars.upgrade_all_command:
                        print(f"---executing '{i}'---")
                        run_and_log(i)
                        print()
                elif vars.upgrade_specified_command:
                    run_and_log(vars.upgrade_specified_command + ' ' + ' '.join(vars.args.packages))
                else:
                    print(not_available_msg)
            else:
                print(not_available_msg)

        case 'install':
            if vars.install_command:
                if not vars.args.packages:
                    print("Please specify the package(s) you want to install.")
                else:
                    run_and_log(vars.install_command + ' ' + ' '.join(vars.args.packages))
            else:
                print(not_available_msg)

        case 'remove':
            if vars.remove_command:
                if not vars.args.packages:
                    print("Please specify the package(s) you want to delete.")
                else:
                    run_and_log(vars.remove_command + ' ' + ' '.join(vars.args.packages))
            else:
                print(not_available_msg)

        case 'clean':
            if vars.clean_command:
                if vars.args.packages:
                    print("No arguments expected after 'clean'")
                    exit()
                else:
                    run_and_log(vars.clean_command)
            else:
                print(not_available_msg)

        case 'search':
            if vars.search_repo_command:
                if not vars.args.packages:
                    print("Please specify search")
                else:
                    run_and_log(vars.search_repo_command + ' ' + ' '.join(vars.args.packages))
            else:
                print(not_available_msg)

        case 'searchlocal':
            if vars.search_local_command:
                if not vars.args.packages:
                    print("Please specify search")
                else:
                    run_and_log(vars.search_local_command + ' ' + ' '.join(vars.args.packages))
            else:
                print(not_available_msg)
        
        case 'info':
            if vars.info_command:
                if not vars.args.packages:
                    print("Please sepify package.")
                elif len(vars.args.packages) > 1:
                    print("Info can be shown for only one package.")
                else:
                    run_and_log(vars.info_command + ' ' + ' '.join(vars.args.packages))
        
        case 'addrepo':
            if vars.addrepo_command:
                if not vars.args.packages:
                    print("Please specify repository link.")
                else:
                    run_and_log(vars.addrepo_command + ' ' + ' '.join(vars.args.packages))

        case 'everything':
            if vars.args.packages:
                print("No arguments expected after 'everything'")
                exit()
            else:
                execute('update')
                execute('upgrade')
                print(f"---executing '{vars.clean_command}'---")
                execute('clean')

        case _:
            print(f"Unknown command: {command}")
