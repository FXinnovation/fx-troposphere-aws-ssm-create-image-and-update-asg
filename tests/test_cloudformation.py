"""
@author: Pascal Clermont

Tests that are concerning CloudFormation portion of this code.
"""
#
import json
import os
import unittest
from src import main


CLOUDFORMATION_FILE = 'CloudFormation.json'


def read_cloudformation():
    """
    reads the cloudformation file that is generated and return the data in
    json format
    """
    json_file = open(
        CLOUDFORMATION_FILE
    )
    data = json.load(json_file)
    json_file.close()
    return data


def find_ressource_type(ressource_type):
    """
    validates against the cloudformation file that the provided ressource is
    going to be created.
    """
    _data = read_cloudformation()
    for _item in _data.get('Resources').keys():
        if _data.get('Resources').get(_item).get('Type') == ressource_type:
            return True
    return False


class CloudFormationTestCase(unittest.TestCase):
    """
    CloudFormation Test Cases
    """
    def setUp(self):
        """
        setUp will run before execution of each test case
        main.main() will generate the CloudFormation File
        """
        main.main()

    def tearDown(self):
        """
        tearDown will run after execution of each test case
        """
        os.remove(CLOUDFORMATION_FILE)

    def test_we_can_generate_a_cloudformation_file(self):
        """
        check that the main python code generates a cloudformation
        """
        self.assertEqual(os.path.exists(CLOUDFORMATION_FILE), True)

    def test_cloudformation_should_contain_ssm_document(self):
        """
        Load CloudFormation  template generated and makes sure there is a
        ssm document configured
        """
        self.assertEqual(
            find_ressource_type('AWS::SSM::Document'),
            True
        )

    def test_cloudformation_should_contain_ssm_parameter(self):
        """
        Load CloudFormation  template generated and makes sure there is a
        ssm document configured
        """
        self.assertEqual(
            find_ressource_type('AWS::SSM::Parameter'),
            True
        )

    def test_cloudformation_should_not_contain_ec2_instance(self):
        """
        Load CloudFormation  template generated and makes sure there is a
        IAM role configured
        """
        self.assertEqual(
            find_ressource_type('AWS::EC2::Instance'),
            False
        )
