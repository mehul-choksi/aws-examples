#!/usr/bin/env python3
import os

import aws_cdk as cdk

from sample_cdk.sample_cdk_stack import SampleCdkStack


app = cdk.App()
SampleCdkStack(app, "SampleCdkStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    env=cdk.Environment(account='ACCOUNT_ID_HERE', region='REGION_HERE'),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
