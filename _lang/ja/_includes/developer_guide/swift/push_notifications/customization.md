{% multi_lang_include developer_guide/prerequisites/swift.md %} また、[プッシュ通知s]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)を設定する必要があります。

## アクションキーのカスタマイズ {#push-action-buttons-integration}

Braze Swift SDK では、プッシュアクションボタン用の URL 処理がサポートされています。Braze のデフォルトプッシュカテゴリのデフォルトプッシュアクションボタンには、4つのセット `Accept/Decline`、`Yes/No`、`Confirm/Cancel`、`More` があります。

![2つのカスタマイズ可能なアクションボタンを表示するためにプルダウンされているプッシュメッセージのGIF。]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

### アクションを手動で登録する

{% alert important %}
手動でプッシュアクションボタンを登録することはお勧めしません。
{% endalert %}

[ で`configuration.push.automation` 設定オプションを使用してプッシュ通知s]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) を設定した場合、Braze はデフォルトプッシュカテゴリのアクションボタンを自動的に登録し、プッシュアクションボタンのクリック分析とURL ルーティングを処理します。

ただし、代わりにプッシュアクションボタンsを手動で登録することもできます。

#### ステップ 1: Braze デフォルトプッシュカテゴリの追加 {#registering}

[register for push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze) の場合、デフォルトのプッシュカテゴリに登録するには、次のコードを使用します。

{% tabs %}
{% tab swift %}
a
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

#### ステップ2:インタラクティブなプッシュ処理を有効にする {#enable-push-handling}

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

`UNNotification` フレームワークを使用し、Braze [通知メソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling) を実装した場合、このメソッドはすでに統合されている必要があります。 

## プッシュカテゴリのカスタマイズ {#customizing-push-categories}

Brazeはデフォルトのプッシュカテゴリのセットを提供するだけでなく、カスタムの通知カテゴリとアクションもサポートしています。アプリケーションにカテゴリを登録すると、Braze ダッシュボードを使用してこれらのカスタム通知カテゴリをユーザーに送信できます。

デバイスに表示される `LIKE_CATEGORY` を活用する例を次に示します。

![「いいねを取り消す」と「いいね」の2つのプッシュアクションボタンを表示するプッシュメッセージ]({% image_buster /assets/img_archive/push_example_category.png %})

### ステップ1:カテゴリを登録する

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

### ステップ2:カテゴリを選択

カテゴリを登録したら、Braze ダッシュボードを使用して、そのタイプの通知をユーザーに送信します。

{% alert tip %}
アプリケーションにディープリンクしたり、URL を開いたりするアクションなど、_特殊なアクション_を含むアクションボタンの場合にのみ、カスタム通知カテゴリを定義する必要があります。通知を閉じるだけのアクションボタン用に定義する必要はありません。
{% endalert %}

1. Braze ダッシュボードで、**メッセージング**> **プッシュ通知**を選択し、iOS [プッシュキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message)を選択します。
2. [**プッシュ通知を作成する**] の下で、[**アクションボタン**] をオンにします。
3. [**iOS 通知カテゴリ**] ドロップダウンで、[**事前登録されたカスタム iOS カテゴリを入力**] を選択します。
4. 最後に、前に作成したカテゴリのいずれかを入力します。次の例では、カスタムカテゴリ`LIKE_CATEGORY` を使用します。

![カスタムカテゴリの設定を含むプッシュ通知 キャンペーン ダッシュボード。]({% image_buster /assets/img_archive/ios-notification-category.png %})

## バッジのカスタマイズ

バッジは小さなアイコンで、ユーザーの注意を引くのに最適です。Braze ダッシュボードを使用してプッシュ通知を作成する場合、[**設定**]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_settings)タブでバッジ数を指定できます。アプリケーションの [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) プロパティまたは[リモート通知ペイロード](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1)を使用して、バッジ数を手動で更新することもできます。 

Brazeは、アプリがフォアグラウンドにあるときにBraze通知を受信すると、バッジカウントを自動的にクリアします。バッジ番号を手動で0に設定すると、通知センターの通知もクリアされます。 

通常のアプリ操作の一部として、またはバッジをクリアするプッシュを送信してバッジをクリアする計画がない場合は、次のコードをアプリの `applicationDidBecomeActive:` デリゲートメソッドに追加してアプリがアクティブになったときにバッジをクリアする必要があります。

{% tabs %}
{% tab swift %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

## サウンドのカスタマイズ

### ステップ 1: アプリでサウンドをホスティングする

カスタムプッシュ通知サウンドは、アプリのメインバンドル内でローカルにホストする必要があります。次のオーディオデータ形式が使用できます。

- リニア PCM
- MA4
- µLaw
- aLaw

オーディオデータは AIFF、WAV、または CAF ファイルにパッケージできます。Xcode で、サウンドファイルをアプリケーションバンドルの非ローカライズリソースとしてプロジェクトに追加します。

{% alert note %}
カスタムサウンドを再生する場合は、30 秒未満にする必要があります。カスタムサウンドがこの制限を超えている場合、デフォルトのシステムサウンドが代わりに再生されます。
{% endalert %}

#### サウンドファイルを変換する

afconvert ツールを使用して、サウンドを変換できます。たとえば、16ビットリニア PCM システムサウンド Submarine.aiff を CAF ファイルの IMA4オーディオに変換するには、ターミナルで次のコマンドを使用します。

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
QuickTime Player でサウンドを開き、[**ムービー**] メニューから [**ムービーインスペクターを表示**] を選択するとサウンドのデータ形式を確認できます。
{% endalert %}

### ステップ 2:サウンドのプロトコルURL を指定する

アプリ内のサウンドファイルの場所にリダイレクトするプロトコル URL を指定する必要があります。これには2 つの方法があります。

* [Appleプッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object)の`sound`パラメータを使用して、URLをBrazeに渡します。
* ダッシュボードで URL を指定します。[push composer]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android)で**Settings**を選択し、**Sound**フィールドにプロトコールURLを入力します。 

![Braze ダッシュボードのプッシュコンポーザー]({% image_buster /assets/img_archive/sound_push_ios.png %})

指定したサウンドファイルが存在しない場合、またはキーワード「default」を入力した場合は、Braze では、デバイスのデフォルトのアラートサウンドが使用されます。ダッシュボードとは別に、[messaging API][12] でサウンドを設定することもできます。

詳細については、[カスタムアラートサウンドの準備](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html)に関するApple Developer のドキュメントを参照してください。

## 設定

ダッシュボードからプッシュキャンペーンを作成する場合、**作成**ステップで**設定**タブをクリックし、利用可能な詳細設定を表示する。

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

### キーと値のペア

Braze を使用すると、`extras` として知られるカスタム定義の文字列キーと値のペアを、アプリケーションへプッシュ通知と一緒に送ることができます。エクストラは、ダッシュボードまたは API を介して定義することができ、プッシュデリゲートの実装に渡される `notification` 辞書内のキーと値のペアとして利用できます。

### アラートオプション

**Alert Options（アラート・オプション）**チェックボックスを選択すると、デバイスにどのように通知が表示されるかを調整するために利用可能なキー値のドロップダウンが表示される。

### コンテンツ利用可能フラグを追加する

新しいコンテンツをバックグラウンドでダウンロードするようにデバイスに指示するには、[**コンテンツ利用可能フラグを追加**] チェックボックスをオンにします。最も一般的には、これは[サイレント通知]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)の送信に関心がある場合にチェックできます。

### mutable-content フラグを追加する

**Add Mutable-Content Flag**チェックボックスをチェックして、受信機の高度なカスタマイズを有効にする。このフラグは、このチェックボックスの値に関係なく、[rich notification]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift)を作成するときに自動的に送信されます。

### 折りたたみ ID

同様の通知をまとめるには、折りたたみ ID を指定します。同一の折りたたみ ID を使用して複数の通知を送信すると、デバイスには最後に受信した通知のみが表示されます。[統合された通知](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)については、Apple のドキュメントを参照してください。

### 有効期限

[**有効期限**] チェックボックスをオンにすると、メッセージの有効期限を設定できます。ユーザーのデバイスが接続性を失った場合、Braze は指定された時間までメッセージの送信を試行し続けます。設定されていない場合、プラットフォームの有効期限はデフォルトで30日となります。配信前に有効期限切れとなったプッシュ通知は失敗とはみなされず、バウンスとして記録されないことに注意してください。
