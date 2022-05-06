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
    MeasurementTime = parameters[0].toFloat();                           
    SamplingTime = parameters[1].toFloat();                              
    int ArraysLenght = (int)(MeasurementTime/SamplingTime);              
    
    byte InputVoltage;
    long Dec_val;
    String SignalType = parameters[2];
    int FinalV = parameters[3].toFloat();
    int InitialV = parameters[4].toFloat();
    unsigned long Period = parameters[5].toInt();
    unsigned long FinalTime = MeasurementTime+SamplingTime;  
 

    //#########ASIGNACIÓN DE TIEMPOS#########                                                  
    float m =((float)(FinalV-InitialV)/((float)(FinalTime-InitialTime)));    //  (FinalV-InitialV)/(FinalTime-InitialTime)   
    Serial.print(SignalType);Serial.print(" ");Serial.println(m);

    //#########EVALUAR SignalType###################3

//    else (SignalType == "noise"){    
//    }


    //#######STEP BUCLE#####################
    //#######STEP BUCLE#####################
    //#######STEP BUCLE#####################
    if((SignalType == "step")){
      InputVoltage = FinalV;
      InitialTime = micros();                                                      
      CurrentTime = micros();                                                      
      TriggerTime = InitialTime;
        
      do{
        for(int i=7; i>=0; i--){
          bool LogicState = bitRead(InputVoltage, i); 
          //Serial.print(LogicState, BIN);  //shows: 00000011
          if(LogicState==1){
              digitalWrite(FeedingVoltagePin[i],HIGH);
          }
          else{
            digitalWrite((FeedingVoltagePin[i]),LOW);
            }
      }
      if((CurrentTime-TriggerTime)>SamplingTime){                                 //if the sampling time has elapsed, then update TriggerTime and measure  
        TriggerTime = CurrentTime;
        //take the measurement  
        Serial.println(analogRead(InputPinMeasurement));
        Serial.println(analogRead(OutputPinMeasurement));
        Serial.println(micros());
      } 
        Serial.println(FinalV);
  
        CurrentTime = micros();
      }    while((CurrentTime-InitialTime)<=(MeasurementTime+SamplingTime));
    }

    
    //#######SLOPE BUCLE#####################
    //#######SLOPE BUCLE#####################
    //#######SLOPE BUCLE#####################
    if((SignalType == "slope")){

      InitialTime = micros();                                                      
      CurrentTime = micros();                                                      
      TriggerTime = InitialTime;
        
      do{
         Dec_val= round(m*(CurrentTime-InitialTime)+InitialV);
         Serial.println(Dec_val);
         InputVoltage=Dec_val;

        for(int i=7; i>=0; i--){
          bool LogicState = bitRead(InputVoltage, i); 
          //Serial.print(LogicState, BIN);  //shows: 00000011
          if(LogicState==1){
              digitalWrite(FeedingVoltagePin[i],HIGH);
          }
          else{
            digitalWrite((FeedingVoltagePin[i]),LOW);
            }
        }
        if((CurrentTime-TriggerTime)>SamplingTime){                                 //if the sampling time has elapsed, then update TriggerTime and measure  
          TriggerTime = CurrentTime;
          //take the measurement  
          Serial.println(analogRead(InputPinMeasurement));
          Serial.println(analogRead(OutputPinMeasurement));
          Serial.println(micros());
        } 
  
        CurrentTime = micros();
      }    while((CurrentTime-InitialTime)<=(MeasurementTime+SamplingTime));
    }

      
    //#######SINE BUCLE#####################
    //#######SINE BUCLE#####################
    //#######SINE BUCLE#####################
    if((SignalType == "sine")){
      InitialTime = micros();                                                      
      CurrentTime = micros();                                                      
      TriggerTime = InitialTime;
        
      do{
        Dec_val = round(InitialV + float(FinalV*sin((2*PI/(float)Period)*CurrentTime)));
        if (Dec_val>255){
          Dec_val = 255;
          InputVoltage = Dec_val;
        }
        if(0>Dec_val){
          Dec_val = 0;
          InputVoltage = Dec_val;
        }
        for(int i=7; i>=0; i--){
          bool LogicState = bitRead(InputVoltage, i); 

          if(LogicState==1){
            digitalWrite(FeedingVoltagePin[i],HIGH);
          }
          else{
            digitalWrite((FeedingVoltagePin[i]),LOW);
            }
        }
        if((CurrentTime-TriggerTime)>SamplingTime){                                 //if the sampling time has elapsed, then update TriggerTime and measure  
          TriggerTime = CurrentTime;
          //take the measurement  
          Serial.println(analogRead(InputPinMeasurement));
          Serial.println(analogRead(OutputPinMeasurement));
          Serial.println(micros());
        }
        Serial.println(Dec_val);
  
        CurrentTime = micros();
      }    while((CurrentTime-InitialTime)<=(MeasurementTime+SamplingTime));
    }       //While MeasurementTime hasn't elapsed yet, keep up measuring
         
    unsigned long dif = CurrentTime-(InitialTime+SamplingTime);                   //Shows the "real" MeasurementTime
    //Serial.println(dif);  
    //Serial.println(samples);                                                      //Shows the amount of measurements done 
                                                            
    for (int j=1; j<9; j++){                                                      //Turn off all digital pins
      digitalWrite(FeedingVoltagePin[j],LOW);
    }

    Serial.println("Measurements completed!");Serial.println(" ");
    }
    
}
 
