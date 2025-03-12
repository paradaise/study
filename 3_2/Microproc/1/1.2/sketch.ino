const int buttonPin1 = 8; 
const int buttonPin2 = 9; 
const int ledPins[] = {1, 2, 3, 4, 5, 6}; 
const int numLeds = sizeof(ledPins) / sizeof(ledPins[0]); 
void setup() {
    pinMode(buttonPin1, INPUT_PULLUP); 
    pinMode(buttonPin2, INPUT_PULLUP); 
    for (int i = 0; i < numLeds; i++) {
        pinMode(ledPins[i], OUTPUT); 
    }
}

void loop() {
    if (digitalRead(buttonPin1) == LOW) { 
        for (int i = 0; i < numLeds; i++) {
            digitalWrite(ledPins[i], HIGH);
            delay(200);
            digitalWrite(ledPins[i], LOW); 
        }
    }

    if (digitalRead(buttonPin2) == LOW) { 
        for (int i = numLeds - 1; i >= 0; i--) {
            digitalWrite(ledPins[i], HIGH); 
            delay(200); 
            digitalWrite(ledPins[i], LOW);
        }
    }
}
