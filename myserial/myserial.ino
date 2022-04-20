int  PIN_led = 13;

#define ArraySize 4
String parameters[ArraySize], DataChain, element;
#define SeparatorCharacter ","
int InitialPosition, Separator_LastPosition, ArrayIndex;

void setup() {
  Serial.begin(9600);                     //Serial Port opened at a baudrate of 9600 b/s
  pinMode(PIN_led,OUTPUT);                //The pin "2" is named as "señal" and is setted up as an output
  digitalWrite(PIN_led,1);                // The initial state of "señal" is off
}

void loop() {
  DecodeDataChain();
 }

 void DecodeDataChain() {
  if(Serial.available()){
    DataChain = Serial.readString();
    Serial.println(DataChain);
    InitialPosition=0;
    Separator_LastPosition = DataChain.indexOf(SeparatorCharacter,InitialPosition);
    
    ArrayIndex = 0;
    while (Separator_LastPosition!=-1) {
      Serial.print(ArrayIndex);
      element = DataChain.substring(InitialPosition,  Separator_LastPosition); 
      parameters[ArrayIndex]= element;
  
      InitialPosition = Separator_LastPosition+1;
      Separator_LastPosition = DataChain.indexOf(SeparatorCharacter, InitialPosition);
      ArrayIndex =ArrayIndex+1;
    }
    Serial.println(ArrayIndex);
    Serial.println(" ");
    element = DataChain.substring(InitialPosition, DataChain.length());
    parameters[ArraySize-1] = element;
    Serial.println(parameters[0]);
    Serial.println(parameters[1]);
    Serial.println(parameters[2]);
    Serial.println(parameters[3]);
  }
  } 
 
