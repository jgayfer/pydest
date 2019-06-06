import setuptools
import re

with open('pydest/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="pydest",
        version=version,
        author="James Gayfer",
        author_email="gayfer.james@gmail.com",
        description="Async wrapper for Destiny 2 API",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/jgayfer/pydest",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
        )
