"""
@author: Pascal Clermont

this file is simply sets the loggers
"""
from __future__ import unicode_literals

import logging
import os


# Disable extra logging for tests
logging.getLogger('boto').setLevel(logging.CRITICAL)
logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logging.getLogger('unittest').setLevel(logging.CRITICAL)

# Setup fake AWS Credentials
os.environ['AWS_ACCESS_KEY_ID'] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
os.environ['AWS_SECRET_ACCESS_KEY'] = '123456789'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
