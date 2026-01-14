{% multi_lang_include developer_guide/prerequisites/android.md %} また、[プッシュ通知s]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)を設定する必要があります。

## カスタム通知レイアウト

Braze 通知 s は[データメッセージ](https://firebase.google.com/docs/cloud-messaging/concept-options) として送信されます。つまり、アプリライセンスは、バックグラウンド内でも(アプリがバックグラウンドにいるときにシステムによって自動的に処理される通知 メッセージとは対照的に)、それに応じて応答し、動作を実行する機会を常に持っています。そのため、通知トレイに配信される通知にパーソナライズされた UI 要素を表示するなどして、アプリケーションでエクスペリエンスをカスタマイズできます。この方法でプッシュを実装することに慣れていない方もいるかもしれませんが、Braze でよく知られている機能の 1 つである[プッシュ通知ストーリー]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)は、カスタムビューコンポーネントを使用して魅力的なエクスペリエンスを生み出す機能の良い例です。

{% alert important %}
Android では、カスタム通知ビューを実装するために使用できるコンポーネントにいくつかの制限があります。通知ビューレイアウトには、[RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews) フレームワークと互換性のある View オブジェクト_のみ_を含める必要があります。
{% endalert %}

[`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) インターフェイスを使用して、Braze プッシュ通知の表示方法をカスタマイズできます。`BrazeNotificationFactory` を拡張することで、通知がユーザーに表示される前に Braze はファクトリーの`createNotification()` メソッドを呼び出します。その後、Braze ダッシュボードまたは REST API を通じて送信されたカスタムのキーと値のペアを含むペイロードを渡します。

このセクションでは、野生動物救助チームが誰が一番多くのフクロウを救えるかを競う新しいゲーム番組の司会者、スーパーブクロウとパートナーを組むことになる。通知 s をAndroid アプリでライブアップデートすることで、進行中の試合のステータスを表示し、リアルタイムでダイナミックな 更新を作成できるようにすることを求めています。

![Superb Owlが見せたいライブアップデート。「ワイルドバード・ファンド」と「オール・レスキュー」の間で進行中の試合を表示する。現在のところ第4四半期で、OWLがリードしているスコアは2-4です。]({% image_buster /assets/img/android/android-live-activity-superb-owl-example.jpg %}){: style="max-width:65%;"}

### ステップ 1: カスタムレイアウトの追加

1 つ以上のカスタム通知 リモートビューレイアウトをプロジェクトに追加できます。これらは、折りたたんだり展開したりしたときに通知sがどのように表示されるかを扱うのに役立ちます。ディレクトリ構造は、次のようになります。

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_collapsed.xml
        └── liveupdate_expanded.xml
```

各XMLファイルで、カスタムレイアウトを作成します。Superb Owl は、折りたたまれて展開されたRemoteView レイアウト用に次のレイアウトを作成しました。

{% tabs local %}
{% tab  Example: Collapsed layout %}
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">

    <TextView
        android:id="@+id/notification_title"
        style="@style/TextAppearance.Compat.Notification.Title"
        android:layout_width="wrap_content"
        android:layout_height="0dp"
        android:layout_weight="1" />
</LinearLayout>
```
{% endtab %}

{% tab Example: Expanded layout %}
{% details Show the sample code %}
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal">

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"

        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team1logo"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:layout_gravity="center"
            android:src="@drawable/team_default1"/>

        <TextView
            android:id="@+id/team1name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1.6"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <TextView
            android:id="@+id/score"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="2-4"
            android:textColor="#555555"
            android:textAlignment="center"
            android:textSize="32sp"
            android:textStyle="bold" />

        <TextView
            android:id="@+id/timeInfo"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>


    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team2logo"
            android:layout_gravity="center"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:src="@drawable/team_default2"/>

        <TextView
            android:id="@+id/team2name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>
</LinearLayout>
```
{% enddetails %}
{% endtab %}
{% endtabs %}

### ステップ 2:カスタム通知ファクトリーを作成する

アプリ ライセンスで、[`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) という名前の新しいファイルを作成し、カスタムRemoteView レイアウトの表示方法を処理します。

次の例では、Superb Owlがカスタム通知ファクトリを作成し、現在のマッチングのRemoteViewレイアウトを表示しました。[next ステップ](#android_step-3-map-custom-data) では、`getTeamInfo` という新しいメソッドを作成して、チームデータをアクティビティにマッピングします。

{% details Show the sample code %}
```kotlin
import android.app.Notification
import android.widget.RemoteViews
import androidx.core.app.NotificationCompat
import com.braze.models.push.BrazeNotificationPayload
import com.braze.push.BrazeNotificationFactory
import com.braze.push.BrazeNotificationUtils.getOrCreateNotificationChannelId
import com.braze.support.BrazeLogger.brazelog

class MyCustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        if (payload.extras.containsKey("live_update")) {
            val kvp = payload.extras
            val notificationChannelId = getOrCreateNotificationChannelId(payload)
            val context = payload.context

            if (context == null) {
                brazelog { "BrazeNotificationPayload has null context. Not creating notification" }
                return null
            }

            val team1 = kvp["team1"]
            val team2 = kvp["team2"]
            val score1 = kvp["score1"]
            val score2 = kvp["score2"]
            val time = kvp["time"]
            val quarter = kvp["quarter"]

            // Superb Owl will define the 'getTeamInfo' method in the next step.
            val (team1name, team1icon) = getTeamInfo(team1)
            val (team2name, team2icon) = getTeamInfo(team2)

            // Get the layouts to use in the custom notification.
            val notificationLayoutCollapsed = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_collapsed)
            val notificationLayoutExpanded = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_expanded)

            // Very simple notification for the small layout
            notificationLayoutCollapsed.setTextViewText(
                R.id.notification_title,
                "$team1 $score1 - $score2 $team2\n$time $quarter"
            )

            notificationLayoutExpanded.setTextViewText(R.id.score, "$score1 - $score2")
            notificationLayoutExpanded.setTextViewText(R.id.team1name, team1name)
            notificationLayoutExpanded.setTextViewText(R.id.team2name, team2name)
            notificationLayoutExpanded.setTextViewText(R.id.timeInfo, "$time - $quarter")
            notificationLayoutExpanded.setImageViewResource(R.id.team1logo, team1icon)
            notificationLayoutExpanded.setImageViewResource(R.id.team2logo, team2icon)

            val customNotification = NotificationCompat.Builder(context, notificationChannelId)
                .setSmallIcon(R.drawable.notification_small_icon)
                .setStyle(NotificationCompat.DecoratedCustomViewStyle())
                .setCustomContentView(notificationLayout)
                .setCustomBigContentView(notificationLayoutExpanded)
                .build()
            return customNotification
        } else {
            // Use the BrazeNotificationFactory for all other notifications
            return super.createNotification(payload)
        }
    }
}
```
{% enddetails %}

### ステップ 3:顧客データをマップする

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

### ステップ 4: カスタム通知ファクトリーを設定する

アプリケーションクラスで [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?) を使用して、カスタム通知ファクトリを設定します。

```kotlin
import com.braze.Braze

class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### ステップ 5: アクティビティを送信する

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

| キー                           | 説明                                                                                                                                                                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `REST_API_KEY`                | `messages.send` 権限を持つ Braze REST API キー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。                                                                                                     |
| `BRAZE_REST_ENDPOINT`         | RESTエンドポイントのURL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/api/basics/#endpoints) に応じて異なります。                                                                                                                  |
| `USER_ID`                     | 通知を送信するユーザーのID。                                                                                                                                                                                          |
| `messages.android_push.title` | メッセージのタイトル。デフォルトでは、これはカスタム通知ファクトリのライブ通知には使用されませんが、フォールバックとして使用できます。                                                                                                    |
| `messages.android_push.alert` | メッセージの本文。デフォルトでは、これはカスタム通知ファクトリのライブ通知には使用されませんが、フォールバックとして使用できます。                                                                                                     |
| `messages.extra`              | カスタム通知ファクトリがライブ通知に使用するキーと値のペア。この値には任意の文字列を割り当てることができます。ただし、上記の例では、`live_updates` を使用して、デフォルトのプッシュ通知かライブプッシュ通知かを判断します。  |
| `ASSIGNED_NOTIFICATION_ID`    | 選択したユーザーのライブ通知に割り当てたい通知ID。ID はこのゲームに対して一意である必要があり、後で[既存の通知を更新する](#android_step-4-update-data-with-the-braze-rest-api)ために使用する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### ステップ 6: アクティビティを更新する

既存のRemoteView 通知を新しいデータで更新するには、`messages.extra` に割り当てられた関連するキーと値のペアを変更し、同じ`notification_id` を使用して`/messages/send` エンドポイントを再度呼び出します。

## パーソナライズされたプッシュ通知

プッシュ通知では、カスタムビュー階層内にユーザー固有の情報を表示できます。次の例では、API-トリガーを使用してパーソナライズされた プッシュ通知をユーザーに送信し、アプリで特定のタスクを完了した後に現在の進行状況を追跡できるようにします。

![パーソナライズされたプッシュダッシュボード例]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

ダッシュボードでパーソナライズされたプッシュを設定するには、表示するカテゴリを登録し、リキッドを使用して表示する関連ユーザー 属性を設定します。

![パーソナライズされたプッシュダッシュボード例]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}
