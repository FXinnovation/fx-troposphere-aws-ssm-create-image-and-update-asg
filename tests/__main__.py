"""
@author: Pascal Clermont

This will find all tests located in test_*.py files.
"""
import unittest
import xmlrunner

XML_REPORT_DIR = 'Reports'


# Create test suite.
TEST_SUITE = unittest.TestSuite()
# Load all test case class in current folder.
ALL_TEST_CASES = unittest.defaultTestLoader.discover('.', 'test_*.py')
# Loop the found test cases and add them into test suite.
for test_case in ALL_TEST_CASES:
    TEST_SUITE.addTests(test_case)

    # Create HtmlTestRunner object and run the test suite.
TEST_RUNNER = xmlrunner.XMLTestRunner(output=XML_REPORT_DIR)
TEST_RUNNER.run(TEST_SUITE)
