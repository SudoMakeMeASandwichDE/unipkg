def get_commands(pm):
    update_and_upgrade = None
    upgrade_specified_command = None
    install_command = None
    remove_command = None
    clean_command = None
    search_repo_command = None
    search_local_command = None

    if pm == 'apt':
        update_and_upgrade = "sudo apt update && sudo apt upgrade"
        upgrade_specified_command = "sudo apt install --only-upgrade"
        install_command = "sudo apt install"
        remove_command = "sudo apt remove --purge"
        clean_command = "sudo apt clean && sudo apt autoremove"
        search_repo_command = "apt search"
        search_local_command = "apt list --installed"

    elif pm == 'pacman':
        update_and_upgrade = "sudo pacman -Syu"
        upgrade_specified_command = "sudo pacman -S"
        install_command = "sudo pacman -S"
        remove_command = "sudo pacman -Rns"
        clean_command = "sudo pacman -Scc && sudo pacman -Rns $(pacman -Qdtq)"
        search_repo_command = "pacman -Ss"
        search_local_command = "pacman -Qs"

    elif pm == 'yay':
        update_and_upgrade = "yay -Syu"
        upgrade_specified_command = "yay -S"
        install_command = "yay -S"
        remove_command = "yay -Rns"
        clean_command = "yay -Scc && yay -Rns $(pacman -Qdtq)"
        search_repo_command = "yay -Ss"
        search_local_command = "yay -Qs"

    elif pm == 'dnf':
        update_and_upgrade = "sudo dnf upgrade"
        upgrade_specified_command = "sudo dnf upgrade"
        install_command = "sudo dnf install"
        remove_command = "sudo dnf remove"
        clean_command = "sudo dnf clean all"
        search_repo_command = "dnf search"
        search_local_command = "dnf list installed"

    elif pm == 'yum':
        update_and_upgrade = "sudo yum update"
        upgrade_specified_command = "sudo yum update"
        install_command = "sudo yum install"
        remove_command = "sudo yum remove"
        clean_command = "sudo yum clean all"
        search_repo_command = "yum search"
        search_local_command = "yum list installed"

    elif pm == 'zypper':
        update_and_upgrade = "sudo zypper refresh && sudo zypper update"
        upgrade_specified_command = "sudo zypper up"
        install_command = "sudo zypper install"
        remove_command = "sudo zypper remove"
        clean_command = "sudo zypper clean"
        search_repo_command = "zypper search"
        search_local_command = "zypper se --installed-only"

    elif pm == 'snap':
        update_and_upgrade = "sudo snap refresh"
        upgrade_specified_command = "sudo snap refresh"
        install_command = "sudo snap install"
        remove_command = "sudo snap remove"
        clean_command = False
        search_repo_command = "snap find"
        search_local_command = "snap list"

    elif pm == 'flatpak':
        update_and_upgrade = "sudo flatpak update"
        upgrade_specified_command = "sudo flatpak update"
        install_command = "sudo flatpak install"
        remove_command = "sudo flatpak uninstall"
        clean_command = "sudo flatpak uninstall --unused"
        search_repo_command = "flatpak search"
        search_local_command = "flatpak list | grep"

    elif pm == 'apk':
        update_and_upgrade = "sudo apk update && sudo apk upgrade"
        upgrade_specified_command = "sudo apk upgrade"
        install_command = "sudo apk add"
        remove_command = "sudo apk del"
        clean_command = "sudo apk cache clean"
        search_repo_command = "apk search"
        search_local_command = "apk info -vv | grep installed"

    if None in [update_and_upgrade, upgrade_specified_command, install_command, remove_command, clean_command, search_repo_command, search_local_command]:
        return False

    return (update_and_upgrade, upgrade_specified_command, install_command, remove_command, clean_command, search_repo_command, search_local_command)

def get_update_commands(pms):
    update_command = []
    upgrade_all_command = []

    if 'apt' in pms:
        update_command.append("sudo apt update")
        upgrade_all_command.append("sudo apt upgrade")

    if 'pacman' in pms:
        update_command.append("sudo pacman -Sy")
        upgrade_all_command.append("sudo pacman -Syu")

    if 'yay' in pms:
        update_command.append("yay -Sy")
        upgrade_all_command.append("yay -Syu")

    if 'dnf' in pms:
        update_command.append("sudo dnf check-update")
        upgrade_all_command.append("sudo dnf upgrade")

    if 'yum' in pms:
        update_command.append("sudo yum check-update")
        upgrade_all_command.append("sudo yum update")

    if 'zypper' in pms:
        update_command.append("sudo zypper refresh")
        upgrade_all_command.append("sudo zypper update")

    if 'snap' in pms:
        update_command.append("sudo snap refresh")
        upgrade_all_command.append("sudo snap refresh")

    if 'flatpak' in pms:
        update_command.append("sudo flatpak update")
        upgrade_all_command.append("sudo flatpak update")

    if 'apk' in pms:
        update_command.append("sudo apk update")
        upgrade_all_command.append("sudo apk upgrade")

    if any(len(arr) == 0 for arr in [update_command, upgrade_all_command]):
        return False

    return (update_command, upgrade_all_command)

