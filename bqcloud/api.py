"""Module for manage API"""
import json
import os
import urllib.request
from typing import Any, List

from .task import Task

API_ENDPOINT = "https://cloudapi.blueqat.com/v1/"


class Api:
    """Manage API and post request."""
    def __init__(self, api_key: str):
        self.api_key = api_key

    def post_request(self, path: str, body: Any) -> Any:
        """Post request."""
        headers = {
            'Content-Type': 'application/json',
            'X-Api-Key': self.api_key,
        }
        req = urllib.request.Request(API_ENDPOINT + path,
                                     json.dumps(body).encode(), headers)
        with urllib.request.urlopen(req) as res:
            body = res.read()
        return json.loads(body)

    def save_api(self) -> None:
        """Save API to file."""
        d = os.path.join(os.environ["HOME"], ".bqcloud")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "api_key"), "w") as f:
            f.write(self.api_key)

    def credit(self) -> str:
        """Get credit."""
        path = "credit/get"
        return self.post_request(path, {})["amount"]

    def tasks(self, index: int) -> List[Task]:
        """Get tasks."""
        path = "quantum-tasks/list"
        body = {
            "index": index,
        }
        tasks = self.post_request(path, body)
        assert isinstance(tasks, list)
        return [Task(self, **task) for task in tasks]


def load_api() -> Api:
    """Load API from file."""
    with open(os.path.join(os.environ["HOME"], ".bqcloud/api_key")) as f:
        return Api(f.read().strip())


def register_api(api_key: str) -> Api:
    """Save and return API."""
    api = Api(api_key)
    api.save_api()
    return api
