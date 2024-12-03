---
nav_title: 高度な実装 (オプション)
article_title: iOS 用の高度なプッシュ通知の実装 (オプション)
platform: Swift
page_order: 30
description: "この高度な実装ガイドでは、iOSプッシュ通知コンテンツアプリ拡張機能を活用して、SWIFT SDKを使用してプッシュメッセージを最大限に活用する方法について説明します。"
channel:
  - push
---

<br>
{% alert important %}
基本的なプッシュ通知開発者統合ガイドをお探しの場合は、ここで見つけてください[here]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).
{% endalert %}

# 上級実装ガイド

> このオプションの高度な実装ガイドでは、通知コンテンツアプリ拡張機能を活用してプッシュメッセージを最大限に活用する方法について説明します。 

このガイドでは、通知コンテンツアプリ拡張機能の3つの実装例を提供し、それぞれの概念の説明、潜在的な使用例、およびプッシュ通知変数がBrazeダッシュボードでどのように見え、使用されるかについて説明します。
- [インタラクティブなプッシュ通知](#interactive-push-notification)
- [パーソナライズされたプッシュ通知](#personalized-push-notifications)
- [情報キャプチャプッシュ通知](#information-capture-push-notification)

この記事では、これらのカスタム実装のための[ログ分析に関するガイダンス](#logging-analytics)も提供しています。

この実装ガイドは、Swift 実装を中心に扱っていますが、興味のある人のために Objective-C のスニペットが提供されています。

## 通知コンテンツアプリの拡張

![並んで表示される2つのプッシュメッセージ。左側のメッセージは、デフォルトのUIでプッシュがどのように見えるかを示しています。右側のメッセージには、カスタムプッシュ UI を実装して作成したコーヒーパンチカードプッシュが表示されます。]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

通知コンテンツアプリ拡張機能は、プッシュ通知のカスタマイズに最適なオプションを提供します。プッシュ通知を展開すると、通知コンテンツアプリ拡張機能によって、アプリの通知のカスタムインターフェイスが表示されます。 

プッシュ通知は、次の 3 つの方法で展開できます。
- プッシュバナーを長押し
- プッシュバナーを下にスワイプする
- バナーを左にスワイプして「表示」を選択 

これらのカスタムビューでは、顧客を引き付けるスマートな方法が提供され、対話型の通知、ユーザーデータを含む通知、電話番号やメールなどの情報を取得できるプッシュメッセージなど、さまざまな種類のコンテンツを表示できます。Braze でよく知られている機能の 1 つである [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/) は、プッシュ通知コンテンツアプリ拡張機能の例です。

### 要件
![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [プッシュ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)がアプリに正常に統合されました
- ご利用のコード言語に基づいて Xcode によって生成される以下のファイル:

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## インタラクティブなプッシュ通知

プッシュ通知は、コンテンツアプリ拡張内でユーザーのアクションに応答できます。iOS 12以降を使用しているユーザーにとって、これはプッシュ通知を完全にインタラクティブなメッセージに変えることができることを意味します！これにより、プロモーションやアプリケーションにインタラクティビティを導入するエキサイティングなオプションが提供されます。例えば、プッシュ通知には、ユーザーがプレイできるゲーム、割引のためのスピン・トゥ・ウィン・ホイール、リストや曲を保存するための「いいね」ボタンなどがあります。

次の例は、ユーザーが拡張通知内でマッチゲームをプレイできるプッシュ通知を示しています。

![インタラクティブなプッシュ通知のフェーズがどのように見えるかの図。シーケンスは、ユーザーがインタラクティブなマッチングゲームを表示するプッシュ通知を押す様子を示しています。]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### ダッシュボード設定

インタラクティブなプッシュ通知を作成するには、ダッシュボードにカスタムビューを設定する必要があります。 

1. **キャンペーン** ページから、**キャンペーンを作成** をクリックして新しいプッシュ通知キャンペーンを開始します。
2. 「**作成**」タブで、「**通知ボタン**」をオンにします。 
3. **iOS通知カテゴリ**フィールドにカスタムiOSカテゴリを入力します。 
4. 通知コンテンツ拡張ターゲットの`.plist`で、`UNNotificationExtensionCategory`属性をカスタムiOSカテゴリに設定します。ここに指定された値は、Brazeダッシュボードの**iOS通知カテゴリ**で設定されているものと一致する必要があります。 
5. `UNNotificationExtensionInteractionEnabled`キーを`true`に設定して、プッシュ通知でユーザーの操作を有効にします。

![プッシュメッセージコンポーザーの設定にある通知ボタンのオプション。]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

### 分析をログに記録する準備ができましたか?
[ログ分析セクション](#logging-analytics)にアクセスして、データの流れがどのように見えるかをよりよく理解してください。

## パーソナライズされたプッシュ通知
![2台のiPhoneが並んで表示されています。最初の iPhone には、プッシュメッセージの展開されていないビューが表示されます。2台目の iPhone には、プッシュメッセージの展開されたバージョンが表示されます。コースの進行状況、次のセッションの名前、次のセッションの期限を示す「進捗」ショットが表示されます。]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

プッシュ通知では、コンテンツ拡張の内部にユーザ固有の情報を表示できます。これにより、さまざまなプラットフォームで進捗を共有するオプションを追加したり、アンロックされた実績を表示したり、オンボーディングチェックリストを表示したりするなど、ユーザー中心のプッシュコンテンツを作成できます。この例は、ユーザーがBrazeラーニングコースで特定のタスクを完了した後に表示されるプッシュ通知を示しています。通知を展開することで、ユーザーは学習パスの進捗を確認できます。ここで提供される情報はユーザー固有であり、セッションが完了するか、API トリガーを利用して特定のユーザーアクションが実行されたときに呼び出すことができます。 

### ダッシュボード設定

パーソナライズされたプッシュ通知を作成するには、ダッシュボードにカスタムビューを設定する必要があります。 

1. **キャンペーン** ページから、**キャンペーンを作成** をクリックして新しいプッシュ通知キャンペーンを開始します。
2. 「**作成**」タブで、「**通知ボタン**」をオンにします。 
3. **iOS通知カテゴリ**フィールドにカスタムiOSカテゴリを入力します。 
4. **設定** タブで、標準の Liquid を使用してキーと値のペアを作成します。メッセージに表示したい適切なユーザー属性を設定します。これらのビューは、特定のユーザープロファイルの特定のユーザー属性に基づいてカスタマイズできます。
5. 通知コンテンツ拡張ターゲットの`.plist`で、`UNNotificationExtensionCategory`属性をカスタムiOSカテゴリに設定します。ここに指定された値は、Brazeダッシュボードの**iOS通知カテゴリ**で設定されているものと一致する必要があります。 

![4つのキーと値のペアのセットで、「next_session_name」と「next_session_complete_date」はLiquidを使用してAPIトリガープロパティとして設定され、「completed_session count」と「total_session_count」はLiquidを使用してカスタムユーザー属性として設定されます。]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### キーと値のペアの処理

メソッド`didReceive`は、通知コンテンツアプリ拡張機能が通知を受信したときに呼び出されます。この方法は`NotificationViewController`内にあります。ダッシュボードで提供されるキーと値のペアは、`userInfo` 辞書を使用してコードで表されます。

#### プッシュ通知からのキーと値のペアの解析

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo
     
  guard let value = userInfo["YOUR-KEY-VALUE-PAIR"] as? String,
        let otherValue = userInfo["YOUR-OTHER-KEY-VALUE-PAIR"] as? String,
  else { fatalError("Key-Value Pairs are incorrect.")}
 
  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;
   
  if (userInfo[@"YOUR-KEY-VALUE-PAIR"] && userInfo[@"YOUR-OTHER-KEY-VALUE-PAIR"]) {
 
  ...
 
  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```
{% endtab %}
{% endtabs %}

### 分析をログに記録する準備ができましたか?
[ログ分析セクション](#logging-analytics)にアクセスして、データの流れがどのように見えるかをよりよく理解してください。

## 情報取得プッシュ通知

プッシュ通知は、コンテンツアプリ拡張の内部でユーザー情報をキャプチャし、プッシュで可能な事の限界を押し広げます。プッシュ通知を使用してユーザー入力をリクエストすると、名前やメールなどの基本的な情報をリクエストできるだけでなく、フィードバックの送信や未完成のユーザープロファイルの完成をユーザーに促すこともできます。 

次のフローでは、カスタムビューは状態の変化に対応できます。これらの状態変更コンポーネントは、各画像に表示されます。 

1. ユーザーはプッシュ通知を受信します。
2. プッシュが開封されました。展開後、プッシュはユーザーに情報を求めます。この例では、ユーザーのメールアドレスがリクエストされますが、任意の種類の情報をリクエストすることもできます。
3. 情報が提供され、期待される形式であれば、登録ボタンが表示されます。
3. 確認画面が表示され、プッシュが解除されます。 

![]({% image_buster /assets/img/push_implementation_guide/push8.png %}){: style="border:0;"}

### ダッシュボード設定

情報キャプチャプッシュ通知を作成するには、ダッシュボードにカスタムビューを設定する必要があります。 

1. **キャンペーン** ページから、**キャンペーンを作成** をクリックして新しいプッシュ通知キャンペーンを開始します。
2. 「**作成**」タブで、「**通知ボタン**」をオンにします。 
3. **iOS通知カテゴリ**フィールドにカスタムiOSカテゴリを入力します。 
4. **設定** タブで、標準の Liquid を使用してキーと値のペアを作成します。メッセージに表示したい適切なユーザー属性を設定します。 
5. 通知コンテンツ拡張ターゲットの`.plist`で、`UNNotificationExtensionCategory`属性をカスタムiOSカテゴリに設定します。ここに指定された値は、Brazeダッシュボードの**iOS通知カテゴリ**で設定されているものと一致する必要があります。 

例に見られるように、プッシュ通知に画像を含めることもできます。これを行うには、[リッチプッシュ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/)を統合し、キャンペーンの通知スタイルをリッチプッシュ通知に設定し、リッチプッシュ画像を含める必要があります。

![キーと値のペアが3セットあるプッシュメッセージ。1\.「Braze_id」は、Braze ID を取得するための Liquid 呼び出しとして設定されます。2.「cert_title」は「Braze マーケター認証」として設定されます。3\.「Cert_description」は、「認定 Braze マーケタードライブ...」として設定されます]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### ボタンアクションの処理

各アクションボタンは一意に識別されます。コードは、応答識別子が `actionIndentifier` と等しいかどうかをチェックし、等しい場合は、ユーザーがアクションボタンをクリックしたことと認識します。

**プッシュ通知アクションボタンの応答の処理**<br>

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  if response.actionIdentifier == "YOUR-REGISTER-IDENTIFIER" {
    // do something
  } else {
    // do something else
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier isEqualToString:@"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }
}
```
{% endtab %}
{% endtabs %}

### プッシュの解除

プッシュ通知は、アクションボタンを押すと自動的に解除できます。推奨される事前構築済みのプッシュ解除オプションは3つあります。

1. `completion(.dismiss)` - 通知を解除します
2. `completion(.doNotDismiss)` - 通知は開いたままです
3. `completion(.dismissAndForward)` - プッシュが解除され、ユーザーがアプリケーションに転送されます

### 分析をログに記録する準備ができましたか?
[以下のセクション](#logging-analytics)を参照して、データのフローがどうあるべきかを理解してください。 

## 分析のログ記録

### Braze API を使用したロギング (推奨)

ログ分析は、Braze API [`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用してリアルタイムで実行できます。分析をログに記録するには、`braze_id` 値をキーと値のペアフィールド (次のスクリーンショットを参照) に送信し、更新するユーザープロファイルを識別します。

![キーと値のペアが3セットあるプッシュメッセージ。1\.「Braze_id」は、Braze ID を取得するための Liquid 呼び出しとして設定されます。2.「cert_title」は「Braze マーケター認証」として設定されます。3\.「Cert_description」は、「認定 Braze マーケタードライブ...」として設定されます]({% image_buster /assets/img/push_implementation_guide/push18.png %}){: style="max-width:80%;"}

### 手動ロギング

手動でログを記録するには、まず Xcode 内でワークスペースを設定してから、分析を作成、保存、および取得する必要があります。これには、お客様の側でカスタム開発者の作業が必要になります。以下に示すコードスニペットは、これを解決するのに役立ちます。 

分析はモバイルアプリケーションがその後起動されるまでBrazeに送信されないことに注意することが重要です。つまり、削除設定に応じて、プッシュ通知が破棄されてモバイルアプリが起動し、分析が取得されるまでに不確定な期間が存在することがよくあります。この場合バッファーがすべてのユースケースに影響するとは限りませんが、影響を考慮して、必要に応じて、アプリケーションを開いてこの問題に対処するようにユーザー体験を調整する必要があります。 

![Brazeで分析が処理される方法を説明するグラフィック。1\.分析データが作成されます。2\.分析データが保存されます。3\.プッシュ通知を解除します。4\.プッシュ通知が解除されてからモバイルアプリが起動するまでの不確定な期間。5\.モバイルアプリが起動します。6\.分析データを受信します。7. 分析データはBraze に送信されます。]({% image_buster /assets/img/push_implementation_guide/push13.png %})

#### ステップ1:Xcode内でアプリグループを構成する
Xcode で `App Groups` 機能を追加します。アプリにワークスペースがない場合は、メインアプリターゲットの機能に移動し、`App Groups` をオンにして、[**+ 追加**] ボタンをクリックします。次に、アプリのバンドルIDを使用してワークスペースを作成します。例えば、アプリのバンドルIDが`com.company.appname`の場合、ワークスペースの名前を`group.com.company.appname.xyz`にすることができます。メインアプリターゲットとコンテンツ拡張ターゲットの両方で `App Groups` がオンになっていることを確認します。

![]({% image_buster /assets/img/swift/push_story/add_app_groups.png %})

#### ステップ 2:コードスニペットの統合
以下のコードスニペットは、カスタムイベント、カスタム属性、およびユーザー属性を保存および送信する方法についての役立つ参考情報です。このガイドでは`UserDefaults`の用語で説明しますが、コードの表現はヘルパーファイル`RemoteStorage`の形式になります。また、追加のヘルパーファイル `UserAttributes` と `EventName Dictionary` もあり、ユーザー属性の送信と保存に使用されます。

{% tabs local %}
{% tab カスタムイベント %}

##### カスタムイベントの保存

カスタムイベントを保存するには、分析をゼロから作成する必要があります。これを行うには、辞書を作成し、メタデータを入力し、ヘルパーファイルを使用してデータを保存します。

1. イベントメタデータを使用して辞書を初期化します
2. イベントデータを取得して保存するには、`userDefaults` を初期化します
3. 既存の配列がある場合は、既存の配列に新しいデータを追加して保存します
4. 既存の配列がない場合は、新しい配列を `userDefaults` に保存します

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveCustomEvent(with properties: [String: Any]? = nil) {
  // 1
  let customEventDictionary = Dictionary(eventName: "YOUR-EVENT-NAME", properties: properties)
  
  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3   
  if var pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] {
    pendingEvents.append(contentsOf: [customEventDictionary])
    remoteStorage.store(pendingEvents, forKey: .pendingCustomEvents)
  } else {
  // 4
    remoteStorage.store([customEventDictionary], forKey: .pendingCustomEvents)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveCustomEvent:(NSDictionary<NSString *, id> *)properties {
  // 1 
  NSDictionary<NSString *, id> *customEventDictionary = [[NSDictionary alloc] initWithEventName:@"YOUR-EVENT-NAME" properties:properties];
  
  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingEvents = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents] mutableCopy];
  
  // 3 
  if (pendingEvents) {
    [pendingEvents addObject:customEventDictionary];
    [remoteStorage store:pendingEvents forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4
    [remoteStorage store:@[ customEventDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### カスタムイベントの Braze への送信

通知コンテンツアプリの拡張機能から保存された分析をログに記録するのに最適なタイミングは SDK の初期化直後です。これは、保留中のイベントをループして「イベント名」キーをチェックし、Brazeに適切な値を設定し、次回この機能が必要なときのためにストレージをクリアすることで実行できます。

1. 保留中のイベントの配列をループします
2. `pendingEvents` 辞書の各キーと値のペアをループします
3. 「Event Name」のキーを明示的にチェックし、それに応じて値を設定します
4. 他のすべてのキー値が `properties` 辞書に追加されます
5. 個別のカスタムイベントを記録します 
6. すべての保留中のイベントをストレージから削除します

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingCustomEventsIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] else { return }
  
  // 1    
  for event in pendingEvents {
    var eventName: String?
    var properties: [AnyHashable: Any] = [:]
    
  // 2
    for (key, value) in event {
      if key == PushNotificationKey.eventName.rawValue {
  // 3      
        if let eventNameValue = value as? String {
          eventName = eventNameValue
        } else {
          print("Invalid type for event_name key")
        }
      } else {
  // 4 
        properties[key] = value
      }
    }
  // 5    
    if let eventName = eventName {
      AppDelegate.braze?.logCustomEvent(eventName, properties: properties)
    }
  }

  // 6    
  remoteStorage.removeObject(forKey: .pendingCustomEvents)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingEventsIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingEvents = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents];
  
  // 1 
  for (NSDictionary<NSString *, id> *event in pendingEvents) {
    NSString *eventName = nil;
    NSMutableDictionary *properties = [NSMutableDictionary dictionary];
    
  // 2 
    for (NSString* key in event) {
      if ([key isEqualToString:@"event_name"]) {
  // 3       
        if ([[event objectForKey:key] isKindOfClass:[NSString class]]) {
          eventName = [event objectForKey:key];
        } else {
          NSLog(@"Invalid type for event_name key");
        }
      } else {
  // 4 
        properties[key] = event[key];
      }
    }
  // 5  
    if (eventName != nil) {
      [AppDelegate.braze logCustomEvent:eventName properties:properties];
    }
  }

  // 6  
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomEvents];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab カスタム属性 %}

##### カスタム属性の保存

カスタム属性を保存するには、分析をゼロから作成する必要があります。これを行うには、辞書を作成し、メタデータを入力し、ヘルパーファイルを使用してデータを保存します。

1. 属性メタデータを使用してディクショナリを初期化します
2. 属性データを取得して格納するには、`userDefaults` を初期化します
3. 既存の配列がある場合は、既存の配列に新しいデータを追加して保存します
4. 既存の配列がない場合は、新しい配列を `userDefaults` に保存します

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveCustomAttribute() {
  // 1 
  let customAttributeDictionary: [String: Any] = ["YOUR-CUSTOM-ATTRIBUTE-KEY": "YOUR-CUSTOM-ATTRIBUTE-VALUE"]
  
  // 2 
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3 
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] {
    pendingAttributes.append(contentsOf: [customAttributeDictionary])
    remoteStorage.store(pendingAttributes, forKey: .pendingCustomAttributes)
  } else {
  // 4 
    remoteStorage.store([customAttributeDictionary], forKey: .pendingCustomAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
``` objc
- (void)saveCustomAttribute {
  // 1 
  NSDictionary<NSString *, id> *customAttributeDictionary = @{ @"YOUR-CUSTOM-ATTRIBUTE-KEY": @"YOUR-CUSTOM-ATTRIBUTE-VALUE" };
  
  // 2  
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes] mutableCopy];
  
  // 3
  if (pendingAttributes) {
    [pendingAttributes addObject:customAttributeDictionary];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4 
    [remoteStorage store:@[ customAttributeDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### カスタム属性の Braze への送信

通知コンテンツアプリの拡張機能から保存された分析をログに記録するのに最適なタイミングは SDK の初期化直後です。これは、保留中の属性をループし、Braze で適切なカスタム属性を設定し、次回この関数が必要になったときに備えてストレージをクリアすることで実行できます。

1. 保留中の属性の配列をループスルーします
2. `pendingAttributes` 辞書の各キーと値のペアをループします
3. 対応するキーと値で個々のカスタム属性を記録する
4. ストレージからすべての保留中の属性を削除します

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingCustomAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] else { return }
     
  // 1
  pendingAttributes.forEach { setCustomAttributesWith(keysAndValues: $0) }
  
  // 4 
  remoteStorage.removeObject(forKey: .pendingCustomAttributes)
}
   
func setCustomAttributesWith(keysAndValues: [String: Any]) {
  // 2 
  for (key, value) in keysAndValues {
  // 3
    if let value = value as? [String] {
      setCustomAttributeArrayWithKey(key, andValue: value)
    } else {
      setCustomAttributeWithKey(key, andValue: value)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingCustomAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes];
   
  // 1
  for (NSDictionary<NSString*, id> *attribute in pendingAttributes) {
    [self setCustomAttributeWith:attribute];
  }

  // 4 
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomAttributes];
}
 
- (void)setCustomAttributeWith:(NSDictionary<NSString *, id> *)keysAndValues {
  // 2
  for (NSString *key in keysAndValues) {
  // 3 
    [self setCustomAttributeWith:key andValue:[keysAndValues objectForKey:key]];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ユーザー属性 %}

##### ユーザー属性の保存

ユーザー属性を保存する際には、どのタイプの属性が更新されているかを判別するためにカスタムオブジェクトを作成することをお勧めします（`email`、`first_name`、`phone_number`など）。オブジェクトは、`UserDefaults` からの保管 / 取得に対応している必要があります。これを行う方法の一例については、`UserAttribute` ヘルパーファイルを参照してください。

1. エンコードされた`UserAttribute` オブジェクトを対応する型で初期化します
2. イベントデータを取得して保存するには、`userDefaults` を初期化します
3. 既存の配列がある場合は、既存の配列に新しいデータを追加して保存します
4. 既存の配列がない場合は、新しい配列を `userDefaults` に保存します

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveUserAttribute() {
  // 1 
  guard let data = try? PropertyListEncoder().encode(UserAttribute.userAttributeType("USER-ATTRIBUTE-VALUE")) else { return }
  
  // 2       
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3    
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] {
    pendingAttributes.append(contentsOf: [data])
    remoteStorage.store(pendingAttributes, forKey: .pendingUserAttributes)
  } else {
  // 4 
    remoteStorage.store([data], forKey: .pendingUserAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveUserAttribute {
  // 1 
  UserAttribute *userAttribute = [[UserAttribute alloc] initWithUserField:@"USER-ATTRIBUTE-VALUE" attributeType:UserAttributeTypeEmail];
   
  NSError *error;
  NSData *data = [NSKeyedArchiver archivedDataWithRootObject:userAttribute requiringSecureCoding:YES error:&error];

  if (error != nil) {
    // log error
  }
  // 2  
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes] mutableCopy];
  
  // 3 
  if (pendingAttributes) {
    [pendingAttributes addObject:data];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingUserAttributes];
  } else {
  // 4 
    [remoteStorage store:@[data] forKey:RemoteStorageKeyPendingUserAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Braze へのユーザー属性の送信

通知コンテンツアプリの拡張機能から保存された分析をログに記録するのに最適なタイミングは SDK の初期化直後です。これは、保留中の属性をループし、Braze で適切なカスタム属性を設定し、次回この関数が必要になったときに備えてストレージをクリアすることで実行できます。

1. `pendingAttributes` データの配列をループします
2. 属性データからエンコードされた`UserAttribute` オブジェクトを初期化します
3. ユーザー属性タイプ (電子メール) に基づいて特定のユーザーフィールドを設定します
4. ストレージからすべての保留中のユーザー属性を削除します

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingUserAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] else { return }
  
  // 1    
  for attributeData in pendingAttributes {
  // 2 
    guard let userAttribute = try? PropertyListDecoder().decode(UserAttribute.self, from: attributeData) else { continue }
    
  // 3    
    switch userAttribute {
    case .email(let email):
      user?.email = email
    }
  }
  // 4   
  remoteStorage.removeObject(forKey: .pendingUserAttributes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingUserAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes];
  
  // 1  
  for (NSData *attributeData in pendingAttributes) {
    NSError *error;
  
  // 2 
    UserAttribute *userAttribute = [NSKeyedUnarchiver unarchivedObjectOfClass:[UserAttribute class] fromData:attributeData error:&error];

    if (error != nil) {
      // log error
    }
    
  // 3  
    if (userAttribute) {
      switch (userAttribute.attributeType) {
        case UserAttributeTypeEmail:
          [self user].email = userAttribute.userField;
          break;
      }
    }
  }
  // 4 
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingUserAttributes];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ヘルパーファイル %}

##### ヘルパーファイル

{% details RemoteStorageヘルパーファイル %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum RemoteStorageKey: String, CaseIterable {
   
  // MARK: - Notification Content Extension Analytics
  case pendingCustomEvents = "pending_custom_events"
  case pendingCustomAttributes = "pending_custom_attributes"
  case pendingUserAttributes = "pending_user_attributes"
}
 
enum RemoteStorageType {
  case standard
  case suite
}
 
class RemoteStorage: NSObject {
  private var storageType: RemoteStorageType = .standard
  private lazy var defaults: UserDefaults = {
    switch storageType {
    case .standard:
      return .standard
    case .suite:
      return UserDefaults(suiteName: "YOUR-DOMAIN-IDENTIFIER")!
    }
  }()
   
  init(storageType: RemoteStorageType = .standard) {
    self.storageType = storageType
  }
   
  func store(_ value: Any, forKey key: RemoteStorageKey) {
    defaults.set(value, forKey: key.rawValue)
  }
   
  func retrieve(forKey key: RemoteStorageKey) -> Any? {
    return defaults.object(forKey: key.rawValue)
  }
   
  func removeObject(forKey key: RemoteStorageKey) {
    defaults.removeObject(forKey: key.rawValue)
  }
   
  func resetStorageKeys() {
    for key in RemoteStorageKey.allCases {
      defaults.removeObject(forKey: key.rawValue)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@interface RemoteStorage ()
 
@property (nonatomic) StorageType storageType;
@property (nonatomic, strong) NSUserDefaults *defaults;
 
@end
 
@implementation RemoteStorage
 
- (id)initWithStorageType:(StorageType)storageType {
  if (self = [super init]) {
    self.storageType = storageType;
  }
  return self;
}
 
- (void)store:(id)value forKey:(RemoteStorageKey)key {
  [[self defaults] setValue:value forKey:[self rawValueForKey:key]];
}
 
- (id)retrieveForKey:(RemoteStorageKey)key {
  return [[self defaults] objectForKey:[self rawValueForKey:key]];
}
 
- (void)removeObjectForKey:(RemoteStorageKey)key {
  [[self defaults] removeObjectForKey:[self rawValueForKey:key]];
}
 
- (void)resetStorageKeys {
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomEvents]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomAttributes]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingUserAttributes]];
}
 
- (NSUserDefaults *)defaults {
  if (!self.defaults) {
    switch (self.storageType) {
      case StorageTypeStandard:
        return [NSUserDefaults standardUserDefaults];
        break;
      case StorageTypeSuite:
        return [[NSUserDefaults alloc] initWithSuiteName:@"YOUR-DOMAIN-IDENTIFIER"];
    }
  } else {
    return self.defaults;
  }
}
 
- (NSString*)rawValueForKey:(RemoteStorageKey)remoteStorageKey {
    switch(remoteStorageKey) {
    case RemoteStorageKeyPendingCustomEvents:
      return @"pending_custom_events";
    case RemoteStorageKeyPendingCustomAttributes:
      return @"pending_custom_attributes";
    case RemoteStorageKeyPendingUserAttributes:
      return @"pending_user_attributes";
    default:
      [NSException raise:NSGenericException format:@"Unexpected FormatType."];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details UserAttribute ヘルパーファイル %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum UserAttribute: Hashable {
  case email(String?)
}
 
// MARK: - Codable
extension UserAttribute: Codable {
  private enum CodingKeys: String, CodingKey {
    case email
  }
   
  func encode(to encoder: Encoder) throws {
    var values = encoder.container(keyedBy: CodingKeys.self)
     
    switch self {
    case .email(let email):
      try values.encode(email, forKey: .email)
    }
  }
   
  init(from decoder: Decoder) throws {
    let values = try decoder.container(keyedBy: CodingKeys.self)
     
    let email = try values.decode(String.self, forKey: .email)
    self = .email(email)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation UserAttribute
 
- (id)initWithUserField:(NSString *)userField attributeType:(UserAttributeType)attributeType {
  if (self = [super init]) {
    self.userField = userField;
    self.attributeType = attributeType;
  }
  return self;
}
 
- (void)encodeWithCoder:(NSCoder *)encoder {
  [encoder encodeObject:self.userField forKey:@"userField"];
  [encoder encodeInteger:self.attributeType forKey:@"attributeType"];
}
 
- (id)initWithCoder:(NSCoder *)decoder {
  if (self = [super init]) {
    self.userField = [decoder decodeObjectForKey:@"userField"];
     
    NSInteger attributeRawValue = [decoder decodeIntegerForKey:@"attributeType"];
    self.attributeType = (UserAttributeType) attributeRawValue;
  }
  return self;
}
 
@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details EventName Dictionary ヘルパーファイル %}
{% subtabs global %}
{% subtab Swift %}
```swift
extension Dictionary where Key == String, Value == Any {
  init(eventName: String, properties: [String: Any]? = nil) {
    self.init()
    self[PushNotificationKey.eventName.rawValue] = eventName
     
    if let properties = properties {
      for (key, value) in properties {
        self[key] = value
      }
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation NSDictionary (Helper)
 
- (id)initWithEventName:(NSString *)eventName properties:(NSDictionary *)properties {
  self = [self init];
  if (self) {
    dict[@"event_name"] = eventName;
     
    for(id key in properties) {
      dict[key] = properties[key];
    }
  }
  return self;
}
 
@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
<br>
{% endtab %}
{% endtabs %}

