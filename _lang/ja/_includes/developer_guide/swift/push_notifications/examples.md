{% multi_lang_include developer_guide/prerequisites/swift.md %} また、[プッシュ通知s]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)を設定する必要があります。

{% alert note %}
この実装ガイドは Swift の実装を中心としていますが、興味のある人のために Objective-C のスニペットが提供されています。
{% endalert %}

## 通知コンテンツアプリの拡張

![並んで表示される2つのプッシュメッセージ。左側のメッセージは、デフォルトのUIでプッシュがどのように見えるかを示しています。右側のメッセージには、カスタムプッシュ UI ]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"} を実装して作成したコーヒーパンチカードプッシュが表示されます。

通知コンテンツアプリ拡張機能は、プッシュ通知のカスタマイズに最適なオプションを提供します。プッシュ通知を展開すると、通知コンテンツアプリ拡張機能によって、アプリの通知のカスタムインターフェイスが表示されます。

プッシュ通知は、次の 3 つの方法で展開できます。
- プッシュバナーを長押し
- プッシュバナーを下にスワイプする
- バナーを左にスワイプして「表示」を選択

これらのカスタムビューでは、顧客を引き付けるスマートな方法が提供され、対話型の通知、ユーザーデータを含む通知、電話番号やメールなどの情報を取得できるプッシュメッセージなど、さまざまな種類のコンテンツを表示できます。Braze でよく知られている機能の 1 つである [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/) は、プッシュ通知コンテンツアプリ拡張機能の例です。

### 要件

![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [プッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)がアプリに正常に統合されました
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

### ダッシュボードの構成

インタラクティブなプッシュ通知を作成するには、ダッシュボードにカスタムビューを設定する必要があります。 

1. **キャンペーン** ページから、**キャンペーンを作成** をクリックして新しいプッシュ通知キャンペーンを開始します。
2. 「**作成**」タブで、「**通知ボタン**」をオンにします。 
3. **iOS通知カテゴリ**フィールドにカスタムiOSカテゴリを入力します。 
4. 通知コンテンツ拡張ターゲットの`.plist`で、`UNNotificationExtensionCategory`属性をカスタムiOSカテゴリに設定します。ここに指定された値は、Brazeダッシュボードの**iOS通知カテゴリ**で設定されているものと一致する必要があります。 
5. `UNNotificationExtensionInteractionEnabled`キーを`true`に設定して、プッシュ通知でユーザーの操作を有効にします。

![プッシュメッセージ作成画面の設定にある通知ボタンオプション。]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## パーソナライズされたプッシュ通知

![2台のiPhoneが並んで表示されています。最初の iPhone には、プッシュメッセージの展開されていないビューが表示されます。2番目のiPhoneは、プッシュメッセージの拡張バージョンを表示し、コースの進行状況の「進捗」ショット、次のセッションの名前、および次のセッションを完了する必要がある時期を示しています。]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

プッシュ通知では、コンテンツ拡張の内部にユーザ固有の情報を表示できます。これにより、さまざまなプラットフォームで進捗を共有するオプションを追加したり、アンロックされた実績を表示したり、オンボーディングチェックリストを表示したりするなど、ユーザー中心のプッシュコンテンツを作成できます。この例は、ユーザーがBrazeラーニングコースで特定のタスクを完了した後に表示されるプッシュ通知を示しています。通知を展開することで、ユーザーは学習パスの進捗を確認できます。ここで提供される情報はユーザー固有であり、セッションが完了するか、API トリガーを利用して特定のユーザーアクションが実行されたときに呼び出すことができます。 

### ダッシュボード設定

パーソナライズされたプッシュ通知を作成するには、ダッシュボードにカスタムビューを設定する必要があります。 

1. **キャンペーン** ページから、**キャンペーンを作成** をクリックして新しいプッシュ通知キャンペーンを開始します。
2. 「**作成**」タブで、「**通知ボタン**」をオンにします。 
3. **iOS通知カテゴリ**フィールドにカスタムiOSカテゴリを入力します。 
4. **設定** タブで、標準の Liquid を使用してキーと値のペアを作成します。メッセージに表示したい適切なユーザー属性を設定します。これらのビューは、特定のユーザープロファイルの特定のユーザー属性に基づいてカスタマイズできます。
5. 通知コンテンツ拡張ターゲットの`.plist`で、`UNNotificationExtensionCategory`属性をカスタムiOSカテゴリに設定します。ここに指定された値は、Brazeダッシュボードの**iOS通知カテゴリ**で設定されているものと一致する必要があります。 

![Liquid を使用してAPI トリガー プロパティとして"next_session_name" と"next_session_complete_date" が設定され、"completed_session count" および"total_session_count" がLiquid を使用してカスタムユーザー 属性として設定される4 組のキーと値のペア。]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

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

## 情報取得プッシュ通知

プッシュ通知は、コンテンツアプリ拡張の内部でユーザー情報をキャプチャし、プッシュで可能な事の限界を押し広げます。プッシュ通知を使用してユーザー入力をリクエストすると、名前やメールなどの基本的な情報をリクエストできるだけでなく、フィードバックの送信や未完成のユーザープロファイルの完成をユーザーに促すこともできます。 

{% alert tip %}
詳細については、[ログプッシュ通知データ]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications/)を参照してください。
{% endalert %}

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

例に見られるように、プッシュ通知に画像を含めることもできます。これを行うには、[リッチプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift)を統合し、キャンペーンの通知スタイルをリッチプッシュ通知に設定し、リッチプッシュ画像を含める必要があります。

![キーと値のペアが3セットあるプッシュメッセージ。1. "Braze_id" は、Braze ID を取得するためのリキッドコールとして設定されます。2. "cert_title" &quot として設定; Braze マーケター認証&クォート;3. "Cert_description" &quot として設定;Certified Braze マーケター s drive..."。]({% image_buster /assets/img/push_implementation_guide/push9.png %})

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
