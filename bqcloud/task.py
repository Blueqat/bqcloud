"""Module for task."""
from .api import Api
from dataclasses import dataclass


@dataclass
class TaskData:
    device: str
    action: str
    deviceParameters: str
    shots: int


class Task:
    """Task."""
    def __init__(self, api: Api, taskdata: TaskData):
        self._api = api
        self.taskdata = taskdata

    def detail(self):
        """This method may be changed."""
        path = "quantum-tasks/get"
        body = {
            "id": self.data['id'],
        }
        return self._api.post_request(path, body)
