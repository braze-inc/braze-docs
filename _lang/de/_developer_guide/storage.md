---
nav_title: Speicher
article_title: Speicher für iOS
page_order: 3.60
page_type: reference
description: "Erfahren Sie mehr über die verschiedenen Eigenschaften auf Geräteebene, die vom Braze SDK gespeichert werden."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Speicher

> Erfahren Sie mehr über die verschiedenen Eigenschaften auf Geräteebene, die vom Braze SDK gespeichert werden.

## Geräteeigenschaften

Standardmäßig erfasst Braze die folgenden Eigenschaften auf Geräteebene, um die Personalisierung von Nachrichten auf der Grundlage von Gerät, Sprache und Zeitzone zu ermöglichen:

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
`AD_TRACKING_ENABLED` und `TIMEZONE` werden nicht erfasst, wenn sie `null` oder leer sind. `GOOGLE_ADVERTISING_ID` wird nicht automatisch vom SDK erfasst und muss über [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) übergeben werden.
{% endalert %}
{% endtab %}

{% tab swift %}
- Netzbetreiber des Geräts (siehe Hinweis zur [`CTCarrier`-Deprecation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier))
- Gebietsschema des Geräts
- Gerätemodell
- Betriebssystemversion des Geräts
- Push-Autorisierungsstatus
- Push-Anzeigeoptionen
- Push aktiviert
- Geräteauflösung
- Zeitzone des Geräts

{% alert note %}
Das Braze SDK erfasst den Identifier for Advertisers (IDFA) nicht automatisch. Apps können den IDFA optional an Braze übergeben, indem sie die nachfolgenden Methoden direkt implementieren. Apps müssen das ausdrückliche Opt-in für das Tracking durch die Endnutzer:innen über das App Tracking Transparency Framework einholen, bevor sie den IDFA an Braze übergeben.

1. Um den Status des Werbe-Trackings festzulegen, verwenden Sie [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. Um den Identifier for Advertisers (IDFA) festzulegen, verwenden Sie [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}
{% endtab %}
{% endtabs %}

Standardmäßig sind alle Eigenschaften aktiviert. Sie können sie jedoch auch manuell aktivieren oder deaktivieren. Beachten Sie, dass einige Features des Braze SDK bestimmte Eigenschaften erfordern (z. B. Zustellung zur Ortszeit und Zeitzone). Testen Sie daher unbedingt Ihre Konfiguration, bevor Sie sie in die Produktion überführen.

{% tabs %}
{% tab web %}
Sie können zum Beispiel die Sprache des Geräts angeben, die auf die Allowlist gesetzt werden soll. Weitere Informationen finden Sie unter der Option `devicePropertyAllowlist` für [`InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions).

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```
{% endtab %}

{% tab android %}
Sie können zum Beispiel die Android-Betriebssystemversion und das Gebietsschema des Geräts angeben, die auf die Allowlist gesetzt werden sollen. Weitere Informationen finden Sie in den Methoden [`setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) und [`setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html). 

```java
new BrazeConfig.Builder()
    .setDeviceObjectAllowlistEnabled(true)
    .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
{% endtab %}

{% tab swift %}
Sie können zum Beispiel die Erfassung von Zeitzone und Gebietsschema angeben, die zugelassen werden sollen. Weitere Informationen finden Sie unter der Eigenschaft [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) des `configuration`-Objekts.

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
Wenn Sie mehr über automatisch erfasste Geräteeigenschaften erfahren möchten, lesen Sie den Abschnitt [SDK-Datenerfassung]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).
{% endalert %}

## Speichern von Cookies (nur Internet) {#cookies}

Nach der [Initialisierung des Internet Braze SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) werden Cookies mit einer Gültigkeitsdauer von 400 Tagen erstellt und gespeichert, die bei neuen Sitzungen automatisch erneuert werden.

Die folgenden Cookies werden gespeichert:

|Cookie|Beschreibung|Größe|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Wird verwendet, um festzustellen, ob sich die aktuell angemeldete Nutzer:in geändert hat, und um Ereignisse mit der aktuellen Nutzer:in zu verknüpfen.|Basierend auf der Größe des Werts, der an `changeUser` übergeben wird|
|`ab.storage.sessionId.[your-api-key]`|Zufällig generierter String, der verwendet wird, um festzustellen, ob die Nutzer:in eine neue oder bestehende Sitzung startet, um Nachrichten zu synchronisieren und Sitzungs-Analytics zu berechnen.|~200 Bytes|
|`ab.storage.deviceId.[your-api-key]`|Zufällig generierter String zur Identifizierung anonymer Nutzer:innen und zur Unterscheidung der Geräte der Nutzer:innen, der gerätebasiertes Messaging ermöglicht.|~200 Bytes|
|`ab.optOut`|Wird verwendet, um die Opt-out-Präferenz einer Nutzer:in zu speichern, wenn `disableSDK` aufgerufen wird.|~40 Bytes|
|`ab._gd`|Wird vorübergehend erstellt (und dann gelöscht), um die Root-Level-Cookie-Domain zu bestimmen, damit das SDK über Sub-Domains hinweg korrekt funktioniert.|k.A.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Ablauf von Cookies ändern {#cookie-expiry}

Standardmäßig laufen Braze-Cookies nach 400 Tagen ab. Um dies zu überschreiben, verwenden Sie die Option `cookieExpiryInDays` bei der Initialisierung des Internet SDK. Die Werte müssen größer als 0 sein. Wird die Option weggelassen oder auf 0 oder weniger gesetzt, gilt der Standard von 400 Tagen. Diese Option erfordert Internet SDK 6.6.0 oder höher.

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("API-KEY", {
  baseUrl: "BASE-URL",
  cookieExpiryInDays: 30 // expires after 30 days
});
```

### Cookies deaktivieren {#disable-cookies}

Um alle Cookies zu deaktivieren, verwenden Sie die Option [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) bei der Initialisierung des Internet SDK. Damit verhindern Sie, dass anonyme Nutzer:innen, die über Sub-Domains hinweg navigieren, miteinander verknüpft werden. Dies führt dazu, dass auf jeder Sub-Domain eine neue Nutzer:in angelegt wird.

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("API-KEY", {
  baseUrl: "BASE-URL",
  noCookies: true
});
```

Um das Braze-Tracking generell zu beenden oder alle gespeicherten Browserdaten zu löschen, verwenden Sie die SDK-Methoden [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) bzw. [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata). Diese beiden Methoden können nützlich sein, wenn eine Nutzer:in ihre Zustimmung widerruft oder Sie alle Braze-Funktionen beenden möchten, nachdem das SDK bereits initialisiert wurde.