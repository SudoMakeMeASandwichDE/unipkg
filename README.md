# unipkg

`unipkg` is a command-line tool designed for managing packages across various Linux distributions. It provides a unified command line syntax for common package management tasks such as updating, upgrading, installing, removing, and cleaning packages.
Intended for Linux beginners and people who often work on various distributions and don't want to write down syntax of package managers (understandable).

## How it works

1. By the first time executing `unipkg`, you have to configure which package managers you want to include for updating and upgrading packages and which package manager you want to use primarily (for all the other commands, e.g., installing packages). You can always change the configuration with `unipkg --set update` or `unipkg --set primary`, more about that under "Commands". 
2. When executing a command like `unipkg install firefox` it translates it to the equivalent command of the chosen package manager (e.g., for `apt` `sudo apt install firefox` or for `pacman` `sudo pacman -S firefox`).
3. The now translated command wil be executed in the current environment. Remember that most likely you will be asked by `sudo` to enter your password. 

Configuration file is on `~/.config/unipkg/unipkg.conf`
Log file is on `~/.config/unipkg/unipkg.log`

## Features

- Compatible with most Linux distributions.
- Supports common package management commands: `update`, `upgrade`, `update-repo`, `install`, `remove`, `clean`, `searchlocal`, `search`, `info` and `addrepo`.
- Automatically detects the available package manager(s) on your system.

## Requirements

- Python version 3.10 or newer (check with `python3 --version`)
- Linux distribution with one of the following package managers:

  - `apt` (Debian/Ubuntu)
  - `pacman` (Arch)
  - `yay` (Arch)
  - `dnf` (Fedora/CentOS)
  - `zypper` (OpenSUSE)
  - `apk` (Alpine Linux)
  - Portage (gentoo)
  - `snap` (universal)
  - `flatpak` (universal)

**The following package managers have been tested:**

- `apt`
- `pacman`
- `snap`
- `flatpak`

**(Please report any issues!)**

## Installation

```bash
pipx install git+https://github.com/SudoMakeMeASandwichDE/unipkg.git
```
Make sure you have [pipx](https://github.com/pypa/pipx) installed.

## Update unipkg

```bash
pipx upgrade unipkg
```

## Usage

To use `unipkg`, run the command with the desired argument and any necessary package names. The basic syntax is:

```bash
unipkg <manage> [packages]
# Replace <manage> with one of the commands, e.g., 'install'
```
## Commands

- `update`: Update and upgrade of your packages.
- `upgrade`: Upgrade installed packages. You can specify package names or upgrade all.
- `update-repo`: Update you package managers' databases.
- `install`: Install specified packages.
- `remove`: Remove specified packages.
- `clean`: Remove unused dependencies and clean up cache.
- `search`: Search for packages in the online repository.
- `searchlocal`: Search for installed packages.
- `info`: Display information for a package.
- `addrepo`: Add an external repository.
- `--set update`: Configure, which of your used package managers you want to update with the the `update`- and `upgrade`-command
- `--set primary`: Choose one package manager you want to use the package management commands (install, remove, search, etc.) on top of the update command.
- `--pm <package manager>`: Execute a command for a specific package manager.
