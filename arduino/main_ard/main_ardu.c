//#include <Servo.h>
#include <Wire.h>


byte pin_forwLeft = 9;
byte pin_forwRight = 8;
byte pin_vertLeft = 7;
byte pin_vertRight = 6;
byte pin_claw = 5;

/*

Servo forwLeft;
Servo forwRight;
Servo vertLeft;
Servo vertRight;*/

#define SLAVE_ADDRESS 0x04
int number = 0;
int state = 0;
int stateUp = 0;
int turn = 0;


void setup() {
  Wire.begin(SLAVE_ADDRESS);
  //Wire.onReceive(receiveData);
  //Wire.onRequest(sendData);

  /*forwLeft.attach(pin_forwLeft);
  forwRight.attach(pin_forwRight);
  vertLeft.attach(pin_vertLeft);
  vertRight.attach(pin_vertRight);

  forwLeft.writeMicroseconds(1500);
  forwRight.writeMicroseconds(1500);
  vertLeft.writeMicroseconds(1500);
  vertRight.writeMicroseconds(1500);*/

  delay(1000); // delay to allow the ESC to recognize the stopped signal
}

void loop() {

  while (Wire.available()) {
    number = Wire.read();
    //state = 1500 + (number - 64) * 6.25;
    switch (number / 30) {
      case 1:
        digitalWrite(13,HIGH);
        //state = (number - 30) * 80 / 3 + 1100;
        //forwLeft.writeMicroseconds(state - turn);
        //forwRight.writeMicroseconds(state + turn);
        break;

      /*case 0:
        turn = (number * 80 / 3 - 400) / 2;
        //forwLeft.writeMicroseconds(1500 + state);
        //forwRight.writeMicroseconds(1500 - state);
        break;

      case 2:
        stateUp = (number - 60) * 80 / 3 + 1100;
        vertLeft.writeMicroseconds(stateUp);
        vertRight.writeMicroseconds(stateUp);
        break;

      case 3:
        state = (number - 105) * 255 / 14;
        if (state > 0)
          claw.setDirection(DIR_CCW);
        else
          claw.setDirection(DIR_CW);
        claw.setBrake(BRAKE_OFF);
        claw.setSpeed(abs(state));
        break;*/

    }

  }
}

//callback for sending data
//void sendData() {
//  Wire.write(number);

