---
nav_title: Standort-Tracking
article_title: Standort-Tracking für das Internet
platform: Web
page_order: 5
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie das Standort-Tracking für das Internet aktivieren."
tool: Location

---

# Standort-Tracking

> Dieser Artikel beschreibt, wie Sie das Standort-Tracking für das Internet aktivieren.

Um den aktuellen Standort eines oder einer Nutzer festzulegen, verwenden Sie die [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition)-Methode der Geolocation API und protokollieren die Standortdaten in Braze:

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

Wenn Sie `navigator.geolocation.getCurrentPosition()` aufrufen, wird der Nutzer sofort um Erlaubnis gefragt, es sei denn, er/sie hat die Erlaubnis bereits erteilt oder verweigert. In den [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation) finden Sie Informationen zum Festlegen des letzten bekannten Standorts des Nutzers:innen.

## Protokollierung eines einzelnen Standorts

Wenn das Internet SDK Daten an Braze Server sendet, wird das Land des Nutzers automatisch anhand seiner IP-Adresse erkannt, wenn es nicht manuell von Ihrer Anwendung eingestellt wurde.

### Kontinuierliches Tracking

Wenn Sie den Nutzerstandort während des Ladens einer Seite kontinuierlich verfolgen möchten, verwenden Sie die [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition)-Methode der Geolocation API. Diese Methode ruft den Erfolgs-Callback jedes Mal auf, wenn der Standort aktualisiert wird:

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

Wenn Sie `navigator.geolocation.watchPosition()` aufrufen, wird der Nutzer sofort um Erlaubnis gefragt, es sei denn, er/sie hat die Erlaubnis bereits erteilt oder verweigert. Informationen zum Konfigurieren und Beenden des Standort-Trackings finden Sie in den [Dokumentationen für Mozilla Entwickler](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition).

