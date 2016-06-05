import boto3

def main():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('airquality')