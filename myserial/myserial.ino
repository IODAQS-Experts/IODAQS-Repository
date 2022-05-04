#define InputPinMeasurement A1
#define OutputPinMeasurement A2
const int FeedingVoltagePin[]={2,3,4,5,6,7,8,9};
void setup() {
  Serial.begin(115200);
  Serial.println("Puerto encendido");
  pinMode(InputPinMeasurement,INPUT);
  pinMode(OutputPinMeasurement,INPUT);
  for(int j=0;j<8;j++){
    pinMode(FeedingVoltagePin[j],OUTPUT);
  }

}

void loop() {
  DecodeDataChain();
}

void DecodeDataChain(){
    if(Serial.available()){
    
    //Serial.println("Serial Port Open");
    #define ArraySize 4
    String parameters[ArraySize],DataChain, element;
    #define SeparatorCharacter ","
    int SubstringInitialPosition, SubstringLastPosition, ArrayIndex;
    
    DataChain = Serial.readString();                                                         //if something in Serial Port, save it in a variable
    delay(1000);
    SubstringInitialPosition=0;                                                              //first character's position of the first substring
    SubstringLastPosition = DataChain.indexOf(SeparatorCharacter,SubstringInitialPosition);  //last character's position of the first substring
      
    ArrayIndex = 0;                                                                   
    while (SubstringLastPosition!=-1) {                                                      //while last comma's position is different from the end of DataChain, keep decoding
      //Serial.print(ArrayIndex);
      element = DataChain.substring(SubstringInitialPosition,  SubstringLastPosition); 
      parameters[ArrayIndex]= element;
    
      SubstringInitialPosition = SubstringLastPosition+1;
      SubstringLastPosition = DataChain.indexOf(SeparatorCharacter, SubstringInitialPosition);
      ArrayIndex =ArrayIndex+1;
    }
    //Serial.println(ArrayIndex);
    //Serial.println(" ");
    element = DataChain.substring(SubstringInitialPosition, DataChain.length());
    parameters[ArraySize-1] = element;

        //##### SECTION [Measuring and feeding the circuit]
    unsigned long InitialTime,CurrentTime,MeasurementTime,SamplingTime,TriggerTime;
    
    MeasurementTime = parameters[0].toFloat();                            //MeasurementTime in seconds conveerted in microseconds
    SamplingTime = parameters[1].toFloat();                               //SamplingTime in seconds converted in microseconds
    int ArraysLenght = (int)(MeasurementTime/SamplingTime);               //Lenght of all the measurements arrays
    
    int samples=0;

    //###DAC 8 bits converter DC signal
    String SignalType = parameters[2];                                    //Signal Type
  
    byte InputVoltage = parameters[3].toInt();                            //Voltage in binary numbers in range 0 to 255
    //Serial.println(SignalType);                                                 
    //Serial.println(parameters[3]);
        
    //Serial.println(InputVoltage, BIN);
    //------------------------------------
    
    for(int i=7; i>=0; i--){
      bool LogicState = bitRead(InputVoltage, i); 
      //Serial.print(LogicState, BIN);  //shows: 00000011
      if(LogicState==1){
          digitalWrite(FeedingVoltagePin[i],HIGH);
          //Serial.print(FeedingVoltagePin[i]);Serial.println("high");
      }
      else{
        digitalWrite((FeedingVoltagePin[i]),LOW);
        //Serial.print(FeedingVoltagePin[i]);Serial.println("low");
        }
    }
    //Serial.println("########## ");
    InitialTime = micros();                                                       //Arduino board initial time
    CurrentTime = micros();                                                       //Arduino board current time
    TriggerTime = InitialTime;                                                    //Arduino board measurements start time

    do{
      if((CurrentTime-TriggerTime)>SamplingTime){                                 //if the sampling time has elapsed, then update TriggerTime and measure  
        TriggerTime = CurrentTime;
        
        //take the measurement  
        Serial.println(analogRead(InputPinMeasurement));
        Serial.println(analogRead(OutputPinMeasurement));
        Serial.println(micros());
        
        samples = samples+1;
      }
      CurrentTime = micros();
    }    while((CurrentTime-InitialTime)<=(MeasurementTime+SamplingTime));        //While MeasurementTime hasn't elapsed yet, keep up measuring
         
    unsigned long dif = CurrentTime-(InitialTime+SamplingTime);                   //Shows the "real" MeasurementTime
    //Serial.println(dif);  
    //Serial.println(samples);                                                      //Shows the amount of measurements done 
                                                            
    for (int j=1; j<9; j++){                                                      //Turn off all digital pins
      digitalWrite(FeedingVoltagePin[j],LOW);
    }

    Serial.println("Measurements completed!");Serial.println(" ");
    }
    
}
 
