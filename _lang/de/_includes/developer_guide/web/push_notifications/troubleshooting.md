## Fehlersuche

Wenn Sie nach der Einrichtung von Push-Benachrichtigungen Probleme haben, sollten Sie Folgendes beachten:

- Für Web-Push-Benachrichtigungen muss Ihre Website über HTTPS verfügen.
- Nicht alle Browser können Push-Nachrichten empfangen. Stellen Sie sicher, dass `braze.isPushSupported()` im Browser `true` zurückgibt.
- Wenn ein Nutzer:innen den Push-Zugriff auf eine Website verweigert hat, wird er nicht mehr um Erlaubnis gefragt, es sei denn, er entfernt den Status "verweigert" aus seinen Browsereinstellungen.
