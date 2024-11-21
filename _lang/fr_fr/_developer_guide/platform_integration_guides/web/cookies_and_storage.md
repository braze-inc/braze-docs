---
nav_title: Cookies et stockage
article_title: Cookies et stockage pour le web
platform: Web
page_order: 15
page_type: reference
description: "Cet article de référence décrit les différents cookies utilisés par le SDK Web de Braze."

---

# Cookies et stockage

> Cet article décrit les différents cookies utilisés par le SDK Web de Braze.

Avant de poursuivre la lecture, notez que le SDK Web de Braze ne stocke aucune donnée dans le navigateur (cookies ou autres) jusqu’à ce que votre site web [initialise](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) le SDK.

En outre, ces valeurs sont susceptibles d’être modifiées et ne doivent pas être consultées directement par le biais de votre intégration. Consultez plutôt notre [documentation JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) pour connaître les interfaces de notre API publique.

{% multi_lang_include archive/web-v4-rename.md %}

## Cookies {#cookies}

Cette section fournit des informations sur la manière dont les cookies du SDK Web de Braze peuvent être définis et gérés. Le SDK Web de Braze est conçu pour vous offrir un maximum de flexibilité, de conformité juridique et de pertinence des envois de messages.

Lorsque Braze crée des cookies, ceux-ci sont stockés avec une expiration de 400 jours qui se renouvelle automatiquement lors de nouvelles sessions.

### Désactiver les cookies {#disable-cookies}

Pour désactiver tous les cookies, utilisez l’option [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) lors de l’initialisation du SDK Web.
La désactivation des cookies vous empêchera d’associer des utilisateurs anonymes qui naviguent sur des sous-domaines et entraînera la création d’un nouvel utilisateur sur chaque sous-domaine.

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

Pour mettre fin au suivi de Braze en général, ou pour effacer toutes les données stockées dans le navigateur, consultez les rubriques [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) et [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata) du SDK, respectivement. Ces deux méthodes peuvent être utiles si un utilisateur révoque son consentement ou si vous souhaitez arrêter toutes les fonctionnalités de Braze alors que le SDK a déjà été initialisé.

### Liste des cookies

|Cookie|Description|Taille|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Utilisé pour déterminer si l’utilisateur actuellement connecté a changé et pour associer les événements à l’utilisateur actuel.|En fonction de la taille de la valeur transmise à `changeUser`|
|`ab.storage.sessionId.[your-api-key]`|Chaîne de caractères/string générée de manière aléatoire, utilisée pour déterminer si l’utilisateur démarre une nouvelle session ou une session existante afin de synchroniser les messages et de calculer les analyses de session.|~200 octets|
|`ab.storage.deviceId.[your-api-key]`|Chaîne de caractères/string générée de façon aléatoire, utilisée pour identifier les utilisateurs anonymes et pour différencier les appareils des utilisateurs, ce qui permet un envoi de messages en fonction des appareils.|~200 octets|
|`ab.optOut`|Utilisé pour stocker les préférences de refus de l’utilisateur lorsque `disableSDK` est appelé.|~40 octets|
|`ab._gd`|Créé temporairement (puis supprimé) pour déterminer le domaine de cookie de niveau racine, ce qui permet au SDK de fonctionner correctement sur les sous-domaines.|s/o|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Propriétés de l’appareil

Par défaut, Braze collecte les propriétés suivantes au niveau de l’appareil pour permettre la personnalisation des messages en fonction de l’appareil, de la langue et du fuseau horaire :

* NAVIGATEUR
* BROWSER_VERSION
* LANGUE
* OS
* RÉSOLUTION
* TIME_ZONE
* USER_AGENT

Vous pouvez désactiver ou spécifier les propriétés que vous souhaitez collecter en définissant l'option d'initialisation `devicePropertyAllowlist` sur une liste de . [`DeviceProperties`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.deviceproperties.html). 

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```

Par défaut, tous les champs sont activés. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, la livraison du fuseau horaire local ne fonctionnera pas sans le fuseau horaire.

Pour en savoir plus sur les propriétés de l'appareil collectées automatiquement, consultez les [options de collecte de données du SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 


