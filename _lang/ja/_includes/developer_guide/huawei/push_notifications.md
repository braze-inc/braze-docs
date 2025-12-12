{% multi_lang_include developer_guide/prerequisites/android.md %}

## プッシュ通知の設定

[Huawei](https://huaweimobileservices.com/) 製の新しいスマートフォンには、プッシュ配信に使用されるサービス、Huawei Mobile Services (HMS) が、Google の Firebase Cloud Messaging (FCM) の代わりに搭載されています。

### ステップ 1: Huawei 開発者アカウントに登録する

始める前に、[Huawei 開発者アカウント](https://developer.huawei.com/consumer/en/console)への登録と設定が必要です。Huawei アカウントで、**[My Projects] > [Project Settings] > [App Information]** に移動し、`App ID` と`App secret` を書き留めます。

![]({% image_buster /assets/img/huawei/huawei-credentials.png %})

### ステップ 2:Braze ダッシュボードで新しい Huawei アプリを作成する

Braze ダッシュボードで、[**設定**] ナビゲーションの下にある [**アプリ設定**] に移動します。

[**\+ アプリ**] をクリックし、名前 (My Huawei App など) を入力し、プラットフォームとして `Android` を選択します。

![]({% image_buster /assets/img/huawei/huawei-create-app.png %}){: style="max-width:60%;"}

新しい Braze アプリを作成したら、プッシュ通知設定を見つけて、プッシュプロバイダーとして `Huawei` を選択します。次に、`Huawei Client Secret` と `Huawei App ID` を指定します。

![]({% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %})

### ステップ 3:Huawei メッセージング SDK をアプリに統合する

Huawei は、Huawei Messaging Service をアプリケーションに統合する [Android 統合 codelab](https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html) を提供しています。以下の手順に従って開始してください。

codelab が完了したら、カスタムの [Huawei Message Service](https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls) を作成してプッシュトークンを取得し、メッセージを Braze SDK に転送する必要があります。

{% tabs %}
{% tab JAVA %}

```java
public class CustomPushService extends HmsMessageService {
  @Override
  public void onNewToken(String token) {
    super.onNewToken(token);
    Braze.getInstance(this.getApplicationContext()).setRegisteredPushToken(token);
  }

  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(this.getApplicationContext(), remoteMessage.getDataOfMap())) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomPushService: HmsMessageService() {
  override fun onNewToken(token: String?) {
    super.onNewToken(token)
    Braze.getInstance(applicationContext).setRegisteredPushToken(token!!)
  }

  override fun onMessageReceived(hmsRemoteMessage: RemoteMessage?) {
    super.onMessageReceived(hmsRemoteMessage)
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(applicationContext, hmsRemoteMessage?.dataOfMap)) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% endtabs %}

カスタムプッシュサービスを追加した後、`AndroidManifest.xml` に以下を追加します。

```xml
<service
  android:name="package.of.your.CustomPushService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

### ステップ 4: プッシュ通知をテストする（オプション）

ここまでで、Braze ダッシュボードに新しい Huawei Android アプリを作成し、Huawei 開発者の認証情報を使用して設定し、Braze および Huawei SDK をアプリに統合しました。

次に、Braze で新しいプッシュキャンペーンをテストすることで、統合をテストします。

#### ステップ4.1：新しいプッシュ通知キャンペーンを作成する

[**キャンペーン**] ページで、新しいキャンペーンを作成し、メッセージタイプとして [**プッシュ通知**] を選択します。

キャンペーンに名前を付けたら、プッシュプラットフォームとして [**Android プッシュ通知**] を選択します。

![利用可能なプッシュ・プラットフォームを表示するキャンペーン作成コンポーザー。]({% image_buster /assets/img/huawei/huawei-test-push-platforms.png %})

次に、タイトルとメッセージを付けてプッシュキャンペーンを作成します。

#### ステップ4.2：テストプッシュを送信する

[**Test**] タブで、[`changeUser(USER_ID_STRING)` method]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#assigning-a-user-id) を使ってアプリに設定したユーザーIDを入力し、[**Send Test**] をクリックしてテストプッシュを送信する。

![キャンペーン作成コンポーザーのテストタブを見ると、ユーザーIDを入力し、「個人ユーザーを追加」フィールドに入力することで、自分自身にテストメッセージを送信できることがわかる。]({% image_buster /assets/img/huawei/huawei-test-send.png %})

この時点で、Braze から Huawei (HMS) デバイスにテストプッシュ通知が届くはずです。

#### ステップ4.3：ファーウェイのセグメンテーションを設定する（オプション）

Braze ダッシュボードの Huawei アプリは Android プッシュプラットフォーム上に構築されているため、すべての Android ユーザー (Firebase Cloud Messaging および Huawei Mobile Services) にプッシュを送信するか、キャンペーンオーディエンスを特定のアプリにセグメント化するかを柔軟に選択できます。

Huawei アプリのみにプッシュを送信するには、[新しいセグメントを作成]({{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) して、[**アプリ**] セクション内で Huawei アプリを選択します。

![]({% image_buster /assets/img/huawei/huawei-segmentation.png %})

もちろん、すべての Android プッシュプロバイダーに同じプッシュを送信する場合は、アプリを指定しないことを選択することで、現在のワークスペース内で設定されているすべての Android アプリに送信できます。
