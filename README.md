# unipkg

`unipkg` is a command-line tool designed for managing packages across various Linux distributions. It provides a unified interface for common package management tasks such as updating, upgrading, installing, removing, and cleaning packages.

## Features

- Compatible with most Linux distributions.
- Supports common package management commands: `update`, `upgrade`, `install`, `remove`, `clean`, `searchlocal`, and `search`.
- Automatically detects the package manager of the system.

## Requirements

- Python 3.x
- Linux operating system

## Compatible package manager

- `apt` (Debian/Ubuntu)
- `pacman` (Arch)
- `yay` (Arch)
- `yum` (CentOS)
- `dnf` (Fedora)
- `zapper` (OpenSUSE)
- `snap` (universal)

## Tested package manager

- `apt`

**(Please report any problems!)**

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3 installed on your system.
3. Run `unipkg.py`

## Usage

To use `unipkg`, run the script with the desired command and any necessary package names. The basic syntax is:

```bash
python3 unipkg.py <manage> [packages]
# Replace <manage> with one of the commands, e.g. 'update'
```
## Commands
`update`: Update the package manager's database.
`upgrade`: Upgrade installed packages. You can specify package names or upgrade all.
`install`: Install specified packages.
`remove`: Remove specified packages.
`clean`: Clean up unused dependencies.
`search`: Search for packages in the online repository.
`searchlocal`: Search for installed packages.

## This isn't a finished version!

But it works with it's few features. `unipkg` is in it's (very) early developement and there will be meny features added in near future. In this moment, `unipkg` only works with basic commands but you can expect some more interesting features coming in the next few weeks and months. 
