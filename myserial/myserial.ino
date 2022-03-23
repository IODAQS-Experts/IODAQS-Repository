int  PIN_led = 2;
String command,pin_name,pin_val;
int led_val = 0;
int cut_car; 

void setup() {
  Serial.begin(9600);                     //Serial Port opened at a baudrate of 9600 b/s
  pinMode(PIN_led,OUTPUT);                //The pin "2" is named as "señal" and is setted up as an output
  digitalWrite(PIN_led,led_val);                // The initial state of "señal" is off
  
}

void loop() {
  if(Serial.available()){               //Check if the serial port sends for something (a command)
    command = Serial.readString();      // Command format: (led,x) -----> the first parameter indicates the name of the output, and second its value
    cut_car = command.indexOf(",");
    pin_name = command.substring(0,cut_car);
    pin_val = command.substring(cut_car+1);

    if(led_val != pin_val.toInt()){
      led_val = pin_val.toInt();
      digitalWrite(PIN_led,led_val);
    }
    Serial.print(pin_name +" state:"+pin_val);
    Serial.print(" (1 for high, 0 for low)");
    Serial.println(" ");
  }
 }
