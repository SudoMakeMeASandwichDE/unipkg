import src.vars as vars
import json

def settings(update=False, manage=False):
    with open(vars.config_path, 'r') as f:
        content = f.readlines()
    if len(vars.pms) > 1:
        i = 1
        if not manage:
            while True:
                for p in vars.pms:
                    print(str(i) + ". " + p)
                    i += 1
                try:
                    update_pms = input("Which pms do you want to update with the update command (separate with space)?\n> ").strip().split()
                except KeyboardInterrupt:
                    print("\nexited with ^C")
                    exit()                
                if all(item in vars.pms for item in update_pms):
                    vars.update_pms = update_pms
                    
                    try:
                        with open(vars.config_path, 'w') as a:
                            a.write(json.dumps(vars.update_pms) + '\n')
                            a.write(content[1] if len(content) > 1 else '')
                    except Exception as e:
                        print(f"Error while saving settings: {str(e)}")
                        exit()
                    print("Saved settings.")
                    break
                else:
                    print("One or more package manager(s) not found. Please choose from the list.")
                    i = 1
                    continue

        i = 1
        if not update:
            while True:
                for p in vars.pms:
                    print(str(i) + ". " + p)
                    i += 1
                try:
                    install_pm = input("Which pm do you want to use with the install, remove and search command?\n> ").strip()
                except KeyboardInterrupt:
                    print("\nexited with ^C")
                    exit()
                if install_pm in vars.pms:
                    vars.install_pm = install_pm
                    try:
                        with open(vars.config_path, 'w') as f:
                            f.write(content[0]if len(content) >= 0 else '')
                            f.write(install_pm)
                    except Exception as e:
                        print(f"Error while saving install_pm: {str(e)}")
                        exit()
                    print("Saved settings.")
                    break
                else:
                    print("Package manager not found. Please choose ONE from the list.")
                    i = 1
                    continue

    else:
        print(f"Only one package manager is available: {vars.pms[0]}. It will be used.")
