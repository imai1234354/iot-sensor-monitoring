import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # イベントからデータを取得
    sensor_data = event['sensor_data']
    
    # DynamoDBにデータを保存
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('SensorDataTable')
    
    table.put_item(
        Item={
            'timestamp': datetime.utcnow().isoformat(),
            'sensor_data': sensor_data
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data saved successfully')
    }
