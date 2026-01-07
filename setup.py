from setuptools import setup, find_packages

setup(
    name="terminai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.12.0",
        "typer>=0.9.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "fixit=terminai.main:entry_point",
        ],
    },
)