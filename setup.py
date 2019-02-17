from io import open
from os import path

from setuptools import setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sensehat_exporter',
    version='0.1.0',
    description='Sense HAT exporter for Prometheus',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ymyzk/sensehat_exporter',
    author='Yusuke Miyazaki',
    author_email='miyazaki.dev@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='prometheus',
    packages=['sensehat_exporter'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    install_requires=[
        'prometheus-client>=0.5.0',
        'RTIMULib>=7.2.1',
        'sense-hat>=2.2.0',
    ],
    entry_points={
        'console_scripts': [
            'sensehat_exporter=sensehat_exporter.__main__',
        ],
    },
)
