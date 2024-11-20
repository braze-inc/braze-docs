---
nav_title: Seguimiento de ubicación
article_title: Seguimiento de ubicación para Web
platform: Web
page_order: 5
page_type: reference
description: "Este artículo explica cómo habilitar el seguimiento de ubicación para la Web."
tool: Location

---

# seguimiento de ubicación

> Este artículo explica cómo habilitar el seguimiento de ubicación para la Web.

Para establecer la ubicación actual de un usuario, utiliza el método [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) de la API de geolocalización y registra los datos de ubicación en Braze:

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

Al llamar a `navigator.geolocation.getCurrentPosition()` se solicitará inmediatamente permiso al usuario, a menos que éste ya lo haya concedido o denegado. Consulta [los JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation) para obtener información sobre la configuración de la última ubicación conocida del usuario.

## Registro de una única ubicación

Cuando el SDK de la Web envíe datos a los servidores Braze, el país del usuario se detectará automáticamente a partir de su dirección IP si no ha sido configurado manualmente por tu aplicación.

### Seguimiento continuo

Si quieres hacer un seguimiento continuo de la ubicación de un usuario durante la carga de una página, utiliza el método [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) de la API de geolocalización. Este método invocará la devolución de llamada de éxito cada vez que se actualice la ubicación del usuario:

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

Al llamar a `navigator.geolocation.watchPosition()` se solicitará inmediatamente permiso al usuario, a menos que éste ya lo haya concedido o denegado. Consulta [los documentos para desarrolladores de Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) para obtener información sobre cómo configurar y detener el seguimiento de ubicación.

