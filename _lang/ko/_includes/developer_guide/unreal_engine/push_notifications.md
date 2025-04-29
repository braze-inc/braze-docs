{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## 푸시 알림 설정하기

### 1단계: 프로젝트 설정

{% tabs %}
{% tab Android %}
먼저, Android 프로젝트에 Firebase를 추가합니다. 단계별 지침은 Google의 [Firebase 설정 가이드를](https://firebase.google.com/docs/android/setup) 참조하세요.
{% endtab %}

{% tab iOS %}
{% multi_lang_include developer_guide/swift/apns_token.md %}
{% endtab %}
{% endtabs %}

### 2단계: 푸시 알림 사용 설정

{% tabs %}
{% tab Android %}
프로젝트의 `engine.ini` 파일에 다음 줄을 추가합니다. [Firebase 프로젝트에서](https://firebase.google.com/docs/cloud-messaging/concept-options#credentials) `YOUR_SEND_ID` 을 [발신자 ID로](https://firebase.google.com/docs/cloud-messaging/concept-options#credentials) 바꾸어야 합니다.

```ini
bEnableFirebaseCloudMessagingSupport=true
bIsFirebaseCloudMessagingRegistrationEnabled=true
FirebaseCloudMessagingSenderIdKey=YOUR_SENDER_ID
```

와 같은 디렉터리 내에 [BrazeUPLAndroid.xml](./BrazeSample/Plugins/Braze/Source/Braze/BrazeUPLAndroid.xml)와 같은 디렉토리에 `AndroidCopies` 라는 이름의 새 디렉토리를 만들고 `google-services.json` 파일을 추가합니다.
{% endtab %}

{% tab iOS %}
프로젝트에서 **설정** > **프로젝트 설정** > **iOS** > **온라인으로** 이동한 다음 **원격 알림 지원 활성화에** 체크합니다. 완료되면 프로비저닝에 푸시 기능이 사용 설정되어 있는지 확인합니다.

{% alert important %}
iOS용 푸시 기능을 사용하려면 프로젝트가 소스에서 빌드되어 있어야 합니다. 자세한 내용은 [언리얼 엔진을 참조하세요: 소스에서 빌드](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source).
{% endalert %}
{% endtab %}
{% endtabs %}

## 선택적 구성

{% tabs %}
{% tab Android %}
#### 작은 아이콘과 큰 아이콘 설정하기

[작은 알림 아이콘과 큰 알림 아이콘을]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android&tab=android#configure-icons) 설정하려면 다음과 같이 하세요:

1. `AndroidCopies/res` 폴더 안에 있는 적절한 그리기 가능한 폴더(기본값은`drawable` )에 아이콘을 추가합니다.
2. `AndroidCopies/res/values` 폴더에 `braze.xml` 을 추가하여 아이콘을 설정합니다. 아주 기본적인 braze.xml 파일입니다:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <drawable name="com_braze_push_small_notification_icon">@drawable/notification_small_icon</drawable>
        <drawable name="com_braze_push_large_notification_icon">@drawable/notification_large_icon</drawable>
    </resources>
    ```

{% alert note %}
`AndroidCopies` 폴더의 파일은 `BrazeUPLAndroid.xml` 에 정의된 대로 생성된 안드로이드 프로젝트 구조에 복사됩니다.
{% endalert %}
{% endtab %}

{% tab iOS %}
#### 원격 실행 알림

언리얼 엔진 4.25.3 버전부터 UE4 에는 애플리케이션 초기 실행을 유발하는 원격 알림 수신 기능이 제대로 지원되지 않습니다. 이 알림 수신을 지원하기 위해 UE4용과 Braze SDK 플러그인용 두 개의 git 패치를 만들었습니다.

1. UE4 엔진 `Source` 디렉터리에서 git 패치 `UE4_Engine-Cache-Launch-Remote-Notification.patch` 를 적용합니다.
2. Braze 언리얼 SDK 디렉터리에서 git 패치 `Braze_SDK-Read-Cached-Remote-Launch-Notification.patch` 를 적용합니다.
{% endtab %}
{% endtabs %}
