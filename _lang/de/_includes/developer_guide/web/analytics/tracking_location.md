## Aufzeichnung des aktuellen Standorts

Um den aktuellen Standort eines Nutzers:innen zu ermitteln, verwenden Sie die Geolocation APIs [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) Methode. Dadurch wird der Nutzer:in sofort aufgefordert, Tracking zuzulassen oder zu verbieten (sofern er dies nicht bereits getan hat).

```javascript
import * as braze from "@braze/web-sdk";
function success(position) {
  var coords = position.coords;
  braze.getUser().setLastKnownLocation(
    coords.latitude,
    coords.longitude,
    coords.accuracy,
    coords.altitude,
    coords.altitudeAccuracy
  );
}

navigator.geolocation.getCurrentPosition(success);
```

Wenn nun Daten an Braze gesendet werden, kann das SDK das Land des Nutzers:innen anhand seiner IP-Adresse automatisch erkennen. Für weitere Informationen siehe [setLastKnownLocation()](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation).

## Kontinuierliches Tracking des Standorts

Um den Standort eines Nutzers während des Ladens einer Seite kontinuierlich zu verfolgen, verwenden Sie die Geolocation API's [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) Methode. Wenn Sie diese Methode aufrufen, wird der Nutzer:in sofort aufgefordert, das Tracking zuzulassen oder zu verbieten (es sei denn, er hat dies bereits getan).

Bei Opt-in wird nun bei jedem Update des Standorts ein Callback für den Erfolg aufgerufen.

```javascript
function success(position) {
  var coords = position.coords;
  braze.getUser().setLastKnownLocation(
    coords.latitude,
    coords.longitude,
    coords.accuracy,
    coords.altitude,
    coords.altitudeAccuracy
  );
}

navigator.geolocation.watchPosition(success);
```

{% alert important %}
Um zu erfahren, wie Sie das kontinuierliche Tracking deaktivieren können, lesen Sie die [Mozilla Entwickler](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition):in.
{% endalert %}
