from enum import Enum


class Device(str, Enum):
    Local = "local"
    IonQDevice = "aws/ionq/ionQdevice"
    AspenM2 = "aws/rigetti/Aspen-M-2"
    SimSv1 = "aws/amazon/sv1"
    SimTn1 = "aws/amazon/tn1"
    SimDm1 = "aws/amazon/dm1"
