---
nav_title: Lagerung
article_title: Speicher für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 9
page_type: reference
description: "Dieser Referenzartikel beschreibt die Eigenschaften auf Geräteebene, die vom Braze Android SDK erfasst werden."

---

# Lagerung

> Dieser Artikel beschreibt die verschiedenen Eigenschaften auf Geräteebene, die bei der Verwendung des Braze Android SDK erfasst werden.

## Eigenschaften des Geräts

Standardmäßig erfasst Braze die folgenden [Eigenschaften auf Geräteebene](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.enums/-device-key/index.html), um die Personalisierung von Nachrichten nach Gerät, Sprache und Zeitzone zu ermöglichen:

* `AD_TRACKING_ENABLED`
* `ANDROID_VERSION`
* `CARRIER`
* `IS_BACKGROUND_RESTRICTED`
* `LOCALE`
* `MODEL`
* `NOTIFICIATION_ENABLED`
* `RESOLUTION`
* `TIMEZONE`

{% alert note %}
`AD_TRACKING_ENABLED` und `TIMEZONE` werden nicht erfasst, wenn sie `null` oder leer sind. `GOOGLE_ADVERTISING_ID` wird nicht automatisch vom SDK erfasst und muss über [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) weitergegeben werden.
{% endalert %}

Sie können die Eigenschaften, die Sie sammeln möchten, deaktivieren oder angeben, indem Sie sie über [`BrazeConfig.Builder.setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) und [`BrazeConfig.Builder.setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html) festlegen.

Das folgende Beispiel zeigt, wie Sie das Geräteobjekt so auflisten können, dass nur die Android-Version und das Gebietsschema des Geräts in das Geräteobjekt aufgenommen werden:
```
  new BrazeConfig.Builder()
      .setDeviceObjectAllowlistEnabled(true)
      .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
Standardmäßig sind alle Felder aktiviert. Beachten Sie, dass ohne einige Eigenschaften nicht alle Features ordnungsgemäß funktionieren werden. Zum Beispiel funktioniert die Zustellung zur Ortszeit nicht ohne die Zeitzone.

Besuchen Sie unseren Artikel [SDK Datenerfassung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/), um mehr über die automatisch erfassten Eigenschaften des Geräts zu erfahren.


