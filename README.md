# IoTセンサーデータモニタリングシステム

このプロジェクトは、AWSサービスを使用してIoTデバイスからデータを収集し、リアルタイムでモニタリングする方法を示します。

## 使用技術

- AWS IoT
- AWS Lambda
- Amazon DynamoDB
- Amazon QuickSight


## セットアップ手順

1. リポジトリをクローンします:
    ```
    git clone <リポジトリURL>
    cd iot-sensor-monitoring
    ```

2. DynamoDBテーブルの作成:
    - AWSコンソールにログインし、DynamoDBテーブルを作成します。
    - テーブル名: `SensorDataTable`
    - プライマリキー: `timestamp`（文字列）

3. Lambda関数のデプロイ:
    - AWS Lambdaコンソールで新しい関数を作成します。
    - `lambda_function.py`のコードを関数にコピーします。
    - `boto3`ライブラリを含むLambdaレイヤーを作成して関数にアタッチします。

4. AWS IoTの設定:
    - AWS IoTコンソールで新しいデバイスを作成し、証明書を取得します。
    - IoTルールを作成し、デバイスから送信されたデータをLambda関数に送信します。

5. データの可視化:
    - Amazon QuickSightでDynamoDBテーブルからデータセットを作成し、データを可視化します。

## 使用方法

- IoTデバイスがセンサーデータをAWS IoTに送信します。
- AWS IoTルールに基づいて、データがLambda関数に転送されます。
- Lambda関数がデータを処理してDynamoDBに保存します。
- Amazon QuickSightでデータを可視化してモニタリングします。



