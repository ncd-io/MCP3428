

# About

This Library is intended for use with any MCP3428  board available from ncd.io

### Developer information
NCD has been designing and manufacturing computer control products since 1995.  We have specialized in hardware design and manufacturing of Relay controllers for 20 years.  We pride ourselves as being the industry leader of computer control relay products.  Our products are proven reliable and we are very excited to support Particle.  For more information on NCD please visit ncd.io

### Requirements
- The Python SMBus Module: https://pypi.python.org/pypi/smbus-cffi/
- An I2C connection to MCP3428 board
- Knowledge base for developing and programming with Python.

### Version
1.0.0

### How to use this library

The libary must be imported into your application and an I2C bus must be created with the SMBus module.

Once the library is imported and the I2C Bus created you can create a MCP3428 object, pass it the I2C Bus and start to communicate to the chip.  You can optionally pass in a kwarg to the object that contains many configuration options such as mode, sample_rate, gain, and analog_range. Analog range is the most important as it defines if you have a 0-10v sensor, 4-20mA, or any other. The values passed won't be an exact match to what the board says it is as we put a safety buffer to keep the inputs from taking too much power. For instance a 0-10 is actually 0-11.17 and 0-20 will actually be 0-20.18.

The default values for these configuration option are:
{'address': 0x68, 'mode': 0x10, 'sample_rate': 0x08, 'gain': 0x00, 'analog_range': [0, 11.17]}

### Publicly accessible methods
```cpp
take_readings()
```
>This function returns all of the readings on all of the channel in an array.

```cpp
take_single_reading()
```
>This function returns a single reading on a single channel. This will return a float value.
