"""
Generates a cloudformation to deploy this functionality into SSM
@author: pclermont
"""
from __future__ import print_function

import json
import re
import codecs
from os import path
from troposphere import Template, Parameter, Ref
from troposphere.constants import STRING
from troposphere.ssm import Document
from troposphere.ssm import Parameter as SSMParameter


def read(*parts):
    """Reads a relative file and returns the content"""
    with codecs.open(
            path.join(
                path.abspath(path.dirname(__file__)),
                *parts
            ), 'r') as _file:
        return _file.read()


def find_version(*file_paths):
    """Retrieves the __version__ value from the package"""
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def main():
    """
    main function
    """
    cf_template = Template()

    cf_template.set_version('2010-09-09')

    update_asg_document = cf_template.add_parameter(
        Parameter(
            'UpdateASG',
            Type='AWS::SSM::Parameter::Value<String>',
            Description=' '.join([
                'ssm parameter that contains the name of the document',
                ' for UpdateASG'
            ]),
            Default='/Documents/SSM/UpdateASG'
        )
    )

    json_file = open(
        path.join(
            path.dirname(__file__),
            'data/ssm_document.json'
        )
    )

    ssm_document_data = json.load(json_file)

    ssm_document_data['mainSteps'][1]['inputs']['DocumentName'] = \
        Ref(update_asg_document)

    ssm_document = cf_template.add_resource(
        Document(
            'AmiAndUpdate',
            Content=ssm_document_data,
            DocumentType='Automation'
        )
    )

    cf_template.add_resource(
        SSMParameter(
            'SSMParameter',
            Type=STRING,
            Name='/Documents/SSM/create_ami_update_asg/Name',
            Value=Ref(ssm_document),
            Description=' '.join([
                'This Value is generated by CloudFormation in order to link'
                'the documents dynamically.'
            ])
        )
    )

    cf_template.add_resource(
        SSMParameter(
            'SSMParameterVersion',
            Type=STRING,
            Name='/Documents/SSM/create_ami_update_asg/Version',
            Value=find_version('__init__.py'),
            Description=' '.join([
                'This Value is generated by CloudFormation in order to link'
                'the documents dynamically.'
            ])
        )
    )

    with open('CloudFormation.json', 'w') as cf_file:
        cf_file.write(cf_template.to_json())


if __name__ == '__main__':
    main()
