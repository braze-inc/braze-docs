---
nav_title: カスタムイベントを記録する
article_title: Braze SDKによるカスタムイベントのログ記録
page_order: 3.1
description: "Braze SDKを通してカスタムイベントを記録する方法を学習する。"

---

# カスタムイベントのログ記録

> Braze SDKを通してカスタムイベントを記録する方法を学習する。

{% alert note %}
リストにないラッパーSDKについては、代わりに関連するAndroidまたはSwiftのネイティブ・メソッドを使用する。
{% endalert %}

## カスタムイベントをログに記録する

カスタムイベントを記録するには、以下のイベント・ロギング・メソッドを使用する。

{% tabs %}
{% tab Android %}
Androidネイティブの場合は、以下の方法が使える：

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

アプリに[Infillion Beaconを](https://infillion.com/software/beacons/)統合している場合、さらに`visit.getPlace()` 、ロケーション固有のイベントをログに記録することができる。`requestImmediateDataFlush` 、アプリがバックグラウンドでもイベントがログに記録されることを確認する。

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

{% tab ウェブ %}
標準的なWeb SDK実装の場合、以下の方法を使用できる：

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

代わりにGoogle Tagマネージャーを使用したい場合は、**カスタムイベントタグタイプを**使用して、[`logCustomEvent` メソッドを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)呼び出し、カスタムイベントプロパティをオプションで含めて、カスタムイベントをBrazeに送信することができる。そのためだ：

1. 変数を使用するか、イベント名を入力して、**Event Name**を入力します。
2. イベントプロパティを追加するには、**Add Row** ボタンを使用します。

![Braze アクションタグ構成設定を示すダイアログボックス。設定には、「タグタイプ」（カスタムイベント）、「イベント名」（ボタンクリック）、「イベントプロパティ」が含まれる。]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab Flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab React Native %}
```javascript
Braze.logCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab ロク %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```
{% endtab %}

{% tab Unity %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab Unreal Engine %}
```cpp
UBraze->LogCustomEvent(TEXT("YOUR_EVENT_NAME"));
```
{% endtab %}
{% endtabs %}

## メタデータ・プロパティを追加する

カスタムイベントをログに記録する際、イベントと一緒にプロパティ・オブジェクトを渡すことで、そのカスタムイベントに関するメタデータを追加するオプションがある。プロパティはキーと値のペアとして定義されています。キーは文字列で、値は `string`、`numeric`、`boolean`、または [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) オブジェクトになります。

メタデータ・プロパティを追加するには、以下のイベント・ロギング・メソッドを使用する。

{% tabs %}
{% tab Android %}
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

{% tab ウェブ %}
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

{% tab Flutter %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab React Native %}
```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```
{% endtab %}

{% tab ロク %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
{% endtab %}

{% tab Unity %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}

{% tab Unreal Engine %}
```cpp
TMap<FString, FString> Properties;
Properties.Add(TEXT("you"), TEXT("can"));
Properties.Add(TEXT("pass"), TEXT("false"));
Properties.Add(TEXT("orNumbers"), FString::FromInt(42));
Properties.Add(TEXT("orDates"), FDateTime::Now().ToString());
Properties.Add(TEXT("or"), TEXT("any,array,here")); // Arrays are stored as comma-separated strings
Properties.Add(TEXT("andEven"), TEXT("deeply:nested,json"));

UBraze->LogCustomEventWithProperties(TEXT("YOUR_EVENT_NAME"), Properties);
```
{% endtab %}
{% endtabs %}

{% alert important %}
`time` と`event_name` のキーは予約されており、カスタムイベントプロパティとして使用することはできない。
{% endalert %}
