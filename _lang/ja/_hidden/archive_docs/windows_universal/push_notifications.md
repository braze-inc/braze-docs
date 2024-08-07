---
nav_title: プッシュ通知
article_title: Windows Universal のプッシュ通知
platform: Windows Universal
page_order: 1
description: "本稿では、ウィンドウズ汎用プラットフォームのプッシュ通知インテグレーションについて説明します。"
channel: push 
hidden: true
---

# プッシュ通知の統合
{% multi_lang_include archive/windows_deprecation.md %}

![windows universal push の例。][10]{: style="float:right;max-width:40%;margin-left:15px;"}

プッシュ通知は、重要なアップデートが発生したときにユーザーの画面に表示されるアプリ外のアラートです。プッシュ通知は、時間的制約があって関連性の高いコンテンツをユーザーに提供したり、ユーザーをアプリに再エンゲージしたりするための効果的な方法です。

追加のベストプラクティスについては、\[ドキュメント][9]を参照してください。

## ステップ 1:プッシュ用にアプリライケーションを設定する

`Package.appxmanifest` ファイルで、次の設定s が設定されていることを確認します。

**Application**タブ内で、`Toast Capable`が`YES`に設定されていることを確認します。

## ステップ2:Braze ダッシュボードの設定

1. [SID とクライアントシークレットの検索][4]
2. 設定s に、Braze ダッシュボードの**設定s** ページ内にSID とクライアントシークレットを追加します。<br>![][6]

## ステップ3:バックグラウンド 開封ログのアップデート

`OnLaunched` メソッドで、`OpenSession` を呼び出した後に、以下のコード スニペットを追加します。

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);          
}
```

## ステップ 4:イベントハンドラの作成

プッシュを受信して有効化(ユーザーでクリック) したときに起動されるイベントをリスンするには、イベントハンドラを作成し、それらを`PushManager` イベントに追加します。

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

イベントハンドラには、以下のシグネチャが必要です。

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## ステップ 5: アプリへの押し込みによる深いリンク

### パート 1:アプリのためのディープリンクの作成

ディープリンクは、アプリライケーションの外部からアプリライケーションの特定のスクリーンまたはページにユーザーをナビゲートするために使用されます。通常、これは、URL スキーム(myapp://mypage など) をオペレーティングシステムに登録し、そのスキームを処理するためにアプリライセンスを登録することによって行われます。OS が、そのフォーマットのURL を開封するよう求められたときに、アプリライセンスにコントロールを転送します。

WNS のディープリンクサポートは、ユーザーの送信先に関するデータを含むアプリライケーションを起動するため、これとは異なります。WNSプッシュが作成されると、プッシュがクリックされ、アプリのライケーションが開封されたときに、アプリライケーションの`OnLaunched` に渡される起動文字列を含めることができます。すでにこの起動文字列を使用してキャンペーン "トラッキングを実行しています。ユーザー には、アプリの起動時に構文解析およびユーザーのナビゲートに使用できる独自のデータをアプリできます。

ダッシュボード またはREST API で追加の起動文字列を指定すると、キー"abextras=" の後に、作成した起動文字列の末尾に追加されます。そのため、サンプルの起動文字列は`ab_cn_id=_trackingid_abextras=page=settings` のようになります。この場合、追加の起動文字列パラメータで`page=settings` を指定すると、それを解析してユーザーを設定のs ページに移動できます。

### パート 2:ダッシュボードを介した深いリンク

"Additional Launch String Configuration" フィールド in プッシュ通知 設定 s で、起動文字列に対してアプリ終了する文字列を指定します。

![][15]

### 第3部:REST API を介したディープリンク

Braze では、REST API を介してディープリンクを送信することもできます。\[Windows Universal push objects][13] オプションの`extra_launch_string` パラメータを受け入れます。

[4]: http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx
[6]: {% image_buster /assets/img_archive/windows_sid.png %} "Windows SID ダッシュボード"
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[10]: {% image_buster /assets/img_archive/windows_uni_push_sample.png %}
[13]: {{site.baseurl}}/api/objects_filters/messaging/windows_objects/
[15]: {% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Deep Link Click Action"
