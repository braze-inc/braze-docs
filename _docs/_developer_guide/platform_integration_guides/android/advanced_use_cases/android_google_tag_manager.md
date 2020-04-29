---
nav_title: Google Tag Manager
platform: Android
page_order: 8

---
### Google Tag Manager

#### Initializing the SDK {#initializing-android-google-tag-provider}

Braze's SDK can be initialized and controlled within tags configured from Google Tag Manager.

To initialize the Braze Android SDK, please follow [Initial SDK Setup][1].

#### Braze SDK Custom Tag Provider {#adding-android-google-tag-provider}

In your app, first setup [Google Tag Manager for Android][2]. 

Next, add the following custom tag provider to use the Braze SDK. Be sure to note the classpath to the file for later use in the [Google Tag Manager][5] console.

{% tabs %}
{% tab JAVA %}

```java
public class BrazeGtmTagProvider implements CustomTagProvider {
  private static final String TAG = AppboyLogger.getAppboyLogTag(BrazeGtmTagProvider.class);
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
   * Must be set before calling any of the below methods to
   * ensure that the proper application context is available when needed.
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
    AppboyLogger.i(TAG, "Got google tag manager parameters map: " + map);

    if (sApplicationContext == null) {
      AppboyLogger.w(TAG, "No application context provided to this tag provider.");
      return;
    }

    if (!map.containsKey(ACTION_TYPE_KEY)) {
      AppboyLogger.w(TAG, "Map does not contain the braze action type key: " + ACTION_TYPE_KEY);
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
        AppboyLogger.w(TAG, "Got unknown action type: " + actionType);
        break;
    }
  }

  private void logEvent(Map<String, Object> tagParameterMap) {
    String eventName = String.valueOf(tagParameterMap.remove(EVENT_NAME_VARIABLE));
    Appboy.getInstance(sApplicationContext).logCustomEvent(eventName, parseMapIntoProperties(tagParameterMap));
  }

  private AppboyProperties parseMapIntoProperties(Map<String, Object> map) {
    AppboyProperties appboyProperties = new AppboyProperties();
    for (Map.Entry<String, Object> entry : map.entrySet()) {
      final Object value = entry.getValue();
      final String key = entry.getKey();
      if (value instanceof Boolean) {
        appboyProperties.addProperty(key, (Boolean) value);
      } else if (value instanceof Integer) {
        appboyProperties.addProperty(key, (Integer) value);
      } else if (value instanceof Date) {
        appboyProperties.addProperty(key, (Date) value);
      } else if (value instanceof Long) {
        appboyProperties.addProperty(key, (Long) value);
      } else if (value instanceof String) {
        appboyProperties.addProperty(key, (String) value);
      } else if (value instanceof Double) {
        appboyProperties.addProperty(key, (Double) value);
      } else {
        AppboyLogger.w(TAG, "Failed to parse value into an AppboyProperties "
            + "accepted type. Key: '" + key + "' Value: '" + value + "'");
      }
    }

    return appboyProperties;
  }

  private void setCustomAttribute(Map<String, Object> tagParameterMap) {
    String key = String.valueOf(tagParameterMap.get(CUSTOM_ATTRIBUTE_KEY));
    Object value = tagParameterMap.get(CUSTOM_ATTRIBUTE_VALUE_KEY);

    AppboyUser appboyUser = Appboy.getInstance(sApplicationContext).getCurrentUser();
    if (appboyUser == null) {
      AppboyLogger.w(TAG, "AppboyUser was null. Returning.");
      return;
    }

    if (value instanceof Boolean) {
      appboyUser.setCustomUserAttribute(key, (Boolean) value);
    } else if (value instanceof Integer) {
      appboyUser.setCustomUserAttribute(key, (Integer) value);
    } else if (value instanceof Long) {
      appboyUser.setCustomUserAttribute(key, (Long) value);
    } else if (value instanceof String) {
      appboyUser.setCustomUserAttribute(key, (String) value);
    } else if (value instanceof Double) {
      appboyUser.setCustomUserAttribute(key, (Double) value);
    } else if (value instanceof Float) {
      appboyUser.setCustomUserAttribute(key, (Float) value);
    } else {
      AppboyLogger.w(TAG, "Failed to parse value into a custom "
          + "attribute accepted type. Key: '" + key + "' Value: '" + value + "'");
    }
  }

  private void changeUser(Map<String, Object> tagParameterMap) {
    String userId = String.valueOf(tagParameterMap.get(CHANGE_USER_ID_VARIABLE));
    Appboy.getInstance(sApplicationContext).changeUser(userId);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class BrazeGtmTagProvider : CustomTagProvider {

  override fun execute(map: MutableMap<String, Any>) {
    AppboyLogger.i(TAG, "Got google tag manager parameters map: $map")

    if (sApplicationContext == null) {
      AppboyLogger.w(TAG, "No application context provided to this tag provider.")
      return
    }

    if (!map.containsKey(ACTION_TYPE_KEY)) {
      AppboyLogger.w(TAG, "Map does not contain the braze action type key: $ACTION_TYPE_KEY")
      return
    }
    val actionType = map.remove(ACTION_TYPE_KEY).toString()

    when (actionType) {
      LOG_EVENT_ACTION_TYPE -> logEvent(map)
      CUSTOM_ATTRIBUTE_ACTION_TYPE -> setCustomAttribute(map)
      CHANGE_USER_ACTION_TYPE -> changeUser(map)
      else -> AppboyLogger.w(TAG, "Got unknown action type: $actionType")
    }
  }

  private fun logEvent(tagParameterMap: MutableMap<String, Any>) {
    val eventName = tagParameterMap.remove(EVENT_NAME_VARIABLE).toString()
    Appboy.getInstance(sApplicationContext).logCustomEvent(eventName, parseMapIntoProperties(tagParameterMap))
  }

  private fun parseMapIntoProperties(map: Map<String, Any>): AppboyProperties {
    val appboyProperties = AppboyProperties()
    map.forEach { param ->
      val key = param.key
      val value = param.value
      when (value) {
        is Boolean -> appboyProperties.addProperty(key, value)
        is Int -> appboyProperties.addProperty(key, value)
        is Date -> appboyProperties.addProperty(key, value)
        is Long -> appboyProperties.addProperty(key, value)
        is String -> appboyProperties.addProperty(key, value)
        is Double -> appboyProperties.addProperty(key, value)
        else -> AppboyLogger.w(TAG, "Failed to parse value into an AppboyProperties "
            + "accepted type. Key: '" + key + "' Value: '" + value + "'")
      }
    }

    return appboyProperties
  }

  private fun setCustomAttribute(tagParameterMap: Map<String, Any>) {
    val key = tagParameterMap[CUSTOM_ATTRIBUTE_KEY].toString()
    val value = tagParameterMap[CUSTOM_ATTRIBUTE_VALUE_KEY]

    val appboyUser = Appboy.getInstance(sApplicationContext).currentUser
    if (appboyUser == null) {
      AppboyLogger.w(TAG, "AppboyUser was null. Returning.")
      return
    }

    when (value) {
      is Boolean -> appboyUser.setCustomUserAttribute(key, (value as Boolean?)!!)
      is Int -> appboyUser.setCustomUserAttribute(key, (value as Int?)!!)
      is Long -> appboyUser.setCustomUserAttribute(key, (value as Long?)!!)
      is String -> appboyUser.setCustomUserAttribute(key, value as String?)
      is Double -> appboyUser.setCustomUserAttribute(key, (value as Double?)!!)
      is Float -> appboyUser.setCustomUserAttribute(key, (value as Float?)!!)
      else -> AppboyLogger.w(TAG, "Failed to parse value into a custom "
          + "attribute accepted type. Key: '" + key + "' Value: '" + value + "'")
    }
  }

  private fun changeUser(tagParameterMap: Map<String, Any>) {
    val userId = tagParameterMap[CHANGE_USER_ID_VARIABLE].toString()
    Appboy.getInstance(sApplicationContext).changeUser(userId)
  }

  companion object {
    private val TAG = AppboyLogger.getAppboyLogTag(BrazeGtmTagProvider::class.java!!)
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
     * Must be set before calling any of the below methods to
     * ensure that the proper application context is available when needed.
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

In your `Application.onCreate()` be sure to add the following initialization for the previous snippet:

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

#### Configuring Your Google Tag Manager {#configuring-android-google-tag-manager}

While your integration can be customized, the following is how our sample Google Tag Manager integration was setup for logging events.

First, create an "Event Name" trigger for `logEvent`:

![Event Name Trigger for events][3]

Next, create a "Function Call" tag that uses the classpath of the custom tag provider from before. This tag will be triggered using the `logEvent` trigger we just created. Note the `actionType` key being set to `logEvent` here. The custom Braze tag provider will use this key to determine what action to take with the Google Tag Manager data.

![Function Call Tag][4]

In the above tag are templated variables, such as `eventName` that allow you to use the same tag for multiple events on the fly without having to create a separate tag for each event in your app. The below variable is a "Firebase - Event Parameter" variable since Google Tag Manager for Android uses Firebase as the data layer.

![Tag Variable Event Name][6]

Lastly, log an event through Firebase/Google Tag Manager using the Firebase Analytics event name `logEvent`.

{% tabs %}
{% tab JAVA %}

```java
Bundle params = new Bundle();
params.putString("eventName", "played song event");
params.putBoolean("My Boolean Parameter", true);
params.putString("My String Parameter", "hello");
mFirebaseAnalytics.logEvent("logEvent", params);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val params = Bundle()
params.putString("eventName", "played tune event")
params.putBoolean("My Boolean Parameter", true)
params.putString("My String Parameter", "world")
mFirebaseAnalytics!!logEvent("logEvent", params)
```

{% endtab %}
{% endtabs %}

#### Logging Custom Attributes

Custom attributes are set via an `actionType` set to `customAttribute`.

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
mFirebaseAnalytics!!.logEvent("customAttribute", params)
```

{% endtab %}
{% endtabs %}

#### Calling ChangeUser

Calls to `changeUser()` are made via an `actionType` set to `changeUser`.

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
mFirebaseAnalytics!!.logEvent("changeUser", params)
```

{% endtab %}
{% endtabs %}


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration
[2]: https://developers.google.com/tag-manager/android/v5/
[3]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %}
[4]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %}
[5]: https://tagmanager.google.com/
[6]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %}
