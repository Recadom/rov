#include <Servo.h>

Servo rel;

const int REED_PIN = 2; // Pin connected to reed switch
const int LED_PIN = 13; // LED pin - active-high
int pos = 0; 

void setup() 
{
  //Serial.begin(9600);
  rel.attach(9);
  // Since the other end of the reed switch is connected to ground, we need
  // to pull-up the reed switch pin internally.
  pinMode(REED_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
  //rel.write(0);
  //for (pos = 0; pos <= 115; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    rel.write(15);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  //}
}

void loop() 
{
  int proximity = digitalRead(REED_PIN); // Read the state of the switch
  if (proximity == LOW) // If the pin reads low, the switch is closed.
  {
    //Serial.println("Switch closed");
    digitalWrite(LED_PIN, HIGH); // Turn the LED on
    //for (pos = 115; pos >= 95; pos -= 1) { // goes from 180 degrees to 0 degrees
      rel.write(50);              // tell servo to go to position in variable 'pos'
      delay(15);                       // waits 15ms for the servo to reach the position
    //}
    delay(10000);

  }
  else
  {
    digitalWrite(LED_PIN, LOW); // Turn the LED off
    rel.write(15);

  }
}



