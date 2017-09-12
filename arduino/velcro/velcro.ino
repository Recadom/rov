#include <Wire.h>
#include <Servo.h>

#define SLAVE_ADDRESS 0x04
int starttime = millis();

// define motor pins
byte pin_forwLeft = 9;
byte pin_forwRight = 8;
byte pin_vertLeft = 7;
byte pin_vertRight = 6;

// start servos
Servo forwLeft;
Servo forwRight;
Servo vertLeft;
Servo vertRight;

void setup()
{
  Wire.begin(SLAVE_ADDRESS);      // join i2c bus with address #4
  Wire.onReceive(receiveEvent);   // register event

  // attatch all the motors to their pins
  forwLeft.attach(pin_forwLeft);
  forwRight.attach(pin_forwRight);
  vertLeft.attach(pin_vertLeft);
  vertRight.attach(pin_vertRight);

  // set all the motors to an off state
  forwLeft.writeMicroseconds(1500);
  forwRight.writeMicroseconds(1500);
  vertLeft.writeMicroseconds(1500);
  vertRight.writeMicroseconds(1500);

  delay(1000); // delay to allow the ESC to recognize the stopped signal
}

void receiveEvent(int bytes) {
  int x = Wire.read();    // read one character from the I2C
  starttime = millis();   // reset turnoff counter
  //led(x);
  motor(x);
}


//* testing function for led lights
void led(int x) {
  if (x == 1) {
    digitalWrite(9, HIGH);
    digitalWrite(8, LOW);
  }
  if (x == 2) {
    digitalWrite(8, HIGH);
    digitalWrite(9, LOW);
  }
  if (x == 0) {
    digitalWrite(8, LOW);
    digitalWrite(9, LOW);
  }
}
//*/

void motor(int x) {
  static byte mot = 0;    // create a number that will rememember its last value
  int state = (x - 64) * 400 / 63 + 1500;    //convert from 0-127 to 1100-1900
  
  // iterate to next motor after every signal
  switch (mot) {
    case 0:
      forwLeft.writeMicroseconds(state);
      ++mot;
      break;
      
    case 1:
    forwRight.writeMicroseconds(state);
      ++mot;
      break;
      
    case 2:
    vertLeft.writeMicroseconds(state);
      ++mot;
      break;
      
    case 3:
    vertRight.writeMicroseconds(state);
      mot = 0;
      break;
  }
}

void loop() {
  // automatic shutoff loop
  static int endtime = starttime;
  if ((endtime - starttime) >= 500) // when 500ms has passed without signal
    forwLeft.writeMicroseconds(1500);
    forwRight.writeMicroseconds(1500);
    vertLeft.writeMicroseconds(1500);
    vertRight.writeMicroseconds(1500);
    endtime = millis();
  delay(100);
}

