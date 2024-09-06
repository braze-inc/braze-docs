---
nav_title: "通知オプション"
article_title: iOSの通知オプション
page_order: 2
page_layout: reference
description: "この参考記事では、重要なアラート、静かな通知、暫定的なプッシュ通知など、iOSの通知オプションについて取り上げている。"

platform: iOS
channel:
  - push

---

# 通知オプション

> アップルのiOS 12のリリースに伴い、Brazeは、[通知グループ](#notification-groups)、[静かな通知／暫定承認](#provisional-push-authentication--quiet-notifications)、[重要なアラートなど](#critical-alerts)、いくつかの機能をサポートしている。

## 通知グループ

メッセージを分類し、ユーザーの通知トレイにグループ分けしたい場合は、Brazeを通じてiOSの通知グループ機能を利用できる。

iOSプッシュ・キャンペーンを作成し、**\[メール送信]**タブの一番上にある\[**通知グループ]**ドロップダウンを探す。

![][26]{: style="max-width:60%;" }

ドロップダウンから通知グループを選択する。通知グループの設定がうまくいかなかったり、ドロップダウンから**Noneを**選択した場合、メッセージは自動的にワークスペース内の定義されたすべてのユーザーに通常通り送信される。

ここに通知グループがない場合は、iOSのスレッドIDを使って追加できる。追加したい通知グループごとに、iOSスレッドIDが1つ必要だ。次に、ドロップダウンの「**Manage Notification Groups」を**クリックし、表示される「**Manage iOS Push Notification Groups**」ウィンドウで必要事項を入力して、通知グループに追加する。

![][27]

iOSプッシュ・キャンペーンを作成し、コンポーザーのトップを見る。そこに、**Notification Groups（通知グループ**）と書かれたドロップダウンがある。

### 要約

スレッドIDで通知をグループ化するだけでなく、アップルでは通知がグループ化されたときに表示されるサマリーを編集することもできる。Brazeユーザーは、私たちのツールを使ってプッシュキャンペーンを作成する際に、サマリーカテゴリー、サマリーカウント、サマリー引数を指定することができる。

{% alert tip %}
同じスレッドIDを持つ通知が通知トレイでグループ化される方法は、OSの制御下にあることに注意。iOSは、最適と思われる方法によって、同じスレッドIDを持つ通知を別々に表示するか、グループ化して表示するかを選択できる。
{% endalert %}

**Push Composerの** **Alert Options**ボックスをチェックする。

次に、`summary-arg` と`summary-arg-count` をキーとして選択し、対応する列にそれらの値を入力する。`summary-arg` に値を設定しなければ、デフォルトで1になる。

### 概要カテゴリー

サマリーカテゴリーでは、通知がグループ化されたときに表示されるサマリー全体をカスタマイズできる。複数のカテゴリーを作成し、適用することができる。

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
`%u` 、`%@` 、それぞれ要約カウントと要約引数のフォーマット文字列であることに注意。要約が表示されると、これらのプレースホルダーは`summary-count` と`summary-arg` の値に置き換えられる。
{% endalert %}

これがアプリに設定されたら、**Notification Buttons（通知ボタン）**ボックスをチェックし、**Enter Pre-registered iOS Category（事前登録されたiOSカテゴリーを入力**）を選択して、サマリーカテゴリーを使用する。

次に、アプリで設定した要約カテゴリー識別子を入力する。

### 暫定的なプッシュ認証と静かな通知 {#provisional-push}

アップルは、ユーザーが正式に明示的にオプトインする前に、ブランドがユーザーの通知センターに静かなプッシュ通知を送信するオプションを認めている。あなたのアプリで[仮のプッシュ通知を設定](#set-up-provisional-push-notifications)するだけで、仮のプッシュトークンを持っているユーザーは誰でもあなたのメッセージを受け取ることができる。

従来のiOSプッシュトークンとは異なり、プロビジョナル・プッシュトークンは「トライアル・パス」として機能し、ブランドがアップルのネイティブ・プッシュのオプトイン・プロンプトを見たりクリックしたりする前の新規ユーザーにアプローチすることを可能にする。この機能により、あなたのプッシュ通知は新規ユーザーの通知トレイに直接配信され、今後の通知を "保持 "または "オフ "にすることができる。ユーザーは「オプトイン」の旅を体験する代わりに、「オプトアウト」の旅に近いものを体験することになる。

{% alert tip %}
仮承認は、オプトイン率を劇的に高める可能性を秘めているが、それはユーザーがあなたのメッセージに価値を見出した場合に限られる。[ユーザーセグメンテーション]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)、[ロケーションターゲティング]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/)、[パーソナライゼーション]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)機能を使って、適切なユーザーが適切なタイミングで「トライアル」通知を受け取れるようにしよう。そうすれば、プッシュ通知がユーザーのアプリ体験に付加価値を与えることを理解した上で、ユーザーにプッシュ通知への完全なオプトインを促すことができる。
{% endalert %}

ユーザーがどちらのオプションを選択しても、ユーザープロフィールの**Engagement**タブにある[Contact Settingsに]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab)適切なトークンまたは[サブスクリプションステータスが]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/)追加される。

![]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

[セグメンテーション・フィルターを使って]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)、仮承認か否かに基づいてユーザーをターゲティングすることができる。

![セグメント詳細パネルにサンプルセグメントフィルター「iOSストップウォッチ(iOS)で仮承認がtrue」を設定し、ユーザーを絞り込む]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
もしユーザーがあなたからの暫定プッシュを「オフ」にすると、もうあなたからの暫定プッシュメッセージは表示されなくなる。この機能を使って送信されるメッセージの内容や順序には十分注意すること！
{% endalert %}

{% alert important %}
追加のプッシュプロンプトや[アプリ内プッシュプライマー](https://www.braze.com/resources/glossary/priming-for-push/)（プッシュ通知へのオプトインを促すアプリ内メッセージ）を使用する場合は、Brazeの担当者に連絡して追加のガイダンスを受ける。
{% endalert %}

#### 仮のプッシュ通知を設定する

Brazeでは、以下のスニペットを例として、Braze iOS SDK実装内のトークン登録スニペットでコードを更新することで、プロビジョナル認証に登録することができる（これらを開発者に送信するか、[統合プロセス中にプロビジョナルプッシュ認証を実装する]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)ようにしてください）。

{% alert warning %}
プロビジョナル・プッシュ認証の実装はiOS 12+のみをサポートしており、デプロイメント対象がそれ以前の場合はエラーとなる。これについては[、こちらの詳細な実装ドキュメントを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)ご覧いただきたい。
{% endalert %}

{% tabs ローカル %}
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

### 中断レベル（iOS 15以上） {#interruption-level}

![iOSの通知設定ページでは、即時配信が有効な通知と、時間指定通知が有効な通知が表示される。]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15の新しいフォーカス・モードでは、ユーザーはアプリの通知を音や振動で「中断」させるタイミングをより自由にコントロールできる。

アプリは、緊急度に基づいて、通知にどのレベルの中断を含めるべきかを指定できるようになった。

最終的にフォーカスをコントロールできるのはユーザーであり、たとえTime Sensitive通知が配信されても、フォーカスを突破することを許さないアプリを指定できることを心に留めておいてほしい。

中断レベルとその説明については、以下の表を参照のこと。

|中断レベル|説明|いつ使うか|ブレイクスルー・フォーカスモード|
|--|--|--|--|
|[パッシブ](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|音やバイブレーション、画面の点灯なしに通知を送る。|直ちに注意を払う必要のない通知。|いいえ|
|[アクティブ](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active)（デフォルト）|フォーカスモードでない場合のみ、音と振動が鳴り、スクリーンが点灯する。|ユーザーがフォーカスモードを有効にしていない限り、すぐに注意を払う必要がある通知。|いいえ|
|[時間に敏感](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|フォーカスモード中でも音が鳴り、振動し、画面が点灯する。このためには、Xcode でアプリに**Time Sensitive Notifications 機能を**追加する必要がある。|ライドシェアや配達通知など、フォーカスのモードに関係なくユーザーの邪魔になるようなタイムリーな通知。|はい|
|[クリティカル](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|携帯電話の**Do Not Disturb**スイッチが有効になっていても、音が鳴り、バイブレーションが鳴り、画面がオンになる。[これにはアップルの明確な承認が必要](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/)だ。|悪天候や安全警告などの緊急事態|はい|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

iOSプッシュ通知の中断レベルを変更するには、**「設定」**タブを選択し、「**中断レベル」**ドロップダウンメニューから希望のレベルを選択する。

![中断レベルをアクティブ（デフォルト）に設定し、使用可能なすべての中断レベルを表示するように拡大する：パッシブ、アクティブ（デフォルト）、タイムセンシティブ、クリティカル。][28]

この機能にはSDKの最小バージョン要件はないが、iOS 15以上を搭載したデバイスにのみ適用される。

### 関連性スコア（iOS 15以上） {#relevance-score}

![]({% image_buster /assets/img/ios/ios15-notification-summary.png %}) "Your Evening Summary "と題されたiOS用の通知サマリーと3つの通知。{: style="float:right;max-width:25%;margin-left:15px;border:0"}

またiOS 15では、1日を通して指定した時間に、複数の通知をダイジェストでまとめるスケジュールをユーザーが任意に設定できるようになった。これは、すぐに注意を払う必要のない通知で一日中中断され続けるのを防ぐためだ。

アプリは、**関連性スコアを**設定することで、どのプッシュ通知が最も関連性があるかを指定できる。アップルはこのスコアを使って、スケジュールされた通知サマリーでどの通知を表示すべきかを決定し、他の通知はユーザーがサマリーをクリックしたときに表示されるようにする。 

すべての通知は、ユーザーの通知センターでアクセスできる。

iOS通知の関連性スコアを設定するには、**設定**タブで`0.0` から`1.0` の間の値を入力する。例えば、最重要メッセージは`1.0` で送るべきであり、中重要メッセージは`0.5` で送ることができる。

![][29]

この機能にはSDKの最小バージョン要件はないが、iOS 15以上を搭載したデバイスにのみ適用される。

メッセージタイプ別の最大メッセージ長については、以下のリソースを参照のこと：

- [画像とテキストの仕様]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [iOSの文字数ガイドライン]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

[26]: {% image_buster /assets/img_archive/notification_group_dropdown.png %}
[27]: {% image_buster /assets/img_archive/managenotgroups.png %}
[28]: {% image_buster /assets/img/ios/interruption-level.png %}
[29]: {% image_buster /assets/img/ios/relevance-score.png %}
