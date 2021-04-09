from blueqat import Circuit
from bqbraket import convert

from braket.device_schema import GateModelParameters
from braket.device_schema.ionq import IonqDeviceParameters
from braket.device_schema.rigetti import RigettiDeviceParameters
from braket.device_schema.simulators import GateModelSimulatorDeviceParameters

from ..device import Device
from ..task import TaskData


def make_taskdata(c: Circuit, dev: Device, shots: int) -> TaskData:
    action = convert(c).to_ir().json()
    dev_params = make_device_params(c, dev)
    return TaskData(str(dev), action, dev_params, shots)


def make_device_params(c: Circuit, dev: Device) -> str:
    paradigm_params = GateModelParameters(qubitCount=c.n_qubits, disableQubitRewiring=False)
    if "/rigetti/" in str(dev):
        return RigettiDeviceParameters(paradigmParameters=paradigm_params).json()
    if "/ionq/" in str(dev):
        return IonqDeviceParameters(paradigmParameters=paradigm_params).json()
    raise ValueError("Unknown AWS device.")
