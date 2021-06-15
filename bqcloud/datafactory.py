"""Module for making Task and TaskData.

This module is for internal use.
"""
import typing
from typing import Any, Dict, Optional

from .device import Device
from .device_specific import aws_device
from .data import ExecutionRequest

if typing.TYPE_CHECKING:
    from blueqat import Circuit
    from .abstract_result import AbstractResult
    from .api import Api


def make_executiondata(c: 'Circuit',
                       dev: Device,
                       shots: int,
                       group: Optional[str] = None,
                       send_email: bool = False,
                       options: Optional[Dict[str, Any]] = None) -> ExecutionRequest:
    """Make ExecutionData for send job to the server."""
    if options is None:
        options = {}
    if dev.value.startswith("aws/"):
        return aws_device.make_executiondata(c, dev, shots, group, send_email, options)
    raise ValueError(f"Cannot make {str(dev)} device task")


def make_result(data: Dict[str, Any],
                dev: Device) -> Optional['AbstractResult']:
    if not data:
        return None
    if dev.value.startswith("aws/"):
        return aws_device.make_result(data, dev)
    raise ValueError(f"Cannot make {str(dev)} result")
