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
  for (int i = segA; i <= segG; i++) {
    pinMode(i, OUTPUT);
  }
  pinMode(buttonPin, INPUT_PULLUP);
  
  displayNumber(number);
}

void loop() {
  if (digitalRead(buttonPin) == LOW) {  
    delay(10); 
    number = (number + 1) % 10;
    displayNumber(number);
    while (digitalRead(buttonPin) == LOW); 
  }
}
