# Roboboter
---
Dies ist eine Programmierung für den Lego ev3 Mindstorm Roboter. Das Programm dient dazu, dass der Roboter gegen einen anderen Roboter in einem Kreis sumoringt. Dazu muss der Roboter folgende Sensoren haben: 
- TouchSensor (SensorPort.S1) 
- ColorSensor (SensorPort.S3)
- UltrasonicSensor (SensorPort.S4)
---
Mit dem Code und den Sensoren kann der Roboter folgendes: 
1. Er sucht mit dem UltrasonicSensor, ob der Roboter vor ihm ist. 
2. Falls dies nicht der Fall ist dreht er sich und wiederholt Schritt 1.
3. Falls der Ultrasonicsensor aber den anderen Roboter entdeckt, erhöht er die Geschwindigkeit und fährt geradeaus. 
4. Dabei wird mit dem ColorSensor immer gemessen, ob der Roboter den Rand des Kreises wahrnimmt.
5. Wenn er den Rand wahrnimmt, fährt er rückwärts und dreht sich und beginnt erneut die Suche.
6. Sobald der Roboter den Gegner erfolgreich aus dem Kreis gestossen hat, kann der Touchsensor gedrückt werden.
7. Der Roboter macht nun einen Siegestanz, er tanzt und spielt gleichzeitig Töne ab, bevor er sich ausschaltet. 
