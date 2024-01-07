from setuptools import setup

setup(
    name = 'myrino',
    version = '0.1',
    author='amirali irvany',
    author_email = 'dev.metect@gmail.com',
    description = 'Myrino is an api-based library for Rubino messengers',
    keywords = ['Bot', 'rubino', 'rubika', 'myrino'],
    long_description = open('README.md', encoding='utf-8').read(),
    python_requires='~=3.6',
    url = 'https://github.com/metect',
    install_requires = ['requests'],
    classifiers = [
    	'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ]
)
