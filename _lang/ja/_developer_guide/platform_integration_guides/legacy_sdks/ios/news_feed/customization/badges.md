---
nav_title: バッジ
article_title: iOS 用ニュースフィードバッジ
platform: iOS
page_order: 3
description: "この参照記事では、iOS アプリケーションにニュースフィードのバッジカウントを実装する方法について説明します。"
channel:
  - news feed

noindex: true
---

{% multi_lang_include archive/objective-c-deprecation-notice.md %}

# バッジ

{% alert note %}
ニュースフィードは非推奨になります。Braze では、ニュースフィードツールを使用しているお客様に、より柔軟でカスタマイズ可能で信頼性の高いコンテンツカードメッセージングチャネルに移行することをお勧めします。詳細については、[移行ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

## 未読のニュースフィードカードカウントのリクエスト

![][45]{: style="float:right;max-width:25%;margin-left:15px;"}

バッジは、ニュースフィードでユーザーを待っている新しいコンテンツへ注意を喚起する優れた方法です。ニュースフィードにバッジを追加したい場合、Braze SDK には次のクエリを実行するメソッドが用意されています。

- 現在のユーザーの未読のニュースフィードカード
- 現在のユーザーが閲覧できるニュースフィードカードの合計数

[\`ABKFeedController\`][44] の次のメソッド宣言でこれについて詳しく説明します。

\`\`\`
\- (NSInteger)unreadCardCountForCategories:(ABKCardCategory)categories;
/*
This method returns the number of currently active Content Cards that have not been viewed.
A "view" happens when a card becomes visible in the Content Cards view. This differentiates between cards that are off-screen in the scrolling view and those which are on-screen; when a card scrolls onto the screen, it's counted as viewed.
Cards are counted as viewed only once -- if a card scrolls off the screen and back on, it's not re-counted.
Cards are counted only once, even if they appear in multiple Content Cards views or across multiple devices.
*/

- (NSInteger)cardCountForCategories:(ABKCardCategory)categories;
/*
This method returns the total number of currently active Content Cards. Cards are counted only once, even if they appear in multiple Content Cards views.
*/
\`\`\`

## ニュースフィードの未読項目の数をアプリバッジ数に表示する

バッジは、アプリのプッシュ通知リマインダーとして機能するだけでなく、ユーザーのニュースフィード内の未表示の項目を示すこともできます。未読のニュースフィードの更新に基づいてバッジ数を更新することは、ユーザーをアプリに引き戻し、セッションを増やすための貴重な手段となります。

アプリが閉じられ、ユーザーのセッションが終了した後にバッジ数を記録するこのメソッドを呼び出します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

{% endtab %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

{% endtab %}
{% endtabs %}

このメソッド内で、ユーザーが特定のセッション中にカードを表示している間にバッジ数をアクティブに更新する次のコードを実装します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].feedController unreadCardCountForCategories:ABKCardCategoryAll];
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = Appboy.sharedInstance()?.feedController.unreadCardCount(forCategories: ABKCardCategory.all) ?? 0
```

{% endtab %}
{% endtabs %}

任意の時点で、たとえば `applicationDidBecomeActive` メソッドで、次のコードを使用してバッジ数をクリアします。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% endtabs %}

詳細については、`Appboy.h` の[ヘッダーファイル][15]を参照してください。

[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h ヘッダー ファイル"
[42]: {% image_buster /assets/img_archive/badge_example.png %} 「バッジの例」
[44]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk feed controller"
[45]: {% image_buster /assets/img_archive/newsfeed_badges.png %}