---
nav_title: Google Tag Manager for Android
article_title: Android と FireOS 用の Google Tag Manager for Android
platform: 
  - Android
  - FireOS
page_order: 8
description: "このリファレンス記事では、Google Tag Manager を初期化、構成、Android アプリや FireOS アプリに実装する方法について説明します。"

---

# Google Tag Manager for Android

> このリファレンス記事では、Google Tag Manager を初期化、構成、Android アプリや FireOS アプリに実装する方法について説明します。

## SDK の初期化{#initializing-android-google-tag-provider}

Braze Android SDK は、[Google Tag Manager][5] 内で設定されたタグによって初期化および制御できます。

この実装の前提条件として、[Android SDK の統合][1]が完了している必要があります。

## Google Tag Manager の設定 {#configuring-android-google-tag-manager}

この例は、ユーザーが曲を聴いている間に別のイベントをロギングする必要がある音楽ストリーミングアプリを想定しています。Google Tag Manager for Android を使用して、どのサードパーティベンダーがこのイベントを受信し、Braze 固有のタグを作成するのかを制御できます。

### カスタムイベント

カスタムイベントは、`logEvent` に設定した `actionType` によってログに記録されます。この例の Braze カスタムタグプロバイダーは、`eventName` を使用してカスタムイベント名を設定することを想定しています。

最初に、`played song` である「イベント名」を検索するトリガーを作成します

![「eventName」が「played song」である場合に一部のイベントに対してトリガーするよう設定された Google Tag Manager のカスタムトリガー。][3]

次に、新しいタグ (「Function Call」) を作成し、この記事で後述する[カスタムタグプロバイダー](#adding-android-google-tag-provider)のクラスパスを入力します。

このタグは、先ほど作成した `played song` イベントをロギングするとトリガーされます。

タグのカスタムパラメーター (キーと値のペア) では、`played song`を`eventName`に設定しました。これは Braze に記録されるカスタムイベント名になります。

{% alert important %}
カスタムイベントを送信するときは、必ず `actionType` を `logEvent` に設定し、`eventName` の値を次のスクリーンショットのように設定します。

この例のカスタムタグプロバイダーは、これらのキーを使用して、Google Tag Manager からデータを受信したときに Braze に送信するアクションと送信するイベント名を決定します。
{% endalert %}

![classpath フィールドと、キーと値のペアフィールドを含む Google Tag Manager のタグ。このタグは、事前に作成した「played song」トリガーによってトリガーするよう設定されている。][4]

また、追加のキーと値のペア引数をタグに含めることもできます。この引数は、カスタムイベントプロパティとして Braze に送信されます。`eventName` および `actionType` は、カスタムイベントプロパティで無視されません。次のサンプルタグでは、`genre` で引数を渡します。これは、Google Tag Manager でタグ変数を使用して定義されており、アプリでロギングしたカスタムイベントから取得されます。

`genre` イベントプロパティが、「Firebase - Event Parameter」変数として Google Tag Manager に送信されます。Google Tag Manager for Android では、Firebase がデータレイヤーとして使用されるためです。

![「genre」が「Braze - Played Song Event」タグのイベントパラメーターとして追加される Google Tag Manager の変数。][6]

最後に、ユーザーがアプリで曲を再生すると、タグのトリガー名 `played song` と一致する Firebase 分析イベント名を使用し、Firebase と Google Tag Manager を介してイベントがロギングされます。

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
mFirebaseAnalytics!!logEvent("played song", params)
```

{% endtab %}
{% endtabs %}

### カスタム属性のロギング

カスタム属性は、 `customAttribute` に設定された `actionType` を介して設定されます。Braze カスタムタグプロバイダーは、カスタム属性のキーと値が `customAttributeKey` および `customAttributeValue` を介して設定されることを想定しています。

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

### changeUser の呼び出し

`changeUser()` の呼び出しは、`changeUser` に設定された `actionType` を介して行われます。Braze カスタムタグプロバイダーは、Braze ユーザー ID がタグ内のキーと値のペア `externalUserId` を介して設定されることを想定しています。

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

## Braze SDK カスタムタグプロバイダー {#adding-android-google-tag-provider}

タグとトリガーが設定されたら、Android アプリに Google Tag Manager を実装する必要もあります。これについては、Google の[ドキュメント][2]に記載されています。

Google Tag Manager がアプリにインストールされたら、カスタムタグプロバイダーを追加し、Google Tag Manager 内で設定したタグに基づいて Braze SDK メソッドを呼び出します。

ファイルに「クラスパス」を必ず書き留めておいてください。[Google Tag Manager][5] コンソールでタグを設定する際に、これを入力します。

この例は、カスタムタグプロバイダーを構築する多くの方法の 1 つを示しています。ここでは、GTM タグから送信されたキーと値のペア `actionType` に基づいて、呼び出す Braze SDK メソッドを決定します。

この例でサポートされている `actionType` は `logEvent`、`customAttribute`、`changeUser` ですが、タグプロバイダーによる Google Tag Manager からのデータの処理方法を変更することもできます。

{% tabs %}
{% tab JAVA %}

\`\`\`java
public class BrazeGtmTagProvider implements CustomTagProvider {
  private static final String TAG = BrazeLogger.getBrazeLogTag(BrazeGtmTagProvider.class);
  private static final String ACTION\_TYPE\_KEY = "actionType";

  // カスタムイベント
  private static final String LOG\_EVENT\_ACTION\_TYPE = "logEvent";
  private static final String EVENT\_NAME\_VARIABLE = "eventName";

  // カスタム属性
  private static final String CUSTOM\_ATTRIBUTE\_ACTION\_TYPE = "customAttribute";
  private static final String CUSTOM\_ATTRIBUTE\_KEY = "customAttributeKey";
  private static final String CUSTOM\_ATTRIBUTE\_VALUE\_KEY = "customAttributeValue";

  // ユーザーを変更
  private static final String CHANGE\_USER\_ACTION\_TYPE = "changeUser";
  private static final String CHANGE\_USER\_ID\_VARIABLE = "externalUserId";

  private static Context sApplicationContext;

  /**
* Must be set before calling any of the follwing methods to
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
    String eventName = String.valueOf(tagParameterMap.remove(EVENT\_NAME\_VARIABLE));
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
    String key = String.valueOf(tagParameterMap.get(CUSTOM\_ATTRIBUTE\_KEY));
    Object value = tagParameterMap.get(CUSTOM\_ATTRIBUTE\_VALUE\_KEY);

    BrazeUser brazeUser = Braze.getInstance(sApplicationContext).getCurrentUser();
    if (brazeUser == null) {
      BrazeLogger.w(TAG, "BrazeUser was null. Returning.");
      return;
    }

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

  private void changeUser(Map<String, Object> tagParameterMap) {
    String UserID = String.valueOf (TagParameterMap.GET (CHANGE\_USER\_ID\_VARIABLE));
    Braze.getInstance(sApplicationContext).changeUser(userId);
  }
}
\`\`\`

{% endtab %}
{% tab KOTLIN %}

\`\`\`kotlin
class BrazeGtmTagProvider :CustomTagProvider {

  override fun execute(map:MutableMap<String, Any>) {
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

  private fun logEvent(tagParameterMap:MutableMap<String, Any>) {
    val eventName = tagParameterMap.remove(EVENT\_NAME\_VARIABLE).toString()
    Braze.getInstance(sApplicationContext).logCustomEvent(eventName, parseMapIntoProperties(tagParameterMap))
  }

  private fun parseMapIntoProperties(map:Map<String, Any>):BrazeProperties {
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

  private fun setCustomAttribute(tagParameterMap:Map<String, Any>) {
    val key = tagParameterMap[CUSTOM\_ATTRIBUTE\_KEY].toString()
    val value = tagParameterMap[CUSTOM\_ATTRIBUTE\_VALUE\_KEY]

    val brazeUser = Braze.getInstance(sApplicationContext).currentUser
    if (brazeUser == null) {
      BrazeLogger.w(TAG, "BrazeUser was null. Returning.")
      return
    }

    when (value) {
      is Boolean -> brazeUser.setCustomUserAttribute(key, (value as Boolean?)!!)
      is Int -> brazeUser.setCustomUserAttribute(key, (value as Int?)!!)
      is Long -> brazeUser.setCustomUserAttribute(key, (value as Long?)!!)
      is String -> brazeUser.setCustomUserAttribute(key, value as String?)
      is Double -> brazeUser.setCustomUserAttribute(key, (value as Double?)!!)
      is Float -> brazeUser.setCustomUserAttribute(key, (value as Float?)!!)
      else -> BrazeLogger.w(TAG, "Failed to parse value into a custom "
          + "attribute accepted type. Key: '" + key + "' Value: '" + value + "'")
    }
  }

  private fun changeUser(tagParameterMap:Map<String, Any>) {
    val userId = tagParameterMap[CHANGE\_USER\_ID\_VARIABLE].toString()
    Braze.getInstance(sApplicationContext).changeUser(userId)
  }

  companion object {
    private val TAG = BrazeLogger.getBrazeLogTag(BrazeGtmTagProvider::class.java!!)
    private val ACTION\_TYPE\_KEY = "actionType"

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
     * Must be set before calling any of the following methods to
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
\`\`\`

{% endtab %}
{% endtabs %}

`Application.onCreate()` で、前のスニペットに次の初期化を必ず追加してください。

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

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration
[2]: https://developers.google.com/tag-manager/android/v5/
[3]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %}
[4]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %}
[5]: https://tagmanager.google.com/
[6]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %}
