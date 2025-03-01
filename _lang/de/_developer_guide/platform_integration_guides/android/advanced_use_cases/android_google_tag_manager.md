---
nav_title: Google Tag Manager für Android
article_title: Google Tag Manager für Android für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "Dieser Referenzartikel beschreibt, wie Sie den Google Tag Manager initialisieren, konfigurieren und in Ihre Android- oder FireOS-App implementieren."

---

# Google Tag Manager für Android

> Dieser Referenzartikel beschreibt, wie Sie den Google Tag Manager initialisieren, konfigurieren und in Ihre Android- oder FireOS-App implementieren.

## Initialisierung des SDK {#initializing-android-google-tag-provider}

Das Braze Android SDK kann durch Tags, die im [Google Tag Manager](https://tagmanager.google.com/) konfiguriert wurden, initialisiert und gesteuert werden.

Als Voraussetzung für diese Implementierung muss Ihre [Android SDK-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration) vollständig sein.

## Konfigurieren Sie Ihren Google Tag Manager {#configuring-android-google-tag-manager}

In diesem Beispiel tun wir so, als ob wir eine Musik-Streaming-App wären, die verschiedene Ereignisse protokollieren möchte, während die Benutzer Lieder hören. Mit dem Google Tag Manager für Android können wir kontrollieren, welche unserer Drittanbieter dieses Ereignis erhalten, und Tags speziell für Braze erstellen.

### Angepasste Events

Benutzerdefinierte Ereignisse werden protokolliert, wenn `actionType` auf `logEvent` eingestellt ist. Der Custom Tag Provider in unserem Beispiel geht davon aus, dass der Name des angepassten Events mit `eventName` festgelegt wird.

Erstellen Sie zunächst einen Trigger, der nach einem mit `played song` übereinstimmenden Event-Namen sucht.

![Angepasster Trigger im Google Tag Manager, der für einige Events ausgelöst wird, wenn "Event-Name" mit "played song" übereinstimmt.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Als Nächstes erstellen Sie ein neues Tag ("Funktionsaufruf") und geben den Klassenpfad Ihres [Custom Tag Providers](#adding-android-google-tag-provider) ein, der später in diesem Artikel beschrieben wird.

Dieses Tag wird ausgelöst, wenn Sie das soeben erstellte Event `played song` protokollieren.

In den angepassten Parametern unseres Tags (Schlüssel-Wert-Paare) haben wir `eventName` auf `played song` festgelegt – dies ist der Name des angepassten Events, der in Braze protokolliert wird.

{% alert important %}
Wenn Sie ein angepasstes Event senden, stellen Sie sicher, dass `actionType` auf `logEvent` festgelegt ist, und geben Sie einen Wert für `eventName` an (siehe folgenden Screenshot).

Der benutzerdefinierte Tag-Anbieter in unserem Beispiel verwendet diese Schlüssel, um zu bestimmen, welche Aktion er durchführen und welchen Ereignisnamen er an Braze senden soll, wenn er Daten vom Google Tag Manager erhält.
{% endalert %}

![Tag in Google Tag Manager mit den Feldern "Klassenpfad" und "Schlüssel-Wert-Paar". Dieses Tag wird mit dem zuvor erstellten Trigger "played song" ausgelöst.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

Sie können dem Tag auch weitere Schlüssel-Wert-Paar-Argumente hinzufügen, die als angepasste Event-Eigenschaften an Braze gesendet werden. `eventName` und `actionType` werden für angepasste Event-Eigenschaften nicht ignoriert. Im folgenden Beispiel-Tag übergeben wir `genre`, das über eine Tag-Variable in Google Tag Manager definiert wurde und aus dem angepassten Event stammt, das wir in unserer App protokolliert haben.

Die Event-Eigenschaft `genre` wird als Variable "Firebase - Event Parameter" an Google Tag Manager gesendet, da Google Tag Manager für Android Firebase als Daten-Layer verwendet.

![Variable in Google Tag Manager, bei der "Genre" als Event-Parameter für das Tag "Braze - Played Song Event" hinzugefügt wird.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Wenn ein Benutzer einen Song in unserer App abspielt, protokollieren wir ein Ereignis über Firebase und den Google Tag Manager unter Verwendung des Firebase-Analytics-Ereignisnamens, der mit dem Auslösernamen unseres Tags übereinstimmt: `played song`:

{% tabs %}
{% tab JAVA %}

```java
Bundle params = new Bundle();
params.putString("genre", "pop");
params.putInt("number of times listened", 42);
mFirebaseAnalytics.logEvent("played song", params);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val params = Bundle()
params.putString("genre", "pop")
params.putInt("number of times listened", 42);
mFirebaseAnalytics.logEvent("played song", params)
```

{% endtab %}
{% endtabs %}

### Benutzerdefinierte Attribute protokollieren

Angepasste Attribute werden über `actionType` gesetzt, der auf `customAttribute` festgelegt ist. Der Custom Tag Provider geht davon aus, dass das angepasste Attribut des Schlüssel-Wert-Paares auf `customAttributeKey` und `customAttributeValue` festgelegt wird.

{% tabs %}
{% tab JAVA %}

```java
Bundle params = new Bundle();
params.putString("customAttributeKey", "favorite song");
params.putString("customAttributeValue", "Private Eyes");
mFirebaseAnalytics.logEvent("customAttribute", params);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val params = Bundle()
params.putString("customAttributeKey", "favorite song")
params.putString("customAttributeValue", "Private Eyes")
mFirebaseAnalytics.logEvent("customAttribute", params)
```

{% endtab %}
{% endtabs %}

### Aufruf von changeUser

Anrufe an `changeUser()` erfolgen über ein `actionType`, das auf `changeUser` eingestellt ist. Der Customer Tag Provider geht davon aus, dass die Braze-Nutzer-ID über ein Schlüssel-Wert-Paar `externalUserId` in Ihrem Tag festgelegt wird:

{% tabs %}
{% tab JAVA %}

```java
Bundle params = new Bundle();
params.putString("externalUserId", userId);
mFirebaseAnalytics.logEvent("changeUser", params);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val params = Bundle()
params.putString("externalUserId", userId)
mFirebaseAnalytics.logEvent("changeUser", params)
```

{% endtab %}
{% endtabs %}

## Braze SDK: Custom Tag Provider {#adding-android-google-tag-provider}

Wenn Sie die Tags und Auslöser eingerichtet haben, müssen Sie auch den Google Tag Manager in Ihrer Android-App implementieren, den Sie in der [Dokumentation](https://developers.google.com/tag-manager/android/v5/) von Google finden.

Sobald Google Tag Manager in Ihrer App installiert ist, fügen Sie einen benutzerdefinierten Tag-Anbieter hinzu, um Braze SDK-Methoden auf der Grundlage der Tags aufzurufen, die Sie in Google Tag Manager konfiguriert haben.

Achten Sie darauf, den "Klassenpfad" der Datei zu notieren. Diesen geben Sie ein, wenn Sie ein Tag in der [Google Tag Manager-Konsole](https://tagmanager.google.com/) einrichten.

Dieses Beispiel zeigt eine von vielen Möglichkeiten, wie Sie Ihren benutzerdefinierten Tag-Provider strukturieren können. Dabei bestimmen wir anhand des vom GTM-Tag gesendeten Schlüssel-Wert-Paares `actionType`, welche Methode des Braze SDK aufgerufen werden soll.

In unserem Beispiel haben wir `logEvent`, `customAttribute` und `changeUser` als `actionType` verwendet. Vielleicht möchten Sie aber die Art und Weise ändern, wie Ihr Tag Provider Daten von Google Tag Manager verarbeitet.

{% tabs %}
{% tab JAVA %}

```java
public class BrazeGtmTagProvider implements CustomTagProvider {
  private static final String TAG = BrazeLogger.getBrazeLogTag(BrazeGtmTagProvider.class);
  private static final String ACTION_TYPE_KEY = "actionType";

  // Custom Events
  private static final String LOG_EVENT_ACTION_TYPE = "logEvent";
  private static final String EVENT_NAME_VARIABLE = "eventName";

  // Custom Attributes
  private static final String CUSTOM_ATTRIBUTE_ACTION_TYPE = "customAttribute";
  private static final String CUSTOM_ATTRIBUTE_KEY = "customAttributeKey";
  private static final String CUSTOM_ATTRIBUTE_VALUE_KEY = "customAttributeValue";

  // Change User
  private static final String CHANGE_USER_ACTION_TYPE = "changeUser";
  private static final String CHANGE_USER_ID_VARIABLE = "externalUserId";

  private static Context sApplicationContext;

  /**
   * Must be set before calling any of the following methods
   * so that the proper application context is available when needed.
   *
   * Recommended to be called in your {@link Application#onCreate()}.
   */
  public static void setApplicationContext(Context applicationContext) {
    if (applicationContext != null) {
      sApplicationContext = applicationContext.getApplicationContext();
    }
  }

  @Override
  public void execute(Map<String, Object> map) {
    BrazeLogger.i(TAG, "Got google tag manager parameters map: " + map);

    if (sApplicationContext == null) {
      BrazeLogger.w(TAG, "No application context provided to this tag provider.");
      return;
    }

    if (!map.containsKey(ACTION_TYPE_KEY)) {
      BrazeLogger.w(TAG, "Map does not contain the Braze action type key: " + ACTION_TYPE_KEY);
      return;
    }
    String actionType = String.valueOf(map.remove(ACTION_TYPE_KEY));

    switch (actionType) {
      case LOG_EVENT_ACTION_TYPE:
        logEvent(map);
        break;
      case CUSTOM_ATTRIBUTE_ACTION_TYPE:
        setCustomAttribute(map);
        break;
      case CHANGE_USER_ACTION_TYPE:
        changeUser(map);
        break;
      default:
        BrazeLogger.w(TAG, "Got unknown action type: " + actionType);
        break;
    }
  }

  private void logEvent(Map<String, Object> tagParameterMap) {
    String eventName = String.valueOf(tagParameterMap.remove(EVENT_NAME_VARIABLE));
    Braze.getInstance(sApplicationContext).logCustomEvent(eventName, parseMapIntoProperties(tagParameterMap));
  }

  private BrazeProperties parseMapIntoProperties(Map<String, Object> map) {
    BrazeProperties brazeProperties = new BrazeProperties();
    for (Map.Entry<String, Object> entry : map.entrySet()) {
      final Object value = entry.getValue();
      final String key = entry.getKey();
      if (value instanceof Boolean) {
        brazeProperties.addProperty(key, (Boolean) value);
      } else if (value instanceof Integer) {
        brazeProperties.addProperty(key, (Integer) value);
      } else if (value instanceof Date) {
        brazeProperties.addProperty(key, (Date) value);
      } else if (value instanceof Long) {
        brazeProperties.addProperty(key, (Long) value);
      } else if (value instanceof String) {
        brazeProperties.addProperty(key, (String) value);
      } else if (value instanceof Double) {
        brazeProperties.addProperty(key, (Double) value);
      } else {
        BrazeLogger.w(TAG, "Failed to parse value into an BrazeProperties "
            + "accepted type. Key: '" + key + "' Value: '" + value + "'");
      }
    }

    return brazeProperties;
  }

  private void setCustomAttribute(Map<String, Object> tagParameterMap) {
    String key = String.valueOf(tagParameterMap.get(CUSTOM_ATTRIBUTE_KEY));
    Object value = tagParameterMap.get(CUSTOM_ATTRIBUTE_VALUE_KEY);

    Braze.getInstance(sApplicationContext).getCurrentUser(new IValueCallback<BrazeUser>() {
      @Override
      public void onSuccess(BrazeUser brazeUser) {
        if (value instanceof Boolean) {
          brazeUser.setCustomUserAttribute(key, (Boolean) value);
        } else if (value instanceof Integer) {
          brazeUser.setCustomUserAttribute(key, (Integer) value);
        } else if (value instanceof Long) {
          brazeUser.setCustomUserAttribute(key, (Long) value);
        } else if (value instanceof String) {
          brazeUser.setCustomUserAttribute(key, (String) value);
        } else if (value instanceof Double) {
          brazeUser.setCustomUserAttribute(key, (Double) value);
        } else if (value instanceof Float) {
          brazeUser.setCustomUserAttribute(key, (Float) value);
        } else {
          BrazeLogger.w(TAG, "Failed to parse value into a custom "
              + "attribute accepted type. Key: '" + key + "' Value: '" + value + "'");
        }
      }
    });
  }

  private void changeUser(Map<String, Object> tagParameterMap) {
    String userId = String.valueOf(tagParameterMap.get(CHANGE_USER_ID_VARIABLE));
    Braze.getInstance(sApplicationContext).changeUser(userId);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class BrazeGtmTagProvider : CustomTagProvider {

  override fun execute(map: MutableMap<String, Any>) {
    BrazeLogger.i(TAG, "Got google tag manager parameters map: $map")

    if (sApplicationContext == null) {
      BrazeLogger.w(TAG, "No application context provided to this tag provider.")
      return
    }

    if (!map.containsKey(ACTION_TYPE_KEY)) {
      BrazeLogger.w(TAG, "Map does not contain the Braze action type key: $ACTION_TYPE_KEY")
      return
    }
    val actionType = map.remove(ACTION_TYPE_KEY).toString()

    when (actionType) {
      LOG_EVENT_ACTION_TYPE -> logEvent(map)
      CUSTOM_ATTRIBUTE_ACTION_TYPE -> setCustomAttribute(map)
      CHANGE_USER_ACTION_TYPE -> changeUser(map)
      else -> BrazeLogger.w(TAG, "Got unknown action type: $actionType")
    }
  }

  private fun logEvent(tagParameterMap: MutableMap<String, Any>) {
    val eventName = tagParameterMap.remove(EVENT_NAME_VARIABLE).toString()
    Braze.getInstance(sApplicationContext).logCustomEvent(eventName, parseMapIntoProperties(tagParameterMap))
  }

  private fun parseMapIntoProperties(map: Map<String, Any>): BrazeProperties {
    val brazeProperties = BrazeProperties()
    map.forEach { param ->
      val key = param.key
      val value = param.value
      when (value) {
        is Boolean -> brazeProperties.addProperty(key, value)
        is Int -> brazeProperties.addProperty(key, value)
        is Date -> brazeProperties.addProperty(key, value)
        is Long -> brazeProperties.addProperty(key, value)
        is String -> brazeProperties.addProperty(key, value)
        is Double -> brazeProperties.addProperty(key, value)
        else -> BrazeLogger.w(TAG, "Failed to parse value into an BrazeProperties "
            + "accepted type. Key: '" + key + "' Value: '" + value + "'")
      }
    }

    return brazeProperties
  }

  private fun setCustomAttribute(tagParameterMap: Map<String, Any>) {
    val key = tagParameterMap[CUSTOM_ATTRIBUTE_KEY].toString()
    val value = tagParameterMap[CUSTOM_ATTRIBUTE_VALUE_KEY]

    Braze.getInstance(sApplicationContext).getCurrentUser { brazeUser ->
      when (value) {
        is Boolean -> brazeUser.setCustomUserAttribute(key, value)
        is Int -> brazeUser.setCustomUserAttribute(key, value)
        is Long -> brazeUser.setCustomUserAttribute(key, value)
        is String -> brazeUser.setCustomUserAttribute(key, value)
        is Double -> brazeUser.setCustomUserAttribute(key, value)
        is Float -> brazeUser.setCustomUserAttribute(key, value)
        else -> BrazeLogger.w(
          TAG, "Failed to parse value into a custom "
            + "attribute accepted type. Key: '" + key + "' Value: '" + value + "'"
        )
      }
    }
  }

  private fun changeUser(tagParameterMap: Map<String, Any>) {
    val userId = tagParameterMap[CHANGE_USER_ID_VARIABLE].toString()
    Braze.getInstance(sApplicationContext).changeUser(userId)
  }

  companion object {
    private val TAG = BrazeLogger.getBrazeLogTag(BrazeGtmTagProvider::class.java)
    private val ACTION_TYPE_KEY = "actionType"

    // Custom Events
    private val LOG_EVENT_ACTION_TYPE = "logEvent"
    private val EVENT_NAME_VARIABLE = "eventName"

    // Custom Attributes
    private val CUSTOM_ATTRIBUTE_ACTION_TYPE = "customAttribute"
    private val CUSTOM_ATTRIBUTE_KEY = "customAttributeKey"
    private val CUSTOM_ATTRIBUTE_VALUE_KEY = "customAttributeValue"

    // Change User
    private val CHANGE_USER_ACTION_TYPE = "changeUser"
    private val CHANGE_USER_ID_VARIABLE = "externalUserId"

    private var sApplicationContext: Context? = null

    /**
     * Must be set before calling any of the following methods so
     * that the proper application context is available when needed.
     *
     * Recommended to be called in your [Application.onCreate].
     */
    fun setApplicationContext(applicationContext: Context?) {
      if (applicationContext != null) {
        sApplicationContext = applicationContext.applicationContext
      }
    }
  }
}
```

{% endtab %}
{% endtabs %}

Fügen Sie `Application.onCreate()` unbedingt die folgende Initialisierung für das vorherige Snippet hinzu:

{% tabs %}
{% tab JAVA %}

```java
BrazeGtmTagProvider.setApplicationContext(this.getApplicationContext());
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeGtmTagProvider.setApplicationContext(this.applicationContext)
```

{% endtab %}
{% endtabs %}

