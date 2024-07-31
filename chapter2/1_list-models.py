# AWS SDKを用いて各モデルのAPIへリクエストを行う
# Pyhton外部モジュールのインポート
import boto3

# Bedrockクライアントの作成
bedrock = boto3.client("bedrock")

# モデル一覧取得APIの呼び出し
result = bedrock.list_foundation_models()

# 結果をコンソールに表示
print(result)
