boolean buttonWasUp = true; // предполагаем что опущена в передыщем цикле
boolean ledEnabled = false; // и светодиод не горит

void setup() {
  pinMode(13, OUTPUT); //управление светодиодом на выход
  pinMode(2, INPUT_PULLUP); //управление кнопкой на вход
}
 
void loop() {

   boolean buttonIsUp = digitalRead(2);
 

   if (buttonWasUp && !buttonIsUp) {


      delay(10);

    buttonIsUp = digitalRead(2);

      if (!buttonIsUp) {
         ledEnabled = !ledEnabled;
         digitalWrite(13, ledEnabled);
      }
   }
 
   buttonWasUp = buttonIsUp;
}