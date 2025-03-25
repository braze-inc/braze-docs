---
nav_title: Android SDK 통합
article_title: Android SDK 통합 for Android and FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 Android SDK를 통합하는 방법을 다룹니다."
search_rank: 4
---

# Android SDK 통합

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 Android SDK를 통합하는 방법을 다룹니다. Braze SDK를 설치하면 기본 분석 기능과 사용자와 상호 작용할 수 있는 작동 중인 인앱 메시지가 제공됩니다.

{% alert note %}
최적의 성능을 위해 Android 12에서 가능한 한 빨리 [Braze Android 소프트웨어 개발 키트 v13.1.2+](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312)로 업그레이드할 것을 권장합니다. 자세한 내용은 [Android 12 업그레이드 가이드]({{site.baseurl}}/android_12/)를 참조하세요.
{% endalert %}

## 1단계: Braze 라이브러리를 통합하십시오

Braze Android SDK는 UI 구성요소 없이 선택적으로 통합될 수 있습니다. 그러나 콘텐츠 카드 및 인앱 메시징은 사용자가 디자인한 UI에 커스텀 데이터를 전달하지 않으면 작동하지 않습니다. 또한 푸시 알림은 푸시 처리 코드가 UI 라이브러리에 있기 때문에 작동하지 않습니다. 이 UI 요소는 완전히 사용자 지정할 수 있습니다. 우리는 이러한 기능들의 통합을 강력히 권장합니다. 각 채널 또는 도구를 사용할 때의 이점 목록은 [콘텐츠 카드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/#advantages-of-using-content-cards) 및 [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) 설명서를 참조하십시오.

### 기본 통합

Braze 메시징 기능에 접근하려면 UI 라이브러리를 통합해야 합니다. IDE에 따라 UI 라이브러리를 통합하려면 다음 Android Studio 지침을 참조하세요.

#### Braze 종속성 추가

앱의 `build.gradle`에 `android-sdk-ui` 종속성을 추가하십시오. 

위치 또는 Braze 지오펜스 기능을 사용하는 경우 앱의 `build.gradle`에 `android-sdk-location`도 포함합니다.

{% alert important %}
기본 외 Android SDK(예: Flutter, Cordova, Unity 등)를 사용하는 경우, 해당 SDK에는 이미 올바른 버전의 Android SDK에 대한 `android-sdk-ui` 종속성이 포함되어 있습니다. 해당 버전을 수동으로 업데이트하지 마십시오.
{% endalert %}

```gradle
dependencies {
  implementation "com.braze:android-sdk-ui:+"
  implementation "com.braze:android-sdk-location:+"
}
```

다음 예제에서는 `build.gradle`에 종속성 줄을 배치할 위치를 보여줍니다. 예제에서 사용된 버전은 오래된 버전을 사용하고 있음을 유의하십시오. 최신 버전의 Braze 안드로이드 SDK를 확인하려면 Braze 안드로이드 SDK [릴리스를](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md) 방문하세요.

![파일 끝에 종속성 코드가 추가된 "build.gradle"가 표시되는 안드로이드 스튜디오]({% image_buster /assets/img_archive/androidstudio2.png %})

#### Gradle 동기화 수행

Gradle 동기화를 수행하여 프로젝트를 구축하고 [종속성 추가 사항](#add-braze-dependency)을 통합하십시오.

![Android 스튜디오의 배너 "마지막 프로젝트 동기화 이후 Gradle 파일이 변경되었습니다. IDE가 제대로 작동하려면 프로젝트 동기화가 필요할 수 있습니다. 지금 동기화."]({% image_buster /assets/img_archive/androidstudio3.png %})

## 2단계: braze.xml에서 Braze SDK 구성

{% alert note %}
2019년 12월부터 커스텀 엔드포인트는 더 이상 제공되지 않으며, 기존 커스텀 엔드포인트가 있는 경우 계속 사용할 수 있습니다. 자세한 내용은 <a href="{{site.baseurl}}/api/basics/#endpoints">사용 가능한 엔드포인트 목록</a>을 참조하십시오.
{% endalert %}

라이브러리가 통합되었으므로 프로젝트의 `res/values` 폴더에서 `braze.xml` 파일을 생성해야 합니다. 특정 데이터 클러스터에 있거나 기존 커스텀 엔드포인트가 있는 경우 `braze.xml` 파일에서도 엔드포인트를 지정해야 합니다. 

해당 파일의 내용은 다음 코드 스니펫과 유사해야 합니다. Braze 대시보드의 **설정 관리** 페이지에서 식별자로 `YOUR_APP_IDENTIFIER_API_KEY`을(를) 대체하십시오. [dashboard.braze.com](https://dashboard.braze.com)에 로그인하여 [클러스터 주소]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)를 찾으십시오. 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

## 3단계: 필요한 권한을 AndroidManifest.xml에 추가하십시오
API 키를 추가했으므로 `AndroidManifest.xml`에 다음 권한을 추가해야 합니다.

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Android M의 출시와 함께 Android는 설치 시점에서 런타임 권한 모델로 전환되었습니다. 그러나 이 두 권한 모두 일반 권한이며 앱 매니페스트에 나열된 경우 자동으로 부여됩니다. 자세한 내용은 Android의 [권한 설명서](https://developer.android.com/training/permissions/index.html)를 참조하십시오.
{% endalert %}

## 4단계: Android에서 사용자 세션 추적

### 활동 생명주기 콜백 통합

`openSession()`, `closeSession()`,[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html)및 `InAppMessageManager` 등록은 선택적으로 자동으로 처리됩니다.

#### 활동 수명 주기 콜백 등록

`onCreate()` 메서드에 다음 코드를 추가하십시오: `Application` 클래스:

{% tabs %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

{% endtab %}
{% endtabs %}

에 사용할 수 있는 매개 변수에 대한 자세한 내용은 SDK 참조 문서를 참조하십시오. [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

## 5단계: 위치 추적 활성화

Braze 위치 수집을 활성화하려면 `braze.xml` 파일을 업데이트하여 `com_braze_enable_location_collection`를 포함하고 해당 값이 `true`로 설정되어 있는지 확인하십시오:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Braze Android SDK 버전 3.6.0부터 Braze 위치 수집은 기본적으로 비활성화됩니다.
{% endalert %}

## SDK 통합 완료

이제 Braze가 [애플리케이션에서 지정된 데이터]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/)를 수집하며 기본 통합이 완료됩니다.

다음 기사를 방문하여 [커스텀 이벤트 추적]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/), [푸시 메시징]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/), [콘텐츠 카드]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/) 및 Braze 기능 전체를 활성화하십시오.

