import setuptools

from google_chat_echo import __version__
from google_chat_echo import name

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=name,
    version=__version__,
    author="Michał Chałupczak",
    author_email="michal@chalupczak.info",
    description="Tiny tool for sending messages to google chat via http webhook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chomik/google-chat-echo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)