import distro
from src.check_other_pms import is_snap_installed
from src.check_other_pms import is_flatpak_installed

def get_pms():
    used_distro = distro.name().lower()
    base_distros = distro.like().lower()
    available_pms = []

    if "ubuntu" in base_distros or "debian" in base_distros or "ubuntu" in used_distro or "debian" in used_distro:
        available_pms = ['apt']

    if "arch" in base_distros or "arch" in used_distro:
        available_pms = ['pacman', 'yay']

    if "fedora" in base_distros or "fedora" in used_distro or "centos" in base_distros or "rhel" in base_distros or "centos" in used_distro or "rhel" in used_distro:
        available_pms = ['dnf']
    
    if "suse" in base_distros or "suse" in used_distro:
        available_pms = ['zypper']
    
    if "alpine" in base_distros or "alpine" in used_distro:
        available_pms = ['apk']
    
    if is_snap_installed():
        available_pms.append('snap')

    if is_flatpak_installed():
        available_pms.append('flatpak')

    return available_pms if available_pms else False
