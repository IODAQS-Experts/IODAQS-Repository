int  PIN_led = 13;

#define ArraySize 4
String parameters[ArraySize], DataChain, element;
#define SeparatorCharacter ","
int SubstringInitialPosition, SubstringLastPosition, ArrayIndex;

void setup() {
  Serial.begin(9600);                     
  pinMode(PIN_led,OUTPUT);                
  digitalWrite(PIN_led,1);                
}

void loop() {
  DecodeDataChain();
 }

 void DecodeDataChain() {
  if(Serial.available()){                                                             //Check if the port is opened
    DataChain = Serial.readString();                                                  //if true, save the string in a variable
    Serial.println(DataChain);                                                        //print the string in serial monitor
    SubstringInitialPosition=0;                                                                //first character's position of the first substring
    SubstringLastPosition = DataChain.indexOf(SeparatorCharacter,SubstringInitialPosition);   //last character's position of the first substring
    
    ArrayIndex = 0;
    while (SubstringLastPosition!=-1) {
      Serial.print(ArrayIndex);
      element = DataChain.substring(SubstringInitialPosition,  SubstringLastPosition); 
      parameters[ArrayIndex]= element;
  
      SubstringInitialPosition = SubstringLastPosition+1;
      SubstringLastPosition = DataChain.indexOf(SeparatorCharacter, SubstringInitialPosition);
      ArrayIndex =ArrayIndex+1;
    }
    Serial.println(ArrayIndex);
    Serial.println(" ");
    element = DataChain.substring(SubstringInitialPosition, DataChain.length());
    parameters[ArraySize-1] = element;
    Serial.println(parameters[0]);
    Serial.println(parameters[1]);
    Serial.println(parameters[2]);
    Serial.println(parameters[3]);
  }
  } 
 
