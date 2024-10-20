import argparse
import os
import platform
from src.get_pms import get_pms
import src.vars as vars
import subprocess
from src.get_commands import get_commands

if platform.system() != "Linux":
     print("unipkg is only compatible with Linux.")
     exit()

config_path = os.path.expanduser('~/.config/unipkg/')

try:
     os.makedirs(config_path, exist_ok=True)
except Exception as e:
     print(f"Error while trying to make configuration folder: {str(e)}")

config_file_path = config_path + 'unipkg.conf'

try:
     with open(config_file_path, 'w'):
          pass
except Exception as e:
     print(f"Error while trying to make configuration file: {str(e)}")

vars.config_path = config_file_path

parser = argparse.ArgumentParser(description="A unifying command line tool for managing packages on various Linux distributions.")

parser.add_argument('manage', choices=['update', 'upgrade', 'install', 'remove', 'clean', 'search', 'searchlocal'], type=str, nargs='?', help="Manage packages (update, upgrade, install, delete and remove unused dependencies) or search for either installed or online packages")
parser.add_argument('packages', nargs='*', type=str, help='List the packages to upgrade, install, delete or search for (not used with update)')

vars.args = parser.parse_args()

vars.pms = get_pms()

# placeholder
used_pm = vars.pms[0]

print(f"using: {used_pm}")

commands = get_commands(used_pm)
if commands:
     vars.update_command, vars.upgrade_all_command, vars.update_and_upgrade, vars.upgrade_specified_command, vars.install_command, vars.remove_command, vars.clean_command, vars.search_repo_command, vars.search_local_command = commands
else:
     print("Your distribution has no supported package manager.")
     exit()

if not vars.args.manage:
     parser.print_help()
     exit()

if ' -' in vars.args.packages or ' --' in vars.args.packages or any(item.startswith('-') for item in vars.args.packages):
     print('Error: no command line arguments after positional arguments')
     exit()

elif vars.args.manage == 'update':
     if vars.args.packages:
          print("No arguments expected after 'update'")
          exit()
     else:
          try:
               subprocess.run(vars.update_command, shell=True, check=True, text=True)
          except Exception as e:
               print(f"Error: {str(e)}")

elif vars.args.manage == 'upgrade':
     if not vars.args.packages:
          try:
               subprocess.run(vars.upgrade_all_command, shell=True, check=True, text=True)
          except Exception as e:
               print(f"Error: {str(e)}")
     else:
          try:
               subprocess.run(vars.upgrade_specified_command + ' ' + ' '.join(vars.args.packages), shell=True, check=True, text=True)
          except Exception as e:
               print(f"Error: {str(e)}")

elif vars.args.manage == 'install':
     if not vars.args.packages:
          print("Please specify the package(s) you want to install.")
     else:
          try:
               subprocess.run(vars.install_command + ' ' + ' '.join(vars.args.packages), shell=True, check=True, text=True)
          except Exception as e:
               print(f"Error: {str(e)}")

elif vars.args.manage == 'remove':
     if not vars.args.packages:
          print("Please specify the package(s) you want to delete.")
     else:
          try:
               subprocess.run(vars.remove_command + ' ' + ' '.join(vars.args.packages), shell=True, check=True, text=True)
          except Exception as e:
               print(f"Error: {str(e)}")

elif vars.args.manage == 'clean':
     if vars.args.packages:
          print("No arguments expected after 'clean'")
          exit()
     elif vars.clean_command:
          try:
               subprocess.run(vars.clean_command, shell=True, check=True, text=True)
          except Exception as e:
               print(f"Error: {str(e)}")

elif vars.args.manage == 'search':
     if not vars.args.packages:
          print("Please specify search")
     else:
          try:
               subprocess.run(vars.search_repo_command + ' ' + ' '.join(vars.args.packages), shell=True, check=True, text=True)
          except Exception as e:
               print(f"Error: {str(e)}")

elif vars.args.manage == 'searchlocal':
     if not vars.args.packages:
          print("Please specify search")
     else:
          try:
               subprocess.run(vars.search_local_command + ' ' + ' '.join(vars.args.packages), shell=True, check=True, text=True)
          except Exception as e:
               print(f"Error: {str(e)}")
