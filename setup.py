# setup.py

from setuptools import setup, find_packages

setup(
    name="chartokenizer",
    version="0.1.0",
    author="R Shashank Kanna",
    author_email="techyworker420@gmail.com",
    description="A basic character-level tokenizer",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MrTechyWorker/chartokenizer",  # URL of your project (can be left blank if you don't have one)
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
