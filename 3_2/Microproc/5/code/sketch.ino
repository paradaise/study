const int segA = 2;
const int segB = 3;
const int segC = 4;
const int segD = 5;
const int segE = 6;
const int segF = 7;
const int segG = 8;
const int buttonPin = 9;

int number = 0;  

const byte digits[10][7] = {
  {1,1,1,1,1,1,0},  
  {0,1,1,0,0,0,0},  
  {1,1,0,1,1,0,1},  
  {1,1,1,1,0,0,1},  
  {0,1,1,0,0,1,1},  
  {1,0,1,1,0,1,1},  
  {1,0,1,1,1,1,1},  
  {1,1,1,0,0,0,0},  
  {1,1,1,1,1,1,1},  
  {1,1,1,1,0,1,1}   
};

void displayNumber(int num) {
  for (int i = 0; i < 7; i++) {
    digitalWrite(segA + i, digits[num][i]);
  }
}

void setup() {
  pinMode(10, OUTPUT);
  for (int i = segA; i <= segG; i++) {
    pinMode(i, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  }
  displayNumber(number);
}

void loop() { 
  
  for (int i = 0; i <= 255;i++){
    if (digitalRead(buttonPin) == LOW) {  
      delay(200); 
      number = (number + 1) % 10;
      displayNumber(number);
      while (digitalRead(buttonPin) == LOW);}
    analogWrite(10, i);
    delay(10);
  }
  
  for(int i = 255; i>=0;i--){
    if (digitalRead(buttonPin) == LOW) {  
      delay(200); 
      number = (number + 1) % 10;
      displayNumber(number);
      while (digitalRead(buttonPin) == LOW);}
    analogWrite(10, i);
    delay(10);
    }
}