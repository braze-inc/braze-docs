---
nav_title: カスタムイベントのトラッキング
article_title: iOS のカスタムイベントのトラッキング
platform: Swift
page_order: 2
description: "このリファレンス記事では、Swift SDK のカスタムイベントを追加し、トラッキングする方法を説明します。"

---

# カスタムイベントのトラッキング

> Braze でカスタムイベントを記録することで、アプリの使用パターンに関する詳細を把握し、ダッシュボードでのアクションによってユーザーをセグメント化できます。

実装前に、[ベストプラクティス][0]のカスタムイベント、カスタム属性、および購入イベントによって提供されるセグメンテーションオプションの例と、[イベント命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)のメモを必ず確認してください。

## カスタムイベントの追加

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% endtabs %}

### プロパティの追加

`Int`、`Double`、`String`、`Bool`、または `Date` の値が入力された `Dictionary` を渡すことで、カスタムイベントに関するメタデータを追加できます。

{% tabs %}
{% tab swift %}

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

{% endtab %}
{% tab OBJECTIVE-C %}

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

{% endtab %}
{% endtabs %}

### 予約済みのキー {#event-reserved-keys}

以下のキーは予約されているため、カスタムイベントプロパティとして使用できません。

- `time`
- `event_name`

## その他のリソース

- 詳細については、[`logCustomEvent` のドキュメント][1] を参照してください。

[0]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[1]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logcustomevent(name:properties:fileid:line:) "logcustomevent ドキュメント"
