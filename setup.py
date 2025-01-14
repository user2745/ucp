from setuptools import setup, find_packages

setup(
    name="ucp-framework",
    version="0.0.1",
    description="Universal Communication Protocol (UCP) built on MQTT",
    author="Kevin Kamto",
    author_email="kamtokevin@gmail.com",
    url="https://github.com/user2745/ucp",
    packages=find_packages(),
    install_requires=["paho-mqtt"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
