import subprocess

def is_snap_installed():
    try:
        subprocess.run(['snap', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False
    
def is_flatpak_installed():
    try:
        subprocess.run(['flatpak', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False
