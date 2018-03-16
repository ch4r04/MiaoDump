from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

long_description = (
    "This script is just for exporting header files(encrypted)."
    "Security is not now, and will never be based purely on Obscurity."
    "You can delete if you don't need the defines."
    "There may be some bugs, good luck."
)

setup(
    name='miaodump',

    version='0.1.0',

    description='A tool what used to export encrypted header files',

    long_description=long_description,

    url='https://github.com/ch4r04/MiaoDump.git',
    author='ch4r0n',
    author_email='xingrenchan@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Topic :: Documentation',
        'Topic :: Text Processing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='miaodump',
    packages=find_packages(),

    install_requires=[],

    entry_points={
        'console_scripts': [
            'miaodump=miaodump.cli.miaodump_client:main',
        ],
    },
)
