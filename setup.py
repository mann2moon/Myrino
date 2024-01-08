from setuptools import setup, find_packages

setup(
    name='myrino',
    version='0.1',
    author='amirali irvany',
    author_email='dev.metect@gmail.com',
    description='Myrino is an api-based library for Rubino messengers',
    url='https://github.com/metect',
    install_requires=['requests'],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
