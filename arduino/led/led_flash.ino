void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(10, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(10, HIGH);  // turn the LED at Pin 9 on (HIGH is the voltage level)
  delay(250);                      // wait for 250ms
  digitalWrite(10, LOW);   // turn the LED at Pin 9 off by making the voltage LOW
  delay(250);                      // wait for 250ms
}
