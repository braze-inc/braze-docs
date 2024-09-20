---
nav_title: カスタムイベントの追跡
article_title: iOS のカスタムイベントの追跡
platform: iOS
page_order: 2
description: "このリファレンス記事では、iOS アプリケーションのカスタムイベントを追加して追跡する方法について説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS のカスタムイベントの追跡

Braze でカスタムイベントを記録することで、アプリの使用パターンに関する詳細を把握し、ダッシュボードでのアクションによってユーザーをセグメント化できます。

実装前に、[ベストプラクティス][0]のカスタムイベント、カスタム属性、および購入イベントによって提供されるセグメンテーションオプションの例と、[イベント命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)のメモを必ず確認しておいてください。

## カスタムイベントの追加

{% tabs %}
{% tab 目標-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% tab 速い %}

```swift
Appboy.sharedInstance()?.logCustomEvent("YOUR_EVENT_NAME")
```

{% endtab %}
{% endtabs %}

### プロパティの追加

`NSNumber`、`NSString`、または `NSDate` の値が入力された `NSDictionary` を渡すことで、カスタムイベントに関するメタデータを追加できます。

{% tabs %}
{% tab 目標-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR-EVENT-NAME"
                         withProperties:@{
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

{% endtab %}
{% tab 速い %}

```swift
Appboy.sharedInstance()?.logCustomEvent(
  "YOUR-EVENT-NAME",
  withProperties: [
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

{% endtab %}
{% endtabs %}

詳細については、[クラスに関するドキュメント][4]を参照してください。

### 予約済みのキー {#event-reserved-keys}

以下のキーは予約されているため、カスタムイベントプロパティとして使用できません。

- `time`
- `event_name`

## その他のリソース

- `Appboy.h` [ファイル][2]内のメソッドの宣言を参照してください。 
- 詳細については、[`logCustomEvent`][3] のドキュメントを参照してください。

[0]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[3]: http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ad80c39e8c96482a77562a5b1a1d387aa "logcustomevent のドキュメント"
[4]: http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a4f0051d73d85cb37f63c232248124c79 "logcustomevent:withproperties のドキュメント"
