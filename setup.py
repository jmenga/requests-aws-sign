#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='requests_aws_sign',
    version='0.1.3',
    packages=[ 'requests_aws_sign' ],
    install_requires=[ 'requests>=2.0.0', 'boto3' ],
    provides=[ 'requests_aws_sign' ],
    author='Justin Menga',
    author_email='justin.menga@gmail.com',
    url='https://github.com/jmenga/requests-aws-sign',
    description='This package provides AWS V4 request signing using the requests library.',
    keywords='requests aws',
    license='ISC',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: ISC License (ISCL)',
    ],
)
