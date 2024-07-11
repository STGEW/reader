from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")


def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name="reader",
    version="0.0.1",
    description="A reader project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="reader"),
    python_requires=">=3.7, <4",
    install_requires=read_requirements(),
    
    entry_points={  # Optional
        "console_scripts": [
            "reader=reader:main",
        ],
    }
)