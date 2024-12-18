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

Pour définir l'emplacement/localisation actuel d'un utilisateur, utilisez la méthode [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) de l'API de géolocalisation et enregistrez les données d'emplacement/localisation dans Braze :

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

Appeler `navigator.geolocation.getCurrentPosition()` demandera immédiatement l’autorisation de l’utilisateur à moins qu’il ne l’ait déjà accordée ou refusée. Consultez les [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation) pour plus d'informations sur la définition du dernier emplacement/localisation connu de l'utilisateur.

## Enregistrer une seule position

Lorsque le SDK Web envoie des données aux serveurs Braze, le pays de l’utilisateur sera automatiquement détecté à partir de son adresse IP s’il n’a pas été défini manuellement par votre application.

### Suivi continu

Si vous souhaitez suivre en continu l'emplacement/localisation d'un utilisateur pendant le chargement d'une page, utilisez la méthode [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) de l'API Géolocalisation. Cette méthode invoquera la fonction de rappel de réussite à chaque mise à jour de la localisation de l’utilisateur :

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

Appeler `navigator.geolocation.watchPosition()` demandera immédiatement l’autorisation de l’utilisateur à moins qu’il ne l’ait déjà accordée ou refusée. Consultez la [documentation de Mozilla destinée aux développeurs](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) pour obtenir des informations sur la configuration et l'arrêt du suivi des localisations.

