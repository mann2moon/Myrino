from setuptools import setup, find_packages
from myrino import __version__, __github__

setup(
    name='myrino',
    version=__version__,
    author='amirali irvany',
    author_email='dev.metect@gmail.com',
    description='Myrino is an api-based library for Rubino messengers',
    long_description=open('README.md', encoding='utf-8').read(),
    url=__github__,
    install_requires=['requests'],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
