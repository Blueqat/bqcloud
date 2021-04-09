from typing import Optional
from blueqat import Circuit
from .device import Device
from .device_specific import aws_device
from .task import TaskData

def make_taskdata(c: Circuit, dev: Device, shots: int, group: Optional[str]) -> TaskData:
    if str(dev).startswith("aws/"):
        return aws_device.make_taskdata(c, dev, shots, group)
    raise ValueError(f"Cannot make {str(dev)} device task")
