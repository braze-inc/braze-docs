---
nav_title: "プッシュ有効化とサブスクリプション"
article_title: プッシュ有効化とサブスクリプション
page_order: 3
page_type: reference
description: "このリファレンス記事では、iOS、Android、Web 間の動作の基本的な違いを含め、Braze のプッシュ有効化とプッシュ サブスクリプション状態の概念について説明します。"
channel:
  - push

---

# プッシュの有効化とプッシュのサブスクリプション

> このリファレンス記事では、iOS、Android、Web 間の動作の基本的な違いを含め、Braze のプッシュ有効化とプッシュ サブスクリプション状態の概念について説明します。

## プッシュサブスクリプション状態 {#push-sub-states}

Braze の「プッシュ サブスクリプション状態」は、プッシュ通知を受信するかどうかの **ユーザーの** 全体的な設定を識別します。サブスクリプションの状態はユーザーベースであるため、個々のアプリに固有のものではありません。サブスクリプションの状態は、プッシュ通知の対象となるユーザーを決定する際に役立つフラグになります。

{% alert note %}
ユーザーのプッシュ サブスクリプションの状態は、ユーザーのすべてのデバイスを含むユーザー プロファイル全体に適用されます。
{% endalert %}

プッシュ サブスクリプションの状態オプションには 3 つあります。 `Subscribed`、 `Opted-In`、 そして `Unsubscribed`。

デフォルトでは、ユーザーがプッシュ経由でメッセージを受信するには、プッシュサブスクリプションの状態が次のいずれかである必要があります。 `Subscribed` または `Opted-In` [プッシュが有効になって](#push-enabled)いる必要があります。メッセージを作成するときに、必要に応じてこの設定を上書きできます。

|オプトイン状態|説明|
|---|---|
|`Subscribed`| Braze でユーザー プロファイルが作成されたときのデフォルトのプッシュ サブスクリプション状態。 |
|`Opted-In`| ユーザーがプッシュ通知を受信することを明示的に希望しました。Brazeは自動的にユーザーのオプトイン状態を `Opted-In` ユーザーが OS レベルのプッシュ プロンプトを受け入れた場合。<br><br>これは Android 12 以下のユーザーには適用されません。|
|`Unsubscribed`| ユーザーがアプリケーションまたはブランドが提供するその他の方法を通じてプッシュ通知を明示的に解除しました。デフォルトでは、Brazeプッシュキャンペーンは、 `Subscribed` または `Opted-in` プッシュ用。|
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Brazeはユーザーのプッシュサブスクリプション状態を自動的に変更しません。 `Unsubscribed`。ユーザーのプッシュ通知購読状態が `Unsubscribed`、その後、ユーザーの `Push Enabled` セグメンテーションのフィルターは `false`。
{% endalert %}

### プッシュサブスクリプションの状態の更新 {#update-push-subscription-state}

ユーザーのプッシュ サブスクリプション状態を更新するには、次の 3 つの方法があります。

1. **SDK統合**<br>Braze SDK を使用して、ユーザーのサブスクリプション状態を更新します。たとえば、ユーザーが自分のプロフィールのプッシュ通知をオンまたはオフにできる設定ページをアプリに追加できます。<br>これを行うには、 `setPushNotificationSubscriptionType` [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype)、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html)、または [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#afb2c11d1889fd08537f90ee64c94efb3)での方法。<br><br>
2. **REST API**<br>[\` を使用してください/users/track` endpoint][users-track] to update the [`push_subscribe`][user_attributes_object] attribute for a given user.<br><br>
3. **オプトイン時に自動的に**<br>ユーザーがネイティブOSのプッシュ許可プロンプトを受け入れると、Brazeは自動的にそのユーザーのサブスクリプション状態を次のように変更します。 `Opted-In`。

### プッシュサブスクリプションの状態を確認しています

![プッシュ サブスクリプションの状態が [サブスクライブ済み] に設定されている John Doe のユーザー プロファイル。][3]{: style="float:right;max-width:35%;margin-left:15px;"}

Braze を使用してユーザーのプッシュ サブスクリプションの状態を確認するには、次の 2 つの方法があります。

1. **ユーザープロフィールBrazeダッシュボードの **[ユーザー検索][5]** ページから個々のユーザープロファイルにアクセスできます。ユーザーのプロファイル（メールアドレス、電話番号、または外部ユーザー ID 経由）を見つけたら、**[エンゲージメント** ] タブを選択して、ユーザーのサブスクリプション状態を表示し、手動で調整できます。
<br><br>
2. **REST API エクスポート**:エクスポート [セグメント別のユーザー][セグメント] または [識別子別のユーザー][識別子] エンドポイントを使用して、個々のユーザー プロファイルを JSON 形式でエクスポートできます。Braze は、デバイスごとのプッシュ有効化情報を含むプッシュ トークン オブジェクトを返します。

## プッシュ権限

プッシュ対応のすべてのプラットフォーム (iOS、Web、Android) では、OS レベルのシステム プロンプトを介した明示的なオプトインが必要ですが、以下に説明するわずかな違いがあります。

ユーザーの決定は最終的なものであり、拒否した後に再度尋ねることはできないため、[push primer][push-primers] アプリ内メッセージを使用することは、オプトイン率を高めるための重要な戦略です。

**ネイティブOSプッシュ許可プロンプト**

|プラットフォーム|スクリーンショット|説明|
|--|--|--|
|iOS| ![「私のアプリが通知を送信しようとしています」と尋ねる iOS ネイティブのプッシュ プロンプト。メッセージの下部には「許可しない」と「許可」の 2 つのボタンがあります。][ios-push-prompt]{: style="max-width:410px;"}| [暫定プッシュ](#provisional-push) 権限を要求する場合には適用されません。|
|Android| ![「Kitchenerie に通知の送信を許可しますか?」と尋ねる Android プッシュ メッセージ。メッセージの下部には「許可」と「許可しない」の 2 つのボタンがあります。][android-push-prompt]{: style="max-width:410px;"}| このプッシュ権限は Android 13 で導入されました。Android 13 より前では、プッシュを送信するために許可は必要ありませんでした。|
|Web| ![「Braze.com が通知を表示しようとしています」と尋ねる Web ブラウザのネイティブ プッシュ プロンプト。メッセージの下部には「ブロック」と「許可」の 2 つのボタンがあります。][web-push-prompt]{: style="max-width:410px;"}| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Android

Android 13 より前では、プッシュ通知を送信するために許可は必要ありませんでした。Android 12以下では、すべてのユーザーが対象となります `Subscribed` 最初のセッションで Braze が自動的にプッシュ トークンを要求します。この時点で、ユーザーはそのデバイス用の有効なプッシュトークンとデフォルトのサブスクリプション状態により **プッシュが有効になっています。**`Subscribed`。

[Android 13][android-13] 以降では、プッシュ権限はユーザーに要求され、付与される必要があります。アプリは適切なタイミングでユーザーに手動で許可をリクエストできますが、そうでない場合は、アプリが [通知チャネル](https://developer.android.com/reference/android/app/NotificationChannel)を作成するときにユーザーに自動的にプロンプ​​トが表示されます。

### iOS

![システム通知センターの通知。下部に「Yachtr アプリからの通知を受信し続けますか?」というメッセージが表示され、その下に「保持」または「オフにする」の 2 つのボタンがあります][ios-provisional-push]{: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

アプリは暫定プッシュまたは承認済みプッシュをリクエストできます。 

承認されたプッシュでは、通知を送信する前にユーザーからの明示的な許可が必要ですが、[暫定プッシュ][暫定ブログ] では、音やアラートなしで通知センターに直接 __静かに__通知を送信できます。

#### 暫定承認と静かな推進 {#provisional-push}

iOS 12（2018 年リリース）より前では、すべてのユーザーがプッシュ通知を受信することを明示的にオプトインする必要があります。

iOS 12 では、Apple は [暫定承認][暫定ブログ] を導入し、ユーザーが明示的にオプトインする前にブランドがユーザーの通知センターに静かなプッシュ通知を送信できるようにしました。これにより、メッセージの価値を早い段階で実証する機会が与えられます。詳細については、 [暫定承認]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications) を参照してください。

### Web

Web の場合、ネイティブ ブラウザの許可ダイアログを介して明示的なユーザー オプトインを要求する必要があります。

アプリがいつでも許可プロンプトを表示できる iOS や Android とは異なり、一部の最新ブラウザでは、「ユーザー ジェスチャ」(マウス クリックまたはキーストローク) によってトリガーされた場合にのみプロンプトが表示されます。サイトがページの読み込み時にプッシュ通知の許可を要求しようとすると、ブラウザによって無視されるか、または無効にされる可能性があります。

したがって、ページが読み込まれたときにランダムに許可を求めるのではなく、ユーザーが Web サイトのどこかをクリックしたときにのみ許可を求める必要があります。

## プッシュトークン

[プッシュ トークン][push-tokens] は、ユーザーのデバイスによって生成され、各受信者の通知を送信する場所を識別するために Braze に送信される一意の匿名識別子です。

[プッシュ トークン][push-tokens] を分類する方法は 2 つあり、プッシュ通知をユーザーに送信する方法を理解する上で重要です。

1. **フォアグラウンド プッシュは、** ユーザーのデバイスのフォアグラウンドに定期的に表示されるプッシュ通知を送信する機能を提供します。
2. **バックグラウンド プッシュは** 、特定のデバイスがそのブランドからのプッシュ通知を受信するようにオプトインしているかどうかに関係なく利用できます。バックグラウンド プッシュを使用すると、ブランドは、 [アンインストール追跡]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/)などの主要機能をサポートするために、意図的に表示されないサイレント プッシュ通知をデバイスに送信できます。

ユーザー プロファイルにアプリに関連付けられた有効なフォアグラウンド プッシュ トークンがある場合、Braze はユーザーが特定のアプリに対して「プッシュ登録済み」であるとみなします。Brazeは特定のセグメンテーションフィルタを提供します。 `Push Enabled for App,` これらのユーザーを識別するのに役立ちます。

{% alert note %}
の `Push Enabled for App` フィルターは、指定されたアプリの有効なフォアグラウンドおよびバックグラウンド プッシュ トークンの存在のみを考慮します。しかし、より一般的な [`Push Enabled`](#push-enabled) ワークスペース内のアプリに対してプッシュ通知を明示的に有効にしたユーザーをフィルター セグメント化します。この数にはフォアグラウンド プッシュのみが含まれ、登録解除したユーザーは含まれません。これらのフィルターやその他のフィルターの詳細については、[「セグメンテーション フィルター」]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters)を参照してください。
{% endalert %}

### 1つのデバイスで複数のユーザー

プッシュ トークンはデバイスとアプリの両方に固有であるため、プッシュ トークンを使用して同じデバイスを使用している複数のユーザーを区別することはできません。

たとえば、次の 2 人のユーザーがいるとします。チャーリーとキム。チャーリーが自分の携帯電話でアプリのプッシュ通知を有効にしていて、キムがチャーリーの携帯電話を使用してチャーリーのプロフィールからログアウトし、自分のプロフィールにログインした場合、プッシュ トークンはキムのプロフィールに再割り当てされます。プッシュ トークンは、キムがログアウトしてチャーリーが再度ログインするまで、そのデバイス上のキムのプロファイルに割り当てられたままになります。

アプリまたは Web サイトには、デバイスごとに 1 つのプッシュ サブスクリプションのみを設定できます。したがって、ユーザーがデバイスまたは Web サイトからログアウトし、新しいユーザーがログインすると、プッシュ トークンは新しいユーザーに再割り当てされます。これは、 **エンゲージメント**の **連絡先設定** セクションのユーザープロフィールに反映されます。 tab:

![ユーザープロフィールの\*\*エンゲージメント**タブにあるプッシュトークンの変更ログには、プッシュトークンが別のユーザーにいつ移動されたか、およびそのトークンが何であったかがリストされます。][4]

プッシュ プロバイダー (APNs/FCM) が 1 つのデバイス上の複数のユーザーを区別する方法がないため、最後にログインしたユーザーにプッシュ トークンを渡して、デバイス上でプッシュの対象となるユーザーを決定します。

### 複数のデバイスと 1 人のユーザー

プッシュ サブスクリプションの状態はユーザーベースであり、個々のアプリに固有のものではありません。プッシュ サブスクリプションの状態は、最後に設定された値です。ユーザーがプッシュ通知をオプトインした場合、プッシュ通知の購読状態は `Opted-in` すべての対象デバイスでご利用いただけます。ユーザーが後日、アプリケーションまたはブランドが提供する他の方法を通じてプッシュ通知の購読を明示的に解除した場合、プッシュ通知の購読状態は次のように更新されます。 `Unsubscribed` プッシュ登録されたデバイスはプッシュ通知を受信できません。

## プッシュ対応フィルター {#push-enabled}

`Push Enabled` は、Braze のセグメンテーション フィルターであり、マーケティング担当者は、Braze がプッシュ通知を送信することを許可しているユーザーと、プッシュ通知を受信しないことを希望していないユーザーを簡単に識別できます。 

の `Push Enabled` フィルターでは次の点を考慮します。
\- Braze がプッシュ通知を送信する機能 (フォアグラウンド プッシュ トークン)
\- ユーザーが自分のデバイスでプッシュを受信する全体的な設定（プッシュサブスクリプション状態）

![ダッシュボードのスクリーンショット。ユーザーが「マーケティングにプッシュ登録済み (iOS)」であることを示しています][1]{: style="float:right;max-width:50%;margin-left:15px;"}

ユーザーがワークスペース内のアプリに対してアクティブなフォアグラウンド プッシュ トークンを持っている場合、そのユーザーは「プッシュが有効」または「プッシュが登録済み」であると見なされます。つまり、プッシュの有効化ステータスはアプリ固有です。 

{% alert note %}
プッシュ登録状態を確認する方法については、 [プッシュ登録ステータス]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#checking-push-registration-status)をご覧ください。
{% endalert %}

## その他のプラットフォーム固有のシナリオ

{% tabs %}
{% tab Android %}

フォアグラウンド プッシュが有効になっているユーザーが OS 設定でプッシュを無効にした場合、次のセッションの開始時に次の処理が行われます。
\- Braze はこれらをフォアグラウンド プッシュ無効としてマークし、プッシュ メッセージを送信しなくなります。
\- の `Push Enabled for App (Android)` フィルターと `Push Enabled` セグメンテーションフィルタ（ユーザープロファイル上の他のアプリに有効なフォアグラウンドプッシュトークンがないと仮定）は、 `false`。

このシナリオでは、バックグラウンドプッシュトークンがまだ存在するため、セグメンテーションフィルターを使用してバックグラウンド（サイレント）プッシュ通知を送信し続けることができます。 `Background Push Enabled = true`。

Android の場合、Braze は次の場合にユーザー プッシュが無効であるとみなします。

- ユーザーがデバイスからアプリをアンインストールします。
- バウンスのためプッシュ メッセージが配信されません。これはアンインストールによって発生することが多いですが、アプリの更新、新しいプッシュ トークンのバージョン、または形式によって発生することもあります。 
- Firebase Cloud Messaging へのプッシュ登録が失敗します (ネットワーク接続が不良であったり、FCM への接続または FCM 上で有効なトークンを返せなかったりすることが原因である場合があります)。
- ユーザーはデバイス設定内でアプリのプッシュ通知をブロックし、その後セッションをログに記録します。

{% endtab %}
{% tab iOS %}

ユーザーがフォアグラウンドプッシュオプトインプロンプトを受け入れるかどうかに関係なく、Xcodeでリモート通知が有効になっていて、アプリが呼び出している場合は、バックグラウンドプッシュを送信できます。 [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications)。

アプリが暫定的に承認されている場合、またはユーザーがプッシュを選択した場合、フォアグラウンド プッシュ トークンがユーザーに送信され、あらゆる種類のプッシュを送信できるようになります。Braze では、フォアグラウンド プッシュが有効になっている iOS ユーザーは、明示的に (アプリ レベル) または暫定的に (デバイス レベル) プッシュが有効になっているとみなされます。

ユーザーがOSレベルでプッシュ通知の受信を拒否した場合、プッシュ通知の購読状態は `Subscribed`、そのプロファイルにはフォアグラウンド プッシュ トークンが登録されていることは表示されません。 

最初に OS レベルでオプトインしたユーザーが OS 設定でプッシュ通知を無効にした場合、次回のセッション開始時に次のことが起こります。
\- Braze はフォアグラウンド プッシュを無効としてマークし、プッシュ メッセージを送信しなくなります。
\- の `Push Enabled for App (iOS)` フィルターと `Push Enabled` セグメンテーションフィルタ（ユーザープロファイル上の他のアプリに有効なフォアグラウンドプッシュトークンがないと仮定）は、 `false`。

このシナリオでは、バックグラウンドプッシュトークンがまだ存在するため、セグメンテーションフィルターを使用してバックグラウンド（サイレント）プッシュ通知を送信し続けることができます。 `Background Push Enabled = true`。

{% endtab %}
{% tab Web %}

ユーザーがネイティブプッシュ許可プロンプトを承認すると、サブスクリプションステータスは次のように変更されます。 `opted in`。

サブスクリプションを管理するには、ユーザーメソッドを使用できます [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) サイトに環境設定ページを作成すると、ダッシュボードでオプトアウトステータス別にユーザーをフィルタリングできるようになります。

ユーザーがブラウザ内で通知を無効にすると、そのユーザーに送信される次のプッシュ通知はバウンスされ、Braze はそれに応じてユーザーのプッシュ トークンを更新します。これは、プッシュ対応フィルターの適格性を管理するために使用されます（`Background Push Enabled`、 `Push Enabled` そして `Push Enabled for App`）。ユーザーのプロフィールに設定されたサブスクリプション ステータスはユーザー レベルの設定であり、プッシュがバウンスしても変更されません。

{% alert note %}
Web プラットフォームでは、バックグラウンド プッシュやサイレント プッシュは許可されません。
{% endalert %}
{% endtab %}
{% endtabs %}

## ベストプラクティス

Braze でのプッシュの使用を最適化する方法の詳細なガイダンスについては、 [プッシュのベスト プラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices) に関する専用の記事を参照してください。

[1]: {% image_buster /assets/img/push_enablement.png %}
[2]: {% image_buster /assets/img/push_changelog.png %}
[3]: {% image_buster /assets/img/push_example.png %}
[4]: {% image_buster /assets/img/push_token_changelog.png %}
[push-tokens]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
[ios-push-prompt]: {% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}
[android-push-prompt]: {% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}
[web-push-prompt]: {% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}
[ios-provisional-push]: {% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}
[push-primers]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/
[android-13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/android_13/
[仮ブログ]: https://www.braze.com/resources/articles/mastering-provisional-push
[user\_attributes\_object]: {{site.baseurl}}/api/objects_filters/user_attributes_object
[users-track]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
