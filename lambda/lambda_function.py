import json

def lambda_handler(event, context):
    # TODO implement
    # 第2次修改
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Github3!')
    }
