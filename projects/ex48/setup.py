#!/usr/bin/python  
# -*- coding: utf-8 -*-  

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'Ex48',
    'author': 'Antenna lili',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'lilyef2000@163.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Ex48'],
    'scripts': [],
    'name': 'Ex48'
    }

setup(**config)