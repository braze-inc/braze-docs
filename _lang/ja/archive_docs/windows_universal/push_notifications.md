---
nav_title: プッシュ通知
article_title: Windows Universalのプッシュ通知
platform: Windows Universal
page_order: 1
description: "この記事では、ウィンドウズ・ユニバーサル・プラットフォーム用のプッシュ通知統合手順について説明する。"
channel: push 
hidden: true
---

# プッシュ通知の統合
{% multi_lang_include archive/windows_deprecation.md %}

![Windows Universal プッシュ通知の例。]({% image_buster /assets/img_archive/windows_uni_push_sample.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

プッシュ通知は、重要なアップデートが発生したときにユーザーの画面に表示されるアプリ外のアラートです。プッシュ通知は、時間的制約があって関連性の高いコンテンツをユーザーに提供したり、ユーザーをアプリに再エンゲージしたりするための効果的な方法です。

その他のベストプラクティスについては、[ドキュメント[]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/) ] を参照のこと。

## ステップ 1: プッシュ通知用にアプリケーションを設定する

`Package.appxmanifest` ファイルで、次の設定が構成されていることを確認します。

**アプリケーション**タブで、`Toast Capable` が`YES` に設定されていることを確認する。

## ステップ2:Brazeダッシュボードを設定する

1. [SID とクライアントシークレットを検索する](http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx)
2. Brazeダッシュボードの**設定**ページで、SIDとクライアントシークレットを設定に追加する。<br>![]({% image_buster /assets/img_archive/windows_sid.png %} "Windows SID dashboard")

## ステップ 3: バックグラウンド開封ロギングの更新

`OnLaunched` メソッドで、`OpenSession` をコールした後、以下のコード・スニペットを追加する。

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);          
}
```

## ステップ4:イベントハンドラを作成する

プッシュが受信され、アクティベート（ユーザーがクリック）されたときに発生するイベントをリッスンするには、イベント・ハンドラを作成し、`PushManager` のイベントに追加する：

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

イベントハンドラには、署名が必要です。

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## ステップ 5: プッシュからアプリへのディープリンク

### パート 1:アプリのディープリンクを作成する

ディープリンクは、アプリケーションの外部からユーザーをアプリケーションの特定の画面やページに直接ナビゲートするために使用される。通常これは、オペレーティング・システムにURLスキーム（例えば、myapp://mypage ）を登録し、そのスキームを処理するアプリケーションを登録することによって行われる。OSがその形式のURLを開くように要求されると、アプリケーションに制御が移る。

WNSのディープリンクサポートは、ユーザーをどこに送るかについてのデータでアプリケーションを起動するので、これとは異なる。WNS プッシュが作成されると、プッシュがクリックされアプリケーションが開かれたときに、アプリケーションの `OnLaunched` に渡される起動文字列を含めることができます。私たちはすでに、キャンペーン・トラッキングを行うためにこのローンチ文字列を使用しており、アプリが起動したときに解析され、ユーザーをナビゲートするために使用できる独自のデータを追加する能力をユーザーに与えている。

ダッシュボードや REST API で追加の起動文字列を指定すると、作成した起動文字列の末尾、キー「abextras=」の後に追加されます。そのため、起動文字列の例は `ab_cn_id=_trackingid_abextras=page=settings` のようになります。この例では、追加の起動文字列パラメータで `page=settings` を指定しているため、これを解析してユーザーを設定ページに移動できます。

### パート 2:ダッシュボードを使ったディープリンク

プッシュ通知設定の [追加の起動文字列設定] フィールドで、起動文字列に追加する文字列を指定します。

![]({% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Deep Link Click Action")

### パート3：REST APIによるディープリンク

Brazeでは、REST APIを通じてディープリンクを送信することもできる。[Windowsユニバーサルプッシュオブジェクトは]({{site.baseurl}}/api/objects_filters/)、オプションの`extra_launch_string` パラメータを受け付ける。

