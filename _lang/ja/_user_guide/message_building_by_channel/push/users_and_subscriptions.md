---
nav_title: "プッシュ通知のイネーブルメントとサブスクリプション"
article_title: プッシュ通知のイネーブルメントとサブスクリプション
page_order: 3
page_type: reference
description: "このリファレンス記事では、Brazeにおけるプッシュ有効状態とプッシュ購読状態の概念について、iOS、Android、Webにおける動作の基本的な違いを含めて説明する。"
channel:
  - push

---

# プッシュ通知のイネーブルメントとサブスクリプション

> このリファレンス記事では、Braze におけるプッシュ通知のイネーブルメントとサブスクリプションの状態の概念について、iOS、Android、および Webにおける動作の基本的な違いを含めて説明します。

## プッシュ通知のサブスクリプションの状態{#push-sub-states}

Brazeの 「プッシュ通知のサブスクリプションの状態」は、プッシュ通知の受信を希望する**ユーザー**のグローバルな嗜好を識別します。サブスクリプションの状態はユーザーベースなので、個々のアプリに固有のものではない。サブスクリプションの状態は、プッシュ通知のターゲットにするユーザーを決定するときに役立つフラグです。

{% alert note %}
ユーザーのプッシュ通知のサブスクリプションの状態は、ユーザーのすべてのデバイスを含むユーザープロファイル全体に適用されます。
{% endalert %}

プッシュ通知のサブスクリプションの状態には、`Subscribed`、`Opted-In`、および`Unsubscribed` の 3 つのオプションがあります。

デフォルトで、プッシュ通知でユーザーがメッセージを受信するには、プッシュ通知のサブスクリプションの状態が `Subscribed` または`Opted-In` のいずれかであり、かつ [[プッシュ通知が有効](#push-enabled)] になっていなければなりません。メッセージの作成時に、この設定をオーバーライドできます。

|オプトイン状態|説明|
|---|---|
|`Subscribed`| Brazeでユーザープロファイルが作成されたときのデフォルトのプッシュ通知のサブスクリプション状態。 |
|`Opted-In`| ユーザーは、プッシュ通知を受け取ることを明示的に希望した。Braze では、ユーザーが OS レベルのプッシュプロンプトを承認した場合に、ユーザーのオプトイン状態を自動的に `Opted-In` に移動します。<br><br>Android 12 またはそれ以前のユーザーには適用されません。|
|`Unsubscribed`| ユーザーがアプリケーションやブランドが提供するその他の方法で、プッシュ配信を明示的に解除した。デフォルトで、Braze のプッシュキャンペーンは、プッシュが `Subscribed` または `Opted-in` のユーザーのみをターゲットにしています。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze で、ユーザーのプッシュ通知のサブスクリプションの状態を自動的に `Unsubscribed` にすることはありません。ユーザーのプッシュサブスクリプションのステートが`Unsubscribed` の場合、セグメンテーションにおけるユーザーの`Push Enabled` フィルタは`false` になることを覚えておいてほしい。
{% endalert %}

### プッシュ通知のサブスクリプションの状態の更新 {#update-push-subscription-state}

ユーザーのプッシュ通知のサブスクリプションの状態を更新するには、3 つの方法があります。

#### 自動オプトイン (デフォルト)

Braze はデフォルトで、ユーザーが初めてアプリのプッシュ通知を承認したときに、ユーザーのプッシュ通知のサブスクリプションの状態を `Opted-In` に設定します。Braze はまた、ユーザーがシステム設定でプッシュ許可を無効にした後、再度プッシュ許可を有効にした場合にもこれを行います。

{% tabs local %}
{% tab Android %}
このデフォルトの動作を無効にするには、Android Studio プロジェクトの `braze.xml` ファイルに次のプロパティを追加します。

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
[Braze Swift SDKバージョン 7.5.0 から](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0)、Xcode プロジェクトの `AppDelegate.swift` ファイルに `optInWhenPushAuthorized` の設定を追加することで、この動作を無効にしたり、さらにカスタマイズしたりすることができる：

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### SDKの統合

[Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype)、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html)、または [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)) 上で `setPushNotificationSubscriptionType` メソッドを使用して、Braze SDK でユーザーの購読状態を更新できる。例えば、この方法を使って、ユーザーが手動でプッシュ通知を有効または無効にできる設定ページをアプリ内に作成することができる。

#### REST API

[`/users/track` エンドポイント ][users-track] を使用して [`push_subscribe`][user_attributes_object] 属性を更新する Braze の REST API で、ユーザーのサブスクリプションの状態を更新できます。

### プッシュ通知のサブスクリプションの状態の確認

![John Doeのユーザープロファイルで、プッシュ購読の状態がSubscribedに設定されている。][3]{: style="float:right;max-width:35%;margin-left:15px;"}

Braze でユーザーのプッシュ通知のサブスクリプションの状態を確認するには、3 つの方法があります。

1. **ユーザープロフィール:**Braze ダッシュボードの [**[ユーザー検索][5]**] ページから、個々のユーザープロファイルにアクセスできます。Eメールアドレス、電話番号、または外部ユーザーIDを介して）ユーザーのプロフィールを見つけた後、**Engagement**タブを選択してユーザーの購読状態を表示し、手動で調整することができる。
<br><br>
2. **Rest API でのエクスポート**：[セグメント別のユーザー][segment] または[識別子別のユーザー][identifier]のエクスポートのエンドポイントを使用して、個々のユーザープロファイルを JSON 形式でエクスポートできます。Brazeは、デバイスごとのプッシュ有効化情報を含むプッシュトークンオブジェクトを返す。

## プッシュ許可

iOS、Web、Android のすべてのプッシュ対応プラットフォームで、OS レベルのシステムプロンプトからの明示的なオプトインが必要ですが、若干の違いがあり、それを以下にを示します。

ユーザーの決定は最終的なものであり、却下後に再度依頼することはできないため、[プッシュプライマー][push-primers] の アプリ内メッセージを使用することが、オプトイン率を高めるための重要な戦略です。

**ネイティブ OS のプッシュ許可プロンプト**

|プラットフォーム|スクリーンショット|説明|
|--|--|--|
|iOS| ![iOS のネイティブプッシュプロンプト「My App から通知を送信してよいですか?」と、メッセージの下部にある「許可しない」と「許可する」の 2 つのボタン。][ios-push-prompt]{: style="max-width:410px;"} | ただし、[仮のプッシュ](#provisional-push)許可を申請する場合はこの限りではない。|
|Android| ![Kitchenerieからの通知を許可しますか」と尋ねるアンドロイドのプッシュメッセージ。メッセージの下部に「許可する」と「許可しない」の2つのボタンがある。][android-push-prompt]{: style="max-width:410px;"} | このプッシュ許可は Android 13 で導入されました。Android 13 以前には、プッシュ通知の送信に許可は不要でした。|
|Web| ![Web ブラウザーのネイティブプッシュプロンプト「Braze.com からの通知を表示しますか?」と、メッセージの下部にある「ブロックする」と「許可する」の 2 つのボタン。][web-push-prompt]{: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Android

Android 13 以前には、プッシュ通知の送信に許可は不要でした。Android 12 とそれ以前では、最初のセッションで Braze が自動的にプッシュトークンを要求すると、すべてのユーザーが `Subscribed` と見なされました。この時点で、ユーザーはそのデバイスの有効なプッシュトークンと、`Subscribed` というデフォルトの購読状態で**プッシュ有効**になっている。

[Android 13][android-13] 以降、プッシュ許可を求めて、ユーザーから許可を得る必要があります。アプリから手動で、適切なタイミングでユーザーに許可を求めることができますが、そうでない場合は、アプリが[通知チャネル](https://developer.android.com/reference/android/app/NotificationChannel)を作成するときに、ユーザーに自動的にプロンプトが表示されます。

### iOS

![システムの通知センターに通知が表示され、下部に「Yachtrアプリからの通知を受信し続けますか」というメッセージと、その下に「受信し続ける」または「オフにする」の2つのボタンが表示される][ios-provisional-push]{: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

アプリから暫定プッシュまたは承認プッシュを要求できます。 

承認プッシュでは、通知を送信する前にユーザーからの明示的な許可が必要ですが、[暫定プッシュ][provisional-blog]では、音やアラートなしで通知センターに直接、__静かに__通知を送信できます。

#### 暫定承認とサイレントプッシュ{#provisional-push}

iOS 12（2018年リリース）以前は、すべてのユーザーがプッシュ通知の受信を明示的にオプトインする必要があった。

iOS12 で Apple は[暫定承認][provisional-blog]を導入し、ユーザーが明示的にオプトインする前に、ユーザーの通知センターにサイレントプッシュ通知の送信をブランドに許可したため、メッセージの価値を早期に示す機会が得られました。詳しくは[仮承認を]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications)参照のこと。

### Web

Web の場合、ネイティブブラウザーの許可ダイアログを通じて、ユーザーの明示的なオプトインを要求する必要があります。

iOS や Android の場合、アプリからいつでも許可プロンプトを表示できますが、最近のブラウザーの中には、「ユーザーのジェスチャー」(マウスクリックやキーストローク) でトリガーされたときにのみプロンプトを表示するものもあります。御社サイトでページの読み込み時にプッシュ通知の許可を要求しようとした場合、おそらくブラウザーによって無視されるか、表示されない可能性があります。

その結果、ユーザーがあなたのウェブサイトのどこかをクリックしたときにのみ許可を求めるべきであり、ページがロードされたときにランダムに許可を求めるべきでない。

## プッシュトークン

[プッシュトークン][push-tokens] ] は、ユーザーのデバイスによって生成され、各受信者の通知を送信する場所を特定するためにBrazeに送信される一意の匿名識別子である。

[プッシュトークン][push-tokens]には 2 つの分類方法があり、プッシュ通知をユーザーに送信する方法を理解するうえで不可欠です。

1. **フォアグラウンドプッシュ**は、ユーザーのデバイスのフォアグラウンドに、定期的に目に見えるプッシュ通知を送信する機能です。
2. **バックグラウンドプッシュ**は、特定のデバイスがそのブランドからのプッシュ通知の受信をオプトインしているかどうかに関係なく使用できます。バックグラウンドプッシュを使用すると、ブランドはサイレントプッシュ通知 (意図的に表示しない通知） をデバイスに送信して、[アンインストール追跡]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/)のような重要な機能をサポートできます。

ユーザープロファイルにアプリに関連付けられた有効なフォアグラウンドプッシュトークンがある場合、Brazeはそのユーザーを指定されたアプリの「プッシュ登録済み」とみなす。そこで、Braze にはそのようなユーザーの特定に役立つ特定のセグメンテーションフィルター `Push Enabled for App,` が用意されています。

{% alert note %}
`Push Enabled for App` フィルターは、指定されたアプリについて、有効なフォアグラウンドとバックグラウンドのプッシュトークンの有無のみを考慮します。しかし、より一般的な [`Push Enabled`](#push-enabled)フィルターは、ワークスペース内のアプリのプッシュ通知を明示的に有効にしたユーザーをセグメントする。この数にはフォアグラウンドプッシュのみが含まれ、配信停止したユーザーは含まれません。これらのフィルターやその他のフィルターについては、[セグメンテーション・フィルターで]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters)詳しく説明している。
{% endalert %}

### 1台のデバイスで複数のユーザーが利用できる

プッシュトークンはデバイスとアプリの両方に固有なので、プッシュトークンを使って同じデバイスを使っている複数のユーザーを区別することはできない。

例えば、2人のユーザーがいるとする：Charlie と Kim です。Charlie が自分の携帯電話でアプリのプッシュ通知を有効にしている場合、Kim が Charlie の携帯電話を使用して Charlie のプロファイルからログアウトし、自分のプロファイルにログインすると、プッシュトークンは Kim のプロファイルに割り当てし直されます。プッシュトークンは、Kim がログアウトして、Charlie が再度ログインするまで、そのデバイスの Kim のプロファイルに割り当てられたままになります。

アプリや Web サイトは、1 つのデバイスにつき 1 つのプッシュ通知サブスクリプションのみを持つことができます。そのため、ユーザーがデバイスやウェブサイトからログアウトし、新しいユーザーがログインすると、プッシュトークンは新しいユーザーに再割り当てされる。これは、[**エンゲージメント**] タブの [**連絡先の設定**] セクションにあるユーザープロファイルに反映されます。

![ユーザープロファイルの [エンゲージメント] タブにあるプッシュトークンの変更ログ。プッシュトークンが他のユーザーに移動した時点と、そのトークンがリストされます。][4]

プッシュ・プロバイダ（APN/FCM）には、1つのデバイス上の複数のユーザーを区別する方法がないため、最後にログインしたユーザーにプッシュ・トークンを渡し、デバイス上のどのユーザーをプッシュのターゲットにするかを決定する。

### 複数のデバイスと1人のユーザー

プッシュサブスクリプションの状態はユーザーベースであり、個々のアプリに固有のものではない。プッシュサブスクリプションの状態は、最後に設定された値である。そのため、ユーザーがプッシュ通知をオプトインしている場合、そのプッシュ通知のサブスクリプション状態は、該当するすべてのデバイスで `Opted-in` になります。その後、ユーザーがアプリケーションやブランドが提供するその他の方法でプッシュ通知を明示的に配信停止した場合、そのユーザーのプッシュ通知のサブスクリプション状態が `Unsubscribed` に更新され、プッシュが登録されているデバイスはプッシュ通知を受信できなくなります。

## 「プッシュ通知が有効」フィルター{#push-enabled}

`Push Enabled` は、Braze のセグメンテーションフィルターであり、これを使用すると、マーケターは、Braze によるプッシュ通知の送信を許可しているユーザーと、プッシュ通知を受信しないことを表明していないユーザーを簡単に識別できます。 

`Push Enabled` フィルターでは以下が考慮されます。
- Brazeがプッシュ通知を送信する機能（フォアグラウンド・プッシュ・トークン）
- どのデバイスでもプッシュを受信したいというユーザーの全体的な希望（プッシュ購読状態）

![ユーザーが "Push Registered for Marketing（iOS）"であることを示すダッシュボードのスクリーンショット。][1]{: style="float:right;max-width:50%;margin-left:15px;"}

ユーザーは、ワークスペース内のアプリについてアクティブなフォアグラウンドプッシュトークンを持っている場合に、「プッシュ有効」または「プッシュ登録済み」とみなされます。つまり、プッシュのイネーブルメントステータスはアプリに固有です。 

{% alert note %}
プッシュ登録状態の確認方法については、[プッシュ登録ステータス]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#checking-push-registration-status)を参照してください。
{% endalert %}

## その他のプラットフォーム固有のシナリオ

{% tabs %}
{% tab Android %}

フォアグラウンドプッシュを有効にしているユーザーが OS の設定でプッシュを無効にすると、次のセッションの開始時に次の処理が行われます。
- Brazeはそれらをフォアグラウンドプッシュ無効としてマークし、プッシュメッセージの送信を試みなくなった。
- `Push Enabled for App (Android)` フィルターと`Push Enabled` セグメンテーションフィルター (ユーザープロファイルで他のアプリが有効なフォアグラウンドプッシュトークンを持っていない場合) は、`false` を返します。

このシナリオでは、バックグラウンドプッシュトークンがまだ存在するので、セグメンテーションフィルター `Background Push Enabled = true` を使用して引き続きバックグラウンド (サイレント) プッシュ通知を送信できます。

Androidの場合、Brazeは以下の場合にユーザーのプッシュが無効であるとみなす：

- ユーザーは自分のデバイスからアプリをアンインストールする。
- バウンスによりプッシュメッセージの配信に失敗した。これはアンインストールが原因であることが多いが、アプリのアップデート、新しいプッシュトークンバージョン、フォーマットなどが原因であることもある。 
- Firebase Cloud Messaging へのプッシュ登録に失敗する (原因として、ネットワーク接続不良、FCM への接続失敗、FCM が有効なトークンを返さないことがある)。
- ユーザーはデバイスの設定でアプリのプッシュ通知をブロックし、その後セッションを記録する。

{% endtab %}
{% tab iOS %}

ユーザーがフォアグラウンドプッシュのオプトインプロンプトを受け入れるかどうかに関係なく、Xcodeで リモート通知を有効にしていて、アプリから [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications) を呼び出せば、バックグラウンドプッシュを送信できます。

アプリが仮承認されているか、ユーザーがプッシュ通知をオプトインしている場合、ユーザーはフォアグラウンドプッシュトークンを受信するので、あらゆる種類のプッシュをユーザーに送信できます。Brazeでは、iOSでフォアグラウンドプッシュが有効になっているユーザーを、明示的（アプリレベル）または暫定的（デバイスレベル）にプッシュが有効になっているとみなす。

ユーザーが OS レベルでプッシュ通知の受信を拒否した場合、そのユーザーのプッシュ通知のサブスクリプション状態は `Subscribed` になり、ユーザープロファイルにはフォアグラウンドプッシュトークンが登録されていることが表示されません。 

最初に OS レベルでオプトインしたユーザーが、OS の設定でプッシュ通知を無効にしたシナリオでは、次のセッション開始時に以下のことが起こります。
- Brazeはそれらをフォアグラウンドプッシュ無効とマークし、プッシュメッセージの送信を試みなくなった。
- `Push Enabled for App (iOS)` フィルターと`Push Enabled` セグメンテーションフィルター (ユーザープロファイルで他のアプリが有効なフォアグラウンドプッシュトークンを持っていない場合) は、`false` を返します。

このシナリオでは、バックグラウンドプッシュトークンがまだ存在するので、セグメンテーションフィルター `Background Push Enabled = true` を使用して引き続きバックグラウンド (サイレント) プッシュ通知を送信できます。

{% endtab %}
{% tab Web %}

ユーザーがネイティブプッシュ許可のプロンプトを受け入れると、そのサブスクリプションステータスは `opted in` に変更されます。

サブスクリプションを管理するには、ユーザーメソッド [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype)を使用して、自分のサイトに基本設定のページを作成します。その後、ダッシュボードでオプトアウトステータスを使用してユーザーをフィルター処理できます。

ユーザーがブラウザ内で通知を無効にした場合、そのユーザーに次に送信されるプッシュ通知はバウンスされ、Brazeはそれに応じてユーザーのプッシュトークンを更新する。これは、プッシュ有効フィルター (`Background Push Enabled`、`Push Enabled`、`Push Enabled for App`) の適格性を管理するために使用されます。ユーザープロファイルに設定されたサブスクリプションステータスは、ユーザーレベルの設定であり、プッシュがバウンスしても変化しません。

{% alert note %}
ウェブ・プラットフォームでは、バックグラウンド・プッシュやサイレント・プッシュはできない。
{% endalert %}
{% endtab %}
{% endtabs %}

## ベストプラクティス

Brazeでのプッシュの使い方を最適化するための詳しいガイダンスについては、[プッシュのベストプラクティスに関する]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices)専用記事を参照のこと。

[1]: {% image_buster /assets/img/push_enablement.png %}
[2]: {% image_buster /assets/img/push_changelog.png %}
[3]: {% image_buster /assets/img/push_example.png %}
[4]: {% image_buster /assets/img/push_token_changelog.png %}
[push-tokens]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/
[identifier] ：{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment] ：{{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
[ios-push-prompt] ： {% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}
[android-push-prompt] ： {% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}
[web-push-prompt] ： {% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}
[ios-provisional-push] ： {% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}
[push-primers]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/
[android-13] ： {{site.baseurl}}/developer_guide/platform_integration_guides/android/android_13/
[provisional-blog] ： https://www.braze.com/resources/articles/mastering-provisional-push
[user_attributes_object]: {{site.baseurl}}/api/objects_filters/user_attributes_object
[users-track] ：{{site.baseurl}}/api/endpoints/user_data/post_user_track/
