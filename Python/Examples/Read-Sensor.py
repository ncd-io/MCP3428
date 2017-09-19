import time
import smbus
import mcp3428
# Get I2C bus, this is I2C Bus 1
bus = smbus.SMBus(1)

#kwargs is a Python set that contains the address of your device as well as additional device and calibration values.
#kwargs does not have to be populated as every value is optional and will be replaced with a default value if not is specified.

#below is an example of a kwarg declaration that is populated with all of the default values for each user configurable property
#refer to the datasheet for this chip to calculate what values you should be using for your project.
kwargs = {'address': 0x68, 'mode': 0x10, 'sample_rate': 0x00, 'gain': 0x00}
#create the MCP3428 object from the MCP3428 library
#the object requires that you pass it the bus object so that it can communicate and share the bus with other chips if necessary
mcp3428 = mcp3428.MCP3428(bus, kwargs)

while True :
#     Get the readings on all channel in an array
    all_readings = mcp3428.take_readings()
    print 'All Readings:'
    print all_readings
    print '---'
    for reading in all_readings:
        print reading
#     Get the reading on just on channel, channel 0 is the first channel on the device.
    print 'Channel 0 reading: '
    print mcp3428.take_single_reading(0)
    print '\r\n'
    time.sleep(.25)
