import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (aws_apigateway as api_gateway, aws_s3 as s3,aws_lambda as lambda_)

class WidgetService(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        bucket = s3.Bucket(self, "WidgetStore")

        handler = lambda_.Function(self, "WidgetHandler",
                    runtime=lambda_.Runtime.NODEJS_14_X,
                    code=lambda_.Code.from_asset("resources"),
                    handler="widgets.main",
                    environment=dict(
                    BUCKET=bucket.bucket_name)
                    )

        bucket.grant_read_write(handler)

        api = api_gateway.RestApi(self, "widgets-api",
                  rest_api_name="Widget Service",
                  description="This service serves widgets.")

        get_widgets_integration = api_gateway.LambdaIntegration(handler,
                request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", get_widgets_integration)   # GET /