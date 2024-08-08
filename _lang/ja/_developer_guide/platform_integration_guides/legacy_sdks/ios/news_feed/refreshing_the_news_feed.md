---
nav_title: フィードの更新
article_title: iOS のニュースフィードを更新する
platform: iOS
page_order: 6
description: "この参照記事では、iOS アプリケーションでニュースフィードを更新する方法について説明します。"
channel:
  - news feed

noindex: true
---

{% multi_lang_include archive/objective-c-deprecation-notice.md %}

# ニュースフィードの更新

{% alert note %}
ニュースフィードは非推奨になります。Braze では、ニュースフィードツールを使用しているお客様に、より柔軟でカスタマイズ可能で信頼性の高いコンテンツカードメッセージングチャネルに移行することをお勧めします。詳細については、[移行ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

`- (void) requestFeedRefresh;` を使用して、`Appboy.h` のユーザーのニュースフィードを更新するよう Braze に手動で要求できます。例:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestFeedRefresh];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestFeedRefresh()
```

{% endtab %}
{% endtabs %}

詳細については、`Appboy.h` の [ヘッダーファイル][15] を参照してください。


[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h ヘッダー ファイル"
