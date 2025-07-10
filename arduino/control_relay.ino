#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
int relayPin = 3;

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(relayPin, OUTPUT);
}

void loop() {
  float temp = dht.readTemperature();
  if (Serial.available()) {
    char cmd = Serial.read();
    digitalWrite(relayPin, cmd == '1' ? HIGH : LOW);
  }
  Serial.println(temp);
  delay(2000);
}
