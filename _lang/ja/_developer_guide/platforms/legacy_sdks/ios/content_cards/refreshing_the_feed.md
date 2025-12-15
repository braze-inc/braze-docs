---
nav_title: フィードの更新
article_title: iOS 用コンテンツカードフィードの更新
platform: iOS
page_order: 4
description: "この参考記事では、iOS アプリケーションでのコンテンツカード更新の実装について説明します。"
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# フィードの更新

## コンテンツカードの更新

`Appboy` インターフェースの `requestContentCardsRefresh:` メソッドを使用して、ユーザーのコンテンツカードを更新するように Braze に手動でリクエストできます。
{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestContentCardsRefresh];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestContentCardsRefresh()
```

{% endtab %}
{% endtabs %}

詳細については、`Appboy.h` の[ヘッダーファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h)を参照してください。
