void setup() {
  Serial.begin(9600);
}

void loop() {
  float voltage = analogRead(A0) * (5.0 / 1023.0) * 220;
  float current = analogRead(A1) * (5.0 / 1023.0) * 5;
  float power = voltage * current;

  Serial.print(voltage);
  Serial.print(",");
  Serial.print(current);
  Serial.print(",");
  Serial.println(power);

  delay(1000);
}
