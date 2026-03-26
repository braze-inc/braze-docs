---
nav_title: カスタムイベントをログに記録する
article_title: Braze SDKを通じてカスタムイベントをログに記録する
page_order: 3.1
description: "Braze SDKを通してカスタムイベントを記録する方法を学習する。"

---

# カスタムイベントをログに記録する

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

![Braze アクションタグ構成設定を示すダイアログボックス。設定項目には「タグタイプ」（カスタムイベント）、「イベント名」（ボタンクリック）、「イベントプロパティ」が含まれる。]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
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

{% tab cordova %}
Braze Cordovaプラグインメソッドを使う：

```javascript
BrazePlugin.logCustomEvent("YOUR_EVENT_NAME");
```

この`logCustomEvent`APIは以下を受け付ける：
- `eventName` (必須の文字列):最大255文字まで使用できる。名前を . `$`で始めてはいけない。英数字と句読点を使え。
- `eventProperties` (オプションのオブジェクト):イベントメタデータ用のキーと値のペアを追加する。キーは最大255文字まで使用し、キーを . `$`で始めてはいけない。

プロパティ値には、文字列（最大255文字）、`numeric`数値`boolean`、配列、または`string`ネストされたJSONオブジェクトを使用する。

実装の詳細については、Braze Cordova SDK のソースを参照すること。
- [`www/BrazePlugin.js` `logCustomEvent` メソッド（138行目から140行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L138-L140)
- [`www/BrazePlugin.js` JSDoc（128行目から140行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Androidハンドラー`src/android/BrazePlugin.kt`（108行目から115行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [iOSハンドラー（`src/ios/BrazePlugin.m`308行目から313行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
- [iOSメソッド宣言`src/ios/BrazePlugin.h`（24行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.h#L24)
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

カスタムイベントを記録する際、そのイベントにプロパティオブジェクトを渡すことで、そのカスタムイベントに関するメタデータを追加する選択肢がある。プロパティはキーと値のペアとして定義されています。キーは文字列であり、値はオブジェクト[`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp)、配列`numeric`、またはネストされたJSON`boolean`オブジェクトである`string`。

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

{% tab cordova %}
プロパティオブジェクトを使ってカスタムイベントをログに記録する：

```javascript
var properties = {};
properties["key1"] = "value1";
properties["key2"] = ["value2", "value3"];
properties["key3"] = false;
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", properties);
```

プロパティをインラインで渡すこともできる：

```javascript
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", {
  "key": "value",
  "amount": 42,
});
```

公式のCordovaサンプルアプリには、文字列、数値、ブール値、配列、およびネストされたオブジェクトのプロパティが含まれている。
- [`sample-project/www/js/index.js` (230行目から251行目)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/sample-project/www/js/index.js#L230-L251)

サンプルプロジェクトの抜粋：

```javascript
var properties = {};
properties["One"] = "That's the Way of the World";
properties["Two"] = "After the Love Has Gone";
properties["Three"] = "Can't Hide Love";
BrazePlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
BrazePlugin.logCustomEvent("cordovaCustomEventWithoutProperties");
BrazePlugin.logCustomEvent("cordovaCustomEventWithFloatProperties", {
  "Cart Value": 4.95,
  "Cart Item Name": "Spicy Chicken Bites 5 pack"
});
BrazePlugin.logCustomEvent("cordovaCustomEventWithNestedProperties", {
  "array key": [1, "2", false],
  "object key": {
    "k1": "1",
    "k2": 2,
    "k3": false,
  },
  "deep key": {
    "key": [1, "2", true]
  }
});
```

APIとネイティブブリッジの詳細については、以下を参照のこと：
- [`www/BrazePlugin.js` JSDoc（128行目から140行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Androidハンドラー`src/android/BrazePlugin.kt`（108行目から115行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [iOSハンドラー（`src/ios/BrazePlugin.m`308行目から313行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
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

カスタムイベントのプロパティが期待通りに記録されるようにするには、次の3つの重要な確認事項を実施する必要がある：

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
3. イベントについては、**[プロパティの管理]**を選択すると、そのイベントに関連付けられたプロパティの名前が表示される。

### 値を確認する

[テストユーザーとしてユーザーを追加]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#adding-test-users)した後、以下のステップで値を確認する： 

1. アプリ内でカスタムイベントを実行する。
2. データがフラッシュされるまで約10秒待ちます。
3. [イベントユーザーログ]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/)を更新して、渡されたカスタムイベントとイベントプロパティの値を表示します。
