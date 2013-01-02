#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='django-singlerecord',
    version='0.1.1',
    description='Abstraction for models with only one record for Django',
    author='Bruno Tavares',
    author_email='eu@brunotavares.net',
    url='http://github.com/tavaresb/django-singlerecord',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
