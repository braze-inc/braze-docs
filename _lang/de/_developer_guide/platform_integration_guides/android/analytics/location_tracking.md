---
nav_title: Standort-Tracking
article_title: Standort-Tracking für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 6
description: "Dieser Artikel zeigt, wie Sie das Standort-Tracking für Ihre Android- oder FireOS-Anwendung konfigurieren."
Tool:
  - Location

---

# Standort-Tracking

> Dieser Artikel zeigt, wie Sie das Standort-Tracking für Ihre Android- oder FireOS-Anwendung konfigurieren.

Fügen Sie mindestens eine der folgenden Berechtigungen zu Ihrer `AndroidManifest.xml`-Datei hinzu, um die Absicht Ihrer App zu erklären, Standortdaten zu sammeln:

```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```
```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

`ACCESS_FINE_LOCATION` enthält GPS-Daten für die Angabe des Nutzer:in-Standorts, während `ACCESS_COARSE_LOCATION` Daten des batterieeffizientesten verfügbaren Nicht-GPS-Anbieters (z.B. des Netzes) enthält. Für die meisten Anwendungsfälle von Standortdaten ist der grobe Standort wahrscheinlich ausreichend. Im Rahmen des Modells der Laufzeitberechtigungen wird jedoch durch die Erteilung der Standortberechtigung durch den Nutzer:innen implizit auch die Erfassung der feinen Standortdaten genehmigt. Werfen Sie einen Blick auf [Standort-Strategien](https://stuff.mit.edu/afs/sipb/project/android/docs/guide/topics/location/strategies.html) von Android-Entwickler:in, um mehr über die Unterschiede zwischen diesen Standort-Berechtigungen zu erfahren und wie Sie sie nutzen sollten.

{% alert important %}
Mit der Veröffentlichung von Android M wechselte Android von einem Installationszeit- zu einem Laufzeit-Berechtigungsmodell. Um das Standort-Tracking auf Geräten mit Android M oder höher zu aktivieren, muss die App vom Nutzer explizit die Erlaubnis erhalten, den Standort zu verwenden (Braze wird dies nicht tun). Nachdem die Berechtigungen für den Standort eingeholt wurden, beginnt Braze beim nächsten Sitzungsstart automatisch mit dem Tracking des Standorts, wenn die Standorterfassung unter `braze.xml` aktiviert ist. Bei Geräten, auf denen frühere Versionen von Android ausgeführt werden, müssen die Standortberechtigungen nur in der `AndroidManifest.xml` angegeben werden. Weitere Informationen finden Sie in der [Dokumentation zu den Berechtigungen](https://developer.android.com/training/permissions/index.html) von Android.
{% endalert %}

## Deaktivieren des automatischen Standort-Trackings

### Option zur Kompilierzeit

Um das automatische Standort-Tracking zur Kompilierungszeit zu deaktivieren, setzen Sie `com_braze_enable_location_collection` auf `false` in `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

### Laufzeit-Option

Um das automatische Standort-Tracking zur Laufzeit selektiv zu deaktivieren, verwenden Sie  [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsLocationCollectionEnabled(false)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsLocationCollectionEnabled(false)
    .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

## Manuelle Standorterfassung

Auch wenn das automatische Tracking deaktiviert ist, können Sie einzelne Datenpunkte des Standorts manuell über die Methode [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html) auf `BrazeUser` wie folgt aufzeichnen:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE)
}
```

{% endtab %}
{% endtabs %}

