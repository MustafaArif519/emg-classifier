//https://github.com/AdvancerTechnologies/MyoWare_MuscleSensor/blob/master/Example%20Code/ReadAnalogVoltage/ReadAnalogVoltage.ino

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {

  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);

  float mtime = millis();
  float voltage = sensorValue * (5.0 / 1023.0);
  Serial.println(voltage);  
}
