int led1 = 9;
int led2 = 10;
int led3 = 11;
int buttonPin = 2

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
}

// the loop function runs over and over again forever
void loop() {
  int sensorVal = digitalRead(2);
  Serial.println(sensorVal);

  if (sensorVal == HIGH) {
  digitalWrite(led1, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(50);
  digitalWrite(led2, HIGH);
  delay(50);
  digitalWrite(led3, HIGH);
  delay(50);
  digitalWrite(led1, LOW);  // turn the LED off (LOW is the voltage level)
  delay(50);
  digitalWrite(led2, LOW);
  delay(50);
  digitalWrite(led3, LOW);
  delay(50);
} else {
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
}
}
