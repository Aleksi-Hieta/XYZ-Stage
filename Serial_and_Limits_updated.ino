//Author:     Aleksi Hieta
//Reference:  https://lastminuteengineers.com/rotary-encoder-arduino-tutorial/
//Date:       1/24/2023
//Purpose:    Dual rotary encoder code. Direction and button presses are tracked
//            through values in serial monitor. Encoders can work simultaneously
//            independent of one another.
//            Note: Limits added to be sent at the front of all input strings to the serial port

// Rotary Encoder Inputs
#define CLK1 2
#define DT1 3
#define SW1 4

#define CLK2 5
#define DT2 6
#define SW2 7

#define CLK3 8
#define DT3 9
#define SW3 10

#define XMIN 11
#define XMAX 12

#define YMIN A3
#define YMAX A2

#define ZMIN A1
#define ZMAX A0

int counter1 = 0;
int currentStateCLK1;
int lastStateCLK1;
String currentDir1 = "";
unsigned long lastButtonPress1 = 0;

int counter2 = 0;
int currentStateCLK2;
int lastStateCLK2;
String currentDir2 = "";
unsigned long lastButtonPress2 = 0;

int counter3 = 0;
int currentStateCLK3;
int lastStateCLK3;
String currentDir3 = "";
unsigned long lastButtonPress3 = 0;

int XMINstatus = 0;
int XMAXstatus = 0;
unsigned long lastButtonPressXMIN = 0;
unsigned long lastButtonPressXMAX = 0;

int YMINstatus = 0;
int YMAXstatus = 0;
unsigned long lastButtonPressYMIN = 0;
unsigned long lastButtonPressYMAX = 0;

int ZMINstatus = 0;
int ZMAXstatus = 0;
unsigned long lastButtonPressZMIN = 0;
unsigned long lastButtonPressZMAX = 0;

String limits = "000000"; //first 0 of each axis pair is min, second is max. 
                            //i.e. Xmin, Xmax, Ymin, Ymax, Zmin, Zmax

void setup() {

  // Set encoder pins as inputs
  pinMode(CLK1, INPUT);
  pinMode(DT1, INPUT);
  pinMode(SW1, INPUT_PULLUP);

  pinMode(CLK2, INPUT);
  pinMode(DT2, INPUT);
  pinMode(SW2, INPUT_PULLUP);

  pinMode(CLK3, INPUT);
  pinMode(DT3, INPUT);
  pinMode(SW3, INPUT_PULLUP);

  pinMode(XMIN, INPUT);
  digitalWrite(XMIN, HIGH);
  pinMode(XMAX, INPUT);
  digitalWrite(XMAX, HIGH);

  pinMode(YMIN, INPUT);
  digitalWrite(YMIN, HIGH);
  pinMode(YMAX, INPUT);
  digitalWrite(YMAX, HIGH);

  pinMode(ZMIN, INPUT);
  digitalWrite(ZMIN, HIGH);
  pinMode(ZMAX, INPUT);
  digitalWrite(ZMAX, HIGH);
  
  // Setup Serial Monitor
  Serial.begin(9600);

  // Read the initial state of CLK1
  lastStateCLK1 = digitalRead(CLK1);

  // Read the initial state of CLK2
  lastStateCLK2 = digitalRead(CLK2);

  // Read the initial state of CLK3
  lastStateCLK3 = digitalRead(CLK3);
}

//************************************************************** 

void loop() {
  unsigned long currentTime = millis();
  //************************************************
  XMINstatus = digitalRead(XMIN);  
  if (XMINstatus == LOW){
    limits[0] = '1'; //low limit hit
  } 
  else {
    limits[0] = '0'; //low limit not hit
  }

  XMAXstatus = digitalRead(XMAX);
  if (XMAXstatus == LOW){
    limits[1] = '1'; //low limit hit
  } 
  else {
    limits[1] = '0'; //low limit not hit
  }
//************************************************
  currentStateCLK1 = digitalRead(CLK1);
  if (currentStateCLK1 != lastStateCLK1  && currentStateCLK1 == 1) {
    if (digitalRead(DT1) != currentStateCLK1) {
      if (XMAXstatus == LOW){
      } else {
        counter1 ++;  
      }
    } else {
      // Encoder is rotating CW so increment
      if (XMINstatus == LOW){
      } else {
        counter1 --;
      }
    }
    Serial.print(limits); //limit switch update
    Serial.print("1 ");
    Serial.println(counter1);
  }

  lastStateCLK1 = currentStateCLK1;
  
  int btnState1 = digitalRead(SW1);

  if (btnState1 == LOW) {
    if (currentTime - lastButtonPress1 > 50) {
      Serial.print(limits); //limit switch update
      Serial.println("B1");
    }
    lastButtonPress1 = currentTime;
  }
  delay(5);

  //************************************************  
  YMINstatus = digitalRead(YMIN);  
  if (YMINstatus == LOW){
    limits[2] = '1'; //low limit hit
  } 
  else {
    limits[2] = '0'; //low limit not hit
  }

  YMAXstatus = digitalRead(YMAX);
  if (YMAXstatus == LOW){
    limits[3] = '1'; //low limit hit
  } 
  else {
    limits[3] = '0'; //low limit not hit
  }
  //************************************************
  currentStateCLK2 = digitalRead(CLK2);
  if (currentStateCLK2 != lastStateCLK2  && currentStateCLK2 == 1) {
    if (digitalRead(DT2) != currentStateCLK2) {
      if (YMAXstatus == LOW){
      } else {
        counter2 ++;
      }
    } else {
      if (YMINstatus == LOW){
      } else {
        counter2 --;
      }
    }
    Serial.print(limits); //limit switch update
    Serial.print("2 ");
    Serial.println(counter2);
  }

  lastStateCLK2 = currentStateCLK2;

  int btnState2 = digitalRead(SW2);

  if (btnState2 == LOW) {
    if (currentTime - lastButtonPress2 > 50) {
      Serial.print(limits); //limit switch update
      Serial.println("B2");
    }
    lastButtonPress2 = currentTime;
  }

  delay(5);
  
  //************************************************  
  ZMINstatus = digitalRead(ZMIN);  
  if (ZMINstatus == LOW){
    limits[4] = '1'; //low limit hit
  }
  else {
    limits[4] = '0'; //low limit not hit
  }
  
  ZMAXstatus = digitalRead(ZMAX);
  if (ZMAXstatus == LOW){
    limits[5] = '1'; //low limit hit
  } 
  else {
    limits[5] = '0'; //low limit not hit
  }
  //************************************************
  currentStateCLK3 = digitalRead(CLK3);
  
  if (currentStateCLK3 != lastStateCLK3  && currentStateCLK3 == 1) {
    if (digitalRead(DT3) != currentStateCLK3) {
      if (ZMAXstatus == LOW){
      } else {
        counter3 ++;
      }
    } else {
      if (ZMINstatus == LOW){
      } else {
        counter3 --;
      }
    }
    Serial.print(limits); //limit switch update
    Serial.print("3 ");
    Serial.println(counter3);
  
  }

  lastStateCLK3 = currentStateCLK3;

  int btnState3 = digitalRead(SW3);

  if (btnState3 == LOW) {
    if (currentTime - lastButtonPress3 > 50) {
      Serial.print(limits); //limit switch update
      Serial.println("B3");
    }
    lastButtonPress3 = currentTime;
  }
  delay(5);
}
