---
nav_title: バッジ
article_title: iOS のプッシュ通知バッジ数
platform: iOS
page_order: 3.1
description: "この参考記事では、iOS プッシュ通知にバッジ数を実装する方法について説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include archive/objective-c-deprecation-notice.md %}

# バッジ

Braze ダッシュボードを通じてプッシュ通知を作成するときに、希望のバッジ数を指定できます。アプリケーションの [`applicationIconBadgeNumber`][20] プロパティまたは[リモート通知ペイロード][21]を使用して、バッジ数を手動で更新することもできます。Braze では、アプリがフォアグラウンドで動作しているときに Braze 通知を受信した場合にもバッジ 数はクリアされます。 

通常のアプリ操作の一部として、またはバッジをクリアするプッシュを送信してバッジをクリアする計画がない場合は、次のコードをアプリの `applicationDidBecomeActive:` デリゲートメソッドに追加してアプリがアクティブになったときにバッジをクリアする必要があります。

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

バッジ番号を 0 に設定すると、通知センターの通知も消去されることに注意してください。したがって、プッシュペイロードにバッジ番号を設定しない場合でも、バッジ番号を0に設定することで、ユーザーがプッシュをクリックした後に通知センターでプッシュ通知を削除できます。

[20]: https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber
[21]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1