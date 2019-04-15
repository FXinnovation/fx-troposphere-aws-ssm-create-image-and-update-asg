# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='create-image-and-update-asg',
    version='0.1.0',
    description=' '.join([
        'Crates an image and Updates the AMI used for an AutoScaling Group in',
        'Amazon, using Systems Manager.'
    ]),
    long_description=readme,
    author='Pascal Clermont',
    author_email='pascal.clermont@fxinnovation.com',
    url=''.join([
        'https://scm.dazzlingwrench.fxinnovation.com/fxinnovation-private/',
        'troposphere-aws-ssm-create-image-and-update-asg.git'
                 ]),
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
