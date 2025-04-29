---
nav_title: Android용 Google Tag Manager
article_title: Android 및 FireOS용 Google Tag Manager
platform: 
  - Android
  - FireOS
page_order: 8
description: "이 참조 문서에서는 Google Tag Manager를 Android 또는 FireOS 앱에 초기화, 구성 및 구현하는 방법을 다룹니다."

---

# Android용 Google Tag Manager

> 이 참조 문서에서는 Google Tag Manager를 Android 또는 FireOS 앱에 초기화, 구성 및 구현하는 방법을 다룹니다.

## SDK 초기화 {#initializing-android-google-tag-provider}

Braze Android SDK는 [Google 태그 관리자](https://tagmanager.google.com/) 내에서 구성된 태그를 통해 초기화 및 제어할 수 있습니다.

이 구현의 전제 조건으로, [Android SDK 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration)이 완료되어야 합니다.

## Google Tag Manager {#configuring-android-google-tag-manager} 설정하기

이 예제에서는 사용자가 노래를 들을 때 다양한 이벤트를 기록하려는 음악 스트리밍 앱이라고 가정해 보겠습니다. Android용 Google Tag Manager를 사용하여 타사 공급업체가 이 이벤트를 수신하는지 제어하고 Braze에 특정한 태그를 생성할 수 있습니다.

### 사용자 지정 이벤트

커스텀 이벤트는 `actionType`이 `logEvent`로 설정되어 기록됩니다. 예제의 Braze 커스텀 태그 공급자는 `eventName`을 사용하여 커스텀 이벤트 이름을 설정한다고 예상합니다.

시작하려면 `played song`과 동일한 '이벤트 이름'을 찾는 트리거를 만듭니다.

!['이벤트 이름'이 '재생된 노래'와 같을 때 일부 이벤트에 대해 트리거되도록 설정된 Google 태그 관리자의 사용자 지정 트리거입니다.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

다음으로 새 태그(“함수 호출”)를 만들고 이 문서의 뒷부분에 설명된 [커스텀 태그 제공자](#adding-android-google-tag-provider)의 클래스 경로를 입력합니다.

이 태그는 방금 만든 `played song` 이벤트를 기록할 때 트리거됩니다.

태그의 커스텀 매개변수(키-값 페어)에서는 `eventName`을 `played song`으로 설정했으며, 이는 Braze에 기록되는 커스텀 이벤트 이름이 됩니다.

{% alert important %}
커스텀 이벤트를 보낼 때는 다음 스크린샷과 같이 `actionType`을 `logEvent`로 설정하고 `eventName`에 대한 값을 설정합니다.

이 예제에서 커스텀 태그 공급자는 이 키를 사용하여 Google Tag Manager에서 데이터를 수신할 때 수행할 작업과 Braze에 전송할 이벤트 이름을 결정합니다.
{% endalert %}

![클래스 경로 및 키-값 페어 필드에서 Google Tag Manager의 태그. 이 태그는 이전에 생성된 'played song' 트리거로 트리거되도록 설정됩니다.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

태그에 추가적인 키-값 페어 인수를 포함할 수 있습니다. 그러면 Braze에 커스텀 이벤트 속성정보로 전송됩니다. `eventName` 및 `actionType`은 커스텀 이벤트 속성정보에 대해 무시되지 않습니다. 다음 예제 태그에서는 `genre`를 전달합니다. 이 항목은 Google Tag Manager에서 태그 변수를 사용하여 정의되며, 해당 변수는 앱에 기록된 커스텀 이벤트에서 가져옵니다.

`genre` 이벤트 속성정보는 Android용 Google Tag Manager가 데이터 레이어로 Firebase를 사용하기 때문에 'Firebase - 이벤트 매개변수' 변수로 Google Tag Manager에 전송됩니다.

![Google Tag Manager의 변수로, "Braze - Played Song Event" 태그에 "genre"가 이벤트 매개변수로 추가됩니다.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

마지막으로, 사용자가 앱에서 노래를 재생하면 Firebase 및 Google Tag Manager를 통해 태그의 트리거 이름(`played song`)과 일치하는 Firebase 분석 이벤트 이름을 사용하여 이벤트를 기록합니다.

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

### 커스텀 속성 로깅

`actionType`을 `customAttribute`로 설정하여 커스텀 속성은 설정됩니다. Braze 커스텀 태그 공급자는 `customAttributeKey` 및 `customAttributeValue`를 통해 커스텀 속성 키-값을 설정한다고 예상합니다.

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

### changeUser 호출

`actionType`을 `changeUser`로 설정하고 `changeUser()`에 대한 호출이 수행됩니다. Braze 커스텀 태그 공급자는 태그 내 `externalUserId` 키-값 페어를 통해 Braze 사용자 ID를 설정한다고 예상합니다.

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

## Braze SDK 커스텀 태그 공급자 {#adding-android-google-tag-provider}

태그 및 트리거를 설정한 상태에서 Google Tag Manager를 Android 앱에서도 구현해야 합니다(Google [설명서](https://developers.google.com/tag-manager/android/v5/) 참조).

앱에 Google Tag Manager를 설치한 후 Google Tag Manager 내에서 구성한 태그를 기반으로 Braze SDK 메서드를 호출하기 위해 커스텀 태그 제공자를 추가합니다.

"클래스 경로"를 파일에 기록해 두십시오. 이는 [Google Tag Manager](https://tagmanager.google.com/) 콘솔에서 태그를 설정할 때 입력할 내용입니다.

이 예제에서는 커스텀 태그 공급자를 구성하는 여러 가지 방법 중 하나를 보여줍니다. 여기서는 Google Tag Manager에서 전송된 `actionType` 키-값 페어에 따라 호출할 Braze SDK 메서드를 결정합니다.

이 예제에서 지원되는 `actionType`은 `logEvent`, `customAttribute`, `changeUser`이지만, 태그 공급자가 Google Tag Manager에서 데이터를 처리하는 방식을 변경할 수도 있습니다.

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

`Application.onCreate()`에서 이전 스니펫에 대해 다음 초기화를 추가합니다.

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

