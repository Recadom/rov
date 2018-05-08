#include <Wire.h>
#include <Servo.h>
Servo claw;

//int speaker_pin = 3;
int in1 = 12;
int in2 = 13;
int adc_id = 0; // Water level
int HistoryValue = 0;
char printBuffer[128];
int clawSpeed;

#define SLAVE_ADDRESS 0x04

// define motor pins
byte pin_forwLeft = 11;
byte pin_forwRight = 10;
byte pin_vertLeft = 5;
byte pin_vertRight = 6;

int prevSignals[5] = { 
  64 };
int Signals[5] = { 
  64 };

/* define claw pins
 int IN1=4;
 int IN2=2;
 int ENA=8;
 */

// start servos
Servo forwLeft;
Servo forwRight;
Servo vertLeft;
Servo vertRight;

void setup()
{
  //Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);      // join i2c bus with address #4
  Wire.onReceive(receiveEvent);   // register event

    // attatch all the motors to their pins
  forwLeft.attach(pin_forwLeft);
  forwRight.attach(pin_forwRight);
  vertLeft.attach(pin_vertLeft);
  vertRight.attach(pin_vertRight);

  //set all the motors to an off state
  forwLeft.writeMicroseconds(1500);
  forwRight.writeMicroseconds(1500);
  vertLeft.writeMicroseconds(1500);
  vertRight.writeMicroseconds(1500);

  /*set up claw
   pinMode(IN1,OUTPUT);
   pinMode(IN2,OUTPUT);*/

  claw.attach(9); 

  pinMode(in1, OUTPUT);
  digitalWrite(in1, HIGH);

  pinMode(in2, OUTPUT);
  digitalWrite(in2, HIGH);

  delay(1000); // delay to allow the ESC to recognize the stopped signal
}

bool equals(int a[5], int b[5]) {
  for (int x=0; x<5; ++x) {
    if (a[x] != b[x]) {
      return false;
    }
  }
  return true;
}

void receiveEvent(int bytes) {
  int x;
  while (Wire.available()) {
    x = Wire.read();    // read one character from the I2C
  }

  static byte mot = 0;

  if (x == 0) {
    mot = 0;
    if (equals(prevSignals, Signals)) {
      for (int i = 0; i < 5; ++i)
        motor(Signals[i], i);
    }
    for (int y=0; y<5; ++y) {
      prevSignals[y] = Signals[y];
    }

  }
  else {
    switch (mot) {
    case 0:
      {
        Signals[0] = x;
        mot = 1;
        break;
      }

    case 1:
      {
        Signals[1] = x;
        mot = 2;
        break;
      }

    case 2:
      {
        Signals[2] = x;
        mot = 3;
        break;
      }

    case 3:
      {
        Signals[3] = x;
        mot = 4;
        break;
      }

    case 4:
      {
        Signals[4] = x;
        mot = 0;
        break;
      }

    }
  }

}
/*else
 {
 noTone(8);
 }*/


void motor(int x, int mot) {

  //static byte mot = 0;    // create a number that will rememember its last value
  /*Serial.print(mot);
   Serial.print('\t');
   Serial.print(x);
   Serial.print('\n');*/
  //if (x == 0) {
  //  mot = 0;
  //  return;
  //}
  int state = (x - 64) * 200 / 63 + 1500;    //convert from 0-127 to 1100-1900 *now speed is halfed

  // iterate to next motor after every signal
  switch (mot) {
  case 0:
    {
      forwLeft.writeMicroseconds(state);
      //mot = 1;
      break;
    }

  case 1:
    {
      forwRight.writeMicroseconds(state);
      //mot = 2;
      break;
    }

  case 2:
    {
      vertLeft.writeMicroseconds(state);
      //mot = 3;
      break;
    }

  case 3:
    {
      vertRight.writeMicroseconds(state);
      //mot = 4;
      break;
    }

  case 4:
    {
      //vertRight.writeMicroseconds(state);
      int clawSpeed = 45 - abs(x - 64) * 45 / 64;
      claw.write(clawSpeed);
      /*if (clawSpeed == 0) {
       analogWrite(ENA, 0);
       }
       else if (clawSpeed > 0) {
       analogWrite(ENA, abs(clawSpeed));  // motor speed
       digitalWrite(IN1, LOW); // rotate forward
       digitalWrite(IN2, HIGH);
       }
       else if (clawSpeed < 0) {
       analogWrite(ENA, abs(clawSpeed)); // motor speed
       digitalWrite(IN1, HIGH); // rotate reverse
       digitalWrite(IN2, LOW);
       }*/
      //mot = 0;
      break;
    }

  }
}

void loop() {
  int value = analogRead(adc_id); // get adc value

  if(((HistoryValue>=value) && ((HistoryValue - value) > 10)) || ((HistoryValue<value) && ((value - HistoryValue) > 10)))
  {
    //sprintf(printBuffer,"ADC%d level is %d\n",adc_id, value);
    //Serial.print(printBuffer);
    HistoryValue = value;
  }

  if(value < 50){
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
  }
  if(value >= 50 && value < 280){
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
  }

  if(value >= 280) {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
  }
  delay(100);
}





