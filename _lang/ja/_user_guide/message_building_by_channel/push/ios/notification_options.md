---
nav_title: "通知オプション"
article_title: iOS 通知オプション
page_order: 2
page_layout: reference
description: "この参考記事では、クリティカルアラート、クワイエット通知、暫定プッシュ通知などの iOS 通知オプションについて説明しています。"

platform: iOS
channel:
  - push

---

# 通知オプション

> [AppleのiOS 12のリリースにより、[Brazeは通知グループ、[クワイエット通知/仮承認](#provisional-push-authentication--quiet-notifications)](#notification-groups)、クリティカルアラートなど、いくつかの機能をサポートするようになりました。](#critical-alerts)

## 通知グループ

メッセージを分類してユーザーの通知トレイにグループ化したい場合は、BrazeのiOSの通知グループ機能を利用できます。

iOSプッシュキャンペーンを作成したら、**作成タブの上部にある**「**通知グループ**」ドロップダウンを見てください。

![][26]{: style="max-width:60%;" }

ドロップダウンから通知グループを選択します。通知グループの設定が誤動作した場合、またはドロップダウンから「**なし**」を選択した場合、メッセージはワークスペースで定義されているすべてのユーザーに通常どおり自動的に送信されます。

ここに通知グループがない場合は、iOS スレッド ID を使用して通知グループを追加できます。追加する通知グループごとに 1 つの iOS スレッド ID が必要です。次に、ドロップダウンの「**通知グループの管理」をクリックし、表示される「iOS プッシュ通知グループの管理****」ウィンドウの必須フィールドに入力して、通知グループに追加します**。

![][27]

iOS プッシュキャンペーンを作成したら、コンポーザーの一番上を見てください。そこに、**通知グループというラベルの付いたドロップダウンが表示されます**。

### 要約引数

通知をスレッドIDでグループ化することに加えて、Appleでは通知がグループ化されたときに表示される概要を編集できます。Brazeユーザーは、当社のツールを使用してプッシュキャンペーンを作成するときに、概要カテゴリ、要約数、および要約引数を指定できます。

{% alert tip %}
同じスレッド ID の通知を通知トレイにグループ化する方法は OS の制御下にあることに注意してください。iOS では、最適と判断される方法に応じて、同じスレッド ID の通知を個別に表示するか、グループ化して表示するかを選択できます。
{% endalert %}

**Push Composer** の「**アラートオプション**」ボックスをチェックします。

次に、`summary-arg``summary-arg-count`キーとしておよびを選択し、それらの値を対応する列に入力します。に値を設定しない場合`summary-arg`、デフォルトで 1 になります。

### 概要カテゴリー

サマリーカテゴリでは、通知をグループ化したときに表示されるサマリー全体をカスタマイズできます。複数のカテゴリを作成して適用できます。

メッセージでカテゴリを使用するには、開発者と協力して次の例を使用して実装してください。

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
これには SDK の更新は必要ありません。
{% endalert %}

{% alert tip %}
`%u``%@`とはそれぞれ、集計カウントと要約引数の文字列をフォーマットしていることに注意してください。概要が表示されると、`summary-count``summary-arg`これらのプレースホルダーはおよびの値に置き換えられます。
{% endalert %}

アプリでこれを設定したら、**通知ボタンボックスをチェックして**、「**事前登録済みのiOSカテゴリに入る」を選択して、概要カテゴリを使用してください**。

次に、アプリに設定したサマリーカテゴリ識別子を入力します。

### 暫定プッシュ認証とクワイエット通知 {#provisional-push}

Appleは、ブランドが公式に明示的にオプトインする前に、ユーザーの通知センターにサイレントプッシュ通知を送信するオプションを許可しています。これにより、メッセージの価値を早期に実証する機会が得られます。[アプリに仮プッシュ通知を設定するだけで、仮プッシュトークンを持っているすべてのユーザーがメッセージを受信できます](#set-up-provisional-push-notifications)。

従来のiOSプッシュトークンとは異なり、仮プッシュトークンは「トライアルパス」の役割を果たします。これにより、ブランドはAppleのネイティブプッシュオプトインプロンプトを見たりクリックしたりする前に、新しいユーザーにリーチできます。この機能により、プッシュ通知は新しいユーザーの通知トレイに直接配信され、今後の通知を「保持」または「オフ」のオプションを選択できます。ユーザーは「オプトイン」ジャーニーではなく、「オプトアウト」ジャーニーに近い体験をすることになります。

{% alert tip %}
仮承認はオプトイン率を劇的に高める可能性がありますが、それはユーザーがあなたのメッセージに価値を見出した場合に限られます。[ユーザーセグメンテーション]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)、[地域ターゲティング]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/)、[パーソナライズ機能を必ず使用して]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)、適切なユーザーにこれらの「トライアル」通知が適切なタイミングで届くようにしてください。そうすれば、プッシュ通知はユーザーのアプリ体験に付加価値をもたらすことがわかっているので、ユーザーにプッシュ通知を完全にオプトインするよう促すことができます。
{% endalert %}

ユーザーがどちらのオプションを選択しても、ユーザープロファイルの [**エンゲージメント**] [[タブにある連絡先設定に適切なトークンまたはサブスクリプションステータスが追加されます]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab)]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/)。

![\]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

[セグメンテーションフィルターを使用して]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)、ユーザーが暫定的に許可されているかどうかに基づいてユーザーをターゲットにすることができます。

![Segment Details panel with the sample segment filter "Provisionally Authorized on iOS Stopwatch (iOS) is true" to target users.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
ユーザーがあなたからの暫定プッシュを「オフにする」ことを選択した場合、あなたからの暫定プッシュメッセージは表示されなくなります。この機能を使用して送信されるメッセージの内容と頻度をよく考えてください。
{% endalert %}

{% alert important %}
[追加のプッシュプロンプトやアプリ内プッシュ入門（ユーザーにプッシュ通知へのオプトインを促すアプリ内メッセージ](https://www.braze.com/resources/glossary/priming-for-push/)）を使用する場合は、Braze の担当者に連絡して追加のガイダンスを受けてください。
{% endalert %}

#### 暫定プッシュ通知の設定

Brazeでは、以下のスニペットを例として使用して、Braze iOS SDK実装内のトークン登録スニペットのコードを更新することで、仮認証に登録できます（開発者に送信するか、[統合プロセス中に仮プッシュ認証を実装するようにしてください]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)）。

{% alert warning %}
暫定プッシュ認証の実装はiOS 12以降のみをサポートしており、デプロイ対象がそれより前の場合はエラーになります。詳細については、[こちらの詳細な実装ドキュメントをご覧ください]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)。
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**スイフト**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

**オブジェクティブ-C**

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

### インタラプション・レベル (iOS 15 以降) {#interruption-level}

![iOS Notification Settings page that shows notifications enabled for immediate delivery and with time sensitive notifications enabled.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15の新しいフォーカスモードにより、ユーザーはアプリの通知が音やバイブレーションで「中断」するタイミングをより細かく制御できます。

アプリは、緊急度に基づいて、通知に含める中断レベルを指定できるようになりました。

最終的にフォーカスをコントロールできるのはユーザーであり、Time Sensitive 通知が配信された場合でも、ユーザーはフォーカスを突破できないようにするアプリを指定できることに注意してください。

中断レベルとその説明については、次の表を参照してください。

|中断レベル|説明|いつ使用するか|ブレークスルーフォーカスモード|
|--|--|--|--|
| [パッシブ](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive) |音、バイブレーション、または画面をオンにせずに通知を送信します。|すぐに対応する必要のない通知。|いいえ|
| [アクティブ](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (デフォルト) |ユーザーがフォーカスモードでない場合にのみ、音とバイブレーションが発生し、画面がオンになります。|ユーザーがフォーカスモードを有効にしていない限り、すぐに注意が必要な通知。|いいえ|
| [タイムセンシティブ](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive) |フォーカスモードでも音が鳴り、振動し、画面がオンになります。そのためには、Xcode|Timely **通知機能を Xcode|Timely 通知にアプリに追加する必要があります。この機能は**、ライドシェアや配達通知など、ユーザーのフォーカスモードに関係なくユーザーの迷惑になるはずです。|はい|
| [クリティカル](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical) |電話の「**サイレントモード」スイッチが有効になっていても**、音が鳴り、振動し、画面がオンになります。[これにはAppleの明示的な承認が必要です](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/)。|悪天候や安全警告などの緊急事態|はい|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

iOS プッシュ通知の中断レベルを変更するには、「**設定**」タブを選択し、「**中断レベル」ドロップダウンメニューから目的のレベルを選択します**。

![中断レベルをアクティブ (デフォルト) に設定し、展開して使用可能なすべての中断レベルを表示:パッシブ、アクティブ (デフォルト)、タイムセンシティブ、クリティカル。] [28]

この機能には SDK の最低バージョン要件はありませんが、iOS 15 以降を実行しているデバイスにのみ適用されます。

### 関連性スコア (iOS 15 以降) {#relevance-score}

![A notification summary for iOS titled "Your Evening Summary" with three notifications.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15では、ユーザーがオプションで複数の通知のダイジェストグループを一日の指定された時間にスケジュールできる新しい方法も導入されています。これは、すぐに対応する必要のない通知が 1 日中絶え間なく中断されるのを防ぐためです。

アプリは、**関連性スコアを設定することで、どのプッシュ通知が最も関連性が高いかを指定できます**。Appleはこのスコアを使用して、どの通知をスケジュールされた通知概要に表示し、他の通知はユーザーが概要をクリックすると表示されるかを決定します。 

すべての通知には、引き続きユーザーの通知センターからアクセスできます。

iOS 通知の関連性スコアを設定するには、`0.0``1.0`**設定タブ内の値との間の値を入力します**。たとえば、最も重要なメッセージはで送信する必要がありますが`1.0`、`0.5`重要度が中程度のメッセージはで送信できます。

![][29]

この機能には SDK の最低バージョン要件はありませんが、iOS 15 以降を実行しているデバイスにのみ適用されます。

さまざまなメッセージタイプの最大メッセージ長の詳細については、次のリソースを参照してください。

- [画像とテキストの仕様]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [iOS 文字数のガイドライン]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

[26]: {% image_buster /assets/img_archive/notification_group_dropdown.png %}
[27]: {% image_buster /assets/img_archive/managenotgroups.png %}
[28]: {% image_buster /assets/img/ios/interruption-level.png %}
[29]: {% image_buster /assets/img/ios/relevance-score.png %}
