//Spring valve model on https://github.com/sinfuls-acedia/opnsrc/blob/main/model/SprVlv_WtrDisp.f3d

#include <Servo.h> //sets code to use the Servo.h library

//creates servo obj
Servo myservo1;
Servo myservo2;

//define constants
const int poscls1 = <clsangle>;
const int posopn1 = <opnangle>;
const int poscls2 = <clsangle>;
const int posopn2 = <opnangle>;
const int trigPin = <pin>;
const int echoPin = <pin>;

//define vars
long duration;
int distance;

void setup() {
  myservo1.attach(<pin>); //associates pin to data channel for servo 1 (Gate Valve)
  myservo2.attach(<pin>); //associates pin to data channel for servo 2 (Spring Valve)
  pinMode(trigPin, OUTPUT); //sets trigger pin to output
  pinMode(echoPin, INPUT); //sets echo pin to input
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW); //clears out the ultrasonic sensor
  
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2; //calculation of distance
  
  Serial.print("Distance: ");
  Serial.println(distance); //debug layer

  if(distance <=10){
    myservo2.write(posopn2); //closes spring valve
    delay(50);
    myservo1.write(posopn1); //open gate valve
  }
  else if(distance >10){
    myservo1.write(poscls1); //close gate valve
    myservo2.write(poscls2); //open spring valve
    }
}
