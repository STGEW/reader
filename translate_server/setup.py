from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name="translate_server",
    version="0.0.1",
    description="A server to manage translations",
    packages=find_packages(where="translate_server"),
    python_requires=">=3.7, <4",
    install_requires=read_requirements(),
    
    entry_points={  # Optional
        "console_scripts": [
            "translate_server=translate_server.translate_thread:main",
        ],
    }
)