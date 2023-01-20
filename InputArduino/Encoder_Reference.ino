//Author:     Aleksi Hieta
//Reference:  https://lastminuteengineers.com/rotary-encoder-arduino-tutorial/
//Date:       12/16/2022
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

int counter1 = 0;
int currentStateCLK1;
int lastStateCLK1;
String currentDir1 ="";
unsigned long lastButtonPress1 = 0;

int counter2 = 0;
int currentStateCLK2;
int lastStateCLK2;
String currentDir2 ="";
unsigned long lastButtonPress2 = 0;

int counter3 = 0;
int currentStateCLK3;
int lastStateCLK3;
String currentDir3 ="";
unsigned long lastButtonPress3 = 0;

void setup() {
  
  // Set encoder pins as inputs
  pinMode(CLK1,INPUT);
  pinMode(DT1,INPUT);
  pinMode(SW1, INPUT_PULLUP);

  pinMode(CLK2,INPUT);
  pinMode(DT2,INPUT);
  pinMode(SW2, INPUT_PULLUP);

  pinMode(CLK3,INPUT);
  pinMode(DT3,INPUT);
  pinMode(SW3, INPUT_PULLUP);

  // Setup Serial Monitor
  Serial.begin(9600);

  // Read the initial state of CLK1
  lastStateCLK1 = digitalRead(CLK1);

  // Read the initial state of CLK2
  lastStateCLK2 = digitalRead(CLK2);

  // Read the initial state of CLK3
  lastStateCLK3 = digitalRead(CLK3);
}

void loop() {
  unsigned long currentTime = millis();
//************************************************  
  // Read the current state of CLK
  currentStateCLK1 = digitalRead(CLK1);

  // If last and current state of CLK are different, then pulse occurred
  // React to only 1 state change to avoid double count
  if (currentStateCLK1 != lastStateCLK1  && currentStateCLK1 == 1){

    // If the DT state is different than the CLK state then
    // the encoder is rotating CCW so decrement
    if (digitalRead(DT1) != currentStateCLK1) {
      counter1 ++;
      currentDir1 ="CW";
    } else {
      // Encoder is rotating CW so increment
      counter1 --;
      currentDir1 ="CCW";
    }

    Serial.print("First Knob | ");
    Serial.print("Direction: ");
    Serial.print(currentDir1);
    Serial.print(" | Counter: ");
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
      Serial.println("Button pressed!");
    }

    // Remember last button press event
    lastButtonPress1 = currentTime;
  }
  delay(5);
//******************************************************

 // Read the current state of CLK
  currentStateCLK2 = digitalRead(CLK2);

  // If last and current state of CLK are different, then pulse occurred
  // React to only 1 state change to avoid double count
  if (currentStateCLK2 != lastStateCLK2  && currentStateCLK2 == 1){

    // If the DT state is different than the CLK state then
    // the encoder is rotating CCW so decrement
    if (digitalRead(DT2) != currentStateCLK2) {
      counter2 ++;
      currentDir2 ="CW";
    } else {
      // Encoder is rotating CW so increment
      counter2 --;
      currentDir2 ="CCW";
    }

    Serial.print("Second Knob | ");
    Serial.print("Direction: ");
    Serial.print(currentDir2);
    Serial.print(" | Counter: ");
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
      Serial.println("Button 2 pressed!");
    }

    // Remember last button press event
    lastButtonPress2 = currentTime;
  }

  // Put in a slight delay to help debounce the reading
  delay(5);
//************************************************  
  // Read the current state of CLK3
  currentStateCLK3 = digitalRead(CLK3);

  // If last and current state of CLK are different, then pulse occurred
  // React to only 1 state change to avoid double count
  if (currentStateCLK3 != lastStateCLK3  && currentStateCLK3 == 1){

    // If the DT state is different than the CLK state then
    // the encoder is rotating CCW so decrement
    if (digitalRead(DT3) != currentStateCLK3) {
      counter3 ++;
      currentDir3 ="CW";
    } else {
      // Encoder is rotating CW so increment
      counter3 --;
      currentDir3 ="CCW";
    }

    Serial.print("Third Knob | ");
    Serial.print("Direction: ");
    Serial.print(currentDir3);
    Serial.print(" | Counter: ");
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
      Serial.println("Button 3 pressed!");
    }

    // Remember last button press event
    lastButtonPress3 = currentTime;
  }
  delay(5);
}
