//Author:     Aleksi Hieta
//Reference:  https://lastminuteengineers.com/rotary-encoder-arduino-tutorial/
//Date:       1/24/2023
//Purpose:    Dual rotary encoder code. Direction and button presses are tracked
//            through values in serial monitor. Encoders can work simultaneously
//            independent of one another.
//            Note: Add enable and disable for all knobs in certain direction

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
    if (currentTime - lastButtonPressXMIN > 50) {
      Serial.println("X min");
    }
    lastButtonPressXMIN = currentTime;
  }

  XMAXstatus = digitalRead(XMAX);  
  if (XMAXstatus == LOW){
    if (currentTime - lastButtonPressXMAX > 50) {
      Serial.println("X max");
    }
    lastButtonPressXMAX = currentTime;
  }
//************************************************
  
  // Read the current state of CLK
  currentStateCLK1 = digitalRead(CLK1);

  // If last and current state of CLK are different, then pulse occurred
  // React to only 1 state change to avoid double count
  if (currentStateCLK1 != lastStateCLK1  && currentStateCLK1 == 1) {

    // If the DT state is different than the CLK state then
    // the encoder is rotating CCW so decrement
    if (digitalRead(DT1) != currentStateCLK1) {
      if (XMAXstatus == LOW){
      } else {
        counter1 ++;
        //currentDir1 = "CW";
      }
    } else {
      // Encoder is rotating CW so increment
      if (XMINstatus == LOW){
      } else {
      counter1 --;
      //currentDir1 = "CCW";
      }
    }
    Serial.print("1 ");
    Serial.println(counter1);
  }

  
  // Remember last CLK state
  lastStateCLK1 = currentStateCLK1;

  // Read the button state
  int btnState1 = digitalRead(SW1);

  //If we detect LOW signal, button is pressed
  if (btnState1 == LOW) {
    //if 50ms have passed since last LOW pulse, it means that the
    //button has been pressed, released and pressed again
    if (currentTime - lastButtonPress1 > 50) {
      Serial.println("B1");
    }

    // Remember last button press event
    lastButtonPress1 = currentTime;
  }
  delay(5);

  //************************************************  
  YMINstatus = digitalRead(YMIN);  
  if (YMINstatus == LOW){
    if (currentTime - lastButtonPressYMIN > 50) {
      Serial.println("Y min");
    }
    lastButtonPressYMIN = currentTime;
  }

  YMAXstatus = digitalRead(YMAX);  
  if (YMAXstatus == LOW){
    if (currentTime - lastButtonPressYMAX > 50) {
      Serial.println("Y max");
    }
    lastButtonPressYMAX = currentTime;
  }
  //************************************************

  // Read the current state of CLK
  currentStateCLK2 = digitalRead(CLK2);

  // If last and current state of CLK are different, then pulse occurred
  // React to only 1 state change to avoid double count
  if (currentStateCLK2 != lastStateCLK2  && currentStateCLK2 == 1) {

    // If the DT state is different than the CLK state then
    // the encoder is rotating CCW so decrement
    if (digitalRead(DT2) != currentStateCLK2) {
      if (YMAXstatus == LOW){
      } else {
        counter2 ++;
      //currentDir2 = "CW";
      }
    } else {
      if (YMINstatus == LOW){
      } else {
      // Encoder is rotating CW so increment
        counter2 --;
      //currentDir2 = "CCW";
      }
    }
    Serial.print("2 ");
    Serial.println(counter2);
  }

  // Remember last CLK state
  lastStateCLK2 = currentStateCLK2;

  // Read the button state
  int btnState2 = digitalRead(SW2);

  //If we detect LOW signal, button is pressed
  if (btnState2 == LOW) {
    //if 50ms have passed since last LOW pulse, it means that the
    //button has been pressed, released and pressed again
    if (currentTime - lastButtonPress2 > 50) {
      Serial.println("B2");
    }

    // Remember last button press event
    lastButtonPress2 = currentTime;
  }

  // Put in a slight delay to help debounce the reading
  delay(5);
  
  //************************************************  
  ZMINstatus = digitalRead(ZMIN);  
  if (ZMINstatus == LOW){
    if (currentTime - lastButtonPressZMIN > 50) {
      Serial.println("Z min");
    }
    lastButtonPressZMIN = currentTime;
  }

  ZMAXstatus = digitalRead(ZMAX);  
  if (ZMAXstatus == LOW){
    if (currentTime - lastButtonPressZMAX > 50) {
      Serial.println("Z max");
    }
    lastButtonPressZMAX = currentTime;
  }
  //************************************************

  
  // Read the current state of CLK3
  currentStateCLK3 = digitalRead(CLK3);

  // If last and current state of CLK are different, then pulse occurred
  // React to only 1 state change to avoid double count
  if (currentStateCLK3 != lastStateCLK3  && currentStateCLK3 == 1) {

    // If the DT state is different than the CLK state then
    // the encoder is rotating CCW so decrement
    if (digitalRead(DT3) != currentStateCLK3) {
      if (ZMAXstatus == LOW){
      } else {
        counter3 ++;
      //currentDir3 = "CW";
      }
    } else {
      if (ZMINstatus == LOW){
      } else {
      // Encoder is rotating CW so increment
        counter3 --;
      //currentDir3 = "CCW";
      }
    }
    Serial.print("3 ");
    Serial.println(counter3);
  
  }

  // Remember last CLK state
  lastStateCLK3 = currentStateCLK3;

  // Read the button state
  int btnState3 = digitalRead(SW3);

  //If we detect LOW signal, button is pressed
  if (btnState3 == LOW) {
    //if 50ms have passed since last LOW pulse, it means that the
    //button has been pressed, released and pressed again
    if (currentTime - lastButtonPress3 > 50) {
      Serial.println("B3");
    }

    // Remember last button press event
    lastButtonPress3 = currentTime;
  }
  delay(5);
/*  Serial.print("1 ");
  Serial.print(counter1);
  Serial.print(" 2 ");
  Serial.print(counter2);
  Serial.print(" 3 ");
  Serial.println(counter3);
 */
}
