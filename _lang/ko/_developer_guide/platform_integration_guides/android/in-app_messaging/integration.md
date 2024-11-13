---
nav_title: 통합
article_title: Android 및 FireOS용 인앱 메시지 통합
page_order: 1
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션에서 인앱 메시징을 통합하는 방법을 다룹니다."
channel:
  - in-app messages
search_rank: 2
---

# 인앱 메시지 통합

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에서 인앱 메시징을 통합하는 방법을 다룹니다.

[인앱 메시지는]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) 푸시 알림을 통해 사용자의 일과를 방해하지 않고 콘텐츠를 전달할 수 있도록 도와줍니다. 사용자 지정 및 맞춤 조정된 인앱 메시지는 사용자 경험을 향상시키고 오디언스가 앱에서 최대한의 가치를 얻을 수 있도록 도와줍니다. 다양한 레이아웃과 사용자 지정 툴을 선택하여 인앱 메시지를 통해 그 어느 때보다 높은 사용자 참여를 유도할 수 있습니다.

인앱 메시지의 예제를 보려면 [사례 연구](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html)를 참조하세요.

## 인앱 메시지 유형

Braze는 메시지, 이미지, [폰트 어썸](https://fontawesome.com/icons?d=gallery&p=2) 아이콘, 클릭 액션, 분석, 편집 가능한 스타일링 및 색 구성표로 각각 사용자 지정할 수 있는 여러 가지 기본 인앱 메시지 유형을 제공합니다. 현재 사용 가능한 유형은 다음과 같습니다:

- [`Slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html)
- [`Modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html)
- [`Full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html)
- [`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html)

[커스텀 인앱 메시지 보기]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-view-factory)를 정의할 수도 있습니다.

모든 인앱 메시지는 모든 인앱 메시지의 기본 동작과 특성을 정의하는 [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html) 인터페이스를 구현합니다. [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html)에서는 `IInAppMessage`를 구현하고 기본 인앱 메시지 구현을 제공하는 추상 클래스입니다. 모든 인앱 메시지 클래스는 `InAppMessageBase` 의 하위 클래스입니다.

또한 [`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html)라고 하는 `IInAppMessage`의 서브인터페이스가 있습니다. 여기에서는 클릭 동작 및 분석 지원 [버튼](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html)과 헤더 텍스트 및 닫기 버튼을 추가합니다.

{% alert important %}
버튼이 포함된 인앱 메시지의 경우 버튼 텍스트를 추가하기 전에 클릭 동작이 추가되면 `clickAction` 메시지도 최종 페이로드에 포함됩니다.
{% endalert %}

[`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html)는 `IInAppMessageImmersive`를 구현하고 기본 `immersive` 인앱 메시지 구현을 제공하는 추상 클래스입니다. `Modal` 인앱 메시지는 `InAppMessageImmersiveBase`의 서브클래스입니다.

HTML 인앱 메시지는 [`InAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) 인스턴스로 구현되며, 이는 [`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html)의 또 다른 서브클래스인 `IInAppMessage`을 구현하는 인스턴스입니다.

### 메시지 유형별 예상 동작

다음은 사용자가 기본 인앱 메시지 유형 중 하나를 여는 상황입니다.

{% tabs local %}
{% tab 슬라이드업 %}
[`Slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) 인앱 메시지는 화면 상단 또는 하단에서 '슬라이드 업' 또는 '슬라이드 다운'되기 때문에 그렇게 이름이 붙여졌습니다. 화면의 작은 부분을 차지하며 효과적이고 방해가 되지 않는 메시징 기능을 제공합니다.

![휴대폰 화면 하단에서 '인간은 복잡하다'는 인앱 메시지가 슬라이딩되는 모습. 커스텀 인게이지먼트는 안 됩니다." 백그라운드에서는 웹 페이지의 오른쪽 하단에 표시되는 것과 동일한 인앱 메시지가 표시됩니다.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab 모달 %}
[`Modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) 인앱 메시지는 화면 중앙에 표시되며 반투명 패널로 둘러싸여 있습니다. 보다 중요한 메시징에 유용하며, 두 개의 클릭 동작과 분석 지원 버튼을 제공할 수 있습니다.

![휴대폰 화면 가운데 다음과 같은 Modal 인앱 메시지가 표시됩니다. "사람은 복잡한 존재입니다. 커스텀 인게이지먼트는 안 됩니다." 백그라운드에서는 웹 페이지의 가운데 표시되는 것과 동일한 인앱 메시지가 표시됩니다.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab 전체 화면 %}
[`Full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) 인앱 메시지는 사용자 커뮤니케이션의 콘텐츠와 효과를 극대화하는 데 유용합니다. `full` 인앱 메시지의 상단에는 이미지가, 하단에는 텍스트와 최대 2개의 클릭 동작 및 분석 지원 버튼이 표시됩니다.

![휴대폰 화면 전체에 다음과 같은 인앱 메시지가 표시됩니다. "사람은 복잡한 존재입니다. 커스텀 인게이지먼트는 안 됩니다." 백그라운드에서는 웹 페이지의 가운데 크게 표시되는 것과 동일한 인앱 메시지가 표시됩니다.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endtab %}
{% tab 사용자 지정 HTML %}
[`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) 인앱 메시지는 완전히 맞춤화된 사용자 콘텐츠를 만드는 데 유용합니다. 사용자 정의 HTML 인앱 메시지 콘텐츠는 `WebView`에 표시되며, 선택적으로 이미지 및 글꼴과 같은 다양한 형식의 기타 콘텐츠를 포함할 수 있으므로 메시지 모양과 기능을 완벽하게 제어할 수 있습니다. <br><br>Android 인앱 메시지는 HTML 내에서 Braze 웹 SDK의 메서드를 호출하기 위해 JavaScript `brazeBridge` 인터페이스를 지원합니다. 자세한 내용은 <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/">모범 사례</a>를 참조하세요.

![콘텐츠 캐러셀과 대화형 버튼이 포함된 HTML 인앱 메시지입니다.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
현재 iOS 및 Android 플랫폼에서는 iFrame에 커스텀 HTML 인앱 메시지를 표시하는 기능을 지원하지 않습니다.
{% endalert %} 

{% endtab %}
{% endtabs %}

#### 사용자 지정 인앱 메시지 유형 정의

`slideup` 인앱 메시지 오브젝트는 [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html)를 확장합니다.
`full` 및 `modal` 유형 메시지는 [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html)를 확장합니다. 이러한 클래스 중 하나를 확장하면 로컬에서 생성된 인앱 메시지에 사용자 지정 기능을 추가할 수 있습니다.

## 통합 {#in-app-messaging-integration}

### 1단계: Braze 인앱 메시지 관리자 등록

인앱 메시지 표시는 [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html) 클래스에 의해 관리됩니다. 앱의 모든 활동을 `BrazeInAppMessageManager`에 등록해야 인앱 메시지 보기를 보기 계층 구조에 추가할 수 있습니다. 이를 달성하는 방법에는 두 가지가 있습니다:

#### 활동 수명 주기 콜백 통합(권장)

[활동 수명 주기 콜백 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android)은 인앱 메시지 등록을 자동으로 처리하므로 추가 통합이 필요하지 않습니다. 인앱 메시지 등록을 처리하는 데 권장되는 통합입니다.

#### 수동 인앱 메시지 등록

{% alert warning %}
활동 수명 주기 통합을 수행한 경우 수동 인앱 메시지 통합을 수행해서는 *안 됩니다*.
{% endalert %}

먼저 [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())에서 [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html)를 호출합니다.

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context)
```

{% endtab %}
{% endtabs %}

다음으로, 인앱 메시지를 표시할 수 있는 모든 활동에서 [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html)를 해당 활동의 `onResume()`에서 호출해야 합니다.

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onResume() {
  super.onResume()
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

마지막으로, [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html)가 호출된 모든 활동에서 [`unregisterInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html)는 해당 활동의 `onPause()`에서 호출해야 합니다.

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onPause() {
  super.onPause();
  // Unregisters the BrazeInAppMessageManager for the current Activity.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onPause() {
  super.onPause()
  // Unregisters the BrazeInAppMessageManager.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

### 2단계: 인앱 메시지 관리자 차단 목록(선택 사항)

통합 시 앱의 특정 활동이 인앱 메시지를 표시하지 않도록 요구할 수 있습니다. [활동 수명 주기 콜백 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android)은 이를 쉽게 수행할 수 있는 방법을 제공합니다.

다음 샘플 코드에서는 인앱 메시지 등록 차단 목록에 두 가지 활동(`SplashActivity` 및 `SettingsActivity`)을 추가합니다.

{% tabs %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    Set<Class> inAppMessageBlocklist = new HashSet<>();
    inAppMessageBlocklist.add(SplashActivity.class);
    inAppMessageBlocklist.add(SettingsActivity.class);
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(inAppMessageBlocklist));
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    val inAppMessageBlocklist = HashSet<Class<*>>()
    inAppMessageBlocklist.add(SplashActivity::class.java)
    inAppMessageBlocklist.add(SettingsActivity::class.java)
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(inAppMessageBlocklist))
  }
}
```

{% endtab %}
{% endtabs %}


