# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re
import codecs
from os import path


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


def read(*parts):
    """Reads a relative file and returns the content"""
    with codecs.open(
            path.join(
                path.abspath(path.dirname(__file__)),
                *parts
            ), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    """Retrieves the __version__ value from the package"""
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='create-image-and-update-asg',
    version=find_version('src', '__init__.py'),
    description=' '.join([
        'Crates an image and Updates the AMI used for an AutoScaling Group in',
        'Amazon, using Systems Manager.'
    ]),
    long_description=readme,
    author='Pascal Clermont',
    author_email='pascal.clermont@fxinnovation.com',
    url=''.join([
        'https://github.com/FXinnovation/',
        'fx-troposphere-aws-ssm-create-image-and-update-asg.git'
                 ]),
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
