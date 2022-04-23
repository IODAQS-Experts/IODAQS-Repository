
#define FeedingVoltagePin 3
#define InputPinMeasurement A1
#define OutputPinMeasurement A2


void setup() {
  Serial.begin(9600);                     
  pinMode(FeedingVoltagePin,OUTPUT);                
  pinMode(InputPinMeasurement,INPUT);
  pinMode(OutputPinMeasurement,INPUT);                
}

void loop() {
  DecodeDataChain();
 }

void DecodeDataChain() {

  #define ArraySize 4
  String parameters[ArraySize],DataChain, element;
  #define SeparatorCharacter ","
  int SubstringInitialPosition, SubstringLastPosition, ArrayIndex;

  if(Serial.available()){    
    DataChain = Serial.readString();                                                         //if something in Serial Port, save it in a variable
    Serial.println(DataChain);                                                               //print the string in serial monitor
    SubstringInitialPosition=0;                                                              //first character's position of the first substring
    SubstringLastPosition = DataChain.indexOf(SeparatorCharacter,SubstringInitialPosition);  //last character's position of the first substring
      
    ArrayIndex = 0;                                                                   
    while (SubstringLastPosition!=-1) {                                                      //while las comma's position is different from the end of DataChain, keep decoding
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

    //##AT##THIS##POINT##THE##DATACHAIN##WAS##ALREADY##DECODED!!##
    //##AT##THIS##POINT##THE##DATACHAIN##WAS##ALREADY##DECODED!!##   
    //##AT##THIS##POINT##THE##DATACHAIN##WAS##ALREADY##DECODED!!##      


    //##### SECTION [Measuring and feeding the circuit]
    unsigned long InitialTime,CurrentTime,MeasurementTime,SamplingTime,TriggerTime;
    
    MeasurementTime = parameters[0].toFloat()*1000000;                            //MeasurementTime in seconds conveerted in microseconds
    SamplingTime = parameters[1].toFloat()*1000000;                               //SamplingTime in seconds converted in microseconds
    int ArraysLenght = round(MeasurementTime/SamplingTime);                       //Lenght of all the measurements arrays
    
    int InVoltageArray[ArraysLenght], OutVoltageArray[ArraysLenght], ArraysIndex=0;
    unsigned long TimeArray[ArraysLenght];                                        //Array with time measurements
    
    String SignalType = parameters[2];                                            //Signal Type
    #define MaxPWMVoltage 4.52                                                    //Maximun PWM Voltage
    int InputVoltage = round((255/MaxPWMVoltage)*parameters[3].toFloat());        //PWM Voltage convertion to int numbers in range 0 to 255
    Serial.println(SignalType);                                                 
    Serial.println(InputVoltage);
    
    InitialTime = micros();                                                       //Arduino board initial time
    CurrentTime = micros();                                                       //Arduino board current time
    TriggerTime = InitialTime;                                                    //Arduino board measurements start time

    do{
      if((CurrentTime-TriggerTime)>SamplingTime){                                 //if the sampling time has elapsed, then measure and update TriggerTime
        TriggerTime = CurrentTime;
        analogWrite(FeedingVoltagePin, InputVoltage);
        //take the measurement
        TimeArray[ArraysIndex]=micros();
        InVoltageArray[ArraysIndex]= analogRead(InputPinMeasurement);
        OutVoltageArray[ArraysIndex]=analogRead(OutputPinMeasurement);
        ArraysIndex = ArraysIndex+1;
      }
      CurrentTime = micros();
    }    while((CurrentTime-InitialTime)<=(MeasurementTime+SamplingTime));        //While MeasurementTime hasn't elapsed yet, keep up measuring
         
    unsigned long dif = CurrentTime-(InitialTime+SamplingTime);                   //Shows the "real" MeasurementTime
    Serial.println(dif);  
    Serial.println(ArraysIndex);                                                  //Shows the amount of measurements done by each variable's array
    Serial.println("#########");
    analogWrite(FeedingVoltagePin,0);                                             //Stops feeding the circuit

    int cycles=0;
    unsigned long MeasuredDataArray[ArraysLenght][3];
    for(int i=0.0;i< ArraysLenght;i++){                                           //Joins the individual arrays into a single one
        MeasuredDataArray[i][0] = (unsigned long)InVoltageArray[i];   
        MeasuredDataArray[i][1] = (unsigned long)OutVoltageArray[i];
        MeasuredDataArray[i][2] = TimeArray[i];
        Serial.println(MeasuredDataArray[i][2]);
        cycles++;                                                                 //Shows the amount of measurements done by each variable in the matrix
    }
    Serial.println(cycles);
    Serial.println(" ");
  }
} 

 
