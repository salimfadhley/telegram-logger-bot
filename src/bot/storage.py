import functools
import os
from typing import IO


from boto3_type_annotations.s3 import ServiceResource, Bucket

import boto3

@functools.lru_cache()
def get_bucket_name()->str:
    return os.environ["BUCKET_NAME"]

@functools.lru_cache()
def get_resource()->ServiceResource:
    return boto3.resource('s3')

@functools.lru_cache()
def get_bucket()->Bucket:
    resource:ServiceResource = get_resource()
    bucket_name:str = get_bucket_name()
    bucket = resource.Bucket(bucket_name)
    bucket.create()
    return bucket

def store_object(file_name:str, file_obj:IO[bytes]):
    bucket = get_bucket()
    bucket.upload_fileobj(
        Fileobj=file_obj,
        Key=file_name
    )
