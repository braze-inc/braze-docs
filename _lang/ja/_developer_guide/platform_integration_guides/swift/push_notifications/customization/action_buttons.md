---
nav_title: アクションボタン
article_title: iOS 用プッシュアクションボタン
platform: Swift
page_order: 1
description: "この記事では、Swift SDK に関して、iOS プッシュ通知にアクションボタンを実装する方法について説明します。"
channel:
  - push

---

# アクションボタン {#push-action-buttons-integration}

> Braze Swift SDK では、プッシュアクションボタン用の URL 処理がサポートされています。 

Braze のデフォルトプッシュカテゴリのデフォルトプッシュアクションボタンには、4つのセット `Accept/Decline`、`Yes/No`、`Confirm/Cancel`、`More` があります。 

![2つのカスタマイズ可能なアクションボタンを表示するためにプルダウンされているプッシュメッセージのGIF。][13]{: style="max-width:60%"}

独自の通知カテゴリを作成する場合は、[アクションボタンカスタマイズ](#push-category-customization)を参照してください。

## 自動統合(推奨)

`configuration.push.automation`設定オプションを使用してプッシュを統合すると、Brazeは自動的にデフォルトプッシュカテゴリのアクションボタンを登録し、プッシュアクションボタンのクリック分析とURLルーティングを処理します。

## 手動統合

これらのプッシュアクションボタンs を手動で有効にするには、まずデフォルトプッシュカテゴリに登録します。次に、`didReceive(_:completionHandler:)` デリゲートメソッドを使用してプッシュアクションボタンs を有効にします。

### ステップ1:Braze デフォルトプッシュカテゴリの追加 {#registering}

\[プッシュ登録][36] を行うときに、次のコードを使用してデフォルトのプッシュカテゴリに登録します。

{% tabs %}
{% tab swift %}

```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
バックグラウンドアクティベーションモードでプッシュアクションボタンをクリックすると、通知が閉じられるだけで、アプリは開きません。ユーザーが次回アプリを開くと、これらのアクションのボタンクリック分析がサーバーにフラッシュされます。
{% endalert %}

### ステップ2:インタラクティブなプッシュ処理を有効にする {#enable-push-handling}

クリック分析や URL ルーティングを含むプッシュアクションボタンの処理を有効にするには、アプリの `didReceive(_:completionHandler:)` デリゲートメソッドに次のコードを追加します。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```

{% endtab %}
{% endtabs %}

`UNNotification` フレームワークを使用して、Braze [通知メソッド][39]を実装している場合は、このメソッドはすでに統合されています。 

## プッシュカテゴリのカスタマイズ

Brazeはデフォルトのプッシュカテゴリのセットを提供するだけでなく、カスタムの通知カテゴリとアクションもサポートしています。アプリケーションにカテゴリを登録すると、Braze ダッシュボードを使用してこれらのカスタム通知カテゴリをユーザーに送信できます。

その後、これらのカテゴリーをダッシュボードからプッシュ通知に割り当てて、デザインのアクションボタン構成をトリガーできます。 

### カスタムプッシュカテゴリの例

デバイスに表示される `LIKE_CATEGORY` を活用する例を次に示します。

![「いいねを取り消す」と「いいね」の2つのプッシュアクションボタンを表示するプッシュメッセージ][17]

#### ステップ1:カテゴリを登録する

以下のような方法で、アプリにカテゴリを登録します。

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like", options: [.foreground]),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
NSMutableSet<UNNotificationCategory *> *categories = [BRZNotifications.categories mutableCopy];

UNNotificationAction *likeAction = [UNNotificationAction actionWithIdentifier:@"LIKE_IDENTIFIER"
                                                                        title:@"Like"
                                                                      options:UNNotificationActionOptionForeground];

UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionForeground];

UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction, unlikeAction]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone];

[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
`UNNotificationAction` を作成するときに、アクションオプションのリストを指定できます。たとえば、`UNNotificationActionOptions.foreground` を使用して、ユーザーがアクションボタンをタップしてからアプリを開けるようにします。これは、「アプリを開く」や「アプリケーションにディープリンクする」などのナビゲーションクリック時の動作に必要です。詳細については、[`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions) を参照してください。
{% endalert %}

#### ステップ2:カテゴリを選択

カテゴリを登録したら、Braze ダッシュボードを使用して、そのタイプの通知をユーザーに送信します。

{% alert tip %}
アプリケーションにディープリンクしたり、URL を開いたりするアクションなど、_特殊なアクション_を含むアクションボタンの場合にのみ、カスタム通知カテゴリを定義する必要があります。通知を閉じるだけのアクションボタン用に定義する必要はありません。
{% endalert %}

1. Braze ダッシュボードで、**メッセージング**> **プッシュ通知**を選択し、iOS [プッシュキャンペーン]({{site.baseurl}}/docs/user_guide/message_building_by_channel/push/creating_a_push_message)を選択します。
2. \[**プッシュ通知を作成する**] の下で、\[**アクションボタン**] をオンにします。
3. \[**iOS 通知カテゴリ**] ドロップダウンで、\[**事前登録されたカスタム iOS カテゴリを入力**] を選択します。
4. 最後に、前に作成したカテゴリのいずれかを入力します。次の例では、カスタムカテゴリ`LIKE_CATEGORY` を使用します。

![カスタムカテゴリの設定を含むプッシュ通知 キャンペーン ダッシュボード。][18]

[13]: {% image_buster /assets/img_archive/iOS8Action.gif %}
[17]: {% image_buster /assets/img_archive/push_example_category.png %}
[18]: {% image_buster /assets/img_archive/ios-notification-category.png %}
[36]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze
[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling