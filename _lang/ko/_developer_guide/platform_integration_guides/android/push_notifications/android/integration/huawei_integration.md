---
nav_title: 화웨이 통합
article_title: Android용 화웨이 푸시 통합
platform: Android
page_order: 9
description: "이 문서에서는 Huawei Android 연동 설정 방법에 대해 설명합니다."
channel:
  - push

---

# 화웨이 푸시 통합

> [화웨이에서](https://huaweimobileservices.com/) 제조한 최신 휴대폰에는 Google의 FCM(Firebase Cloud Messaging) 대신 푸시 전송에 사용되는 서비스인 화웨이 모바일 서비스(HMS)가 탑재되어 있습니다.<br><br>이 가이드에서는 Braze를 통해 푸시를 전송하고 세분화, 분석, 캔버스 등 기존의 모든 Braze 기능을 활용하기 위해 Huawei Android 통합을 설정하는 방법을 설명합니다!

## 1단계: 화웨이 개발자 계정 등록

시작하기 전에 [Huawei 개발자 계정을](https://developer.huawei.com/consumer/en/console) 등록하고 설정해야 합니다. Huawei 계정에서 **내 프로젝트 > 프로젝트 설정 > 앱 정보로** 이동하여 `App ID` 및 `App secret` 을 기록해 둡니다.

![]({% image_buster /assets/img/huawei/huawei-credentials.png %})

## 2단계: Braze 대시보드에서 새 Huawei 앱 만들기

Braze 대시보드의 **설정** 탐색 아래에 있는 **앱 설정으로** 이동합니다.

**앱 추가를** 클릭하고 이름(예: 내 Huawei 앱)을 입력한 다음 플랫폼으로 `Android` 을 선택합니다.

![]({% image_buster /assets/img/huawei/huawei-create-app.png %}){: style="max-width:60%;"}

새 Braze 앱이 생성되면 푸시 알림 설정에서 푸시 제공업체로 `Huawei` 을 선택합니다. 다음으로 `Huawei Client Secret` 및 `Huawei App ID` 을 입력합니다.

![]({% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %})

## 3단계: 앱에 화웨이 메시징 SDK를 통합하세요.

화웨이는 애플리케이션에 화웨이 메시징 서비스를 통합하는 방법을 자세히 설명하는 [안드로이드 통합 코델랩을](https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html) 제공했습니다. 시작하려면 다음 단계를 따르세요.

코델랩을 완료한 후에는 사용자 지정 [Huawei 메시지 서비스를](https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls) 생성하여 푸시 토큰을 얻고 메시지를 Braze SDK로 전달해야 합니다.

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

사용자 지정 푸시 서비스를 추가한 후 `AndroidManifest.xml` 에 다음을 추가합니다:

```xml
<service
  android:name="package.of.your.CustomPushService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

## 4단계: Huawei 푸시 보내기

이 시점에서 Braze 대시보드에서 새 Huawei Android 앱을 생성하고, Huawei 개발자 자격 증명으로 앱을 구성하고, Braze 및 Huawei SDK를 앱에 통합했습니다.

다음으로, Braze에서 새로운 푸시 캠페인을 테스트하여 통합을 테스트할 수 있습니다.

### 새 푸시 알림 캠페인 만들기

**캠페인** 페이지에서 새 캠페인을 만들고 메시지 유형으로 **푸시 알림을** 선택합니다.

캠페인 이름을 지정한 후 푸시 플랫폼으로 **Android 푸시를** 선택합니다.

![사용 가능한 푸시 플랫폼을 표시하는 캠페인 생성 작성기.]({% image_buster /assets/img/huawei/huawei-test-push-platforms.png %})

다음으로 제목과 메시지로 푸시 캠페인을 작성합니다.

### 테스트 푸시 보내기

**테스트** 탭에서 [`changeUser(USER_ID_STRING)` 방법을]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#assigning-a-user-id) 사용하여 앱에서 설정한 사용자 ID를 입력하고 **테스트 보내기를** 클릭하여 테스트 푸시를 보냅니다.

![캠페인 작성 작성기의 테스트 탭에서 사용자 ID를 제공하고 '개별 사용자 추가' 필드에 입력하면 자신에게 테스트 메시지를 보낼 수 있습니다.]({% image_buster /assets/img/huawei/huawei-test-send.png %})

이 시점에서 Braze로부터 Huawei(HMS) 디바이스로 테스트 푸시 알림을 받게 될 것입니다.

### Huawei 세분화 설정(선택 사항)

Braze 대시보드의 화웨이 앱은 안드로이드 푸시 플랫폼을 기반으로 구축되었으므로 모든 안드로이드 사용자(Firebase 클라우드 메시징 및 화웨이 모바일 서비스)에게 푸시를 보내거나 특정 앱으로 캠페인 대상을 세분화할 수 있는 유연성이 있습니다.

화웨이 앱에만 푸시를 보내려면 \[새 세그먼트]({{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) )를 생성하고 **앱** 섹션에서 화웨이 앱을 선택합니다.

![]({% image_buster /assets/img/huawei/huawei-segmentation.png %})

물론 모든 안드로이드 푸시 제공업체에 동일한 푸시를 보내려면 현재 작업 영역 내에 구성된 모든 안드로이드 앱에 보낼 앱을 지정하지 않도록 선택할 수 있습니다.

## 분석

캠페인이 시작되면 Android 푸시용으로 집계된 캠페인 또는 캔버스에 대한 애널리틱스가 표시됩니다. Android 푸시 분석 및 설정에 대한 자세한 내용은 [푸시 사용 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) 참조하세요.

