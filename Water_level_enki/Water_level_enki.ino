//www.elegoo.com
//2016.12.9
int in1 = 0;
int in2 = 1;
int adc_id = 0;
int HistoryValue = 0;
char printBuffer[128];

void setup()
{
  //Serial.begin(9600);
  pinMode(in1, OUTPUT);
  digitalWrite(in1, HIGH);

  pinMode(in2, OUTPUT);
  digitalWrite(in2, HIGH);
}



void loop() {

    int value = analogRead(adc_id); // get adc value

    if(((HistoryValue>=value) && ((HistoryValue - value) > 10)) || ((HistoryValue<value) && ((value - HistoryValue) > 10)))
    {
      //sprintf(printBuffer,"ADC%d level is %d\n",adc_id, value);
      //Serial.print(printBuffer);
      delay(100);
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
    delay(500);
    
}
