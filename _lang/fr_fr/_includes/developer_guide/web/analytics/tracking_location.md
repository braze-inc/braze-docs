## Enregistrement de l'emplacement/localisation actuel

Pour obtenir l'emplacement/localisation actuel d'un utilisateur, utilisez la méthode de l'API géolocalisation [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) de l'API de géolocalisation. L'utilisateur sera immédiatement invité à autoriser ou à refuser le suivi (à moins qu'il ne l'ait déjà fait).

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

Désormais, lorsque des données sont envoyées à Braze, le SDK peut automatiquement détecter le pays de l'utilisateur à l'aide de son adresse IP. Pour plus d'informations, voir [setLastKnownLocation().](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation)

## Suivi continu de l'emplacement/localisation

Pour suivre en continu l'emplacement/localisation d'un utilisateur pendant le chargement d'une page, utilisez la méthode de géolocalisation de l'API [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) de l'API de géolocalisation. L'appel de cette méthode invitera immédiatement l'utilisateur à autoriser ou non le suivi (à moins qu'il ne l'ait déjà fait).

En cas d'abonnement, un rappel de succès sera désormais invoqué chaque fois que leur emplacement/localisation sera mis à jour.

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
Pour savoir comment désactiver le suivi continu, consultez la [documentation destinée aux développeurs de Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition).
{% endalert %}
