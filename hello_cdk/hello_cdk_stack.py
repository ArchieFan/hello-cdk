from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_s3 as s3
) 
import aws_cdk as cdk
from constructs import Construct

class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _lambda.Function(
            self,
            'DemoHandler',
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset('lambda'),
            handler='handler.handle'
        )
        
        bucket = s3.Bucket(
            self, 
            "MyFirstBucket", versioned=True,
            removal_policy = cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True)
        
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "HelloCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        

        
