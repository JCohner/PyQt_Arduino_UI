int LEDPin = 13;
int LEDPinStatus = 0;
int sendPin = 3;
int returnPin = 2;
int brakePin = 4;
int disablePin = 6;


char buff[100];
int i = 0;

void setup() {
  Serial.begin(115200);
  pinMode(LEDPin, OUTPUT);
  digitalWrite(LEDPin, LOW);
  pinMode(returnPin, OUTPUT);
  pinMode(sendPin, OUTPUT);
  pinMode(brakePin, OUTPUT);
  pinMode(disablePin, OUTPUT);
  digitalWrite(brakePin,LOW);
  digitalWrite(disablePin,LOW);
  while (!Serial) {
    //LOW enables break
  }
  buff[0] = 'b';
}

void loop() {
  Serial.println(buff[0]);
  switch(buff[0]){
    //Send it case
    case 'o':
      digitalWrite(brakePin, HIGH);
      
      digitalWrite(LEDPin,HIGH);
      digitalWrite(returnPin, LOW);
      digitalWrite(sendPin, HIGH);
      
      break;
    //Return it case
    case 'f':
      digitalWrite(brakePin, HIGH);
      
      digitalWrite(LEDPin,LOW);
      digitalWrite(sendPin, LOW);
      digitalWrite(returnPin, HIGH);
      
      break;
    //Brake Case
    case 'b':
      digitalWrite(brakePin,LOW);
      
      LEDPinStatus = !LEDPinStatus;
      digitalWrite(LEDPin, LEDPinStatus);
      break;

    //Global Control Logic  
    case 'd':
      digitalWrite(disablePin, LOW);
      break;
    case 'i':
      digitalWrite(disablePin, HIGH);
      break;  
    default:
      Serial.print("in default: ");
      Serial.println(buff[0]);
      digitalWrite(4,LOW);
}


  delay(50);
}

void serialEvent(){
  while(Serial.available()){
    buff[i++] = Serial.read();  
  }
  i = 0;
}
