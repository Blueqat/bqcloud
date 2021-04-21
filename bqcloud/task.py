"""Module for task."""
from time import sleep
import typing
from typing import List, Optional, SupportsIndex, overload

from .data import Status, TaskData, TaskListData
if typing.TYPE_CHECKING:
    from .api import Api
    from .abstract_result import AbstractResult


class Task:
    """Task."""
    def __init__(self,
                 api: 'Api',
                 taskdata: TaskData,
                 result: Optional[AbstractResult] = None) -> None:
        self._api = api
        self.taskdata = taskdata
        self.resultdata = result

    def status(self) -> Status:
        return self._api.status(self.taskdata.id)

    def update(self) -> None:
        # TODO: Implement
        pass

    def __repr__(self) -> str:
        return f'Task({repr(self._api)}, {self.taskdata}, {self.resultdata})'

    def wait(self, timeout: int = 0) -> None:  # TODO: return result
        waiting_time = 5
        elipsed = 0
        while self.status().is_done():
            t = min(timeout - waiting_time, waiting_time)
            sleep(t)
            elipsed += t
            if timeout > 0 and elipsed > timeout:
                return None
        return None  # TODO: return result


class TaskList:
    """Task list."""
    def __init__(self, api: 'Api', tasklist: TaskListData,
                 group: Optional[str], index: int, per: Optional[int],
                 option_fields: Optional[str]) -> None:
        self._api = api
        self.tasklist = tasklist
        self.group = group
        self.index = index
        self.per = per
        self.option_fields = option_fields

    @property
    def count(self) -> int:
        """Returns count of tasklist. It may larger than length of TaskList."""
        return self.tasklist.count

    @overload
    def __getitem__(self, idx: SupportsIndex) -> Task:
        ...

    @overload
    def __getitem__(self, idx: slice) -> List[Task]:
        ...

    def __getitem__(self, idx):
        if isinstance(idx, SupportsIndex):
            return Task(self._api, self.tasklist.tasks[idx])
        if isinstance(idx, slice):
            return [Task(self._api, task) for task in self.tasklist.tasks[idx]]
        raise TypeError(
            f'TypeList indices must be integer or slices, not {type(idx)}')

    def __len__(self) -> int:
        return len(self.tasklist.tasks)

    def __bool__(self) -> bool:
        return bool(self.tasklist)

    def nextpage(self) -> 'TaskList':
        """Get next page of task list."""
        return self._api.tasks(group=self.group,
                               index=self.index + 1,
                               per=self.per,
                               option_fields=self.option_fields)


class TaskIter:
    """Paginator of tasks."""
    def __init__(self, api: 'Api', group: Optional[str], index: int,
                 per: Optional[int], option_fields: Optional[str]) -> None:
        self.tasklist = api.tasks(group=group,
                                  index=index,
                                  per=per,
                                  option_fields=option_fields)
        self.next_i = 0

    def __iter__(self) -> 'TaskIter':
        return self

    def __next__(self) -> Task:
        try:
            task = self.tasklist[self.next_i]
        except IndexError:
            self.tasklist = self.tasklist.nextpage()
            self.next_i = 0
            if len(self.tasklist) > 0:
                task = self.tasklist[self.next_i]
            else:
                raise StopIteration
        self.next_i += 1
        return task
