## プッシュ通知のサブスクリプションの状態{#push-sub-states}

Brazeの 「プッシュ通知のサブスクリプションの状態」は、プッシュ通知の受信を希望する**ユーザー**のグローバルな嗜好を識別します。サブスクリプションの状態はユーザーベースなので、個々のアプリに固有のものではない。サブスクリプションの状態は、プッシュ通知のターゲットにするユーザーを決定するときに役立つフラグです。

{% alert note %}
ユーザーのプッシュ通知のサブスクリプションの状態は、ユーザーのすべてのデバイスを含むユーザープロファイル全体に適用されます。
{% endalert %}

以下のサブスクリプション状態オプションが存在する： `Subscribed`, `Opted-In`, および `Unsubscribed`。

デフォルトでは、ユーザーがプッシュ通知でメッセージを受け取るには、プッシュサブスクリプション状態が「許可」または`Subscribed`「拒否」のいずれかでなければならず、かつフォアグラウンド`Opted-In`プッシュがイネーブルドになっている必要がある。メッセージの作成時に、この設定をオーバーライドできます。

|オプトイン状態|説明|
|---|---|
|`Subscribed`| Brazeでユーザープロファイルが作成されたときのデフォルトのプッシュ通知のサブスクリプション状態。 |
|`Opted-In`| ユーザーは、プッシュ通知を受け取ることを明示的に希望した。ユーザーがOSレベルのプッシュ通知プロンプトを受け入れた場合、Brazeは自動的に`Opted-In`そのユーザーのオプトイン状態を「許可済み」に変更する。<br><br>Android 12 またはそれ以前のユーザーには適用されません。|
|`Unsubscribed`| ユーザーがアプリケーションやブランドが提供するその他の方法で、プッシュ配信を明示的に解除した。デフォルトでは、Brazeのプッシュキャンペーンは、プッシュ通知に対して`Opted-in`「許可`Subscribed`」または「拒否」設定のユーザーのみを対象とする。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze で、ユーザーのプッシュ通知のサブスクリプションの状態を自動的に `Unsubscribed` にすることはありません。ユーザーのプッシュサブスクリプション状態が の場合、そのユーザーのセグメンテーションにおける`Unsubscribed``Foreground Push Enabled` フィルターは であることを`false`覚えておけ。
{% endalert %}

### プッシュ通知のサブスクリプションの状態の更新 {#update-push-subscription-state}

ユーザーのプッシュサブスクリプション状態を更新する以下の方法を検討せよ：

#### 自動オプトイン (デフォルト)

Braze はデフォルトで、ユーザーが初めてアプリのプッシュ通知を承認したときに、ユーザーのプッシュ通知のサブスクリプションの状態を `Opted-In` に設定します。Braze はまた、ユーザーがシステム設定でプッシュ許可を無効にした後、再度プッシュ許可を有効にした場合にもこれを行います。

{% tabs local %}
{% tab android %}
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

ユーザーのサブスクリプションの状態を更新するには、Braze REST API で[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して、ユーザーの [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) 属性を更新します。

### プッシュ通知のサブスクリプションの状態の確認

![John Doeのユーザープロファイルで、プッシュ購読の状態がSubscribedに設定されている。]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Brazeでは、以下のいずれかの方法でユーザーのプッシュ通知サブスクリプション状態を確認できる：

* **ユーザープロフィール:**Braze ダッシュボードの [**[ユーザー検索]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)**] ページから、個々のユーザープロファイルにアクセスできます。Eメールアドレス、電話番号、または外部ユーザーIDを介して）ユーザーのプロフィールを見つけた後、**Engagement**タブを選択してユーザーの購読状態を表示し、手動で調整することができる。
* **REST API でのエクスポート:**Export[Users by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)または[Users by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)エンドポイントを使用して、個々のユーザープロファイルを JSON 形式でエクスポートすることができる。Brazeは、デバイスごとのプッシュ通知イネーブルメント情報を含むプッシュトークンオブジェクトを返す。