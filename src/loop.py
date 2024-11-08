from src.settings import settings
import src.vars as vars
from src.execute_command import execute

def main_loop():
    if not vars.args.manage and not vars.args.set and not vars.args.pm:
        vars.parser.print_help()
        exit()

    if ' -' in vars.args.packages or ' --' in vars.args.packages or any(item.startswith('-') for item in vars.args.packages):
        print('Error: no command line arguments after positional arguments')
        exit()

    elif vars.args.set:
        if vars.args.set == 'update':
            settings(update=True)

        elif vars.args.set == 'manage':
            settings(manage=True)

        elif vars.args.set != 'update' and vars.args.set != 'manage':
            print("Usage:\n--set update\n--set manage")
        exit()

    execute(vars.args.manage)

