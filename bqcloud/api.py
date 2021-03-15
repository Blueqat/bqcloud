import json
import os
import urllib.request
from typing import Any

API_ENDPOINT = "https://cloudapi.blueqat.com/v1/"

class Api:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def post_request(self, path: str, body: Any) -> Any:
        headers = {
            'Content-Type': 'application/json',
            'X-Api-Key': self.api_key,
        }
        req = urllib.request.Request(
            API_ENDPOINT + path, json.dumps(body).encode(), headers)
        with urllib.request.urlopen(req) as res:
            body = res.read()
        return json.loads(body)

    def save_api(self) -> None:
        d = os.path.join(os.environ["HOME"], ".bqcloud")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "api_key"), "w") as f:
            f.write(self.api_key)

    def credit(self) -> str:
        path = "credit/get"
        return self.post_request(path, {})["amount"]


def load_api():
    with open(os.path.join(os.environ["HOME"], ".bqcloud/api_key")) as f:
        return Api(f.read().strip())
