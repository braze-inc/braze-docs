---
nav_title: プッシュ通知
article_title: Windows Universal のプッシュ通知
platform: Windows Universal
page_order: 1
description: "この記事では、windowsユニバーサルプラットフォームのプッシュ通知統合手順について説明します。"
channel: push 
hidden: true
---

# プッシュ通知統合
{% multi_lang_include archive/windows_deprecation.md %}

![例:windows universal push.][10]{: style="float:right;max-width:40%;margin-left:15px;"}

プッシュ通知は、重要な更新が発生したときにユーザの画面に表示される、アプリ外アラートです。プッシュ通知は、時間に敏感で関連性のあるコンテンツをユーザーに提供したり、アプリに再び参加させたりするための貴重な手段です。

その他のベストプラクティスについては、[ドキュメンテーション][9] を参照してください。

## ステップ 3:アプリケーションをプッシュ用に設定する

`Package.appxmanifest` ファイルで、次の設定が構成されていることを確認します。

**Application**タブ内で、`Toast Capable`が`YES`に設定されていることを確認します。

## ステップ 3:Brazeダッシュボードの設定

1. [SID とクライアントシークレットの検索][4]
2. Braze ダッシュボードの**Settings** ページで、設定にSID とクライアントシークレットを追加します。<br>![][6]

## ステップ 3:バックグラウンドオープンロギングの更新

`OnLaunched` メソッドで、`OpenSession` を呼び出した後に、以下のコードスニペットを追加します。

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);          
}
```

## ステップ 4: イベントハンドラの作成

プッシュが受信されてアクティブ化(ユーザがクリック) されたときに起動されるイベントをリスンするには、イベントハンドラを作成し、`PushManager` イベントに追加します。

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

イベントハンドラには、以下のシグネチャが必要です。

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## ステップ 5: アプリへのプッシュからのディープリンク

### パート 1アプリのディープリンクの作成

ディープリンクは、アプリケーションの外部から、アプリケーションの特定の画面またはページに直接ユーザをナビゲートするために使用されます。通常、これは、URL スキーム(例: myapp://mypage) をオペレーティングシステムに登録し、そのスキームを処理するためにアプリケーションを登録することによって行われます。OS がそのフォーマットのURL を開くように要求された場合、アプリケーションに制御が転送されます。

WNS のディープリンクサポートは、ユーザーの送信先に関するデータを使用してアプリケーションを起動するため、これとは異なります。WNS プッシュが作成されると、プッシュがクリックされアプリケーションが開かれたときにアプリケーションの`OnLaunched` に渡される起動文字列を含めることができます。すでにこの起動文字列を使用してキャンペーントラッキングを行っており、アプリの起動時にユーザーをナビゲートするために解析および使用できる独自のデータをユーザーに追加する機能をユーザーに提供しています。

ダッシュボードまたはREST API で追加の起動文字列を指定すると、キー"abextras=" の後に、作成した起動文字列の末尾に追加されます。そのため、起動文字列の例は`ab_cn_id=_trackingid_abextras=page=settings` のようになります。この例では、追加の起動文字列パラメータで`page=settings` を指定しています。これを解析して、ユーザを設定ページに移動することができます。

### パート 1ダッシュボードを介したディープリンク

「"Additional Launch String Configuration"」フィールドのプッシュ通知設定で、起動文字列に追加する文字列を指定します。

![][15]

### パート 1REST API を介したディープリンク

Braze では、REST API 経由でディープリンクを送信することもできます。[Windows Universal push objects][13] は、オプションの`extra_launch_string` パラメータを受け入れます。

[4]: http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx
[6]: {% image_buster /assets/img_archive/windows_sid.png %} "Windows SID ダッシュボードとクォート;
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[10]: {% image_buster /assets/img_archive/windows_uni_push_sample.png %}
[13]: {{site.baseurl}}/api/objects_filters/messaging/windows_objects/
[15]: {% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Deep Link Click Action"
