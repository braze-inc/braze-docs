## Aufzeichnung des aktuellen Standorts

Auch wenn das kontinuierliche Tracking deaktiviert ist, können Sie den aktuellen Standort des Nutzers:innen manuell mit der [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html) Methode.

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

## Kontinuierliches Tracking des Standorts

{% alert important %}
[Ab Android Marshmallow](https://developer.android.com/training/permissions/index.html) müssen Sie Ihre Nutzer:innen auffordern, dem Standort-Tracking ausdrücklich zuzustimmen. Sobald sie dies tun, kann Braze zu Beginn der nächsten Sitzung mit dem Tracking ihres Standorts beginnen. Dies unterscheidet sich von früheren Android-Versionen, bei denen nur die Angabe von Standort-Berechtigungen in Ihrem `AndroidManifest.xml` erforderlich war.
{% endalert %}

Um den Standort eines Nutzers kontinuierlich zu verfolgen, müssen Sie die Absicht Ihrer App, Standortdaten zu sammeln, erklären, indem Sie mindestens eine der folgenden Berechtigungen in Ihrer `AndroidManifest.xml` Datei hinzufügen.

|Erlaubnis|Beschreibung|
|---|---|
| `ACCESS_COARSE_LOCATION` | Verwendet den batterieeffizientesten, nicht-GPS-Anbieter (z.B. ein Heimnetzwerk). In der Regel reicht dies für die meisten Anforderungen an Standortdaten aus. Im Rahmen des Laufzeit-Berechtigungsmodells wird durch die Erteilung der Standort-Berechtigung implizit die Sammlung von Feinstandort-Daten genehmigt. |
| `ACCESS_FINE_LOCATION`   | Enthält GPS-Daten für einen genaueren Standort. Im Rahmen des Laufzeit-Berechtigungsmodells umfasst die Erteilung der Standort-Berechtigung auch den Feinzugriff auf Standorte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Ihre `AndroidManifest.xml` sollte in etwa so aussehen wie die folgende:

```xml
<manifest ... >
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

    <application ... >
        ...
    </application>
</manifest>
```

## Deaktivieren des kontinuierlichen Trackings

Sie können das kontinuierliche Tracking bei der Kompilierung oder zur Laufzeit deaktivieren.

{% tabs local %}
{% tab Kompilierzeit %}

Um das kontinuierliche Standort-Tracking zur Kompilierungszeit zu deaktivieren, setzen Sie `com_braze_enable_location_collection` auf `false` in `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

{% endtab %}
{% tab Laufzeit %}

Um das kontinuierliche Standort-Tracking zur Laufzeit selektiv zu deaktivieren, verwenden Sie [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsLocationCollectionEnabled(false)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsLocationCollectionEnabled(false)
    .build()
Braze.configure(this, brazeConfig)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
