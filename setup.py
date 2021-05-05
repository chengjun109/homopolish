from setuptools import setup, find_packages
import os

setup(
    name="homopolish",
    version="0.2.1",
    url='https://github.com/ythuang0522/homopolish',
    author='ythuang0522',
    packages=find_packages(),
    package_data={'homopolish':['R10.3.pkl','R9.4.pkl']},
    entry_points={'console_scripts': ['homopolish =homopolish.homopolish:main']},
    )
