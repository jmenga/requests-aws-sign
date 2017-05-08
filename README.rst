requests-aws-sign
=================

This package allows for AWS V4 request signing using the requests library.

Usage
-----

This package provides the ``AWSV4Sign`` class, which extends requests ``AuthBase``:

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

    url = "https://es-search-domain.ap-southeast-2.es.amazonaws.com/"
    auth=AWSV4Sign(credentials, region, service)
    response = requests.get(url, auth=auth)

When signing requests using this package, the following headers are added to the HTTP Request:

- X-Amz-Date
- X-Amz-Security-Token
- Authorization

See `AWS documentation`_ for further information on the signing process.

.. _AWS documentation: http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html

AWS Services
^^^^^^^^^^^^

To obtain a list of services to pass in the signing request, you can call the Boto3 session :code:`get_available_services()` function:

.. code:: python
  
  >>> import boto3
  >>> boto3.session.Session().get_available_services()
  ['acm', 'apigateway', 'application-autoscaling', 'autoscaling', 'cloudformation', 'cloudfront', 'cloudhsm', 
   'cloudsearch', 'cloudsearchdomain', 'cloudtrail', 'cloudwatch', 'codecommit', 'codedeploy', 'codepipeline', 
   'cognito-identity', 'cognito-idp', 'cognito-sync', 'config', 'datapipeline', 'devicefarm', 'directconnect', 
   'discovery', 'dms', 'ds', 'dynamodb', 'dynamodbstreams', 'ec2', 'ecr', 'ecs', 'efs', 'elasticache', 
   'elasticbeanstalk', 'elastictranscoder', 'elb', 'emr', 'es', 'events', 'firehose', 'gamelift', 'glacier', 'iam', 
   'importexport', 'inspector', 'iot', 'iot-data', 'kinesis', 'kms', 'lambda', 'logs', 'machinelearning', 
   'marketplacecommerceanalytics', 'meteringmarketplace', 'opsworks', 'rds', 'redshift', 'route53', 'route53domains', 
   's3', 'sdb', 'ses', 'sns', 'sqs', 'ssm', 'storagegateway', 'sts', 'support', 'swf', 'waf', 'workspaces']

Note that there is an unlisted service 'execute-api' used for Signing API Gateway requests - see below. 

Support for STS Assume Role and EC2 IAM Instance Profiles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You should use Boto3 to provide your credentials object as demonstrated in the example usage, as it will cache credentials and in the case of assume role profiles and EC2 Instance IAM profiles, automatically refresh credentials as required.

Elasticsearch Usage Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    import requests
    from requests_aws_sign import AWSV4Sign
    from boto3 import session
    from elasticsearch import Elasticsearch, RequestsHttpConnection

    # Establish credentials
    session = session.Session()
    credentials = session.get_credentials()
    region = session.region_name or 'ap-southeast-2'

    # Elasticsearch settings
    service = 'es'
    es_host = "https://es-search-domain.ap-southeast-2.es.amazonaws.com/"
    auth=AWSV4Sign(credentials, region, service)
    es_client = Elasticsearch(host=es_host,
                              port=443,
                              connection_class=RequestsHttpConnection,
                              http_auth=auth,
                              use_ssl=True,
                              verify_ssl=True)
    print es_client.info()


Signing API Gateway requests
----------------------------

API Gateway is an AWS service that lets you create and publish your own REST APIs. API Gateway gives you the option of `Authorizing access to your own API endpoints using IAM <http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html>`_. You can use this library to sign requests to API Gateway.

.. code:: python

    import requests
    from requests_aws_sign import AWSV4Sign
    from boto3 import session
    from elasticsearch import Elasticsearch, RequestsHttpConnection

    # Establish credentials
    session = session.Session()
    credentials = session.get_credentials()
    region = session.region_name or 'ap-southeast-2'

    # API Gateway execute settings
    uri = "https://<my-api-gw-endpoint>.execute-api.ap-southeast-2.amazonaws.com/Prod" + "/test"
    headers={"Content-Type":"application/json"}
    payload = "{}" 
    service = 'execute-api'
    auth=AWSV4Sign(credentials, region, service)
    response = requests.post(uri, auth=auth, headers=headers,json=payload)


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
