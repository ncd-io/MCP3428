import time

MCP3428_ONE_SHOT = 0x00
MCP3428_START_CONVERSION = 0x80

MCP3428_CONTINUOUS_CONVERSION = 0x10

MCP3428_SAMPLE_12_BIT = 0x00
MCP3428_SAMPLE_14_BIT = 0x04
MCP3428_SAMPLE_16_BIT = 0x08

MCP3428_GAIN_1X = 0x00
MCP3428_GAIN_2X = 0x01
MCP3428_GAIN_4X = 0x02
MCP3428_GAIN_8X = 0x03

MCP3428_CHANNEL_1 = 0x00
MCP3428_CHANNEL_2 = 0x20
MCP3428_CHANNEL_3 = 0x40
MCP3428_CHANNEL_4 = 0x60

class MCP3428():
    def __init__(self, smbus, kwargs = {}):
        self.__dict__.update(kwargs)
        if not hasattr(self, 'address'):
            self.address = 0x68
        if not hasattr(self, 'mode'):
            self.mode = MCP3428_CONTINUOUS_CONVERSION
        if not hasattr(self, 'sample_rate'):
            self.sample_rate = MCP3428_SAMPLE_12_BIT
        if not hasattr(self, 'gain'):
            self.gain = MCP3428_GAIN_1X
        if not hasattr(self, 'analog_range'):
            self.analog_range = [0, 11.17]
        self.bits_less = (4-(self.sample_rate/2))
        self.resolution = float(self.analog_range[1] - self.analog_range[0]) / float(65535 >> (self.bits_less + 1))
        self.smbus = smbus

    def take_readings(self):
        readings = []
        for channel in range(0,4):
            readings.append(self.take_single_reading(channel))
        return readings
        
    def take_single_reading(self, channel):
#         TODO SMBus does not currently allow a delay in a read command.
#           It also does not allow a write command to just target a registry.
#           These two things combined have forced an extra byte of 0 to be written with unknown consequence.
        self.smbus.write_byte_data(self.address, self.mode | self.sample_rate | self.gain | (32*channel), 0)
        start = float(time.time())
        while float(time.time() < start+1) :
            if ((self.smbus.read_i2c_block_data(self.address, self.mode | self.sample_rate | self.gain | (32*channel))[2]) & 128) == 0:
                reading = self.smbus.read_i2c_block_data(self.address, self.mode | self.sample_rate | self.gain | (32*channel), 2)
                reading = self.convert_data(reading)
                break
        return reading
        
    def convert_data(self, data):
        raw_data = ((data[0] << 8) + data[1]) & (65535 >> self.bits_less)
        if raw_data > (1 << (16-(self.bits_less+1)))-1:
            raw_data -= ((1 << (16-(2+2)))-1)
#         print 'raw_data'
#         print raw_data
        analog_value = float(raw_data) * float(self.resolution)
#         analog_value = float(raw_data) * float(.01109)
        return analog_value
