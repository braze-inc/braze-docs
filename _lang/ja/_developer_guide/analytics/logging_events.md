---
nav_title: カスタムイベントのログ記録
article_title: Braze SDKによるカスタムイベントのログ記録
page_order: 3.1
description: "Braze SDKを通してカスタムイベントを記録する方法を学習する。"

---

# カスタムイベントのログ記録

> Braze SDKを通してカスタムイベントを記録する方法を学習する。

{% alert note %}
リストされていないラッパーSDK の場合は、代わりに関連するネイティブAndroid またはSwift メソッドを使用します。
{% endalert %}

## カスタムイベントをログに記録する

カスタムイベントを記録するには、以下のイベントロギングメソッドを使用します。

{% tabs %}
{% tab web %}
標準のWeb SDK 実装では、以下の方法を使用できます。

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

代わりにGoogle Tagマネージャーを使用したい場合は、**カスタムイベントタグタイプを**使用して、[`logCustomEvent` メソッドを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)呼び出し、カスタムイベントプロパティをオプションで含めて、カスタムイベントをBrazeに送信することができる。これを行う方法:

1. 変数を使用するか、イベント名を入力して、**Event Name**を入力します。
2. イベントプロパティを追加するには、**Add Row** ボタンを使用します。

![Braze アクションタグ構成設定を示すダイアログボックス。設定には、"タグ type"(カスタムイベント)、"event name"(ボタンクリック)、"event properties"が含まれます。]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab android %}
ネイティブ Android の場合は、次の方法を使用できます。

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab infillion %}
[Infillion Beacons](https://infillion.com/software/beacons/) を Android アプリに統合している場合は、オプションで `visit.getPlace()` を使用して位置情報固有のイベントをログに記録できます。`requestImmediateDataFlush` を使用すると、アプリがバックグラウンドで動作している場合でも、イベントが確実に記録されることが確認されます。

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
```javascript
Braze.logCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}
{% endtabs %}

## メタデータプロパティを追加する

カスタムイベントをログに記録する場合は、イベントとともにプロパティオブジェクトを渡すことで、そのカスタムイベントに関するメタデータを追加できます。プロパティはキーと値のペアとして定義されています。キーは文字列で、値は`string`、`numeric`、`boolean`、[`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) オブジェクト、配列、またはネストされたJSON オブジェクトです。

メタデータプロパティを追加するには、以下のイベントロギングメソッドを使用します。

{% tabs %}
{% tab web %}
```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can", 
  pass: false, 
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
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
{% endsubtab %}
{% subtab kotlin %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(
  name: "YOUR-EVENT-NAME",
  properties: [
    "you": "can",
    "pass": false,
    "orNumbers": 42,
    "orDates": Date(),
    "or": ["any", "array", "here"],
    "andEven": [
      "deeply": ["nested", "json"]
    ]
  ]
)
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR-EVENT-NAME"
                       properties:@{
  @"you": @"can",
  @"pass": @(NO),
  @"orNumbers": @42,
  @"orDates": [NSDate date],
  @"or": @[@"any", @"array", @"here"],
  @"andEven": @{
    @"deeply": @[@"nested", @"json"]
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab react native %}
```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}
{% endtabs %}

{% alert important %}
`time` および `event_name` キーは予約されているため、カスタムイベントプロパティとして使用できません。
{% endalert %}

## ベストプラクティス

カスタムイベントのプロパティーが予期されたとおりに記録されるように実行するには、次の3 つの重要な検査があります。

* [ロギングされるイベントを設定する](#verify-events)
* [ログを確認する](#verify-log)
* [値を確認する](#verify-values)

カスタムイベントがログに記録されるたびに、複数のプロパティーがログに記録されます。

### イベントを検証する

どのイベント・プロパティがトラッキングされているかを開発者に確認する。すべてのイベント・プロパティは大文字と小文字を区別することに留意してほしい。カスタム・イベントのトラッキングに関する追加情報については、プラットフォーム別に以下の記事を参照されたい：

* [Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
* [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
* [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)

### ログを確認する

イベント・プロパティが正常に追跡されていることを確認するには、**カスタム・イベント・**ページからすべてのイベント・プロパティを見ることができる。

1. [**データ設定**] > [**カスタムイベント**] に移動します。
2. リストからカスタムイベントを探す。
3. イベントの場合、**Manage Properties**を選択して、イベントに関連付けられているプロパティの名前を表示します。

### 値を確認する

[ ユーザーをテストユーザー]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#adding-test-users) として追加した後、次のステップに従い、値を確認します。 

1. アプリ内でカスタムイベントを実行する。
2. データがフラッシュされるまで約10秒待ちます。
3. [イベントユーザーログ]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/)を更新して、渡されたカスタムイベントとイベントプロパティの値を表示します。
