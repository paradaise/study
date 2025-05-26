const int buttonOnPin = 8;  // Кнопка ВКЛ
const int buttonOffPin = 9; // Кнопка ВЫКЛ

void setup() {
  pinMode(buttonOnPin, INPUT_PULLUP);
  pinMode(buttonOffPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  // Обработка кнопки ВКЛ
  if (digitalRead(buttonOnPin) == LOW) {
    delay(50);
    if (digitalRead(buttonOnPin) == LOW) {
      Serial.write('1'); // Команда включения
      while(digitalRead(buttonOnPin) == LOW);
    }
  }
  
  // Обработка кнопки ВЫКЛ
  if (digitalRead(buttonOffPin) == LOW) {
    delay(50);
    if (digitalRead(buttonOffPin) == LOW) {
      Serial.write('0'); // Команда выключения
      while(digitalRead(buttonOffPin) == LOW);
    }
  }
}
