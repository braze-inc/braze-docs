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

## Propriétés de l'appareil

Par défaut, Braze collecte les propriétés suivantes au niveau de l'appareil pour permettre la personnalisation des messages en fonction de l'appareil, de la langue et du fuseau horaire :

{% tabs %}
{% tab web %}
- `BROWSER`
- `BROWSER_VERSION`
- `LANGUAGE`
- `OS`
- `RESOLUTION`
- `TIME_ZONE`
- `USER_AGENT`
{% endtab %}

{% tab android %}
- `AD_TRACKING_ENABLED`
- `ANDROID_VERSION`
- `CARRIER`
- `IS_BACKGROUND_RESTRICTED`
- `LOCALE`
- `MODEL`
- `NOTIFICATION_ENABLED`
- `RESOLUTION`
- `TIMEZONE`

{% alert note %}
Les propriétés `AD_TRACKING_ENABLED` et `TIMEZONE` ne sont pas collectées si elles sont `null` ou vides. La propriété `GOOGLE_ADVERTISING_ID` n'est pas collectée automatiquement par le SDK et doit être transmise via [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).
{% endalert %}
{% endtab %}

{% tab swift %}
- Opérateur mobile (voir la note sur [l'obsolescence de `CTCarrier`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier))
- Paramètres régionaux de l'appareil
- Modèle de l'appareil
- Version du système d'exploitation de l'appareil
- État de l'autorisation push
- Options d'affichage push
- Push activé
- Résolution de l'appareil
- Fuseau horaire de l'appareil

{% alert note %}
Le SDK de Braze ne recueille pas automatiquement l'IDFA. Les applications peuvent éventuellement transmettre l'IDFA à Braze en implémentant directement les méthodes ci-dessous. Les applications doivent obtenir l'abonnement explicite au suivi par l'utilisateur final via le framework App Tracking Transparency avant de transmettre l'IDFA à Braze.

1. Pour définir l'état du suivi publicitaire, utilisez [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. Pour définir l'identifiant publicitaire (IDFA), utilisez [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}
{% endtab %}
{% endtabs %}

Par défaut, toutes les propriétés sont activées. Vous pouvez toutefois choisir de les activer ou de les désactiver manuellement. Gardez à l'esprit que certaines fonctionnalités du SDK de Braze nécessitent des propriétés spécifiques (comme la distribution selon le fuseau horaire local), alors pensez à bien tester votre configuration avant de la mettre en production.

{% tabs %}
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

{% tab android %}
Par exemple, vous pouvez spécifier la version du système d'exploitation Android et les paramètres régionaux de l'appareil à inscrire sur la liste d'autorisation. Pour plus d'informations, consultez les méthodes [`setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) et [`setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html). 

```java
new BrazeConfig.Builder()
    .setDeviceObjectAllowlistEnabled(true)
    .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
{% endtab %}

{% tab swift %}
Par exemple, vous pouvez spécifier le fuseau horaire et les paramètres régionaux à autoriser. Pour plus d'informations, consultez la propriété [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) de l'objet `configuration`.

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
{% endtabs %}

{% alert tip %}
Pour en savoir plus sur les propriétés d'appareil collectées automatiquement, consultez la section [Collecte de données du SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).
{% endalert %}

## Stockage des cookies (web uniquement) {#cookies}

Après avoir [initialisé le SDK Web de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize), celui-ci crée et stocke des cookies avec une expiration de 400 jours, automatiquement renouvelée à chaque nouvelle session.

Les cookies suivants sont stockés :

|Cookie|Description|Taille|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Permet de déterminer si l'utilisateur actuellement connecté a changé et d'associer les événements à l'utilisateur actuel.|Dépend de la taille de la valeur transmise à `changeUser`|
|`ab.storage.sessionId.[your-api-key]`|Chaîne de caractères générée aléatoirement, utilisée pour déterminer si l'utilisateur démarre une nouvelle session ou poursuit une session existante, afin de synchroniser les messages et de calculer l'analytique de session.|~200 octets|
|`ab.storage.deviceId.[your-api-key]`|Chaîne de caractères générée aléatoirement, utilisée pour identifier les utilisateurs anonymes et différencier les appareils des utilisateurs, permettant ainsi l'envoi de messages par appareil.|~200 octets|
|`ab.optOut`|Stocke la préférence de refus de l'utilisateur lorsque `disableSDK` est appelé.|~40 octets|
|`ab._gd`|Créé temporairement (puis supprimé) pour déterminer le domaine de cookie racine, ce qui permet au SDK de fonctionner correctement sur les sous-domaines.|s/o|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Modifier l'expiration des cookies {#cookie-expiry}

Par défaut, les cookies de Braze expirent après 400 jours. Pour modifier cette durée, utilisez l'option `cookieExpiryInDays` lors de l'initialisation du SDK Web. La valeur doit être supérieure à 0 ; si l'option est omise ou définie à 0 ou moins, la valeur par défaut de 400 jours s'applique. Cette option nécessite le SDK Web 6.6.0 ou une version ultérieure.

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("API-KEY", {
  baseUrl: "BASE-URL",
  cookieExpiryInDays: 30 // expires after 30 days
});
```

### Désactiver les cookies {#disable-cookies}

Pour désactiver tous les cookies, utilisez l'option [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) lors de l'initialisation du SDK Web. Cela vous empêchera d'associer les utilisateurs anonymes qui naviguent entre les sous-domaines et entraînera la création d'un nouvel utilisateur sur chaque sous-domaine.

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("API-KEY", {
  baseUrl: "BASE-URL",
  noCookies: true
});
```

Pour arrêter le suivi de Braze de manière générale ou pour effacer toutes les données stockées dans le navigateur, consultez respectivement les méthodes [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) et [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata) du SDK. Ces deux méthodes peuvent s'avérer utiles si un utilisateur révoque son consentement ou si vous souhaitez désactiver toutes les fonctionnalités de Braze après l'initialisation du SDK.