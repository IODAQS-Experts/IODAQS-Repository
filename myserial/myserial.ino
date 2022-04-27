#define InputPinMeasurement A1
#define OutputPinMeasurement A2

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Puerto encendido");
  pinMode(InputPinMeasurement,INPUT);
  pinMode(OutputPinMeasurement,INPUT);

}

void loop() {
  DecodeDataChain();
}

void DecodeDataChain(){
    if(Serial.available()){
    
    Serial.println("Serial Port Open");
    #define ArraySize 4
    String parameters[ArraySize],DataChain, element;
    #define SeparatorCharacter ","
    int SubstringInitialPosition, SubstringLastPosition, ArrayIndex;
    
    DataChain = Serial.readString();                                                         //if something in Serial Port, save it in a variable
    Serial.println(DataChain);                                                               //print the string in serial monitor
    delay(1000);
    SubstringInitialPosition=0;                                                              //first character's position of the first substring
    SubstringLastPosition = DataChain.indexOf(SeparatorCharacter,SubstringInitialPosition);  //last character's position of the first substring
      
    ArrayIndex = 0;                                                                   
    while (SubstringLastPosition!=-1) {                                                      //while last comma's position is different from the end of DataChain, keep decoding
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

        //##### SECTION [Measuring and feeding the circuit]
    unsigned long InitialTime,CurrentTime,MeasurementTime,SamplingTime,TriggerTime;
    
    MeasurementTime = parameters[0].toFloat()*1000000;                            //MeasurementTime in seconds conveerted in microseconds
    SamplingTime = parameters[1].toFloat()*1000000;                               //SamplingTime in seconds converted in microseconds
    int ArraysLenght = round(MeasurementTime/SamplingTime);                       //Lenght of all the measurements arrays
    
    int samples=0;

    //###DAC 8 bits converter DC signal
    String SignalType = parameters[2];                                            //Signal Type
    #define MaxPWMVoltage 4.52                                                    //Maximun PWM Voltage
    int InputVoltage = round((255/MaxPWMVoltage)*parameters[3].toFloat());        //Voltage convertion to int numbers in range 0 to 255
    Serial.println(SignalType);                                                 
    Serial.println(InputVoltage);
    uint8_t BitsAmount = sizeof(InputVoltage)*8;
    char InputVoltage_BitWord[BitsAmount+1];
    itoa(InputVoltage,InputVoltage_BitWord,2);
    Serial.println(InputVoltage_BitWord);

    
    const int FeedingVoltagePin[]={8,7,6,5,4,3,2,1};       
    for (int j=0; j<8; j++){                                                      //Set digital pins as outputs with their respective logic level
      if(InputVoltage_BitWord[j]-'0'==1){
        pinMode(FeedingVoltagePin[j],OUTPUT);
        digitalWrite(FeedingVoltagePin[j],HIGH);
        delay(200);
        //Serial.println("high");
      }
      else{
        pinMode(FeedingVoltagePin[j],OUTPUT);
        digitalWrite(FeedingVoltagePin[j],LOW);
        Serial.print(FeedingVoltagePin[j]);
        //Serial.println("low");
      }
    }
    Serial.println("########## ");
    InitialTime = micros();                                                       //Arduino board initial time
    CurrentTime = micros();                                                       //Arduino board current time
    TriggerTime = InitialTime;                                                    //Arduino board measurements start time

    do{
      if((CurrentTime-TriggerTime)>SamplingTime){                                 //if the sampling time has elapsed, then update TriggerTime and measure  
        TriggerTime = CurrentTime;
        
        //take the measurement  
        Serial.print(analogRead(InputPinMeasurement)); Serial.print("  ");
        Serial.print(analogRead(OutputPinMeasurement)); Serial.print("  ");
        Serial.println(micros());
        
        samples = samples+1;
      }
      CurrentTime = micros();
    }    while((CurrentTime-InitialTime)<=(MeasurementTime+SamplingTime));        //While MeasurementTime hasn't elapsed yet, keep up measuring
         
    unsigned long dif = CurrentTime-(InitialTime+SamplingTime);                   //Shows the "real" MeasurementTime
    Serial.println(dif);  
    Serial.println(samples);                                                      //Shows the amount of measurements done by each variable's array
                                                            
    for (int j=1; j<9; j++){                                                      //Turn off all digital pins
      digitalWrite(FeedingVoltagePin[j],LOW);
    }

    Serial.println("Measurements completed!");Serial.println(" ");
    }
    
}
 
