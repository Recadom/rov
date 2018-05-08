int analogPin = 0; // read from multiplexer using analog input 0
int strobePin = 2; // strobe is attached to digital pin 2
int resetPin = 3; // reset is attached to digital pin 3
int spectrumValue[7]; // to hold a2d values
bool g = false, o = false, p = false;
#include <Servo.h> 
Servo rel;

unsigned int time = 0;

void setup()
{
 Serial.begin(9600);
 pinMode(analogPin, INPUT);
 pinMode(strobePin, OUTPUT);
 pinMode(resetPin, OUTPUT);
 analogReference(DEFAULT);

 digitalWrite(resetPin, LOW);
 digitalWrite(strobePin, HIGH);
 rel.attach(9); 

 Serial.println("MSGEQ7 test by J Skoba");
}

void _release()
{
  int pos = 0;
   for(pos = 90; pos < 115; pos += 1)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 1 degree 
    rel.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 
  delay(1000);
  for(pos = 115; pos>=89; pos-=1)     // goes from 180 degrees to 0 degrees 
  {                                
    rel.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 
  delay(1000);
}


void loop()
{
 digitalWrite(resetPin, HIGH);
 digitalWrite(resetPin, LOW);

 for (int i = 0; i < 7; i++)
 {
 digitalWrite(strobePin, LOW);
 delayMicroseconds(30); // to allow the output to settle
 spectrumValue[i] = analogRead(analogPin);
  if (i == 0) {
    //spectrumValue[i] = 0; //blue
    if (g && o && p)
      spectrumValue[i] = 50;
      ++time;
      if (time > 100) {
        _release();
      }
      
     else {
       spectrumValue[i] = 0;
       if (time)
         --time;
     }
  }
  if (i == 1) {
    spectrumValue[i] = 400; //red
  }
  if (i == 2) {
    //spectrumValue[i] = 0; g
    if (spectrumValue[i] > 350)
      g = true;
    else
      g = false;
  }
  if (i == 3) {
    //spectrumValue[i] = 0; o
    if (spectrumValue[i] > 350 && spectrumValue[i] < 650)
      o = true;
    else
      o = false;
  }
  if (i == 4) {
    //spectrumValue[i] = 0; p
    if (spectrumValue[i] > 125 && spectrumValue[i] < 275)
      p = true;
    else
      p = false;
  }
  if (i == 5) {
    spectrumValue[i] = 275; //grey
  }
  if (i == 6) {
    spectrumValue[i] = 125; //t
  }

  //spectrumValue[i] = i * 100;
  
 // comment out/remove the serial stuff to go faster
 // - its just here for show
 /*if (spectrumValue[i] < 10)
 {
 Serial.print(" ");
 Serial.print(spectrumValue[i]);
 }
 else if (spectrumValue[i] < 100 )
 {
 Serial.print(" ");
 Serial.print(spectrumValue[i]);
 }
 else
 {*/
 Serial.print(" ");
 Serial.print(spectrumValue[i]);
 //}

 digitalWrite(strobePin, HIGH);
 }
 Serial.println();
}
