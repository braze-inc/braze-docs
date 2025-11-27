---
nav_title: Android用ライブ更新
article_title: Android Braze SDKのライブ更新
page_order: 0.1
description: "Android Braze SDK の Live 更新の設定方法を学びます。"
platform: 
  - Android
  - FireOS
---

# Android用ライブ更新

> Braze SDK で Android Live 更新 ([Progress Centric Notifications とも言います](https://developer.android.com/about/versions/16/features/progress-centric-notifications)) を使用する方法について説明します。これらの通知は、[Swift Braze SDK のライブアクティビティ]({{site.baseurl}}/developer_guide/live_notifications/live_activities)に似ており、インタラクティブなロック画面通知を表示できます。Android 16 では、進行状況を中心とした通知が導入され、ユーザーが開始した最初から最後までのジャーニーをシームレスに追跡できます。

## CDI の仕組み

[`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) インターフェイスを使用して、Braze プッシュ通知の表示方法をカスタマイズできます。`BrazeNotificationFactory` を拡張することで、通知がユーザーに表示される前に Braze はファクトリーの`createNotification()` メソッドを呼び出します。その後、Braze ダッシュボードまたは REST API を通じて送信されたカスタムのキーと値のペアを含むペイロードを渡します。

## ライブ更新を表示する

このセクションでは、野生動物救助チームが誰が一番多くのフクロウを救えるかを競う新しいゲーム番組の司会者、スーパーブクロウとパートナーを組むことになる。Android アプリで Live 更新を活用して、進行中の一致のステータスを表示し、リアルタイムで通知をダイナミックに更新できるようにしようとしています。

![Androidからのライブ更新の例]({% image_buster /assets/img/android/android-live-update.png %})({: style="max-width:40%;"})

{% multi_lang_include developer_guide/prerequisites/android.md %}

### ステップ 1: カスタム通知ファクトリーを作成する

アプリケーションで、[`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) を拡張して Braze Live 更新の表示方法を処理する、`MyCustomNotificationFactory.kt` という名前の新しいファイルを作成します。

次の例では、Superb Owl は、進行中の一致の Live 更新を表示するカスタム通知ファクトリを作成しました。次のステップでは、`getTeamInfo` という新しいメソッドを作成し、チームのデータをアクティビティにマッピングする。

```kotlin
class MyCustomNotificationFactory : IBrazeNotificationFactory {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        val notificationBuilder = populateNotificationBuilder(payload)
        val context = payload.context ?: return null

        if (notificationBuilder == null) {
            brazelog { "Notification could not be built. Returning null as created notification." }
            return null
        }
        notificationBuilder.setContentTitle("Android Live Updates").setContentText("Ongoing updates below")
        setProgressStyle(notificationBuilder, context)
        return notificationBuilder.build()
    }

    private fun setProgressStyle(notificationBuilder: NotificationCompat.Builder, context: Context) {
        val style = NotificationCompat.ProgressStyle()
            .setStyledByProgress(false)
            .setProgress(200)
            .setProgressTrackerIcon(IconCompat.createWithResource(context, R.drawable.notification_small_icon))
            .setProgressSegments(
                mutableListOf(
                    NotificationCompat.ProgressStyle.Segment(1000).setColor(Color.GRAY),
                    NotificationCompat.ProgressStyle.Segment(200).setColor(Color.BLUE),
                )
            )
            .setProgressPoints(
                mutableListOf(
                    NotificationCompat.ProgressStyle.Point(60).setColor(Color.RED),
                    NotificationCompat.ProgressStyle.Point(560).setColor(Color.GREEN)
                )
            )

        notificationBuilder.setStyle(style)
    }
}
```

### ステップ2: 顧客データをマップする

`MyCustomNotificationFactory.kt` で、ライブ更新が表示されたときにデータを処理するための新しいメソッドを作成する。

Superb Owlは、各チームの名前とロゴを拡大されたライブ更新に対応させるために、以下の方法を作成した：

```kotlin
class CustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        // Your existing code
        return super.createNotification(payload)
    }

    // Your new method
    private fun getTeamInfo(team: String?): Pair<String, Int> {
        return when (team) {
            "WBF" -> Pair("Wild Bird Fund", R.drawable.team_wbf)
            "OWL" -> Pair("Owl Rehab", R.drawable.team_owl)
            else  -> Pair("Unknown", R.drawable.notification_small_icon)
        }
    }
}
```

### ステップ 3:カスタム通知ファクトリーを設定する

アプリケーションクラスで [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?) を使用して、カスタム通知ファクトリを設定します。

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### ステップ4:アクティビティを送信する

あなたは [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)REST APIエンドポイントを使用して、ユーザーのAndroidデバイスにプッシュ通知を送信できる。

#### curlコマンドの例

Superb Owl は以下の curl コマンドを使ってリクエストを送信しました。

```
curl -X POST "https://BRAZE_REST_ENDPOINT/messages/send" \
  -H "Authorization: Bearer {REST_API_KEY}" \
  -H "Content-Type: application/json" \
  --data '{
    "external_user_ids": ["USER_ID"],
    "messages": {
      "android_push": {
        "title": "WBF vs OWL",
        "alert": "2 to 4 1:33 Q4",
        "extra": {
          "live_update": "true",
          "team1": "WBF",
          "team2": "OWL",
          "score1": "2",
          "score2": "4",
          "time": "1:33",
          "quarter": "Q4"
        },
        "notification_id": "ASSIGNED_NOTIFICATION_ID"
      }
    }
  }'
```

{% alert tip %}
curl コマンドはテストに役立ちますが、既に [iOS Live アクティビティ]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift)を処理しているバックエンドでこの呼び出しを処理することをおすすめします。
{% endalert %}

#### リクエストパラメーター

| キー                          | 説明 |
|------------------------------|------------|
| `REST_API_KEY`               | `messages.send` 権限を持つ Braze REST API キー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| `BRAZE_REST_ENDPOINT`         | RESTエンドポイントのURL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/api/basics/#endpoints) に応じて異なります。 |
| `USER_ID`                    | 通知を送信するユーザーのID。 |
| `messages.android_push.title` | メッセージのタイトル。デフォルトでは、これはカスタム通知ファクトリのライブ通知には使用されませんが、フォールバックとして使用できます。 |
| `messages.android_push.alert` | メッセージの本文。デフォルトでは、これはカスタム通知ファクトリのライブ通知には使用されませんが、フォールバックとして使用できます。 |
| `messages.extra`             | カスタム通知ファクトリがライブ通知に使用するキーと値のペア。この値には任意の文字列を割り当てることができます。ただし、上記の例では、`live_updates` を使用して、デフォルトのプッシュ通知かライブプッシュ通知かを判断します。 |
| `ASSIGNED_NOTIFICATION_ID`   | 選択したユーザーのライブ通知に割り当てたい通知ID。ID はこのゲームに対して一意である必要があり、後で[既存の通知を更新する](#android_step-4-update-data-with-the-braze-rest-api)ために使用する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### ステップ 5: アクティビティを更新する

既存のライブアップデートを新しいデータで更新するには、`messages.extra` に割り当てられた関連するキーと値のペアを修正し、同じ`notification_id` を使用し、`/messages/send` エンドポイントを再度呼び出す。
