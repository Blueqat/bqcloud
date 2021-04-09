from enum import Enum


class Device(Enum, str):
    IonQDevice = "aws/ionq/ionQdevice"
    Aspen8 = "aws/rigetti/aspen-8"
    Aspen9 = "aws/rigetti/aspen-9"
