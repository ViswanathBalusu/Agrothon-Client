#include <DHT.h>
// Sensor defiitions
int sensor_pin = A0;
int moisture;
#define DHTPIN 5        // DHT data pin connected to Arduino pin 5
#define DHTTYPE DHT11   // DHT 22 (if your sensor is the DHT 11, only change this line by: #define DHTTYPE DHT11) 
// Variables to be used by Sensor
float tempDHT; // on the final program we will use int insteady of float. No need for high precision measurements 
float humDHT;
// Initialize the DHT sensor
DHT dht(DHTPIN, DHTTYPE); 
void setup() 
{
  Serial.begin(9600); 
  dht.begin();
}
void loop() 
{
  // Wait a few seconds between measurements.
  delay(20000);
  
  //Read temperature and humidity values from DHT sensor:
  moisture = analogRead(sensor_pin);
  moisture = map(moisture,900,190,0,100);
  tempDHT = dht.readTemperature();   
  humDHT = dht.readHumidity();
  // Check if any reads failed and exit early (to try again).
  if (isnan(humDHT) || isnan(tempDHT)) 
  {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
//  // Show measurements at Serial monitor:
 Serial.print(moisture);
 Serial.print(",");
 Serial.print(tempDHT);
 Serial.print(",");
 Serial.println(humDHT);
}
