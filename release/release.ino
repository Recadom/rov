#include <Servo.h>

int IN1=4;
int IN2=5;
int ENA=3;

unsigned long start, finished, elapsed;

void setup()
{
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  finished=millis();
  elapsed=finished-start;
  start=millis();

  while (elapsed < 1000) {


    int max_mot = 255;
    int prop = 0.4;
    int time = elapsed/100;
    int value = prop*max_mot / (time) + (1-prop)*max_mot;

    Serial.println(value);

    if (value == 0) {
      analogWrite(ENA, 0);
    }
    else if (value > 0) {
      analogWrite(ENA, abs(value));  // motor speed
      digitalWrite(IN1, LOW); // rotate forward
      digitalWrite(IN2, HIGH);
    }
    else if (value < 0) {
      analogWrite(ENA, abs(value)); // motor speed
      digitalWrite(IN1, HIGH); // rotate reverse
      digitalWrite(IN2, LOW);
    }

    finished=millis();
    elapsed=finished-start;
  }
}



