import src.vars as vars
from src.logging import log
import json

def settings(update=False, manage=False):
    with open(vars.config_path, 'r') as f:
        content = f.readlines()
    if len(vars.pms) > 1:
        i = 1
        if not manage:
            while True:
                print("Chose pms to include with update command")
                print("0. every listed pm")
                for p in vars.pms:
                    print(str(i) + ". " + p)
                    i += 1
                try:
                    update_pms_user_input = input(f"numbers 1 to {i-1} or 0, seperated with space\n> ").strip().split()
                except KeyboardInterrupt:
                    log("exited settings by user")
                    print("\nexited with ^C")
                    exit()
                try:
                    update_pms_user_input_int = [int(n) for n in update_pms_user_input]
                except Exception:
                    print("Invalid input. Try again.")
                    i = 1
                    continue
                if max(update_pms_user_input_int) >= i:
                    print("Invalid input. Try again.")
                    i = 1
                    continue
                update_pms = []
                if 0 not in update_pms_user_input_int:
                    for i in range(len(vars.pms)):
                        if i + 1 in update_pms_user_input_int: 
                            update_pms.append(vars.pms[i])
                else:
                    update_pms = vars.pms.copy()
                if all(item in vars.pms for item in update_pms):
                    vars.update_pms = update_pms
                    
                    try:
                        with open(vars.config_path, 'w') as a:
                            a.write(json.dumps(vars.update_pms) + '\n')
                            a.write(content[1] if len(content) > 1 else '')
                            log(f"update pms set to {', '.join(update_pms)}")
                    except Exception as e:
                        log(f"error while saving settings (update pms): {str(e)}", error=True)
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
                print("Choose primary pm (to use with management commands install, remove, search, etc.)")
                for p in vars.pms:
                    print(str(i) + ". " + p)
                    i += 1
                try:
                    install_pm_user_input = input(f"one number between 1 and {i-1}\n> ").strip()
                except KeyboardInterrupt:
                    log("exited settings by user")
                    print("\nexited with ^C")
                    exit()
                with open(vars.config_path, 'r') as f:
                    content = f.readlines()
                try:
                    install_pm_user_input_int = int(install_pm_user_input)
                except Exception:
                    print("Invalid input. Try again.")
                    i = 1
                    continue
                if install_pm_user_input_int >= i:
                    print("Invalid input. Try again.")
                    i = 1
                    continue
                install_pm = vars.pms[install_pm_user_input_int - 1]
                if install_pm in vars.pms:
                    vars.install_pm = install_pm
                    try:
                        with open(vars.config_path, 'w') as f:
                            f.write(content[0] if len(content) >= 0 else '')
                            f.write(install_pm)
                            log(f"set primary (managing) pm to {install_pm}")
                    except Exception as e:
                        log(f"Error while saving install_pm: {str(e)}", error=True)
                        print(f"Error while saving install_pm: {str(e)}")
                        exit()
                    print("Saved settings.")
                    break
                else:
                    print("Package manager not found. Please choose ONE from the list.")
                    i = 1
                    continue

    else:
        log(f"only one package manager available: {vars.pms[0]}, set as primary and update pm")
        print(f"Only one package manager is available: {vars.pms[0]}. It will be used.")
