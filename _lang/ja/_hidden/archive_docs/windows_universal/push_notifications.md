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

![ユニバーサル・プッシュの例である。][10]{: style="float:right;max-width:40%;margin-left:15px;"}

プッシュ通知は、重要なアップデートが発生したときにユーザーの画面に表示されるアプリ外のアラートです。プッシュ通知は、時間的制約があって関連性の高いコンテンツをユーザーに提供したり、ユーザーをアプリに再エンゲージしたりするための効果的な方法です。

その他のベストプラクティスについては、\[ドキュメント][9] ] を参照のこと。

## ステップ 1:プッシュ用にアプリケーションを設定する

`Package.appxmanifest` 、以下の設定がされていることを確認する：

**アプリケーション**タブで、`Toast Capable` が`YES` に設定されていることを確認する。

## ステップ2:Brazeダッシュボードを設定する

1. [SIDとクライアントシークレットを検索する][4]
2. Brazeダッシュボードの**設定**ページで、SIDとクライアントシークレットを設定に追加する。<br>![][6]

## ステップ3:バックグラウンド・オープン・ロギングの更新

`OnLaunched` メソッドで、`OpenSession` をコールした後、以下のコード・スニペットを追加する。

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);          
}
```

## ステップ 4:イベントハンドラを作成する

プッシュが受信され、アクティベート（ユーザーがクリック）されたときに発生するイベントをリッスンするには、イベント・ハンドラを作成し、`PushManager` のイベントに追加する：

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

イベント・ハンドラにはシグネチャが必要だ：

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## ステップ 5: プッシュからアプリへのディープリンク

### パート 1:アプリのディープリンクを作成する

ディープリンクは、アプリケーションの外部からユーザーをアプリケーションの特定の画面やページに直接ナビゲートするために使用される。通常これは、オペレーティング・システムにURLスキーム（例えば、myapp://mypage ）を登録し、そのスキームを処理するアプリケーションを登録することによって行われる。OSがその形式のURLを開くように要求されると、アプリケーションに制御が移る。

WNSのディープリンクサポートは、ユーザーをどこに送るかについてのデータでアプリケーションを起動するので、これとは異なる。WNSプッシュが作成されると、プッシュがクリックされアプリケーションが開かれたときに、アプリケーションの`OnLaunched` に渡される起動文字列を含めることができる。私たちはすでに、キャンペーン・トラッキングを行うためにこのローンチ文字列を使用しており、アプリが起動したときに解析され、ユーザーをナビゲートするために使用できる独自のデータを追加する能力をユーザーに与えている。

ダッシュボードやREST APIで追加の打ち上げ文字列を指定すると、作成する打ち上げ文字列の末尾、キー "abextras="の後に追加される。つまり、ローンチ文字列の例は、`ab_cn_id=_trackingid_abextras=page=settings` のようになる。この場合、ローンチ文字列の追加パラメータに`page=settings` を指定することで、それを解析してユーザーを設定ページにナビゲートすることができる。

### パート 2:ダッシュボードを使ったディープリンク

プッシュ通知設定の「追加起動文字列設定」フィールドで、起動文字列に追加する文字列を指定する。

![][15]

### パート3：REST APIによるディープリンク

Brazeは、REST APIを通じてディープリンクを送信することもできる。\[Windowsユニバーサルプッシュオブジェクト][13] は、オプションの`extra_launch_string` パラメータを受け付ける。

[4]: http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx
[6]: {% image_buster /assets/img_archive/windows_sid.png %} 「Windows SIDダッシュボード
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[10]: {% image_buster /assets/img_archive/windows_uni_push_sample.png %}
[13]: {{site.baseurl}}/api/objects_filters/messaging/windows_objects/
[15]: {% image_buster /assets/img_archive/windows_deep_link_click_action.png %} 「ディープリンクのクリックアクション
