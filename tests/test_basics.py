"""
@author: Pascal Clermont

Tests that are concerning basic portion of this code.
"""
import unittest
from src import main


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

    def test_not_getting_a_version(self):
        """
        Load CloudFormation  template generated and makes sure there is a
        ssm document configured
        """
        with self.assertRaises(RuntimeError):
            main.find_version('main.py')
