from setuptools import setup

setup(
    name="unipkg",
    version="0.1.0",
    description="A unifying package manager comand line tool",
    author="SudoMakeMeASandwichDE",
    license="GPL-3.0-or-later",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.10",
    packages=["src"],
    py_modules=["unipkg"],
    entry_points={
        "console_scripts": [
            "unipkg=unipkg:main",
        ],
    },
)
