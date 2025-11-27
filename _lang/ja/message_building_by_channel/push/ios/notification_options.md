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

> アップルのiOS 12のリリースに伴い、Brazeは、[通知グループ](#notification-groups)、[静かな通知／暫定承認](#provisional-push-authentication--quiet-notifications)、[重要なアラートなど](#critical-alerts)、いくつかの機能をサポートしている。

## 通知グループ

メッセージを分類し、ユーザーの通知トレイにグループ分けしたい場合は、Brazeを通じてiOSの通知グループ機能を利用できる。

iOS プッシュ通知のキャンペーンを作成し、[**設定**] タブに移動して、[**通知グループ**] ドロップダウンを開きます。

![[設定] タブの [通知グループ] ドロップダウンで「Coupons」という値が選択されている。]({% image_buster /assets/img_archive/notification_group_dropdown.png %})({: style="max-width:50%;" })

ドロップダウンから通知グループを選択する。通知グループの設定に不具合がある場合、またはドロップダウンから [**なし**] を選択した場合、メッセージはワークスペース内のすべての定義済みユーザーに通常どおり自動的に送信されます。

ここに通知グループがない場合は、iOSのスレッドIDを使って追加できる。追加したい通知グループごとに、iOSスレッドIDが1つ必要だ。次に、ドロップダウンの [**通知グループを管理**] をクリックし、表示される [**iOS プッシュ通知グループを管理**] ウィンドウの必須フィールドに入力して、iOS スレッド ID を通知グループに追加します。

![iOS プッシュ通知グループを管理するためのウィンドウ。]({% image_buster /assets/img_archive/managenotgroups.png %})({: style="max-width:70%;" })

iOS プッシュキャンペーンを作成したら、作成画面の上部を確認します。そこに、**Notification Groups（通知グループ**）と書かれたドロップダウンがある。

### 要約の引数

スレッドIDで通知をグループ化するだけでなく、アップルでは通知がグループ化されたときに表示されるサマリーを編集することもできる。Brazeユーザーは、私たちのツールを使ってプッシュキャンペーンを作成する際に、サマリーカテゴリー、サマリーカウント、サマリー引数を指定することができる。

{% alert tip %}
同じスレッドIDを持つ通知が通知トレイでグループ化される方法は、OSの制御下にあることに注意。iOSは、最適と思われる方法によって、同じスレッドIDを持つ通知を別々に表示するか、グループ化して表示するかを選択できる。
{% endalert %}

**プッシュ作成画面**の [**アラートオプション**] ボックスをオンにします。

次に、キーとして `summary-arg` と `summary-arg-count` を選択し、対応する列にそれらの値を入力します。`summary-arg` に値を設定しなければ、デフォルトで1になる。

### 要約カテゴリ

サマリーカテゴリーでは、通知がグループ化されたときに表示されるサマリー全体をカスタマイズできる。複数のカテゴリを作成して適用できます。

メッセージにカテゴリーを使用するには、開発者と協力して以下の例を使って実装する：

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
これにはSDKのアップデートは必要ない。
{% endalert %}

{% alert tip %}
`%u` および `%@` は、それぞれ要約数と要約の引数の書式設定文字列であることに注意してください。要約が表示されると、これらのプレースホルダーは`summary-count` と`summary-arg` の値に置き換えられる。
{% endalert %}

これがアプリに設定されたら、**Notification Buttons（通知ボタン）**ボックスをチェックし、**Enter Pre-registered iOS Category（事前登録されたiOSカテゴリーを入力**）を選択して、サマリーカテゴリーを使用する。

次に、アプリで設定した要約カテゴリー識別子を入力する。

### 暫定的なプッシュ認証と静かな通知 {#provisional-push}

Apple は、ユーザーが明示的にオプトインする前に、ユーザーの通知センターにサイレントプッシュ通知の送信をブランドに許可ており、お客様のメッセージの価値を早期に示す機会を提供しています。あなたのアプリで[仮のプッシュ通知を設定](#set-up-provisional-push-notifications)するだけで、仮のプッシュトークンを持っているユーザーは誰でもあなたのメッセージを受け取ることができる。

従来のiOSプッシュトークンとは異なり、プロビジョナル・プッシュトークンは「トライアルパス」として機能し、ブランドがアップルのネイティブ・プッシュのオプトイン・プロンプトを見てクリックする前の新規ユーザーにリーチすることを可能にする。この機能により、お客様のプッシュ通知は新規ユーザーの通知トレイに直接配信され、今後の通知を「保持」または「オフ」にするオプションが付きます。ユーザーは「オプトイン」ジャーニーを体験する代わりに、「オプトアウト」ジャーニーのような体験をします。

{% alert tip %}
暫定承認には、オプトイン率を劇的に高める可能性がありますが、ただしユーザーがお客様のメッセージに価値を認めた場合に限られます。[ユーザーセグメンテーション]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)、[ロケーションターゲティング]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/)、[パーソナライゼーション]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)機能を使って、適切なユーザーが適切なタイミングで「トライアル」通知を受け取れるようにしよう。そうすれば、プッシュ通知がユーザーのアプリ体験に付加価値を与えることを理解した上で、ユーザーにプッシュ通知への完全なオプトインを促すことができる。
{% endalert %}

ユーザーがどちらのオプションを選択しても、ユーザープロフィールの**Engagement**タブにある[Contact Settingsに]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab)適切なトークンまたは[サブスクリプションステータスが]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/)追加される。

![プッシュ通知のステータスが [購読登録済み] の連絡先の設定。]({% image_buster /assets/img/profile-push-prov-auth.png %})({: width="50%"})

[セグメンテーション・フィルターを使って]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)、仮承認か否かに基づいてユーザーをターゲティングすることができる。

![セグメント詳細パネルにサンプルセグメントフィルター「iOSストップウォッチ(iOS)で仮承認がtrue」を設定し、ユーザーを絞り込む]({% image_buster /assets/img/segment-push-prov-auth.png %})()

{% alert tip %}
もしユーザーがあなたからの暫定プッシュを「オフ」にすると、もうあなたからの暫定プッシュメッセージは表示されなくなる。この機能を使って送信されるメッセージの内容や順序には十分注意すること！
{% endalert %}

{% alert important %}
追加のプッシュプロンプトや[アプリ内プッシュプライマー](https://www.braze.com/resources/glossary/priming-for-push/)（ユーザーにプッシュ通知のオプトインを促すアプリ内メッセージ）を使用する場合は、Brazeの担当者に連絡して追加のガイダンスを受けてください。
{% endalert %}

#### 仮のプッシュ通知を設定する

Brazeでは、以下のスニペットを例として、Braze iOS SDK実装内のトークン登録スニペットでコードを更新することで、プロビジョナル認証に登録することができる（これらを開発者に送信するか、[統合プロセス中にプロビジョナルプッシュ認証を実装する]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)ようにしてください）。

{% alert warning %}
プロビジョナル・プッシュ認証の実装はiOS 12+のみをサポートしており、デプロイメント対象がそれ以前の場合はエラーとなる。この詳細については、[当社の詳細な実装ドキュメント]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)を参照してください。
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

### 割り込みレベル (iOS 15以降){#interruption-level}

iOS 15の新しいフォーカス・モードでは、ユーザーはアプリの通知を音や振動で「中断」させるタイミングをより自由にコントロールできる。

![iOSの通知設定ページでは、即時配信が有効な通知と、時間指定通知が有効な通知が表示される。]({% image_buster /assets/img/ios/ios15-notification-settings.png %})({: style="max-width:40%"})

緊急度に基づいて、通知に含める必要がある割り込みのレベルをアプリで指定できるようになりました。

iOSプッシュ通知の中断レベルを変更するには、**「設定」**タブを選択し、「**中断レベル」**ドロップダウンメニューから希望のレベルを選択する。

![中断レベルを選択するためのドロップダウン。]({% image_buster /assets/img/ios/interruption_level.png %})({: style="max-width:50%"})

この機能にはSDKの最小バージョン要件はないが、iOS 15以上を搭載したデバイスにのみ適用される。

最終的にフォーカスをコントロールできるのはユーザーであり、たとえTime Sensitive通知が配信されても、フォーカスを突破することを許さないアプリを指定できることを心に留めておいてほしい。

割り込みレベルとその説明については、次の表を参照してください。

|割り込みレベル|説明|いつ使うか|ブレイクスルー・フォーカスモード|
|--|--|--|--|
|[Passive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|音声、振動、または画面表示なしで通知を送信します。|直ちに注意を払う必要のない通知。|いいえ|
|[Active](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (デフォルト)|フォーカスモードでない場合にのみ、音声と振動が伴い、画面表示を行います。|ユーザーがフォーカスモードを有効にしていない限り、すぐに注意を払う必要がある通知。|いいえ|
|[Time Sensitive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|フォーカスモードでも音声と振動を伴い、画面が表示されます。このためには、Xcode でアプリに **Time Sensitive Notifications 機能**を追加する必要があります。|ライドシェアや配送の通知など、フォーカスモードに関係なくユーザーに注意を促すタイムリーな通知。|はい|
|[Critical](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|携帯電話の**Do Not Disturb**スイッチが有効になっていても、音が鳴り、バイブレーションが鳴り、画面がオンになる。これには、[Apple による明示的な承認](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/)が必要です。|悪天候や安全警告などの緊急事態|はい|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 関連性スコア（iOS 15以上） {#relevance-score}

![]({% image_buster /assets/img/ios/ios15-notification-summary.png %})({: style="float:right;max-width:25%;margin-left:15px;border:0"}) "Your Evening Summary "と題されたiOS用の通知サマリーと3つの通知。

またiOS 15では、1日を通して指定した時間に、複数の通知をダイジェストでまとめるスケジュールをユーザーが任意に設定できるようになった。これは、すぐに注意を払う必要のない通知により一日中繰り返される割り込みを防ぐ措置です。

アプリで **Relevance Score** を設定することで、関連性が最も高いプッシュ通知を指定できます。アップルはこのスコアを使って、スケジュールされた通知サマリーでどの通知を表示すべきかを決定し、他の通知はユーザーがサマリーをクリックしたときに表示されるようにする。 

すべての通知には、ユーザーの通知センターで引き続きアクセスできます。

iOS通知の関連性スコアを設定するには、**設定**タブで`0.0` から`1.0` の間の値を入力する。例えば、最重要メッセージは `1.0` で送信する必要があり、重要度が中のメッセージは `0.5` で送信できます。

![「0.5」の関連性スコア。]({% image_buster /assets/img/ios/relevance-score.png %})({: style="max-width:80%;"})

この機能にはSDKの最小バージョン要件はないが、iOS 15以上を搭載したデバイスにのみ適用される。

さまざまなメッセージタイプの最大メッセージ長については、以下のリソースを参照してください。

- [画像とテキストの仕様]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [iOS の文字数ガイドライン]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

