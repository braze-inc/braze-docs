---
nav_title: ニュースフィード
article_title: tvOS 向けニュースフィード
platform: tvOS
page_order: 10
page_type: reference
description: "このページでは、tvOS アプリケーションでニュースフィードデータを取得して表示する方法について説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# ニュースフィード統合

> この記事では、tvOS プラットフォーム用のニュースフィードを設定する方法について説明します。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

## tvOS フィードの統合

tvOS SDK はニュースフィードデータの取得をサポートしているため、独自のカスタム UI を使用してアプリケーションにニュースフィードを表示できます。ニュースフィードを取得するには、次のメソッドを呼び出し、クラスを調べて各カードを解析します。

{% tabs %}
{% tab 目標-C %}

```objc
NSArray *feedCards =  [[Appboy sharedInstance].feedController getNewsFeedCards];
```

{% endtab %}
{% tab 速い %}

```swift
let feedCards = Appboy.sharedInstance()?.feedController.newsFeedCards
```

{% endtab %}
{% endtabs %}
