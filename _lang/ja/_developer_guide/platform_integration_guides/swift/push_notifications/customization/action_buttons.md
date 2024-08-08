---
nav_title: アクションボタン
article_title: iOS 用プッシュアクションボタン
platform: Swift
page_order: 1
description: "この記事では、Swift SDKのiOSプッシュ通知にアクションボタンを実装する方法について説明します。"
channel:
  - push

---

# アクションボタン {#push-action-buttons-integration}

> Braze Swift SDK は、プッシュアクションボタンのURL 処理をサポートしています。 

Braze のデフォルトのプッシュ・アクション・ボタンには、`Accept/Decline`、`Yes/No`、`Confirm/Cancel`、および`More` の4 セットがあります。 

![プッシュメッセージをプルダウンしてカスタマイズ可能な2つのアクションボタンを表示する GIF][13]

独自のカスタム通知カテゴリーを作成する場合は、[アクションボタンのカスタマイズ][37] を参照してください。

## 自動統合(推奨)

`configuration.push.automation` 設定オプションを使用してプッシュを統合すると、Braze はデフォルトのプッシュカテゴリのアクションボタンを自動的に登録し、プッシュアクションボタンのクリックアナリティクスとURL ルーティングを処理します。

## 手動統合

これらのプッシュアクションボタンを手動で有効にするには、最初にデフォルトのプッシュカテゴリを登録します。次に、`didReceive(_:completionHandler:)` デリゲートメソッドを使用して、プッシュアクションボタンを有効にします。

### ステップ 1:Braze のデフォルトのプッシュカテゴリの追加 {#registering}

[プッシュ登録][36] を行うときに、次のコードを使用してデフォルトのプッシュカテゴリーに登録します。

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

### ステップ 2: インタラクティブなプッシュ処理を有効にする {#enable-push-handling}

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

`UNNotification` フレームワークを使用し、Braze [notification methods][39] を実装している場合、このメソッドはすでに統合されている必要があります。 

## プッシュカテゴリのカスタマイズ

Brazeは [デフォルトのプッシュカテゴリ][2] のセットを提供するだけでなく、カスタムの通知カテゴリとアクションもサポートしています。アプリケーションにカテゴリを登録したら、Braze ダッシュボードを使用して、これらのカスタム通知カテゴリをユーザに送信できます。

その後、これらのカテゴリーをダッシュボードからプッシュ通知に割り当てて、デザインのアクションボタン構成をトリガーできます。 

### カスタムプッシュカテゴリの例

デバイスに表示される `LIKE_CATEGORY` を活用する例を次に示します。

![「いいねを取り消す」と「いいね」の2つのプッシュアクションボタンを表示するプッシュメッセージ][17]

アプリケーションにカテゴリを登録するには、次のコードスニペットを参照してください。

{% alert note %}
`UNNotificationAction` を作成する場合、アクションオプションのリストを指定できます。たとえば、`UNNotificationActionOptions.foreground` を追加すると、ユーザーはアクションボタンをクリックしたときにアプリを開くことができます。これは、"Open App"および"Deep Link into Application"など、アプリにナビゲートするBraze on-click ビヘイビアに必要です。

使用方法の詳細については、[`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions)を参照してください。
{% endalert %}

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
                                                                              actions:@[likeAction,
                                                                                        unlikeAction
                                                                                      ]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone
];
[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

アプリケーションにカテゴリを登録したら、Braze ダッシュボードを使用してそのタイプの通知をユーザに送信します。カスタム通知カテゴリを、プッシュコンポーザーの**Compose**ステップで定義します。 

1. **アクションボタン**がオンになっていることを確認します。 
2. **iOS Notification Category**の場合は、**登録済みのカスタムiOS Category**を入力します。
3. 前に定義したカテゴリを入力します(`LIKE_CATEGORY` など)。

![カスタムカテゴリのセットアップを含むプッシュ通知キャンペーンダッシュボード。][18]

[13]: {% image_buster /assets/img_archive/iOS8Action.gif %}
[17]: {% image_buster /assets/img_archive/push_example_category.png %}
[18]: {% image_buster /assets/img_archive/ios-notification-category.png %}
[36]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze
[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling