---
nav_title: カスタムイベントのトラッキング
article_title: iOS のカスタムイベントのトラッキング
platform: iOS
page_order: 2
description: "このリファレンス記事では、iOS アプリケーションのカスタムイベントを追加して追跡する方法について説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS のカスタムイベントの追跡

Braze でカスタムイベントを記録することで、アプリの使用パターンに関する詳細を把握し、ダッシュボードでのアクションによってユーザーをセグメント化できます。

実装前に、[ベストプラクティス]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)のカスタムイベント、カスタム属性、および購入イベントによって提供されるセグメンテーションオプションの例と、[イベント命名規則]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/)のメモを必ず確認しておいてください。

## カスタムイベントの追加

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("YOUR_EVENT_NAME")
```

{% endtab %}
{% endtabs %}

### プロパティの追加

`NSNumber`、`NSString`、または `NSDate` の値が入力された `NSDictionary` を渡すことで、カスタムイベントに関するメタデータを追加できます。

{% tabs %}
{% tab OBJECTIVE-C %}

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
{% tab swift %}

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

詳細については、[クラスに関するドキュメント](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a4f0051d73d85cb37f63c232248124c79)を参照してください。

### 予約済みのキー {#event-reserved-keys}

以下のキーは予約されているため、カスタムイベントプロパティとして使用できません。

- `time`
- `event_name`

## その他のリソース

- `Appboy.h` [ファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h)内のメソッドの宣言を参照してください。 
- 詳細については、[`logCustomEvent` のドキュメント](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ad80c39e8c96482a77562a5b1a1d387aa) を参照してください。

