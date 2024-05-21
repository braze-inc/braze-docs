---
nav_title: ニュースフィード
article_title: Xamarin のニュース フィード
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 3
description: "この記事では、Xamarin プラットフォームの iOS、Android、FireOS ニュース フィードの統合について説明します。"
channel: news feed 
---

# ニュースフィード統合

> この記事では、Xamarin プラットフォーム用に iOS、Android、および FireOS ニュース フィードを設定する方法について説明します。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

## Android

ニュースフィードを Xamarin Android アプリに統合する方法については、 [Android 統合の手順][1] を参照してください。 さらに、 [サンプル・アプリケーション][2] の実装サンプルも参照できます。

## iOS 

ニュース フィードを Xamarin iOS アプリに統合する方法については、 [iOS 統合の手順][11] を参照してください。 さらに、 [サンプル・アプリケーション][12] の実装サンプルも参照できます。

すべての実装オプションの中で、最も迅速に実装できるのはモーダルで、ViewControllerで次のようにして追加できます。

```csharp
// C#
ABKFeedViewControllerModalContext m = new ABKFeedViewControllerModalContext ();
this.PresentViewController (m, true, null);
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/integration/
[2]: https://github.com/braze-inc/braze-xamarin-sdk
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/
[12]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples
