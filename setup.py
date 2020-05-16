import os
from setuptools import setup

path = os.path.dirname(__file__)
long_desc_fd = os.path.join(path, 'README.md')

long_description = ''

with open(long_desc_fd) as f:
    long_description = f.read()

setup(
    name='musicmaybe',
    version='0.0.1',
    packages=['musicmaybe'],
    url='https://github.com/sillyfatcat/musicmaybe',
    license='MIT',
    author='Shelby Shum',
    author_email='sshum00@gmail.com',
    description='musicmaybe is a procedural generated music platform that will hopefully generate sorta reasonable music.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['SOUND', 'MUSIC', 'PROCEDURAL GENERATED'],
    download_url='https://github.com/sillyfatcat/musicmaybe/archive/v0.1.tar.gz',
    install_requires=[
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': []
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
