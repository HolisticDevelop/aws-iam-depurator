#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_iam_cleaner.lambda_dynamodb_stack import CdkLambdaDynamoDBStack

app = cdk.App()
env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region='us-east-1')
stack1 = CdkLambdaDynamoDBStack(app, "CdkLambdaDynamoDBStack",
                                env=env)

app.synth()
