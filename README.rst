requests-aws-sign
=================

This package allows for AWS V4 request signing using the requests library.

Usage
-----

``AWSV4Sign`` extends requests ``AuthBase``, so usage is simple:

.. code:: python

    import requests
    from requests_aws_sign import AWSV4Sign
    from boto3 import session

    # You must provide a credentials object as per http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials
    # This example attempts to get credentials based upon the local environment
    # e.g. Environment Variables, assume role profiles, EC2 Instance IAM profiles
    session = session.Session()
    credentials = session.get_credentials()

    # You must provide an AWS region
    region = session.region_name or 'ap-southeast-2'

    # You must provide the AWS service.  E.g. 'es' for Elasticsearch, 's3' for S3, etc.
    service = 'es'

    requests.get("https://es-search-domain.ap-southeast-2.es.amazonaws.com/",auth=AWSV4Sign(credentials, region, service))

When signing requests using this package, the following headers are added to the HTTP Request:

- X-Amz-Date
- X-Amz-Security-Token
- Authorization

See `AWS documentation`_ for further information on the signing process.

.. _docs: http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html

Support for STS Assume Role and EC2 IAM Instance Profiles
---------------------------------------------------------

You should use Boto3 to provide your credentials object as demonstrated in the example usage, as it will cache credentials and in the case of assume role profiles and EC2 Instance IAM profile, automatically refresh credentials as required.

Installation
------------

    pip install requests_aws_sign

Requirements
------------

- requests_
- boto3_

.. _requests: https://github.com/kennethreitz/requests/
.. _boto3: https://github.com/boto/boto3

Authors
-------

- `Justin Menga`_

.. _Justin Menga: https://github.com/jmenga