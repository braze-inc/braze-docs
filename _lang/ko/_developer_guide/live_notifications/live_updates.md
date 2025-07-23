---
nav_title: Android용 실시간 업데이트
article_title: 안드로이드 브레이즈 SDK용 라이브 활동
page_order: 0.1
description: "Android Braze SDK용 라이브 활동을 설정하는 방법을 알아보세요."
platform: 
  - Android
  - FireOS
---

# Android용 라이브 활동

> 안드로이드 브레이즈 SDK에서 라이브 업데이트를 에뮬레이트하는 방법을 알아보세요. 라이브 업데이트는 공식적으로 지원되지 않지만, 이 가이드에서는 라이브 업데이트의 동작을 에뮬레이트하는 방법을 보여드리므로 [Swift Braze SDK의 라이브 활동과]({{site.baseurl}}/developer_guide/live_notifications/live_activities) 유사한 대화형 잠금 화면 알림을 표시할 수 있습니다. 공식 라이브 업데이트와 달리 이 기능은 이전 Android 버전에서 구현할 수 있습니다.

## How it works

인터페이스를 사용하여 [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) 인터페이스를 사용하여 Braze 푸시 알림이 표시되는 방식을 사용자 지정할 수 있습니다. `BrazeNotificationFactory` 을 확장하면 사용자에게 알림이 표시되기 전에 Braze가 공장의 `createNotification()` 메소드를 호출합니다. 그런 다음 Braze 대시보드 또는 REST API를 통해 전송된 사용자 지정 키-값 쌍이 포함된 페이로드를 전달합니다.

## 라이브 업데이트 에뮬레이션

{% alert important %}
Android OS에서는 라이브 업데이트가 기본적으로 지원되지 않습니다. 다음 섹션에서는 일반적인 동작을 모방하는 방법만 설명합니다.
{% endalert %}

이 섹션에서는 야생동물 구조팀이 누가 가장 많은 올빼미를 구할 수 있는지 경쟁하는 새로운 게임 쇼의 호스트인 슈퍼 올빼미와 파트너가 됩니다. Android 앱에서 실시간 업데이트를 활용하여 진행 중인 경기의 상태를 표시하고 실시간으로 알림을 동적으로 업데이트할 수 있도록 하려고 합니다.

![슈퍼 올빼미의 라이브 업데이트는 '야생 조류 기금'과 '올빼미 구조대'의 진행 중인 경기를 보여줍니다. 현재 4쿼터, 스코어는 2-4로 OWL이 앞서고 있습니다.]({% image_buster /assets/img/android/android-live-activity-superb-owl-example.jpg %}){: style="max-width:65%;"}

#{% multi_lang_include developer_guide/prerequisites/android.md %}

### 1단계: 사용자 지정 레이아웃 추가

프로젝트에 하나 이상의 사용자 지정 라이브 업데이트 레이아웃을 추가할 수 있습니다. 이는 접거나 펼쳤을 때 알림이 표시되는 방식을 처리하는 데 유용합니다. 디렉토리 구조는 다음과 비슷해야 합니다:

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_collapsed.xml
        └── liveupdate_expanded.xml
```

각 XML 파일에서 사용자 지정 레이아웃을 만듭니다. Superb Owl은 라이브 업데이트의 축소 및 확장을 위해 다음과 같은 레이아웃을 만들었습니다:

{% tabs local %}
{% tab  예시: 접힌 레이아웃 %}
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

{% tab 예시: 확장된 레이아웃 %}
{% details 샘플 코드 보기 %}
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

### 2단계: 사용자 지정 알림 팩토리 만들기

애플리케이션에서 확장자가 `MyCustomNotificationFactory.kt` 인 새 파일을 생성합니다. [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) 확장자를 가진 파일을 생성하여 Braze 라이브 업데이트가 표시되는 방식을 처리합니다.

다음 예시에서는 슈퍼 올빼미가 진행 중인 경기에 대한 실시간 업데이트를 표시하는 사용자 지정 알림 팩토리를 만들었습니다. [다음 단계에서는](#android_step-3-map-custom-data) `getTeamInfo` 이라는 새로운 메서드를 만들어 팀의 데이터를 활동에 매핑합니다.

{% details 샘플 코드 보기 %}
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

### 3단계: 사용자 지정 데이터 매핑

`MyCustomNotificationFactory.kt` 에서 라이브 업데이트가 표시될 때 데이터를 처리하는 새로운 메서드를 만듭니다.

슈퍼 올빼미는 각 팀의 이름과 로고를 확장된 라이브 업데이트에 매핑하는 방법을 다음과 같이 만들었습니다:

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

### 4단계: 사용자 지정 알림 팩토리 설정

애플리케이션 클래스에서 [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)를 사용하여 사용자 지정 알림 팩토리를 설정합니다.

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

### 5단계: 활동 보내기

REST API 엔드포인트를 사용하여 [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) REST API 엔드포인트를 사용하여 사용자의 Android 디바이스로 푸시 알림을 보낼 수 있습니다.

#### curl 명령 예제

Superb Owl은 다음 curl 명령을 사용하여 요청을 보냈습니다:

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
컬 명령은 테스트에 유용하지만, 이미 [iOS 라이브 활동을]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift) 처리하고 있는 백엔드에서 이 호출을 처리하는 것이 좋습니다.
{% endalert %}

#### 요청 매개변수

| 키                          | 설명 |
|------------------------------|------------|
| `REST_API_KEY`               | `messages.send` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| `BRAZE_REST_ENDPOINT`         | 귀하의 REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에]({{site.baseurl}}/api/basics/#endpoints) 따라 달라집니다. |
| `USER_ID`                    | 알림을 보낼 사용자의 ID입니다. |
| `messages.android_push.title` | 메시지 제목입니다. 기본적으로 이 기능은 사용자 지정 알림 팩토리의 실시간 알림에 사용되지 않지만, 대체 기능으로 사용할 수 있습니다. |
| `messages.android_push.alert` | 메시지 본문입니다. 기본적으로 이 기능은 사용자 지정 알림 팩토리의 실시간 알림에 사용되지 않지만, 대체 기능으로 사용할 수 있습니다. |
| `messages.extra`             | 사용자 지정 알림 팩토리에서 실시간 알림에 사용하는 키-값 쌍입니다. 이 값에는 어떤 문자열이든 지정할 수 있지만, 위의 예에서는 `live_updates` 을 사용하여 기본 푸시 알림인지 실시간 푸시 알림인지를 결정합니다. |
| `ASSIGNED_NOTIFICATION_ID`   | 선택한 사용자의 실시간 알림에 할당할 알림 ID입니다. 이 ID는 이 게임에 고유해야 하며, 나중에 [기존 알림을 업데이트할](#android_step-4-update-data-with-the-braze-rest-api) 때 사용해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 6단계: 활동 업데이트

기존 라이브 업데이트를 새 데이터로 업데이트하려면 `messages.extra` 에 할당된 관련 키-값 쌍을 수정한 다음 동일한 `notification_id` 을 사용하여 `/messages/send` 엔드포인트를 다시 호출합니다.
