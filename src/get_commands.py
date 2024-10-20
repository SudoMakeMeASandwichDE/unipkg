def get_commands(pm):
    update_command = None
    upgrade_all_command = None
    update_and_upgrade = None
    upgrade_specified_command = None
    install_command = None
    remove_command = None
    clean_command = None

    if pm == 'apt':
        update_command = "sudo apt update"
        upgrade_all_command = "sudo apt upgrade"
        update_and_upgrade = "sudo apt update && sudo apt upgrade"
        upgrade_specified_command = "sudo apt install --only-upgrade"
        install_command = "sudo apt install"
        remove_command = "sudo apt remove --purge"
        clean_command = "sudo apt clean && sudo apt autoremove"
        search_repo_command = "apt search"
        search_local_command = "apt list --installed"

    elif pm == 'pacman':
        update_command = "sudo pacman -Sy"
        upgrade_all_command = "sudo pacman -Syu"
        update_and_upgrade = "sudo pacman -Syu"
        upgrade_specified_command = "sudo pacman -S"
        install_command = "sudo pacman -S"
        remove_command = "sudo pacman -Rns"
        clean_command = "sudo pacman -Scc && sudo pacman -Rns $(pacman -Qdtq)"
        search_repo_command = "pacman -Ss"
        search_local_command = "pacman -Qs"

    elif pm == 'yay':
        update_command = "yay -Sy"
        upgrade_all_command = "yay -Syu"
        update_and_upgrade = "yay -Syu"
        upgrade_specified_command = "yay -S"
        install_command = "yay -S"
        remove_command = "yay -Rns"
        clean_command = "yay -Scc && yay -Rns $(pacman -Qdtq)"
        search_repo_command = "yay -Ss"
        search_local_command = "yay -Qs"

    elif pm == 'dnf':
        update_command = "sudo dnf check-update"
        upgrade_all_command = "sudo dnf upgrade"
        update_and_upgrade = "sudo dnf upgrade"
        upgrade_specified_command = "sudo dnf upgrade"
        install_command = "sudo dnf install"
        remove_command = "sudo dnf remove"
        clean_command = "sudo dnf clean all"
        search_repo_command = "dnf search"
        search_local_command = "dnf list installed"

    elif pm == 'yum':
        update_command = "sudo yum check-update"
        upgrade_all_command = "sudo yum update"
        update_and_upgrade = "sudo yum update"
        upgrade_specified_command = "sudo yum update"
        install_command = "sudo yum install"
        remove_command = "sudo yum remove"
        clean_command = "sudo yum clean all"
        search_repo_command = "yum search"
        search_local_command = "yum list installed"

    elif pm == 'zypper':
        update_command = "sudo zypper refresh"
        upgrade_all_command = "sudo zypper update"
        update_and_upgrade = "sudo zypper refresh && sudo zypper update"
        upgrade_specified_command = "sudo zypper up"
        install_command = "sudo zypper install"
        remove_command = "sudo zypper remove"
        clean_command = "sudo zypper clean"
        search_repo_command = "zypper search"
        search_local_command = "zypper se --installed-only"

    elif pm == 'snap':
        update_command = "sudo snap refresh"
        upgrade_all_command = "sudo snap refresh"
        update_and_upgrade = "sudo snap refresh"
        upgrade_specified_command = "sudo snap refresh"
        install_command = "sudo snap install"
        remove_command = "sudo snap remove"
        clean_command = False
        search_repo_command = "snap find"
        search_local_command = "snap list"

    if None in [update_command, upgrade_all_command, update_and_upgrade, upgrade_specified_command, install_command, remove_command, clean_command, search_repo_command, search_local_command]:
        return False

    return (update_command, upgrade_all_command, update_and_upgrade, upgrade_specified_command, install_command, remove_command, clean_command, search_repo_command, search_local_command)
