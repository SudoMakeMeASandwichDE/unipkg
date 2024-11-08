import subprocess
import src.vars as vars

def execute(command):
    match command:
        case 'update':
            if vars.args.packages:
                print("No arguments expected after 'update'")
                exit()
            else:
                try:
                    subprocess.run(' && '.join(vars.update_command), shell=True, check=True, text=True)
                except subprocess.CalledProcessError:
                    pass
                except Exception as e:
                    print(f"Error: {str(e)}")

        case 'upgrade':
            if not vars.args.packages:
                try:
                    subprocess.run(' && '.join(vars.upgrade_all_command), shell=True, check=True, text=True)
                except subprocess.CalledProcessError:
                    pass
                except Exception as e:
                    print(f"Error: {str(e)}")
            else:
                try:
                    subprocess.run(vars.upgrade_specified_command + ' ' + ' '.join(vars.args.packages), shell=True, check=True, text=True)
                except subprocess.CalledProcessError:
                    pass
                except Exception as e:
                    print(f"Error: {str(e)}")

        case 'install':
            if not vars.args.packages:
                print("Please specify the package(s) you want to install.")
            else:
                try:
                    subprocess.run(vars.install_command + ' ' + ' '.join(vars.args.packages), shell=True, check=True, text=True)
                except subprocess.CalledProcessError:
                    pass
                except Exception as e:
                    print(f"Error: {str(e)}")

        case 'remove':
            if not vars.args.packages:
                print("Please specify the package(s) you want to delete.")
            else:
                try:
                    subprocess.run(vars.remove_command + ' ' + ' '.join(vars.args.packages), shell=True, check=True, text=True)
                except subprocess.CalledProcessError:
                    pass
                except Exception as e:
                    print(f"Error: {str(e)}")

        case 'clean':
            if vars.args.packages:
                print("No arguments expected after 'clean'")
                exit()
            elif vars.clean_command:
                try:
                    subprocess.run(vars.clean_command, shell=True, check=True, text=True)
                except subprocess.CalledProcessError:
                    pass
                except Exception as e:
                    print(f"Error: {str(e)}")

        case 'search':
            if not vars.args.packages:
                print("Please specify search")
            else:
                try:
                    subprocess.run(vars.search_repo_command + ' ' + ' '.join(vars.args.packages), shell=True, check=True, text=True)
                except subprocess.CalledProcessError:
                    pass
                except Exception as e:
                    print(f"Error: {str(e)}")

        case 'searchlocal':
            if not vars.args.packages:
                print("Please specify search")
            else:
                try:
                    subprocess.run(vars.search_local_command + ' ' + ' '.join(vars.args.packages), shell=True, check=True, text=True)
                except subprocess.CalledProcessError:
                    pass
                except Exception as e:
                    print(f"Error: {str(e)}")

        case _:
            print(f"Unknown command: {command}")
