from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="unipkg",
    version="0.1.1",
    description="A unifying package manager command line tool",
    author="SudoMakeMeASandwichDE",
    license="GPL-3.0-or-later",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.10",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["unipkg"],
    install_requires=[

    ],
    entry_points={
        "console_scripts": [
            "unipkg=unipkg:main",
        ],
    },
)
