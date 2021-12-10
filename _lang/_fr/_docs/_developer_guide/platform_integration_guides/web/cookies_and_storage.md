---
nav_title: Cookies et stockage
article_title: Cookies et stockage pour le Web
platform: Web
page_order: 15
page_type: Référence
description: "Cet article de référence décrit les différents cookies utilisés par le Braze Web SDK."
---

# Cookies et stockage

Cet article décrit les différents cookies utilisés par le Braze Web SDK.

Avant de lire, veuillez noter que le Braze Web SDK ne stockera aucune donnée dans le navigateur (cookies ou autrement) _tant que votre site web [n'aura pas initialisé][5] le SDK_.

En outre, ces valeurs sont sujettes à changement et ne doivent pas être accédées directement à travers votre intégration. À la place, veuillez consulter notre [documentation Javascript][1] pour nos interfaces API publiques.

## Cookies {#cookies}

Cette section fournit des informations sur la façon dont les cookies du Braze Web SDK peuvent être configurés et gérés. Le Braze Web SDK est conçu pour vous offrir une flexibilité maximale, la conformité juridique et la pertinence de la messagerie.

Lorsque Braze crée des cookies, ils sont stockés à l'expiration d'un an qui renouvelle automatiquement les nouvelles sessions.

### Désactivation des cookies {#disable-cookies}

Pour désactiver tous les cookies, utilisez l'option [`noCookies`][6] lors de l'initialisation du SDK Web. Désactiver les cookies vous empêchera d'associer des utilisateurs anonymes qui naviguent à travers les sous-domaines et entraînera un nouvel utilisateur sur chaque sous-domaine.

```javascript
importer le braze depuis "@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

Arrêter le suivi de Braze en général, ou effacer _toutes les_ données stockées du navigateur, veuillez consulter les méthodes SDK [`stopWebTracking`][3] et [`wipeData`][4] respectivement. Ces deux méthodes peuvent être utiles si un utilisateur révoque son consentement ou si vous souhaitez arrêter toutes les fonctionnalités de Braze après l'initialisation du SDK.

### Liste des cookies

| Cookie                                              | Libellé                                                                                                                                                                                                          | Taille                                                |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `Identifiant utilisateur ab.storage.[your-api-key]` | Utilisé pour déterminer si l'utilisateur connecté a changé et pour associer des événements avec l'utilisateur actuel.                                                                                            | Basé sur la taille de la valeur passée à `changeUser` |
| `ab.storage.sessionId.[your-api-key]`               | Chaîne générée aléatoirement hors de la boîte pour déterminer si l'utilisateur commence une nouvelle session ou une session existante, afin de synchroniser les messages et de calculer les analyses de session. | ~200 octets                                           |
| `ab.storage.deviceId.[your-api-key]`                | Une chaîne de caractères générée de façon aléatoire pour identifier les utilisateurs anonymes et pour différencier les périphériques des utilisateurs et activer la messagerie sur le périphérique.              | ~200 octets                                           |
| `OptOut`                                            | Utilisé pour stocker les préférences opt-out d'un utilisateur lorsque `stopWebTracking` est appelé                                                                                                               | ~40 octets                                            |
| `_gd`                                               | Créé temporairement (et ensuite supprimé) pour déterminer le domaine de cookie de niveau racine qui permet au SDK de fonctionner correctement entre les sous-domaines.                                           | n/a                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Propriétés de l'appareil

Par défaut, Braze recueillera les propriétés suivantes du niveau de l'appareil pour permettre la personnalisation de l'appareil, de la langue et du fuseau horaire des messages :

* BROWSER
* VERSION DE FONCTIONNALITÉ
* LANGUE
* Système d'exploitation
* RÉSOLUTION
* Fuseau horaire
* USER_AGENT

Vous pouvez désactiver ou spécifier les propriétés que vous souhaitez collecter en définissant l'option d'initialisation `devicePropertyAllowlist` à une liste de [`DeviceProperties`][2].

```javascript
import braze from "@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```

Par défaut, tous les champs sont activés. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, sans le fuseau horaire, la livraison locale du fuseau horaire ne fonctionnera pas.

Pour en savoir plus sur les propriétés de l'appareil automatiquement collectées, visitez notre article [Options de collecte de données SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/).


[1]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html
[2]: https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.deviceproperties.html
[3]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#stopwebtracking
[4]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#wipedata
[5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initialize
[6]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions
