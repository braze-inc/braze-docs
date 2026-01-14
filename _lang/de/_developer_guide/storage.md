---
nav_title: Lagerung
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

# Lagerung

> Erfahren Sie mehr über die verschiedenen Eigenschaften auf Geräteebene, die vom Braze SDK gespeichert werden.

## Eigenschaften des Geräts

Standardmäßig erfasst Braze die folgenden Eigenschaften auf Geräteebene, um die Personalisierung von Nachrichten auf der Grundlage von Gerät, Sprache und Zeitzone zu ermöglichen:

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
`AD_TRACKING_ENABLED` und `TIMEZONE` werden nicht erfasst, wenn sie `null` oder leer sind. `GOOGLE_ADVERTISING_ID` wird nicht automatisch vom SDK erfasst und muss über [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) weitergegeben werden.
{% endalert %}
{% endtab %}

{% tab schnell %}
- Netzbetreiber des Geräts (siehe Hinweis, dass [`CTCarrier` veraltet](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier) ist)
- Gebietsschema des Geräts
- Gerätemodell
- Betriebssystemversion
- Push-Autorisierungsstatus
- Push Display Optionen
- Push aktiviert
- Gerät Auflösung
- Zeitzone des Geräts

{% alert note %}
Der Braze SDK sammelt IDFA nicht automatisch. Apps können optional die IDFA an Braze weitergeben, indem sie die nachfolgenden Methoden direkt implementieren. Apps müssen das ausdrückliche Opt-in für das Tracking durch den Endnutzer über das App Tracking Transparency Framework einholen, bevor sie die IDFA an Braze weitergeben.

1. Um den Status des Werbe-Trackings festzulegen, verwenden Sie [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. Um die IDFA (Identifier for Advertisers ) festzulegen, verwenden Sie [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}
{% endtab %}

{% tab Internet %}
- `BROWSER`
- `BROWSER_VERSION`
- `LANGUAGE`
- `OS`
- `RESOLUTION`
- `TIME_ZONE`
- `USER_AGENT`
{% endtab %}
{% endtabs %}

Standardmäßig sind alle Eigenschaften aktiviert. Sie können sie jedoch auch manuell aktivieren oder deaktivieren. Denken Sie daran, dass einige Features des Braze SDK bestimmte Eigenschaften erfordern (z.B. Zustellung zur Ortszeit und Zeitzone). Testen Sie also unbedingt Ihre Konfiguration, bevor Sie sie für die Produktion freigeben.

{% tabs %}
{% tab android %}
Sie können zum Beispiel die Android-Betriebssystemversion und das Gebietsschema des Geräts angeben, die in der Liste zugelassen werden sollen. Weitere Informationen finden Sie in den [`setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) und [`setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html) Methoden. 

```java
new BrazeConfig.Builder()
    .setDeviceObjectAllowlistEnabled(true)
    .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
{% endtab %}

{% tab schnell %}
Sie können zum Beispiel die Zeitzone und die Gebietsschemasammlung angeben, die zugelassen werden sollen. Weitere Informationen finden Sie unter der [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) Eigenschaft des `configuration` Objekts.

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

{% tab Internet %}
Sie können zum Beispiel die Sprache des Geräts angeben, die in der Liste zugelassen werden soll. Weitere Informationen finden Sie unter der Option `devicePropertyAllowlist` für [`InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions).

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
Wenn Sie mehr über automatisch erfasste Eigenschaften von Geräten erfahren möchten, lesen Sie bitte den Abschnitt [SDK Datenerfassung]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).
{% endalert %}

## Speichern von Cookies (nur Internet) {#cookies}

Nach der [Initialisierung des Internet Braze SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) werden Cookies mit einer Verfallszeit von 400 Tagen erstellt und gespeichert, die bei neuen Sitzungen automatisch erneuert werden.

Die folgenden Cookies werden gespeichert:

|Cookie|Beschreibung|Größe|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Wird verwendet, um festzustellen, ob der aktuell angemeldete Nutzer:in gewechselt hat und um Ereignisse mit dem aktuellen Nutzer:innen zu verknüpfen.|Basierend auf der Größe des Wertes, der an `changeUser` übergeben wird|
|`ab.storage.sessionId.[your-api-key]`|Zufällig generierter String, der verwendet wird, um festzustellen, ob der Nutzer:in eine neue oder eine bestehende Sitzung startet, um Nachrichten zu synchronisieren und Sitzungs-Analytics zu berechnen.|~200 Bytes|
|`ab.storage.deviceId.[your-api-key]`|Zufällig generierter String zur Identifizierung anonymer Nutzer:innen und zur Unterscheidung der Geräte der Nutzer:innen, der gerätebasiertes Messaging ermöglicht.|~200 Bytes|
|`ab.optOut`|Wird verwendet, um die Opt-out-Präferenz eines Nutzers zu speichern, wenn `disableSDK` aufgerufen wird.|~40 Bytes|
|`ab._gd`|Wird vorübergehend erstellt (und dann gelöscht), um die Root-Level-Cookie-Domain zu bestimmen, die es dem SDK erlaubt, über Sub-Domains hinweg korrekt zu arbeiten.|k.A.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Deaktivieren von Cookies {#disable-cookies}

Um alle Cookies zu deaktivieren, verwenden Sie die Option [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) Option, wenn Sie das Internet SDK initialisieren. Damit verhindern Sie, dass anonyme Nutzer:innen, die über Subdomains hinweg navigieren, miteinander in Verbindung gebracht werden. Dies führt dazu, dass auf jeder Subdomain ein neuer Nutzer:in angelegt wird.

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

Um das Tracking von Braze generell zu beenden oder alle gespeicherten Daten des Browsers zu löschen, schlagen Sie in den SDK-Methoden [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) und [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata) nach. Diese beiden Methoden können nützlich sein, wenn ein Nutzer seine Zustimmung widerruft oder Sie alle Braze-Funktionen beenden möchten, nachdem das SDK bereits initialisiert wurde.
