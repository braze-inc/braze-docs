---
nav_title: カスタムイベントのトラッキング
article_title: Android と FireOS のカスタムイベントのトラッキング
platform: 
  - Android
  - FireOS
page_order: 2
description: "このリファレンス記事では、Android または FireOS アプリケーションのカスタムイベントを追加および追跡する方法について説明します。"

---

# カスタムイベントのトラッキング

> Braze でカスタムイベントを記録することで、アプリの使用パターンに関する詳細を把握し、ダッシュボードでのアクションによってユーザーをセグメント化できます。このリファレンス記事では、Android または FireOS アプリケーションのカスタムイベントを追加および追跡する方法について説明します。

実装前に、[分析の概要][0]のカスタムイベント、カスタム属性、および購入イベントによって提供されるセグメンテーションオプションの例と、[イベント命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)のメモを必ず確認してください。

## カスタムイベントの追加

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```

{% endtab %}
{% endtabs %}

詳細については、[KDoc][2] を参照してください。

### プロパティの追加

カスタムイベントに関するメタデータを追加するには、カスタムイベントとともに [Braze プロパティオブジェクト][4]を渡します。

プロパティはキーと値のペアとして定義されています。キーは `String` オブジェクトで、値は `String`、`int`、`float`、`boolean`、または [`Date`][3] オブジェクトになります。

{% tabs %}
{% tab JAVA %}

```java
Braze.logCustomEvent("YOUR-EVENT-NAME",
    new BrazeProperties(new JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", new Date())
        .put("or", new JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", new JSONObject()
            .put("deeply", new JSONArray()
                .put("nested")
                .put("json"))
        )
));
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.logCustomEvent("YOUR-EVENT-NAME",
    BrazeProperties(JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", Date())
        .put("or", JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", JSONObject()
            .put("deeply", JSONArray()
                .put("nested")
                .put("json"))
        )
))
```

{% endtab %}
{% endtabs %}

### 予約済みのキー

以下のキーは予約されているため、カスタムイベントプロパティとして使用できません。

- `time`
- `event_name`

詳細については、[KDoc][2] を参照してください。

[0]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html
[3]: http://developer.android.com/reference/java/util/Date.html
[4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html
