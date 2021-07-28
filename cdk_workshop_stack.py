from aws_cdk import (

    aws_s3 as _s3,
    core
)

class CdkWorkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        my_bucket = _s3.Bucket(self, id = 's3bucket', bucket_name = 'bucketcdk')