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
  delay(1000);
}

void loop() {
releaseMot();
   Serial.println("WOW");
delay(5000);

}

void releaseMot()
{
    finished=millis();
  elapsed=finished-start;
  start=millis();

  while (elapsed < 2000) {
    int max_mot = 255;
    double prop = 0.6;
    double time = (elapsed+100)/100;
    int value = 255;//prop * max_mot / time + (1-prop)*max_mot;

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
  analogWrite(ENA, 0);
}


