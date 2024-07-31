# AWS SDKを用いて各モデルのAPIへリクエストを行う
# 現在のリージョンで使用可能な基盤モデル一覧を取得

# Pyhton外部モジュールのインポート
import boto3

# Bedrockクライアントの作成
bedrock = boto3.client("bedrock")

# モデル一覧取得APIの呼び出し
result = bedrock.list_foundation_models()

# 結果をコンソールに表示
print(result)
