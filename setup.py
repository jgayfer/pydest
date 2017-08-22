import re
from distutils.core import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ''
with open('pydest/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setup(name='pydest',
      author='jgayfer',
      version=version,
      license='MIT',
      description='an asynchronous Destiny 2 API wrapper',
      install_requires=requirements,
      packages=['pydest'])
