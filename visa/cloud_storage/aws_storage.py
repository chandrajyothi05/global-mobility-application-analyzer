import boto3
from io import StringIO
from typing import Union, List
import os,sys
from visa.logger import logging
from visa.exception import USVisaException
from mypy_boto3_s3.service_resource import Bucket
from botocore.exceptions import ClientError
from pandas import DataFrame,read_csv
import pickle

class SimpleStorageService:

    def __init__(self):
        s3_client= S3Client()
        self.s3_resource=s3_client.s3_resource
        self.s3_client=s3_client.s3_client

    def s3_key_path_available(self,bucket_name,s3_key)->bool:
        try:
            bucket=self.get_bucket(bucket_name)