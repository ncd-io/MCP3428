#define MCP3428_ONE_SHOT 0x00
#define MCP3428_START_CONVERSION 0x80

#define MCP3428_CONTINUOUS_CONVERSION 0x10

#define MCP3428_SAMPLE_12_BIT 0x00
#define MCP3428_SAMPLE_14_BIT 0x04
#define MCP3428_SAMPLE_16_BIT 0x08

#define MCP3428_GAIN_1X 0x00
#define MCP3428_GAIN_2X 0x01
#define MCP3428_GAIN_4X 0x02
#define MCP3428_GAIN_8X 0x03

#define MCP3428_CHANNEL_1 0x00
#define MCP3428_CHANNEL_2 0x20
#define MCP3428_CHANNEL_3 0x40
#define MCP3428_CHANNEL_4 0x60

class MCP3428{
public:
	void init();
    void init(bool a);
    void setAddress(int a0, int a1);

    int address = 0x68;
    int sample_rate = MCP3428_SAMPLE_12_BIT;
    int gain = MCP3428_GAIN_1X;
    int mode = MCP3428_CONTINUOUS_CONVERSION;

    void takeReadings();
    int convertData(int *data);
    void readChannel(int channel, int *bytes, int length);

    int channel_1;
    int channel_2;
    int channel_3;
    int channel_4;
};
