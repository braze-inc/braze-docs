---
nav_title: カスタムトリガー
article_title: iOS 用アプリ内メッセージトリガーのカスタマイズ
platform: iOS
page_order: 7
description: "この参考記事では、iOS アプリケーションのアプリ内メッセージングのカスタムトリガーについて説明します。"
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# カスタムアプリ内メッセージトリガー

デフォルトでは、アプリ内メッセージは SDK によって記録されるイベントタイプによってトリガーされます。サーバー送信イベントによってアプリ内メッセージをトリガーしたい場合にも実現できます。

この機能を有効にするには、サイレントプッシュをデバイスに送信し、デバイスが SDK ベースのイベントをログに記録できるようにします。この SDK イベントは、その後、ユーザー向けのアプリ内メッセージをトリガーします。

## ステップ1:サイレントプッシュとキーと値のペアを扱う

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内に次のコードを追加します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [[Appboy sharedInstance] logCustomEvent:@"IAM Trigger" withProperties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
 };
```

{% endtab %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  NSLog("A push was received");
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    Appboy.sharedInstance()?.logCustomEvent("IAM Trigger", withProperties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% endtabs %}

サイレントプッシュを受信すると、ユーザープロファイルに対して SDK が記録したイベント「アプリ内メッセージトリガー」がログに記録されます。なお、これらのアプリ内メッセージは、アプリケーションがフォアグラウンドにある間にサイレントプッシュが受信された場合にのみトリガーされます。

## ステップ2:プッシュキャンペーンを作成する

サーバー送信イベントを介してトリガーされるサイレントプッシュキャンペーンを作成します。サイレントプッシュキャンペーンの作成の詳細については、「[サイレントプッシュ通知][39]」を参照してください。

![カスタムイベント「server\_event」を実行したユーザーに配信されるアクションベースの配信アプリ内メッセージキャンペーンです。][40]

プッシュキャンペーンにはキーと値のペアエクストラを含める必要があります。これは、このプッシュキャンペーンが SDK カスタムイベントを記録するために送信されることを示します。このイベントは次のアプリ内メッセージをトリガーするために使用されます。

![nキーと値のペアが2つあるアクションベースの配信アプリ内メッセージキャンペーン。"CAMPAIGN\_NAME" を "アプリ内メッセージ名の例" に設定し、"IS\_SERVER\_EVENT" を "true" に設定します。][41]

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内のコードはキー `IS_SERVER_EVENT` をチェックし、SDK カスタムイベントがあればログに記録します。

プッシュペイロードのキーと値のペアエクストラ内で目的の値を送信することで、イベント名またはイベントプロパティのいずれかを変更できます。カスタムイベントを記録する場合、これらのエクストラはイベント名のパラメータまたはイベントプロパティとして使用できます。

## ステップ 3:アプリ内メッセージキャンペーンを作成する

Braze ダッシュボード内から、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンにはアクションベースの配信があり、`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内から記録されたカスタムイベントからトリガーされる必要があります。

以下の例では、イベントプロパティを最初のサイレントプッシュの一部として送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

![カスタムイベント「アプリ内メッセージトリガー」を実行したユーザーに配信されるアクションベースの配信アプリ内メッセージキャンペーンです。"campaign\_name" は "アプリ内メッセージ名の例" です。][42]

SDK のログに記録されたカスタムイベントの記録にプッシュメッセージが使用されているため、Braze はこのソリューションを有効にするには、ユーザーごとにプッシュトークンを格納する必要があります。iOS と Android の両方で、Braze はユーザーが OS のプッシュプロンプトを受け取った時点からのトークンのみを保存します。これ以前では、ユーザーはプッシュを使用して到達できず、先行ソリューションも実行できません。

[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[40]: {% image_buster /assets/img_archive/iosServerSentPush.png %}
[41]: {% image_buster /assets/img_archive/iOSServerPush.png %}
[42]: {% image_buster /assets/img_archive/iosIAMeventTrigger.png %}