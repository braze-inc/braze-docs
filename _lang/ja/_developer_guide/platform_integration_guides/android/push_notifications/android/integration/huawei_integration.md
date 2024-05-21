---
nav_title: Huawei の統合
article_title: Android 向け Huawei プッシュ統合
platform: Android
page_order: 9
description: "この記事では、Huawei Android 統合の設定方法について説明します。"
channel:
  - push

---

# Huawei のプッシュ統合

> [Huawei][1] 製の新しいスマートフォンには、プッシュ配信に使用されるサービス、Huawei Mobile Services (HMS) が、Google の Firebase Cloud Messaging (FCM) の代わりに搭載されています。<br><br>このガイドでは、Braze 経由でプッシュを送信し、セグメンテーション、分析、キャンバスなどの既存の Braze 機能をフルに活用できるように Huawei Android 統合を設定する方法について説明します。

## ステップ 1:Huawei 開発者アカウントに登録する

始める前に、[Huawei 開発者アカウント][2]への登録と設定が必要です。Huawei アカウントで、**[My Projects] > [Project Settings] > [App Information]** に移動し、`App ID` と`App secret` を書き留めます。

![][3]

## ステップ 2:Braze ダッシュボードで新しい Huawei アプリを作成する

Braze ダッシュボードで、[**設定**] ナビゲーションの下にある [**アプリ設定**] に移動します。

[**\+ アプリ**] をクリックし、名前 (My Huawei App など) を入力し、プラットフォームとして `Android` を選択します。

![][4]{: style="max-width:60%;"}

新しい Braze アプリを作成したら、プッシュ通知設定を見つけて、プッシュプロバイダーとして `Huawei` を選択します。次に、`Huawei Client Secret` と `Huawei App ID` を指定します。

![][12]

## ステップ 3:Huawei メッセージング SDK をアプリに統合する

Huawei は、Huawei Messaging Service をアプリケーションに統合する [Android 統合codelab][13] を提供しています。以下の手順に従って開始してください。

codelab が完了したら、カスタムの [Huawei Message Service][14] を作成してプッシュトークンを取得し、メッセージを Braze SDK に転送する必要があります。

{% tabs %}
{% tab JAVA %}

\`\`\`java
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
      // Braze が Huawei プッシュ通知を処理しました
    }
  }
}
\`\`\`

{% endtab %}
{% tab KOTLIN %}

\`\`\`kotlin
class CustomPushService:HmsMessageService() {
override fun onNewToken(token: String?) {
super.onNewToken(token)
Braze.getInstance(applicationContext).setRegisteredPushToken(token!!)
}

  override fun onMessageReceived(hmsRemoteMessage:RemoteMessage?) {
    super.onMessageReceived(hmsRemoteMessage)
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(applicationContext, hmsRemoteMessage?.dataOfMap)) {
      // Braze が Huawei プッシュ通知を処理しました
    }
  }
}
\`\`\`

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

## ステップ 4:Huawei プッシュを送信する

ここまでで、Braze ダッシュボードに新しい Huawei Android アプリを作成し、Huawei 開発者の認証情報を使用して設定し、Braze および Huawei SDK をアプリに統合しました。

次に、Braze で新しいプッシュキャンペーンをテストすることで、統合をテストします。

### 新しいプッシュ通知キャンペーンを作成する

[**キャンペーン**] ページで、新しいキャンペーンを作成し、メッセージタイプとして [**プッシュ通知**] を選択します。

キャンペーンに名前を付けたら、プッシュプラットフォームとして [**Android プッシュ通知**] を選択します。

![利用可能なプッシュプラットフォームを表示するキャンペーン作成コンポーザー][5]

次に、タイトルとメッセージを付けてプッシュキャンペーンを作成します。

### テストプッシュを送信する

[**テスト**] タブで、[\`changeUser(USER\_ID\_STRING)\` メソッド][9] を使用してアプリに設定したユーザー ID を入力し、[**テストを送信**] をクリックしてテストプッシュを送信します。

![キャンペーン作成コンポーザーのテストタブでは、ユーザー ID を指定し、[ユーザーを個別に追加] フィールドに入力することで、テストメッセージを自分に送信できます。][7]

この時点で、Braze から Huawei (HMS) デバイスにテストプッシュ通知が届くはずです。

### Huawei セグメンテーションのセットアップ (オプション)

Braze ダッシュボードの Huawei アプリは Android プッシュプラットフォーム上に構築されているため、すべての Android ユーザー (Firebase Cloud Messaging および Huawei Mobile Services) にプッシュを送信するか、キャンペーンオーディエンスを特定のアプリにセグメント化するかを柔軟に選択できます。

Huawei アプリのみにプッシュを送信するには、[新しいセグメントを作成][15] して、[**アプリ**] セクション内で Huawei アプリを選択します。

![][8]

もちろん、すべての Android プッシュプロバイダーに同じプッシュを送信する場合は、アプリを指定しないことを選択することで、現在のワークスペース内で設定されているすべての Android アプリに送信できます。

## 分析

キャンペーンが開始されると、キャンペーンの分析または Android プッシュ用に集計されたキャンバスが表示されます。Android プッシュの分析と設定の詳細については、[プッシュユーザーガイド][10] を参照してください。

[1]: https://huaweimobileservices.com/
[2]: https://developer.huawei.com/consumer/en/console
[3]: {% image_buster /assets/img/huawei/huawei-credentials.png %}
[4]: {% image_buster /assets/img/huawei/huawei-create-app.png %}
[5]: {% image_buster /assets/img/huawei/huawei-test-push-platforms.png %}
[6]: {% image_buster /assets/img/huawei/huawei-test-push-composer.png %}
[7]: {% image_buster /assets/img/huawei/huawei-test-send.png %}
[8]: {% image_buster /assets/img/huawei/huawei-segmentation.png %}
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#assigning-a-user-id
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/
[12]: {% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %}
[13]: https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html
[14]: https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls
[15]: {{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform
