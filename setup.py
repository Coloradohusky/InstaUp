from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='instaup',
    version='1.01',
    description='An auto downloader and uploader for Instagram profiles.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/Coloradohusky/InstaUp',
    author='Coloradohusky',
    py_modules=['instaup'],
    entry_points={
        'console_scripts': [
            'instaup = instaup:main',
        ],
    },
    python_requires='>=3.5, <4',
    install_requires=['internetarchive>=1.9.3', 'instaloader>=4.4.3']
)
