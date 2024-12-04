from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name="reader",
    version="0.0.1",
    description="A reader project",
    packages=find_packages(),
    python_requires=">=3.7, <4",
    install_requires=read_requirements(),
    
    entry_points={  # Optional
        "console_scripts": [
            "reader=reader.main:main",
        ],
    }
)