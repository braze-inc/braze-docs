---
nav_title: Suivi de localisation
article_title: Suivre la position pour le Web
platform: Web
page_order: 5
page_type: reference
description: "Cet article explique comment activer le suivi de position pour le Web."
tool: Location

---

# Suivi de localisation

> Cet article explique comment activer le suivi de position pour le Web.

Pour définir la position actuelle d’un utilisateur, utilisez la méthode [`getCurrentPosition()`][0] de l’API de géolocalisation et enregistrez les données de position sur Braze :

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

Appeler `navigator.geolocation.getCurrentPosition()` demandera immédiatement l’autorisation de l’utilisateur à moins qu’il ne l’ait déjà accordée ou refusée. Consultez les [JSDocs][1] pour plus d’informations sur la configuration de la dernière position connue de l’utilisateur.

## Enregistrer une seule position

Lorsque le SDK Web envoie des données aux serveurs Braze, le pays de l’utilisateur sera automatiquement détecté à partir de son adresse IP s’il n’a pas été défini manuellement par votre application.

### Suivi continu

Si vous souhaitez suivre en continu la position d’un utilisateur pendant qu’une page charge, utilisez la méthode [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) de l’API de géolocalisation. Cette méthode invoquera la fonction de rappel de réussite à chaque mise à jour de la position de l’utilisateur :

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

Appeler `navigator.geolocation.watchPosition()` demandera immédiatement l’autorisation de l’utilisateur à moins qu’il ne l’ait déjà accordée ou refusée. Consultez les [Documents de développeur Mozilla][2] pour plus d’informations sur la configuration et l’arrêt du suivi de position.

[0]: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition
[1]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation
[2]: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition
