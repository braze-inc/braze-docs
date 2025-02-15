---
nav_title: カスタムトリガー
article_title: iOS 用アプリ内メッセージトリガーのカスタマイズ
platform: Swift
page_order: 6
description: "このリファレンス記事では、Swift SDK のカスタム iOS アプリ内メッセージングトリガーについて説明します。"
channel:
  - in-app messages
---

# カスタムトリガー

> デフォルトでは、アプリ内メッセージは SDK によって記録されるイベントによってトリガーされます。また、サーバー送信イベントによってアプリ内メッセージをトリガーすることもできます。

サーバーサイドイベントを使用してアプリ内メッセージをトリガーするには、デバイスにサイレントプッシュを送信して、デバイスで SDK ベースのイベントを記録できるようにします。この SDK イベントは、その後、ユーザー向けのアプリ内メッセージをトリガーできます。

## ステップ1:サイレントプッシュとキーと値のペアを扱う

次の関数を実装し、[`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`: メソッド](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/)内で呼び出します。

{% tabs %}
{% tab SWIFT %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

サイレントプッシュを受信すると、ユーザープロファイルに対して SDK が記録したイベント「アプリ内メッセージトリガー」がログに記録されます。 

{% alert important %}
SDK のログに記録されたカスタムイベントの記録にプッシュメッセージが使用されているため、Braze はこのソリューションを有効にするには、ユーザーごとにプッシュトークンを格納する必要があります。iOS ユーザーの場合、Braze ではユーザーが OS のプッシュプロンプトを受け取った時点からのトークンのみが保存されます。これ以前では、ユーザーはプッシュを使用して到達できず、先行ソリューションも実行できません。
{% endalert %}

## ステップ 2:サイレントプッシュキャンペーンの作成

サーバー送信イベントを介してトリガーされる[サイレントプッシュキャンペーン]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/)を作成します。 

![カスタムイベント「server_event」を持つユーザープロファイルのユーザーに配信されるアクションベースの配信アプリ内メッセージキャンペーンです。]({% image_buster /assets/img_archive/iosServerSentPush.png %})

プッシュキャンペーンにはキーと値のペアエクストラを含める必要があります。これは、このプッシュキャンペーンが SDK カスタムイベントを記録するために送信されることを示します。このイベントは次のアプリ内メッセージをトリガーするために使用されます。

![アクションベースの配信アプリ内メッセージキャンペーンで、2つのキーと値のペアがあります。「キャンペーン_NAME」を「アプリ内メッセージ名の例」に設定し、「IS_SERVER_EVENT」を「true」に設定します。]({% image_buster /assets/img_archive/iOSServerPush.png %})

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内のコードはキー `IS_SERVER_EVENT` をチェックし、SDK カスタムイベントがあればログに記録します。

プッシュペイロードのキーと値のペアエクストラ内で目的の値を送信することで、イベント名またはイベントプロパティのいずれかを変更できます。カスタムイベントを記録する場合、これらのエクストラはイベント名のパラメータまたはイベントプロパティとして使用できます。

## ステップ3: アプリ内メッセージキャンペーンを作成する

Braze ダッシュボードで、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンにはアクションベースの配信があり、`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内から記録されたカスタムイベントからトリガーされる必要があります。

以下の例では、イベントプロパティを最初のサイレントプッシュの一部として送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

![カスタムイベント「アプリ内メッセージトリガー」を実行したユーザーに配信されるアクションベースの配信アプリ内メッセージキャンペーンで、「campaign_name」が「IAM Campaign Name Example」と等しい場合に配信されます。]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
なお、これらのアプリ内メッセージは、アプリケーションがフォアグラウンドにある間にサイレントプッシュが受信された場合にのみトリガーされます。
{% endalert %}

