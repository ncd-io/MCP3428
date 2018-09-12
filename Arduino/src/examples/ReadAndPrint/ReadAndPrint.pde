#include <Arduino.h>
#include "MCP3428.h"

MCP3428 adc;

void setup() {
    adc.init();
    Serial.begin(115200);
}

void loop() {
    adc.takeReadings();
	Serial.println();
	Serial.print("Channel 1: ");
	Serial.println(adc.channel_1);
	Serial.print("Channel 2: ");
	Serial.println(adc.channel_2);
	Serial.print("Channel 3: ");
	Serial.println(adc.channel_3);
	Serial.print("Channel 4: ");
	Serial.println(adc.channel_4);
}
