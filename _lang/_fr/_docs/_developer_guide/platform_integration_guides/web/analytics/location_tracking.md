---
nav_title: Suivi de la localisation
article_title: Suivi de localisation pour le Web
platform: Web
page_order: 5
page_type: Référence
description: "Cet article explique comment activer le suivi de la localisation via le SDK Web de Braze."
tool: Localisation
---

# Suivi de localisation pour le web

Pour définir l'emplacement actuel d'un utilisateur, utilisez la méthode [`getCurrentPosition()`][] de l'API de géolocalisation et enregistrez les données de localisation au Brésil.

```javascript
function success(position) {
  var coords = position.coords;
  appboy. etUser().setLastKnownLocation(
    coords.latitude,
    coords. ongitude,
    coords.accuracy,
    coords.altitude,
    coords. ltitudeAccuracy
  );
}

navigator.geolocation.getCurrentPosition(success);
```

Notez qu'appeler `navigator.geolocation.getCurrentPosition()` demandera immédiatement la permission de l'utilisateur sauf s'ils ont déjà accordé ou refusé la permission. Voir le [JSDocs][1] pour plus d'informations sur le dernier emplacement connu de l'utilisateur.


## Loguer un seul emplacement

De plus, lorsque le Web SDK envoie des données à des serveurs Braze, le pays de l'utilisateur sera automatiquement détecté à partir de son adresse IP s'il n'a pas été défini manuellement par votre application.

### Suivi continu

Si vous souhaitez suivre en permanence l'emplacement d'un utilisateur pendant le chargement d'une page, utilisez la méthode `watchPosition()` de l'API de géolocalisation. Cette méthode invoquera la fonction de rappel de succès à chaque mise à jour de l'emplacement de l'utilisateur.

```javascript
function success(position) {
  var coords = position.coords;
  appboy. etUser().setLastKnownLocation(
    coords.latitude,
    coords. ongitude,
    coords.accuracy,
    coords.altitude,
    coords. ltitudeAccuracy
  );
}

navigator.geolocation.watchPosition(success);
```

Appeler `navigator.geolocation.watchPosition()` demandera immédiatement la permission de l'utilisateur sauf s'ils ont déjà accordé ou refusé la permission. Pour plus d'informations sur la configuration et l'arrêt du suivi d'emplacement, consultez la [documentation des développeurs Mozilla][2].

[`getCurrentPosition()`]: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition
[1]: https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setLastKnownLocation
[2]: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition
