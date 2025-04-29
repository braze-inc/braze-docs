---
nav_title: Android用ライブ更新
article_title: Android Braze SDKのライブ活動
page_order: 0.1
description: "Android Braze SDKのLive Activitiesの設定方法を学習する。"
platform: 
  - Android
  - FireOS
---

# Android用ライブ・アクティビティ

> Android Braze SDKでライブ更新をエミュレートする方法を学ぶ。Live Updatesは公式にはサポートされていないが、このガイドでは、[Swift Braze SDKのLive Activitiesに]({{site.baseurl}}/developer_guide/live_notifications/live_activities)似たインタラクティブなロック画面通知を表示できるように、その動作をエミュレートする方法を紹介する。公式のライブ更新とは異なり、この機能は古いバージョンのAndroidにも実装できる。

## CDI の仕組み

この [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html)インターフェイスを使って、Brazeプッシュ通知の表示方法をカスタマイズできる。`BrazeNotificationFactory` を拡張することで、Brazeはユーザーに通知が表示される前に、ファクトリーの`createNotification()` メソッドを呼び出す。そして、BrazeダッシュボードまたはREST APIを通して送信されるカスタムキーと値のペアを含むペイロードを渡す。

## ライブ更新をエミュレートする

{% alert important %}
ライブ更新はAndroid OSではネイティブにサポートされていない。以下のセクションでは、彼らの一般的な振る舞いをエミュレートする方法のみを紹介する。
{% endalert %}

このセクションでは、野生動物救助チームが誰が一番多くのフクロウを救えるかを競う新しいゲーム番組の司会者、スーパーブクロウとパートナーを組むことになる。彼らはAndroidアプリでライブアップデートを活用し、進行中の試合のステータスを表示し、リアルタイムでダイナミックな通知を更新できるようにしようとしている。

![スーパーフクロウが作りたがっているライブ更新は、「野鳥基金」と「フクロウ救助隊」の現在進行中の試合を表示している。現在第4クォーター、スコアは2-4でOWLがリードしている。]({% image_buster /assets/img/android/android-live-activity-superb-owl-example.jpg %}){: style="max-width:65%;"}

#{% multi_lang_include developer_guide/prerequisites/android.md %}

### ステップ1:顧客レイアウトを追加する

プロジェクトにカスタム・ライブ更新レイアウトを1つ以上追加できる。これらは、折りたたんだり広げたりしたときの通知の表示方法を処理するのに役立つ。ディレクトリ構造は以下のようになっているはずだ：

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_collapsed.xml
        └── liveupdate_expanded.xml
```

各XMLファイルで、カスタムレイアウトを作成する。Superb Owlは、崩壊し拡張されたライブ更新のために以下のレイアウトを作成した：

{% tabs local %}
{% tab  例を挙げよう：折りたたまれたレイアウト %}
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

{% tab 例:レイアウトの拡大 %}
{% details サンプルコードを表示する %}
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

### ステップ2: カスタム通知ファクトリーを作成する

アプリケーションで、`MyCustomNotificationFactory.kt` という名前の新しいファイルを作成する。 [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html)という名前の新しいファイルを作成する。

次の例では、Superb Owlは、進行中の試合のライブ更新を表示するカスタム通知ファクトリーを作成した。[次のステップでは](#android_step-3-map-custom-data)、`getTeamInfo` という新しいメソッドを作り、チームのデータをアクティビティにマッピングする。

{% details サンプルコードを表示する %}
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

### ステップ4:カスタム通知ファクトリーを設定する

アプリケーション・クラスで [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)を使用して、カスタム通知ファクトリを設定する。

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

Superb Owlは以下のcurlコマンドを使ってリクエストを送った：

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
curlコマンドはテストに役立つが、[iOSライブ・アクティビティを]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift)すでに処理しているバックエンドでこの呼び出しを処理することをお勧めする。
{% endalert %}

#### リクエストパラメーター

| キー                          | 説明 |
|------------------------------|------------|
| `REST_API_KEY`               | `messages.send` 権限を持つ Braze REST API キー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| `BRAZE_REST_ENDPOINT`         | RESTエンドポイントのURL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/api/basics/#endpoints) に応じて異なります。 |
| `USER_ID`                    | 通知を送信するユーザーのID。 |
| `messages.android_push.title` | メッセージのタイトルだ。デフォルトでは、これはカスタム通知ファクトリーのライブ通知には使用されないが、フォールバックとして使用することができる。 |
| `messages.android_push.alert` | メッセージの本文だ。デフォルトでは、これはカスタム通知ファクトリーのライブ通知には使用されないが、フォールバックとして使用することができる。 |
| `messages.extra`             | カスタム通知ファクトリがライブ通知に使用するキーと値のペア。この値には任意の文字列を割り当てることができるが、上の例では、`live_updates` 、デフォルトかライブ・プッシュ通知かを判断するために使われている。 |
| `ASSIGNED_NOTIFICATION_ID`   | 選択したユーザーのライブ通知に割り当てたい通知ID。このIDはこのゲームに固有のものでなければならず、[既存の通知を](#android_step-4-update-data-with-the-braze-rest-api)後で[更新](#android_step-4-update-data-with-the-braze-rest-api)するために使用しなければならない。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### ステップ 6: アクティビティを更新する

既存のライブアップデートを新しいデータで更新するには、`messages.extra` に割り当てられた関連するキーと値のペアを修正し、同じ`notification_id` を使用し、`/messages/send` エンドポイントを再度呼び出す。
