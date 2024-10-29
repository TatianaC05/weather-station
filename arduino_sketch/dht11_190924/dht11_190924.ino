/*
Date: 19-09-2024
Developer: Tatiana C.
Sketch description: Get temperature and humidity from DHT11 Sensor
*/
#include "DHT.h"
#define DHTTYPE DHT11
#define DHTPIN 5

float temp = 0;
float hum = 0;

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  dht.begin();
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  delay(1000);
  temp = dht.readTemperature();
  hum = dht.readHumidity();

  if(isnan(temp) || isnan(hum)){
    Serial.println("DHT 11 reading error");
    return;
  }

  Serial.print(temp);
  Serial.print(",");
  Serial.println(hum);

}
