---
nav_title: Cookies et stockage
article_title: Cookies et stockage pour le web
platform: Web
page_order: 15
page_type: reference
description: "Cet article de référence décrit les différents cookies utilisés par le Braze Web SDK. "

---

# Cookies et stockage

Cet article décrit les différents cookies utilisés par le Braze Web SDK.

Avant de poursuivre la lecture, notez que le Braze Web SDK ne stocke aucune donnée dans le navigateur (cookies ou autres) jusqu’à ce que votre site web [initialise][5] le SDK.

En outre, ces valeurs sont susceptibles d’être modifiées et ne doivent pas être consultées directement par le biais de votre intégration. Consultez plutôt notre documentation [Javascript][1] pour connaître les interfaces de notre API publique.

{% include archive/web-v4-rename.md %}

## Cookies {#cookies}

Cette section fournit des informations sur la manière dont les cookies du Braze Web SDK peuvent être définis et gérés. Le Braze Web SDK est conçu pour vous offrir un maximum de flexibilité, de conformité juridique et de pertinence des messages.

Lorsque Braze crée des cookies, ils sont stockés avec une expiration d’un an qui se renouvelle automatiquement lors de nouvelles sessions.

### Désactiver les cookies {#disable-cookies}

Pour désactiver tous les cookies, utilisez l’option [`noCookies`][6] lors de l’initialisation du Web SDK. 
La désactivation des cookies vous empêchera d’associer des utilisateurs anonymes qui naviguent sur des sous-domaines et entraînera la création d’un nouvel utilisateur sur chaque sous-domaine.

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

Pour arrêter le suivi de Braze en général, ou pour effacer toutes les données de navigation stockées, consultez les méthodes SDK [`disableSDK`][3] et [`wipeData`][4], respectivement. Ces deux méthodes peuvent être utiles si un utilisateur révoque son consentement ou si vous souhaitez arrêter toutes les fonctionnalités de Braze alors que le SDK a déjà été initialisé.

### Liste des cookies

|Cookie|Description|Taille|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Utilisé pour déterminer si l’utilisateur actuellement connecté a changé et pour associer les événements à l’utilisateur actuel.|En fonction de la taille de la valeur passée à `changeUser`.|
|`ab.storage.sessionId.[your-api-key]`|Chaîne de caractères/string générée de manière aléatoire et prête à l’emploi, utilisée pour déterminer si l’utilisateur démarre une nouvelle session ou une session existante afin de synchroniser les messages et de calculer les analyses de session.|~200 octets|
|`ab.storage.deviceId.[your-api-key]`|Chaîne de caractères/string générée de façon aléatoire et prête à l’emploi, utilisée pour identifier les utilisateurs anonymes et pour différencier les appareils des utilisateurs, ce qui permet d’envoyer des messages en fonction des appareils.|~200 octets|
|`ab.optOut`|Utilisé pour stocker les préférences de refus de l’utilisateur lorsque `disableSDK` est appelé.|~40 octets|
|`ab._gd`|Créé temporairement (puis supprimé) pour déterminer le domaine de cookie de niveau racine, ce qui permet au SDK de fonctionner correctement sur les sous-domaines.|s/o|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Propriétés du dispositif

Par défaut, Braze collecte les propriétés suivantes au niveau de l’appareil pour permettre la personnalisation des messages en fonction de l’appareil, de la langue et du fuseau horaire :

* NAVIGATEUR
* VERSION DU NAVIGATEUR _
* LANGUE
* OS
* RÉSOLUTION
* FUSEAU _HORAIRE
* UTILISATEUR _AGENT

Vous pouvez désactiver ou spécifier les propriétés que vous souhaitez collecter en définissant l’option d’initialisation `devicePropertyAllowlist` sur une liste de [`DeviceProperties`][2]. 

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```

Par défaut, tous les champs sont activés. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, la livraison du fuseau horaire local ne fonctionnera pas sans le fuseau horaire.

Pour en savoir plus sur les propriétés du périphérique collectées automatiquement, consultez [Options de collecte de données du SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 


[1]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html
[2]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.deviceproperties.html
[3]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK
[4]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata
[5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[6]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions
