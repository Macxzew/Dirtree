from setuptools import setup, find_packages

setup(
    name="dirtree",
    version="1.0",
    author="YourName",
    description="Generate and save folder tree structures from a GUI.",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dirtree = dirtree.main:main",
        ],
    },
    install_requires=open("requirements.txt", encoding="utf-8").read().splitlines(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
