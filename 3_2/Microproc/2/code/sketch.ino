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
        animateLeds(0, numLeds, 1); // Анимация вперёд
    }
    if (digitalRead(buttonPin2) == LOW) {
        animateLeds(numLeds - 1, -1, -1); // Анимация назад
    }
}

void animateLeds(int start, int end, int step) {
    for (int i = start; i != end; i += step) {
        digitalWrite(ledPins[i], HIGH);
        delay(50);
        digitalWrite(ledPins[i], LOW);
    }
}