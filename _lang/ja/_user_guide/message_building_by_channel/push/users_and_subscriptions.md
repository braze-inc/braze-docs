---
nav_title: "プッシュ・イネーブルメントとサブスクリプション"
article_title: プッシュ・イネーブルメントとサブスクリプション
page_order: 3
page_type: reference
description: "このリファレンス記事では、Brazeにおけるプッシュ有効状態とプッシュ購読状態の概念について、iOS、Android、Webにおける動作の基本的な違いを含めて説明する。"
channel:
  - push

---

# プッシュ配信とプッシュ購読

> この参考記事では、Brazeにおけるプッシュ有効化とプッシュ購読状態の概念について、iOS、Android、およびWebにおける動作の基本的な違いを含めて説明する。

## プッシュ購読の状態 {#push-sub-states}

Brazeの "Push Subscription State "は、プッシュ通知の受信を希望する**ユーザーの**グローバルな好みを識別する。サブスクリプションの状態はユーザーベースなので、個々のアプリに固有のものではない。サブスクリプションの状態は、プッシュ通知の対象とするユーザーを決定する際に役立つフラグとなる。

{% alert note %}
ユーザーのプッシュ購読の状態は、ユーザーのすべてのデバイスを含むユーザープロファイル全体に適用される。
{% endalert %}

3つのプッシュ購読状態オプションがある：`Subscribed` `Opted-In` および`Unsubscribed` 。

デフォルトでは、ユーザーがプッシュでメッセージを受信するには、プッシュ購読の状態が`Subscribed` または`Opted-In` のどちらかであり、[プッシュが有効になって](#push-enabled)いなければならない。メッセージを作成する際、必要に応じてこの設定を上書きすることができる。

|オプトイン状態|説明|
|---|---|
|`Subscribed`| Brazeでユーザープロファイルが作成されたときのデフォルトのプッシュ購読状態。 |
|`Opted-In`| ユーザーは、プッシュ通知を受け取ることを明示的に希望した。Brazeは、ユーザーがOSレベルのプッシュプロンプトを受け入れた場合、ユーザーのオプトイン状態を自動的に`Opted-In` 。<br><br>アンドロイド12以下のユーザーには適用されない。|
|`Unsubscribed`| ユーザーがアプリケーションやブランドが提供するその他の方法で、プッシュ配信を明示的に解除した。デフォルトでは、Brazeのプッシュキャンペーンは、`Subscribed` 、または`Opted-in` 、プッシュの対象になっているユーザーのみをターゲットとしている。|
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Brazeは、ユーザーのプッシュ購読状態を自動的に`Unsubscribed` 。ユーザーのプッシュサブスクリプションのステートが`Unsubscribed` の場合、セグメンテーションにおけるユーザーの`Push Enabled` フィルタは`false` になることを覚えておいてほしい。
{% endalert %}

### プッシュ購読の状態を更新する {#update-push-subscription-state}

ユーザーのプッシュ購読状態を更新するには、3つの方法がある：

#### 自動オプトイン（デフォルト）

デフォルトでは、Brazeは、ユーザーが初めてアプリのプッシュ通知を承認したときに、ユーザーのプッシュ購読状態を`Opted-In` 。Brazeはまた、ユーザーがシステム設定でプッシュ許可を無効にした後、再度プッシュ許可を有効にした場合にもこれを行う。

{% tabs ローカル %}
{% tab アンドロイド %}
このデフォルトの動作を無効にするには、Android Studioプロジェクトの`braze.xml` ：

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab 速い %}
[Braze Swift SDKバージョン7.5.0から](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0)、Xcodeプロジェクトの`AppDelegate.swift` ファイルに`optInWhenPushAuthorized` の設定を追加することで、この動作を無効にしたり、さらにカスタマイズしたりすることができる：

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### SDKの統合

[Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype)、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html)、または[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:))上で`setPushNotificationSubscriptionType` メソッドを使用して、Braze SDKでユーザーの購読状態を更新できる。例えば、この方法を使って、ユーザーが手動でプッシュ通知を有効または無効にできる設定ページをアプリ内に作成することができる。

#### REST API

BrazeのREST APIでは、`/users/track` エンドポイント]\[users-track] ] を使って、ユーザーの購読状態を更新することができる \[`push_subscribe`]\[user_attributes_object] ] 。

### プッシュ購読の状態をチェックする

![John Doeのユーザープロファイルで、プッシュ購読の状態がSubscribedに設定されている。][3]{: style="float:right;max-width:35%;margin-left:15px;"}

Brazeでユーザーのプッシュ購読状態を確認するには、2つの方法がある：

1. **ユーザープロフィール:**Brazeダッシュボードの**\[User Search][5] ]**ページから、個々のユーザープロファイルにアクセスできる。Eメールアドレス、電話番号、または外部ユーザーIDを介して）ユーザーのプロフィールを見つけた後、**Engagement**タブを選択してユーザーの購読状態を表示し、手動で調整することができる。
<br><br>
2. **Rest APIエクスポート**：エクスポート \[Users by segment]\[segment] ]] または \[Users by identifier]\[identifier] ] エンドポイントを使用して、個々のユーザー・プロファイルを JSON 形式でエクスポートできる。Brazeは、デバイスごとのプッシュ有効化情報を含むプッシュトークンオブジェクトを返す。

## プッシュ許可

iOS、ウェブ、アンドロイドのすべてのプッシュ対応プラットフォームでは、OSレベルのシステム・プロンプトによる明示的なオプトインが必要だが、以下に若干の違いがある。

ユーザーの決定は最終的なものであり、彼らが辞退した後に再度尋ねることはできないため、\[プッシュプライマー]\[push-primers] ] アプリ内メッセージを使用することは、オプトイン率を高めるための重要な戦略である。

**ネイティブOSのプッシュ許可プロンプト**

|プラットフォーム|スクリーンショット|説明|
|--|--|--|
|iOS| ![メッセージの下部に「許可しない」と「許可する」の2つのボタンがある。]\[ios-push-prompt]{: style="max-width:410px;"} | ただし、[仮のプッシュ](#provisional-push)許可を申請する場合はこの限りではない。|
|Android| ![Kitchenerieからの通知を許可しますか」と尋ねるアンドロイドのプッシュメッセージ。メッセージの下部に「許可する」と「許可しない」の2つのボタンがある。]\[android-push-prompt]{: style="max-width:410px;"} | このプッシュ許可はアンドロイド13で導入された。アンドロイド13以前は、プッシュ送信に許可は必要なかった。|
|Web| ![ウェブブラウザのネイティブプッシュプロンプトは、"Braze.com wants to show notification "と尋ね、メッセージの下部に "Block "と "Allow "の2つのボタンがある。]\[web-push-prompt]{: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Android

アンドロイド13以前は、プッシュ通知の送信に許可は必要なかった。Android 12以下では、Brazeが自動的にプッシュトークンを要求する最初のセッションで、すべてのユーザーが`Subscribed` 。この時点で、ユーザーはそのデバイスの有効なプッシュトークンと、`Subscribed` というデフォルトのサブスクリプション状態で**プッシュ有効になって**いる。

アンドロイド13]\[android-13]] からは、プッシュ許可はユーザーに尋ねて許可されなければならない。あなたのアプリは、適切なタイミングでユーザーに手動で許可を求めることができるが、そうでない場合は、アプリが[通知チャネルを](https://developer.android.com/reference/android/app/NotificationChannel)作成するときに、ユーザーに自動的にプロンプトが表示される。

### iOS

![システムの通知センターに通知が表示され、下部に「Yachtrアプリからの通知を受信し続けますか」というメッセージと、その下に「受信し続ける」または「オフにする」の2つのボタンが表示される]\[ios-provisional-push]{: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

アプリは暫定プッシュまたは認可プッシュを要求できる。 

オーソライズド・プッシュでは、通知を送信する前にユーザーからの明示的な許可が必要だが、\[provisional push]\[provisional-blog] ] では、音やアラートなしで、通知センターに直接、__静かに__通知を送ることができる。

#### 暫定承認と静粛なプッシュ {#provisional-push}

iOS 12（2018年リリース）以前は、すべてのユーザーがプッシュ通知の受信を明示的にオプトインする必要があった。

iOS12では、アップルは\[仮承認]\[仮ブログ]]を導入し、ブランドが、ユーザーが明示的にオプトインする前に、ユーザーの通知センターに静かなプッシュ通知を送信できるようにした。詳しくは[仮承認を]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications)参照のこと。

### Web

ウェブの場合は、ネイティブブラウザの許可ダイアログを通じて、明示的にユーザーのオプトインを要求する必要がある。

iOSやAndroidでは、アプリはいつでも許可プロンプトを表示できるが、最近のブラウザの中には、「ユーザージェスチャー」（マウスクリックやキーストローク）によってのみプロンプトを表示するものもある。もしあなたのサイトがページロード時にプッシュ通知の許可を要求しようとすれば、おそらくブラウザによって無視されるか、沈黙させられるだろう。

その結果、ユーザーがあなたのウェブサイトのどこかをクリックしたときにのみ許可を求めるべきであり、ページがロードされたときにランダムに許可を求めるべきでない。

## プッシュトークン

\[プッシュトークン]\[push-tokens] ] は、ユーザーのデバイスによって生成され、各受信者の通知を送信する場所を特定するためにBrazeに送信される一意の匿名識別子である。

プッシュトークン]\[プッシュトークン] ]には2つの分類方法があり、プッシュ通知をユーザーに送る方法を理解するのに欠かせない。

1. **フォアグラウンド・プッシュは**、ユーザーのデバイスのフォアグラウンドに定期的に目に見えるプッシュ通知を送信する機能を提供する。
2. **バックグラウンド・プッシュは**、特定のデバイスがそのブランドからのプッシュ通知を受け取ることをオプトインしているかどうかに関係なく利用できる。バックグラウンド・プッシュでは、ブランドはサイレント・プッシュ通知（意図的に表示されない通知）をデバイスに送信し、[アンインストール追跡の]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/)ような重要な機能をサポートすることができる。

ユーザープロファイルにアプリに関連付けられた有効なフォアグラウンドプッシュトークンがある場合、Brazeはそのユーザーを指定されたアプリの「プッシュ登録済み」とみなす。そこでBrazeは、このようなユーザーを特定するための特定のセグメンテーションフィルター、`Push Enabled for App,` 。

{% alert note %}
`Push Enabled for App` フィルタは、指定されたアプリの有効なフォアグラウンドとバックグラウンドのプッシュトークンの存在のみを考慮する。しかし、より一般的な [`Push Enabled`](#push-enabled)フィルターは、ワークスペース内のアプリのプッシュ通知を明示的に有効にしたユーザーをセグメントする。このカウントには、フォアグラウンド・プッシュのみが含まれ、購読を解除したユーザーは含まれない。これらのフィルターやその他のフィルターについては、[セグメンテーション・フィルターで]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters)詳しく説明している。
{% endalert %}

### 1台のデバイスで複数のユーザーが利用できる

プッシュトークンはデバイスとアプリの両方に固有なので、プッシュトークンを使って同じデバイスを使っている複数のユーザーを区別することはできない。

例えば、2人のユーザーがいるとする：チャーリーとキムだ。チャーリーが自分の携帯電話であなたのアプリのプッシュ通知を有効にしている場合、キムがチャーリーの携帯電話を使ってチャーリーのプロフィールからログアウトし、自分のプロフィールにログインすると、プッシュトークンはキムのプロフィールに再割り当てされる。プッシュトークンは、キムがログアウトし、チャーリーが再度ログインするまで、そのデバイスのキムのプロファイルに割り当てられたままとなる。

アプリやウェブサイトは、1つのデバイスにつき1つのプッシュ購読しかできない。そのため、ユーザーがデバイスやウェブサイトからログアウトし、新しいユーザーがログインすると、プッシュトークンは新しいユーザーに再割り当てされる。これはユーザーのプロフィール、**エンゲージメント・タブの** **コンタクト設定**セクションに反映される：

![ユーザーのプロフィールの\*\*Engagement**タブにあるプッシュトークンの変更履歴。][4]

プッシュ・プロバイダ（APN/FCM）には、1つのデバイス上の複数のユーザーを区別する方法がないため、最後にログインしたユーザーにプッシュ・トークンを渡し、デバイス上のどのユーザーをプッシュのターゲットにするかを決定する。

### 複数のデバイスと1人のユーザー

プッシュサブスクリプションの状態はユーザーベースであり、個々のアプリに固有のものではない。プッシュサブスクリプションの状態は、最後に設定された値である。そのため、ユーザーがプッシュ通知をオプトインしている場合、そのプッシュ通知の購読状態は、対象となるすべてのデバイスで`Opted-in` 。その後、ユーザーがアプリケーションやブランドが提供するその他の方法でプッシュ通知を明示的に解除した場合、そのユーザーのプッシュ購読状態は`Unsubscribed` に更新され、プッシュ登録されたデバイスはプッシュ通知を受信できなくなる。

## プッシュ有効フィルター {#push-enabled}

`Push Enabled` は、Brazeのセグメンテーションフィルターで、マーケティング担当者は、Brazeがプッシュ通知を送信することを許可しているユーザーと、プッシュ通知を受信しないことを表明していないユーザーを簡単に識別することができる。 

`Push Enabled` フィルタは以下を考慮に入れている：
- Brazeがプッシュ通知を送信する機能（フォアグラウンド・プッシュ・トークン）
- どのデバイスでもプッシュを受信したいというユーザーの全体的な希望（プッシュ購読状態）

![ユーザーが "Push Registered for Marketing（iOS）"であることを示すダッシュボードのスクリーンショット。][1]{: style="float:right;max-width:50%;margin-left:15px;"}

ユーザーは、ワークスペース内のアプリに対してアクティブなフォアグラウンド・プッシュトークンを持っている場合、「プッシュ有効」または「プッシュ登録済み」とみなされる。 

{% alert note %}
プッシュ登録状態の確認方法については、[プッシュ登録状態を]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#checking-push-registration-status)参照のこと。
{% endalert %}

## その他のプラットフォーム固有のシナリオ

{% tabs %}
{% tab アンドロイド %}

フォアグラウンド・プッシュが有効なユーザーがOSの設定でプッシュを無効にすると、次のセッションの開始時にプッシュが無効になる：
- Brazeはそれらをフォアグラウンドプッシュ無効としてマークし、プッシュメッセージの送信を試みなくなった。
- `Push Enabled for App (Android)` フィルタと`Push Enabled` セグメンテーションフィルタ（ユーザープロファイル上の他のアプリが有効なフォアグラウンドプッシュトークンを持っていないと仮定）は、`false` を返す。

このシナリオでは、バックグラウンドプッシュトークンはまだ存在するので、セグメンテーションフィルター`Background Push Enabled = true` を使ってバックグラウンド（サイレント）プッシュ通知を送信し続けることができる。

Androidの場合、Brazeは以下の場合にユーザーのプッシュが無効であるとみなす：

- ユーザーは自分のデバイスからアプリをアンインストールする。
- バウンスによりプッシュメッセージの配信に失敗した。これはアンインストールが原因であることが多いが、アプリのアップデート、新しいプッシュトークンバージョン、フォーマットなどが原因であることもある。 
- Firebase Cloud Messagingへのプッシュ登録に失敗する（ネットワーク接続不良、FCMへの接続失敗、FCMが有効なトークンを返さないことが原因）。
- ユーザーはデバイスの設定でアプリのプッシュ通知をブロックし、その後セッションを記録する。

{% endtab %}
{% tab iOS %}

ユーザーがフォアグラウンド・プッシュのオプトイン・プロンプトを受け入れるかどうかに関係なく、Xcodeでリモート通知を有効にしていて、アプリが次のコマンドを呼び出していれば、バックグラウンド・プッシュを送信することができる。 [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications).

アプリが仮承認されているか、ユーザーがプッシュをオプトインしていれば、フォアグラウンド・プッシュ・トークンを受け取り、あらゆる種類のプッシュを送信できるようになる。Brazeでは、iOSでフォアグラウンドプッシュが有効になっているユーザーを、明示的（アプリレベル）または暫定的（デバイスレベル）にプッシュが有効になっているとみなす。

ユーザーがOSレベルでプッシュ通知の受信を拒否した場合、そのユーザーのプッシュ購読状態は`Subscribed` 、プロフィールにはフォアグラウンドプッシュトークンが登録されていることは表示されない。 

最初にOSレベルでオプトインしたユーザーが、OSの設定でプッシュ通知を無効にした場合、次のセッション開始時に以下のことが起こる：
- Brazeはそれらをフォアグラウンドプッシュ無効とマークし、プッシュメッセージの送信を試みなくなった。
- `Push Enabled for App (iOS)` フィルタと`Push Enabled` セグメンテーションフィルタ（ユーザープロファイル上の他のアプリが有効なフォアグラウンドプッシュトークンを持っていないと仮定）は、`false` を返す。

このシナリオでは、バックグラウンドプッシュトークンはまだ存在するので、セグメンテーションフィルター`Background Push Enabled = true` を使ってバックグラウンド（サイレント）プッシュ通知を送信し続けることができる。

{% endtab %}
{% tab ウェブ %}

ユーザーがネイティブプッシュ許可のプロンプトを受け入れると、その購読ステータスは`opted in` に変更される。

購読を管理するには、ユーザーメソッド [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype)を使用して、あなたのサイトにプリファレンス設定ページを作成し、その後、ダッシュボードでオプトアウトステータスによってユーザーをフィルタリングすることができる。

ユーザーがブラウザ内で通知を無効にした場合、そのユーザーに次に送信されるプッシュ通知はバウンスされ、Brazeはそれに応じてユーザーのプッシュトークンを更新する。これは、プッシュ有効フィルター（`Background Push Enabled` 、`Push Enabled` 、`Push Enabled for App` ）の資格を管理するために使用される。ユーザーのプロファイルに設定された購読ステータスは、ユーザーレベルの設定であり、プッシュがバウンスしても変更されない。

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
\[push-tokens]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/
\[identifier] ：{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
\[segment] ：{{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
\[ios-push-prompt] ： {% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}
\[android-push-prompt] ： {% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}
\[web-push-prompt] ： {% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}
\[ios-provisional-push] ： {% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}
\[push-primers]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/
\[android-13] ： {{site.baseurl}}/developer_guide/platform_integration_guides/android/android_13/
\[provisional-blog] ： https://www.braze.com/resources/articles/mastering-provisional-push
\[user_attributes_object]: {{site.baseurl}}/api/objects_filters/user_attributes_object
\[users-track] ：{{site.baseurl}}/api/endpoints/user_data/post_user_track/
