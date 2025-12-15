---
nav_title: バッジ
article_title: iOS 向けコンテンツカードバッジ
platform: iOS
page_order: 5
description: "この記事では、iOS アプリケーションのコンテンツカードにバッジを追加する方法について説明します。"
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# バッジ

## 未読コンテンツカードの数をリクエストする

ユーザーの未読コンテンツカードの数を表示するには、カード数をリクエストし、それをバッジで表示することをお勧めします。バッジは、コンテンツカードに新着コンテンツがあることをユーザーに知らせる優れた方法です。コンテンツカードにバッジを追加する必要がある場合、Braze SDK には以下のクエリを実行するメソッドが用意されています。

- 現在のユーザーの未閲覧コンテンツカードの数
- 現在のユーザーの閲覧可能なコンテンツカードの総数

[`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html) の次のメソッド宣言はこれについて詳しく説明したものです。

```objc
- (NSInteger)unviewedContentCardCount;
/*
This method returns the number of currently active Content Cards that have not been viewed.
A "view" happens when a card becomes visible in the Content Cards view. This differentiates between cards that are off-screen in the scrolling view and those which are on-screen; when a card scrolls onto the screen, it's counted as viewed.
Cards are counted as viewed only once -- if a card scrolls off the screen and back on, it's not re-counted.
Cards are counted only once, even if they appear in multiple Content Cards views or across multiple devices.
*/

- (NSInteger)contentCardCount;
/* 
This method returns the total number of currently active Content Cards. Cards are counted only once even if they appear in multiple Content Cards views.
 */
```

## アプリのバッジカウントに未閲覧コンテンツカードの数を表示する

バッジは、アプリのプッシュ通知リマインダーとして機能するだけでなく、ユーザーのコンテンツカードフィード内の未閲覧項目を示すために利用することもできます。未閲覧コンテンツカード数の最新情報に基づいてバッジカウントを更新すると、ユーザーをアプリに引き戻し、セッション数を増やすのに役立ちます。

このメソッドは、アプリが閉じられ、ユーザーのセッションが終了した後にバッジカウントを記録します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

このメソッド内で、次のコードを実装します。これにより、ユーザーが特定のセッション中にカードを閲覧している間にバッジカウントがアクティブに更新されます。

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].contentCardsController unviewedContentCardCount];
```

{% endtab %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

このメソッド内で、次のコードを実装します。これにより、ユーザーが特定のセッション中にカードを閲覧している間にバッジカウントがアクティブに更新されます。

```swift
UIApplication.shared.applicationIconBadgeNumber =
  Appboy.sharedInstance()?.contentCardsController.unviewedContentCardCount() ?? 0
```

{% endtab %}
{% endtabs %}

詳細については、`Appboy.h` の[ヘッダーファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h)を参照してください。
