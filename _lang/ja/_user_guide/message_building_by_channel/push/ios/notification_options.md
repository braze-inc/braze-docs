---
nav_title: "通知オプション"
article_title: iOSの通知オプション
page_order: 2
page_layout: reference
description: "このリファレンス記事では、重要なアラート、サイレント通知、暫定プッシュ通知などの iOS 通知オプションについて説明します。"

platform: iOS
channel:
  - push

---

# 通知オプション

> AppleのiOS 12のリリースに伴い、Brazeは[通知グループ](#notification-groups)、[サイレント通知／暫定承認](#provisional-push-authentication--quiet-notifications)、[重要なアラート](#critical-alerts)など、いくつかの機能をサポートしています。

## 通知グループ

メッセージを分類し、ユーザーの通知トレイにグループ分けしたい場合は、Brazeを通じてiOSの通知グループ機能を利用できます。

iOSプッシュキャンペーンを作成したら、**設定**タブに移動し、**通知グループ**ドロップダウンを開きます。

![「設定」タブにある「通知グループ」ドロップダウンで「クーポン」を選択した状態。]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

ドロップダウンから通知グループを選択します。通知グループの設定に不具合がある場合、またはドロップダウンから [**なし**] を選択した場合、メッセージはワークスペース内のすべての定義済みユーザーに通常どおり自動的に送信されます。

ここに通知グループがない場合は、iOSのスレッドIDを使って追加できます。追加したい通知グループごとに、iOSスレッドIDが1つ必要です。次に、ドロップダウンの [**通知グループを管理**] をクリックし、表示される [**iOS プッシュ通知グループを管理**] ウィンドウの必須フィールドに入力して、iOS スレッド ID を通知グループに追加します。

![iOSプッシュ通知グループを管理するウィンドウ。]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

iOSプッシュキャンペーンを作成したら、作成画面の上部を確認します。そこに、**通知グループ**と書かれたドロップダウンがあります。

### 要約の引数

スレッドIDで通知をグループ化するだけでなく、Appleでは通知がグループ化されたときに表示されるサマリーを編集することもできます。Brazeユーザーは、当社のツールを使ってプッシュキャンペーンを作成する際に、サマリーカテゴリー、サマリーカウント、サマリー引数を指定できます。

{% alert tip %}
同じスレッドIDを持つ通知が通知トレイでグループ化される方法は、OSの制御下にあることに注意してください。iOSは、最適と判断した方法に応じて、同じスレッドIDを持つ通知を別々に表示するか、グループ化して表示するかを選択する場合があります。
{% endalert %}

**プッシュ作成画面**の [**アラートオプション**] ボックスをオンにします。

次に、キーとして `summary-arg` と `summary-arg-count` を選択し、対応する列にそれらの値を入力します。`summary-arg` に値を設定しなければ、デフォルトで1になります。

### 要約カテゴリ

サマリーカテゴリーでは、通知がグループ化されたときに表示されるサマリー全体をカスタマイズできます。複数のカテゴリを作成して適用できます。

メッセージにカテゴリーを使用するには、開発者と協力して以下の例を参考に実装してください：

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
これにはSDKの更新は必要ありません。
{% endalert %}

{% alert tip %}
`%u` および `%@` は、それぞれサマリーカウントとサマリー引数の書式設定文字列であることに注意してください。サマリーが表示されると、これらのプレースホルダーは `summary-count` と `summary-arg` の値に置き換えられます。
{% endalert %}

これがアプリに設定されたら、**通知ボタン**ボックスをチェックし、**事前登録されたiOSカテゴリーを入力**を選択して、サマリーカテゴリーを使用します。

次に、アプリで設定したサマリーカテゴリー識別子を入力します。

### 暫定的なプッシュ認証とサイレント通知 {#provisional-push}

Appleは、ユーザーが正式に明示的にオプトインする前に、ユーザーの通知センターにサイレントプッシュ通知を送信するオプションをブランドに提供しており、メッセージの価値を早期に示す機会を与えています。アプリで[暫定プッシュ通知を設定](#set-up-provisional-push-notifications)するだけで、暫定プッシュトークンを持っているユーザーは誰でもメッセージを受け取ることができます。

従来のiOSプッシュトークンとは異なり、暫定プッシュトークンは「お試しパス」として機能し、ブランドは新規ユーザーがAppleのネイティブプッシュオプトインプロンプトを閲覧・クリックする前にリーチできます。この機能により、プッシュ通知は新規ユーザーの通知トレイに直接配信され、今後の通知を「保持」または「オフにする」オプションが付きます。ユーザーは「オプトイン」ジャーニーを体験する代わりに、「オプトアウト」ジャーニーに近い体験をします。

{% alert tip %}
暫定承認には、オプトイン率を劇的に高める可能性がありますが、ユーザーがメッセージに価値を認めた場合に限られます。[ユーザーセグメンテーション]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)、[ロケーションターゲティング]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/)、[パーソナライゼーション]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)機能を使って、適切なユーザーが適切なタイミングで「トライアル」通知を受け取れるようにしましょう。そうすれば、プッシュ通知がユーザーのアプリ体験に付加価値を与えることを理解した上で、ユーザーにプッシュ通知への完全なオプトインを促すことができます。
{% endalert %}

ユーザーがどちらのオプションを選択しても、ユーザープロファイルの**エンゲージメント**タブにある[連絡先設定]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab)に適切なトークンまたは[サブスクリプションステータス]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/)が追加されます。

![プッシュ購読中ステータスの連絡先設定。]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

[セグメンテーションフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)を使って、暫定承認済みかどうかに基づいてユーザーをターゲティングできます。

![ユーザーをターゲットにするため、サンプルセグメントフィルター「iOSストップウォッチで暫定承認済み（iOS）が真」を設定したセグメント詳細パネル。]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
ユーザーが暫定プッシュを「オフにする」を選択すると、それ以降暫定プッシュメッセージは表示されなくなります。この機能を使って送信されるメッセージのコンテンツや頻度には十分注意してください！
{% endalert %}

{% alert important %}
追加のプッシュプロンプトや[アプリ内プッシュプライマー](https://www.braze.com/resources/glossary/priming-for-push/)（プッシュ通知の受信をユーザーに促すアプリ内メッセージ）を使用する場合は、追加のガイダンスについてBraze担当者にお問い合わせください。
{% endalert %}

#### 暫定プッシュ通知を設定する

Brazeでは、以下のスニペットを例として、Braze iOS SDK実装内のトークン登録スニペットでコードを更新することで、暫定認証に登録できます（これらを開発者に送信するか、[統合プロセス中に暫定プッシュ認証を実装する]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)ようにしてください）。

{% alert warning %}
暫定プッシュ認証の実装はiOS 12以降のみをサポートしており、デプロイメントターゲットがそれ以前の場合はエラーとなります。詳細については、[こちらの詳細な実装ドキュメント]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)を参照してください。
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**Swift**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

**Objective-C**

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### 割り込みレベル（iOS 15以降） {#interruption-level}

iOS 15の新しい集中モードでは、ユーザーはアプリの通知が音や振動で「割り込む」タイミングをより自由にコントロールできます。

![iOSの通知設定ページ。即時配信が有効な通知と、時間制限のある通知が有効な状態が表示されている。]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

アプリでは、緊急度に基づいて通知に含める割り込みのレベルを指定できるようになりました。

iOSプッシュ通知の割り込みレベルを変更するには、**設定**タブを選択し、**割り込みレベル**ドロップダウンメニューから希望のレベルを選択します。

![割り込みレベルを選択するためのドロップダウン。]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

この機能にはSDKの最小バージョン要件はありませんが、iOS 15以上を搭載したデバイスにのみ適用されます。

最終的に集中モードをコントロールできるのはユーザーであり、たとえTime Sensitive通知が配信されても、集中モードの突破を許可しないアプリを指定できることに留意してください。

割り込みレベルとその説明については、次の表を参照してください。

|割り込みレベル|説明|使用するタイミング|集中モードの突破|
|--|--|--|--|
|[Passive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|音声、振動、または画面表示なしで通知を送信します。|すぐに注意を払う必要のない通知。|いいえ|
|[Active](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active)（デフォルト）|集中モードでない場合にのみ、音声と振動を伴い、画面を表示します。|ユーザーが集中モードを有効にしていない限り、すぐに注意を払う必要がある通知。|いいえ|
|[Time Sensitive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|集中モード中でも音声と振動を伴い、画面を表示します。このためには、Xcodeでアプリに**Time Sensitive Notifications機能**を追加する必要があります。|ライドシェアや配送の通知など、集中モードに関係なくユーザーに注意を促すタイムリーな通知。|はい|
|[Critical](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|端末の**おやすみモード**スイッチが有効になっていても、音が鳴り、振動し、画面がオンになります。これには、[Appleによる明示的な承認](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/)が必要です。|悪天候や安全警告などの緊急事態。|はい|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 関連性スコア（iOS 15以降） {#relevance-score}

![iOS向けの通知サマリー「あなたの夜のまとめ」には、3つの通知が含まれている。]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

またiOS 15では、1日を通して指定した時間に複数の通知をダイジェストでまとめるスケジュールをユーザーが任意に設定できるようになりました。これは、すぐに注意を払う必要のない通知による一日中の繰り返しの割り込みを防ぐための措置です。

アプリで**関連性スコア**を設定することで、関連性が最も高いプッシュ通知を指定できます。Appleはこのスコアを使って、スケジュールされた通知サマリーでどの通知を表示すべきかを決定し、他の通知はユーザーがサマリーをクリックしたときに表示されるようにします。

すべての通知には、ユーザーの通知センターで引き続きアクセスできます。

iOS通知の関連性スコアを設定するには、**設定**タブで `0.0` から `1.0` の間の値を入力します。例えば、最重要メッセージは `1.0` で送信し、重要度が中程度のメッセージは `0.5` で送信できます。

![関連性スコアは「0.5」。]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

この機能にはSDKの最小バージョン要件はありませんが、iOS 15以上を搭載したデバイスにのみ適用されます。

さまざまなメッセージタイプの最大メッセージ長については、以下のリソースを参照してください。

- [プッシュの画像とテキストの仕様]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)
- [iOSの文字数ガイドライン]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)