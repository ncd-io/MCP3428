// This #include statement was automatically added by the Particle IDE.
#include "MCP3428.h"

MCP3428 adc;

void setup() {
    adc.init();
    Particle.variable("Channel_1", adc.channel_1);
    Particle.variable("Channel_2", adc.channel_2);
    Particle.variable("Channel_3", adc.channel_3);
    Particle.variable("Channel_4", adc.channel_4);
}

void loop() {
    adc.takeReadings();
}
