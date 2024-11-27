from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="unipkg",
    version="0.1.2",
    description="A unifying package manager command line tool",
    author="SudoMakeMeASandwichDE",
    author_email="sudosandwich.contact@gmail.com",
    license="GPL-3.0-or-later",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/SudoMakeMeASandwichDE/unipkg",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.10",
    packages=['src'],
    py_modules=["unipkg"],
    install_requires=[

    ],
    entry_points={
        "console_scripts": [
            "unipkg=unipkg:main",
        ],
    },
)
