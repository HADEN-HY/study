import smbus
import time

#Sensor Setting
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47

bus = smbus.SMBus(1)
Device_Address = 0x68

def MPU_Init():
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    bus.write_byte_data(Device_Address, CONFIG, 0)
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)
    value = ((high << 8) | low)

   if(value > 32768):
    value = value -65536

    return value

#main

try:
    MPU_Init()
    for i in range(10):
        acc_x = read_raw_data(ACCEL_XOUT_H)
        Ax = acc_/16384.0
        accData = accData + Ax
        accData = accData / 10
        print(accData)
        while True:
            acc_x = read_raw_data(ACCEL_XOUT_H)
            Ax = acc_x / 16384.0
            if Ax - accData >= 0.1:
                print("shock!")
            else:
                pass

except KeyboardInterrupt:
    pass
