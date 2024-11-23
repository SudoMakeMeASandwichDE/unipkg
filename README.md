# unipkg

`unipkg` is a command-line tool designed for managing packages across various Linux distributions. It provides a unified command line syntax for common package management tasks such as updating, upgrading, installing, removing, and cleaning packages.
Intended for Linux beginners and people who often work on various distributions and don't want to write down syntax of package managers (understandable).

## How it works

1. By the first time executing `unipkg`, you have to configure which package managers you want to include for updating and upgrading packages and which package manager you want to use primarily (for all the other commands, e.g., installing packages). You can always change the configuration with `unipkg --set upudate` or `unipkg --set manage`. 
2. When executing a command like `unipkg install firefox` it translates it to the equivalent command of the chosen package manager (e.g., for `apt` `sudo apt install firefox` or for `pacman` `sudo pacman -S firefox`).
3. The now translated command wil be executed in the current environment. Remember that most likely you will be asked by `sudo` to enter your password. 

## Features

- Compatible with most Linux distributions.
- Supports common package management commands: `update`, `upgrade`, `install`, `remove`, `clean`, `searchlocal`, and `search`.
- Automatically detects the available package manager(s) on the system.

## Requirements

- at least Python 3.10
- Linux operating system

## Compatible package managers

- `apt` (Debian/Ubuntu)
- `pacman` (Arch)
- `yay` (Arch)
- `dnf` (Fedora/CentOS)
- `zypper` (OpenSUSE)
- `apk` (Alpine Linux)
- `snap` (universal)
- `flatpak` (universal)

## Tested package managers

- `apt`
- `snap`
- `flatpak`

**(Please report any problems!)**

## Installation

1. ensure you have at least Python version 3.10 installed on your Linux system
2. clone the repository or download the source code
3. open a terminal in the project folder and run `pip install .`

## Usage

To use `unipkg`, run the script with the desired command and any necessary package names. The basic syntax is:

```bash
unipkg <manage> [packages]
# Replace <manage> with one of the commands, e.g., 'install'
```
## Commands

- `update`: Update the package manager's database.
- `upgrade`: Upgrade installed packages. You can specify package names or upgrade all.
- `install`: Install specified packages.
- `remove`: Remove specified packages.
- `clean`: Clean up unused dependencies.
- `search`: Search for packages in the online repository.
- `searchlocal`: Search for installed packages.
- `everything`: Executes the `update`, `upgrade` and `clean`-command all at once.
- `--set <update or manage>`: Configure, which package managers you want to update and on which you want to use the package management commands (install, remove, search, etc.).
- `--pm <package manager>`: Execute a command for a specific package manager.

## This isn't a finished version!

But it works with it's few features. `unipkg` is in it's (very) early development, and there will be many features added in near future. For this moment, `unipkg` only works with basic commands, but you can expect some more interesting features coming in the next few weeks and months. 
