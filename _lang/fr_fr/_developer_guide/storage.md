---
nav_title: Stockage
article_title: Stockage pour iOS
page_order: 3.60
page_type: reference
description: "Découvrez les différentes propriétés au niveau de l'appareil qui sont stockées par le SDK de Braze."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Stockage

> Découvrez les différentes propriétés au niveau de l'appareil qui sont stockées par le SDK de Braze.

## Propriétés de l’appareil

Par défaut, Braze collecte les propriétés suivantes au niveau de l'appareil pour permettre la personnalisation des messages en fonction de l'appareil, de la langue et du fuseau horaire :

{% tabs %}
{% tab android %}
- `AD_TRACKING_ENABLED`
- `ANDROID_VERSION`
- `CARRIER`
- `IS_BACKGROUND_RESTRICTED`
- `LOCALE`
- `MODEL`
- `NOTIFICIATION_ENABLED`
- `RESOLUTION`
- `TIMEZONE`

{% alert note %}
Les propriétés `AD_TRACKING_ENABLED` et `TIMEZONE` ne sont pas collectées si elles sont `null` ou vides. La propriété`GOOGLE_ADVERTISING_ID` n'est pas collectée automatiquement par le SDK et doit être transmise via [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).
{% endalert %}
{% endtab %}

{% tab swift %}
- Opérateur mobile (voir la note sur [l’obsolescence de`CTCarrier`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier))
- Paramètres régionaux de l’appareil
- Modèle de l’appareil
- Version du système d’exploitation de l’appareil
- Statut d’autorisation des notifications push
- Options d'affichage des notifications push
- Notifications push activées
- Résolution de l’appareil
- Fuseau horaire de l’appareil

{% alert note %}
Le SDK Braze ne recueille pas automatiquement IDFA. Les applis peuvent éventuellement transmettre l'IDFA à Braze en implémentant directement les méthodes ci-dessous. Les applis doivent obtenir l'abonnement explicite au suivi par l'utilisateur final via le framework de transparence du suivi des applis avant de transmettre l'IDFA à Braze.

1. Pour définir l'état du suivi de la publicité, utilisez [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. Pour définir l'identifiant de l'annonceur (IDFA), utilisez [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}
{% endtab %}

{% tab web %}
- `BROWSER`
- `BROWSER_VERSION`
- `LANGUAGE`
- `OS`
- `RESOLUTION`
- `TIME_ZONE`
- `USER_AGENT`
{% endtab %}
{% endtabs %}

Par défaut, toutes les propriétés sont activées. Toutefois, vous pouvez choisir de les activer ou de les désactiver manuellement. Gardez à l'esprit que certaines fonctionnalités du SDK de Braze nécessitent des propriétés spécifiques (telles que la réception/distribution de l'heure locale et le fuseau horaire), veillez donc à tester votre configuration avant de la mettre en production.

{% tabs %}
{% tab android %}
Par exemple, vous pouvez spécifier la version du système d'exploitation Android et les paramètres régionaux de l'appareil à inscrire sur la liste d'autorisation. Pour plus d'informations, consultez les rubriques [`setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) et [`setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html) . 

```java
new BrazeConfig.Builder()
    .setDeviceObjectAllowlistEnabled(true)
    .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
{% endtab %}

{% tab swift %}
Par exemple, vous pouvez spécifier le fuseau horaire et la collection de paramètres régionaux à autoriser. Pour plus d'informations, consultez la propriété [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) de l'objet `configuration`.

{% subtabs %}
{% subtab swift %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
configuration.devicePropertyAllowList = @[
    BRZDeviceProperty.timeZone,
    BRZDeviceProperty.locale
];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
Par exemple, vous pouvez spécifier la langue de l'appareil à inscrire sur la liste d'autorisation. Pour plus d'informations, reportez-vous à l'option `devicePropertyAllowlist` pour [`InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions).

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Pour en savoir plus sur les propriétés des appareils collectées automatiquement, reportez-vous à la section [Collecte des données du SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).
{% endalert %}

## Stockage des cookies (web uniquement) {#cookies}

Après avoir [initialisé le SDK de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize), il crée et stocke des cookies avec une expiration de 400 jours qui se renouvellent automatiquement lors de nouvelles sessions.

Les cookies suivants sont stockés :

|Cookie|Description|Taille|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Utilisé pour déterminer si l’utilisateur actuellement connecté a changé et pour associer les événements à l’utilisateur actuel.|En fonction de la taille de la valeur transmise à `changeUser`|
|`ab.storage.sessionId.[your-api-key]`|Chaîne de caractères/string générée de manière aléatoire, utilisée pour déterminer si l’utilisateur démarre une nouvelle session ou une session existante afin de synchroniser les messages et de calculer les analyses de session.|~200 octets|
|`ab.storage.deviceId.[your-api-key]`|Chaîne de caractères/string générée de façon aléatoire, utilisée pour identifier les utilisateurs anonymes et pour différencier les appareils des utilisateurs, ce qui permet un envoi de messages en fonction des appareils.|~200 octets|
|`ab.optOut`|Utilisé pour stocker les préférences de refus de l’utilisateur lorsque `disableSDK` est appelé.|~40 octets|
|`ab._gd`|Créé temporairement (puis supprimé) pour déterminer le domaine de cookie de niveau racine, ce qui permet au SDK de fonctionner correctement sur les sous-domaines.|s/o|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Désactiver les cookies {#disable-cookies}

Pour désactiver tous les cookies, utilisez l’option [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) lors de l’initialisation du SDK Web. Cela vous évitera d'associer des utilisateurs anonymes qui naviguent entre les sous-domaines et entraînera la création d'un nouvel utilisateur dans chaque sous-domaine.

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

Pour mettre fin au suivi de Braze en général, ou pour effacer toutes les données stockées dans le navigateur, consultez les rubriques [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) et [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata) du SDK, respectivement. Ces deux méthodes peuvent être utiles si un utilisateur révoque son consentement ou si vous souhaitez arrêter toutes les fonctionnalités de Braze alors que le SDK a déjà été initialisé.
