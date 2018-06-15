int analogPin = 0; // read from multiplexer using analog input 0
int strobePin = 2; // strobe is attached to digital pin 2
int resetPin = 3; // reset is attached to digital pin 3
int spectrumValue[7]; // to hold a2d values

int time_1 = 0;

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

  rel.write(15);              // tell servo to go to position in variable 'pos'
  delay(15);
}

void _release()
{
  rel.write(50);              // tell servo to go to position in variable 'pos'
  delay(10000);
  rel.write(15);              // tell servo to go to position in variable 'pos'
  delay(15);


}


void loop()
{
  digitalWrite(resetPin, HIGH);
  digitalWrite(resetPin, LOW);

  for (int i = 0; i < 4; i++)
  {
    digitalWrite(strobePin, LOW);
    delayMicroseconds(20); // to allow the output to settle
    spectrumValue[i] = analogRead(analogPin);
    if (i == 0) {
      //spectrumValue[i] = 0; //blue
      //if (g && o && p)
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
      spectrumValue[i] = 250; //red
    }
    if (i == 2) {
      //spectrumValue[i] = 0; g
      if (spectrumValue[i] < 150)
        g = true;
      else
        g = false;
    }
    if (i == 3) {
      //spectrumValue[i] = 0; o
      if (spectrumValue[i] > 300)// && spectrumValue[i] < 650)
      {
        time_1 += 1;
        o = true;
      }
      else
        time_1 = 0;
        o = false;
    }
    if (i == 4) {
      //spectrumValue[i] = 0; p
      if (spectrumValue[i] > 50 && spectrumValue[i] < 250)
        p = true;
      else
        p = false;
    }
    if (i == 5) {
      spectrumValue[i] = 150; //grey
    }
    if (i == 6) {
      spectrumValue[i] = 50; //t
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
  p = true;
  g = true;
  o = true;
  Serial.print("Times end: ");
  Serial.print(time_1);
  Serial.print(p);
  Serial.print(o);
  Serial.println(g);
  if (g && o && p and time_1 > 140)
  {
    _release();
    time_1 = 0;
  }
  Serial.println();
}
