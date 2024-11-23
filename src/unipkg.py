# Made in Germany
import argparse
import os
import platform
import ast
from src.get_pms import get_pms
import src.vars as vars
from src.get_commands import get_commands, get_update_commands
from src.settings import settings
from src.loop import main_loop

def main():
     if platform.system() != "Linux":
          print("unipkg is only compatible with Linux.")
          exit()

     config_path = os.path.expanduser('~/.config/unipkg/')


     vars.pms = get_pms()

     try:
          os.makedirs(config_path, exist_ok=True)
     except Exception as e:
          print(f"Error while trying to make configuration folder: {str(e)}")
          exit()

     config_file_path = config_path + 'unipkg.conf'

     vars.config_path = config_file_path

     try:
          with open(config_file_path, 'r') as f:
               vars.configuration = [line.strip() for line in f.readlines()]
     except Exception as e:
          print(f"Error while trying to read configuration file: {str(e)}")
          exit()

     try:
          vars.configuration[0] = ast.literal_eval(vars.configuration[0])
     except Exception:
          print("Broken configuration file. Reconfiguration required.")
          settings()

     if len(vars.configuration) < 2:
          print("Broken configuration file. Reconfiguration required.")
          settings()    

     try:
          with open(config_file_path, 'r') as f:
               vars.configuration = [line.strip() for line in f.readlines()]
     except Exception as e:
          print(f"Error while trying to read configuration file: {str(e)}")
          exit()


     if vars.configuration:
          if all(element in vars.pms for element in ast.literal_eval(vars.configuration[0])):
               vars.update_pms = vars.configuration[0]
          else: 
               print("Reconfiguration required.")
               settings()
          if vars.configuration[1] in vars.pms and ' ' not in vars.configuration[1]:
               vars.install_pm = vars.configuration[1]
          else:
               print("Reconfiguration required.")
               settings()
     else:
          settings()

     vars.parser = argparse.ArgumentParser(description="A unifying command line tool for managing packages on various Linux distributions.")

     vars.parser.add_argument('--pm', type=str, required=False, help='Choose, in which package manager you want to execute the command')
     vars.parser.add_argument('--set', type=str, required=False, help="Choose, which pms you want to update with the update command and wich ones you want to use to install, delete and search packages")
     vars.parser.add_argument('manage', choices=['update', 'upgrade', 'install', 'remove', 'clean', 'search', 'searchlocal', 'everything'], type=str, nargs='?', help="Manage packages (update, upgrade, install, delete packages and remove unused dependencies), search for either installed or online packages or change settings for Package managers")
     vars.parser.add_argument('packages', nargs='*', type=str, help='List the packages to upgrade, install, delete or search for (not used with update and clean)')

     vars.args = vars.parser.parse_args()

     if vars.args.pm:
          if ' ' not in vars.args.pm.strip():
               if vars.args.pm.strip() in vars.pms:
                    vars.install_pm = vars.args.pm
                    vars.update_pms = []
                    vars.update_pms.append(vars.args.pm)
               else:
                    print("Package manager not found.")
                    exit()
          else:
               if all(element in vars.pms for element in vars.args.pm.strip().split()):
                    if vars.args.manage == 'update' or vars.args.manage == 'upgrade':
                         vars.update_pms = vars.args.pm.strip().split()
                    else:
                         print("You can only run this command on a single package manager.")
                         exit()

     commands = get_commands(vars.install_pm)
     if commands:
          vars.update_and_upgrade, vars.upgrade_specified_command, vars.install_command, vars.remove_command, vars.clean_command, vars.search_repo_command, vars.search_local_command = commands
     else:
          print("Your distribution has no supported package manager.")
          exit()

     update_commands = get_update_commands(vars.update_pms)
     if update_commands:
          vars.update_command, vars.upgrade_all_command = update_commands
     else:
          print("Your distribution has no supported package manager.")
          exit() 

     main_loop()

if __name__ == '__main__':
     main()
