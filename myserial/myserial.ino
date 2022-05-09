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
    #define ArraySize 7
    String parameters[ArraySize],DataChain, element;
    #define SeparatorCharacter ","
    int SubstringInitialPosition, SubstringLastPosition, ArrayIndex;
    
    DataChain = Serial.readString();                                                         //if something in Serial Port, save it in a variable
    delay(1000);
    SubstringInitialPosition=0;                                                              //first character's position of the first substring
    SubstringLastPosition = DataChain.indexOf(SeparatorCharacter,SubstringInitialPosition);  //last character's position of the first substring
      
    ArrayIndex = 0;                                                                   
    while (SubstringLastPosition!=-1) {                                                      //while last comma's position is different from the end of DataChain, keep decoding
      element = DataChain.substring(SubstringInitialPosition,  SubstringLastPosition); 
      parameters[ArrayIndex]= element;
    
      SubstringInitialPosition = SubstringLastPosition+1;
      SubstringLastPosition = DataChain.indexOf(SeparatorCharacter, SubstringInitialPosition);
      ArrayIndex =ArrayIndex+1;
    }

    element = DataChain.substring(SubstringInitialPosition, DataChain.length());
    parameters[ArraySize-1] = element;
    
        //##### SECTION [Measuring and feeding the circuit]
    unsigned long InitialTime,CurrentTime,MeasurementTime,SamplingTime,TriggerTime;
    MeasurementTime = parameters[0].toFloat()*1000000;                           
    SamplingTime = parameters[1].toFloat()*1000000;                              
    //int ArraysLenght = (int)(MeasurementTime/SamplingTime);              
    
    byte InputVoltage;
    long Dec_val;
    String SignalType = parameters[2];
    int FinalV = parameters[4].toInt();
    int InitialV = parameters[3].toInt();
    unsigned long Period = parameters[5].toFloat()*1000000;
    unsigned long FinalTime = MeasurementTime+SamplingTime;  
    long seed = parameters[6].toInt();  
    randomSeed(seed);

    //#########ASIGNACIÓN DE TIEMPOS#########                                                  
    float m =((float)(FinalV-InitialV)/((float)(FinalTime-InitialTime)));    //  (FinalV-InitialV)/(FinalTime-InitialTime)   
//    Serial.print(SignalType);Serial.print(" ");Serial.println(m);
//    Serial.print(InitialV);Serial.print(" ");Serial.println(FinalV);

    //#########EVALUAR SignalType###################3

    //#######STEP LOOP#####################
    //#######STEP LOOP#####################
    //#######STEP LOOP#####################
    if((SignalType == "step")){
      InputVoltage = InitialV;
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
      InitialTime = micros();                                                      
      CurrentTime = micros();                                                      
      TriggerTime = InitialTime;
      
      do{
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

    
    //#######SLOPE LOOP#####################
    //#######SLOPE LOOP#####################
    //#######SLOPE LOOP#####################
    if((SignalType == "slope")){

      InitialTime = micros();                                                      
      CurrentTime = micros();                                                      
      TriggerTime = InitialTime;
        
      do{
        InputVoltage= round(m*(CurrentTime-InitialTime)+InitialV);

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
        CurrentTime = micros();
      }    while((CurrentTime-InitialTime)<=(MeasurementTime+SamplingTime));
    }

      
    //#######SINE LOOP#####################
    //#######SINE LOOP#####################
    //#######SINE LOOP#####################
    if((SignalType == "sine")){
      InitialTime = micros();                                                      
      CurrentTime = micros();                                                      
      TriggerTime = InitialTime;
        
      do{
        InputVoltage = round(InitialV + float(FinalV*sin((2*PI/(float)Period)*CurrentTime)));
        
        if (Dec_val>255){
          InputVoltage = 255;
        }
        if(0>Dec_val){
          InputVoltage = 0;
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
        CurrentTime = micros();
      }    while((CurrentTime-InitialTime)<=(MeasurementTime+SamplingTime));      //While MeasurementTime hasn't elapsed yet, keep up measuring
    }       

    //#######NOISE LOOP#####################
    //#######NOISE LOOP#####################
    //#######NOISE LOOP#####################
    if((SignalType == "noise")){
      InitialTime = micros();                                                      
      CurrentTime = micros();                                                      
      TriggerTime = InitialTime;
        
      do{
        InputVoltage = random(InitialV,FinalV+1);
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
        CurrentTime = micros();
      }    while((CurrentTime-InitialTime)<=(MeasurementTime+SamplingTime));
    }
           
    unsigned long dif = CurrentTime-(InitialTime+SamplingTime);                   //Shows the "real" MeasurementTime
    //Serial.println(dif);  
    //Serial.println(samples);                                                      //Shows the amount of measurements done 
                                                            
    for (int j=1; j<9; j++){                                                      //Turn off all digital pins
      digitalWrite(FeedingVoltagePin[j],LOW);
    }

    Serial.println("Measurements completed!");
    }
    
}
 
