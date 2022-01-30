from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from . import widget_service

from constructs import Construct

class SampleCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        widget_service.WidgetService(self, "Widgets")
        # widget_service.WidgetService(self, "Widgets")
