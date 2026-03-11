from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="oaqjp-final-project-emb-ai",
    version="0.1.0",
    author="acashok",
    description="Final project emotion prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/acashok/oaqjp-final-project-emb-ai.git",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)