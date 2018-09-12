#include <Arduino.h>
#include <Wire.h>
#include "MCP3428.h"

void MCP3428::init(){
}

void MCP3428::init(bool a){
    if(a){
        Wire.begin();
    }
}

void MCP3428::setAddress(int a0, int a1){
    if((a0 & a1) == 0 || (a0 & a1) == 2) return;

    if(a0 == 2 || (a0==0 && a1==2)) address |= 4;

    if(a1 == 2 || (a1==1 && a0 == 0)) address |= 2;

    if(a1 == 0 || a0 == 0) address |= 1;
}

unsigned long last_checked =0;
void MCP3428::takeReadings(){
    unsigned long now = millis();
    if(now-last_checked > 1000){

        last_checked = now;

        int data[2];
        readChannel(MCP3428_CHANNEL_1, data, 2);
        channel_1 = convertData(data);

        readChannel(MCP3428_CHANNEL_2, data, 2);
        channel_2 = convertData(data);

        readChannel(MCP3428_CHANNEL_3, data, 2);
        channel_3 = convertData(data);

        readChannel(MCP3428_CHANNEL_4, data, 2);
        channel_4 = convertData(data);
    }


}

int MCP3428::convertData(int *data){
    int bits_less = (4-(sample_rate/2));
    int val = ((data[0] << 8) + data[1]) & (65535 >> bits_less);
    if(val > (1 << (16-(bits_less+1)))-1){
        val -= ((1 << (16-(2+2)))-1);
    }
    return val;
}

void MCP3428::readChannel(int channel, int *bytes, int length){
    Wire.beginTransmission(address);
    Wire.write(mode | sample_rate | gain | channel);
    Wire.endTransmission();

    delay(100);


    Wire.requestFrom(address, length);
    for(int i=0;i<length;i++){
        bytes[i] = Wire.read();
    }
}
