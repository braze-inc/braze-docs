---
nav_title: 사용자 지정 리스너
article_title: Android 및 FireOS용 맞춤형 인앱 메시지 리스너
platform: 
  - Android
  - FireOS
page_order: 3
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션의 커스텀 인앱 메시징 리스너를 다룹니다."
channel:
  - in-app messages

---

# 커스텀 리스너

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션의 커스텀 인앱 메시징 리스너를 다룹니다.

커스텀 리스너로 인앱 메시지를 사용자 지정하기 전에 인앱 메시지 처리의 대부분을 처리하는 [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html)를 이해하는 것이 중요합니다. 인앱 메시지 통합 가이드의 [1단계]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/#step-1-braze-in-app-message-manager-registration)에서 설명한 대로 인앱 메시지가 제대로 작동하려면 인앱 메시지를 등록해야 합니다.

`BrazeInAppMessageManager` 는 Android에서 인앱 메시지 표시를 관리합니다. 여기에는 인앱 메시지의 생애주기 및 표시를 관리하는 데 도움이 되는 헬퍼 클래스 인스턴스가 포함되어 있습니다. 이러한 모든 클래스에는 표준 구현이 있으며 사용자 지정 클래스 정의는 완전히 선택 사항입니다. 그러나 이를 수행하면 인앱 메시지의 표시 및 동작에 대한 제어 수준을 한 단계 더 높일 수 있습니다. 이러한 사용자 지정 가능한 클래스에는 다음이 포함됩니다:

- [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) - [인앱 메시지 표시 및 동작을 사용자 지정 관리](#custom-manager-listener)
- [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) - [맞춤형 인앱 메시지 보기 구축](#custom-view-factory)
- [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html) - [사용자 지정 인앱 메시지 애니메이션 정의](#custom-animation-factory)
- [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html) - [HTML 인앱 메시지 표시 및 동작 사용자 지정 관리](#custom-html-in-app-message-action-listener)
- [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) - [인앱 메시지 보기 계층 구조 상호 작용 사용자 지정 관리](#custom-view-wrapper-factory)

{% alert note %}
이 문서에는 더 이상 사용되지 않는 뉴스피드에 대한 정보가 포함되어 있습니다. Braze는 뉴스피드 도구를 사용하는 고객에게 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요.
{% endalert %}

## 사용자 지정 관리자 리스너

`BrazeInAppMessageManager`는 인앱 메시지의 표시 및 생애주기를 자동으로 처리합니다. 메시지의 생애주기를 더 많이 제어해야 하는 경우 커스텀 매니저 수신기를 설정하면 인앱 메시지 생애주기의 다양한 지점에서 인앱 메시지 오브젝트를 수신하여 직접 표시를 처리하고, 추가 처리를 수행하며, 사용자 동작에 반응하고, 오브젝트의 [추가 항목]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/customization/key_value_pairs/)을 처리하는 등의 작업을 할 수 있습니다.

### 1단계: 인앱 메시지 관리자 리스너 구현하기

[`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html)를 구현하는 클래스를 생성합니다.

`IInAppMessageManagerListener`의 콜백은 인앱 메시지 생애주기의 다양한 지점에서 호출됩니다.

예를 들어, Braze에서 인앱 메시지를 수신할 때 커스텀 매니저 수신기를 설정하면 `beforeInAppMessageDisplayed()` 메서드가 호출됩니다. 이 메서드의 구현이 [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html#27659854%2FClasslikes%2F-1725759721)를 반환하면, 인앱 메시지가 호스트 앱에서 처리되며 Braze에서 표시해서는 안 됨을 Braze에 알립니다. `InAppMessageOperation.DISPLAY_NOW`가 반환되면 Braze는 인앱 메시지를 표시하려고 시도합니다. 이 방법은 인앱 메시지를 사용자 지정 방식으로 표시하도록 선택한 경우에 사용해야 합니다.

`IInAppMessageManagerListener`에는 메시지 자체 또는 버튼 중 하나를 클릭할 때 위임 메서드도 포함되어 있습니다. 일반적인 사용 사례는 추가 처리를 위해 버튼이나 메시지를 클릭할 때 메시지를 가로채는 것입니다.

### 2단계: 인앱 메시지 보기 수명 주기 메서드에 훅 연결(선택 사항)

[`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) 인터페이스에는 인앱 메시지 보기 생애주기의 특정 지점에서 호출되는 인앱 메시지 보기 메서드가 있습니다. 이러한 메서드는 다음 순서로 호출됩니다:

- [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html) - 인앱 메시지가 활동의 보기에 추가되기 직전에 호출됩니다. 현재 인앱 메시지는 아직 사용자에게 표시되지 않습니다.
- [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) - 인앱 메시지가 활동 보기에 추가된 직후에 호출됩니다. 이제 인앱 메시지가 사용자에게 표시됩니다.
- [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) - 인앱 메시지가 활동 보기에서 제거되기 직전에 호출됩니다. 현재 인앱 메시지는 사용자에게 계속 표시됩니다.
- [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html) - 인앱 메시지가 활동 보기에서 제거된 직후에 호출됩니다. 현재 인앱 메시지는 더 이상 사용자에게 표시되지 않습니다.

자세한 맥락을 위해 [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) 및 [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) 사이의 시간은 인앱 메시지 보기가 화면에 나타나 사용자에게 보이는 시간입니다.

{% alert note %}
이러한 방법을 구현할 필요는 없습니다. 단지 인앱 메시지 보기의 생애주기를 추적하고 알리기 위해 제공됩니다. 이러한 메서드 구현을 비워두는 것은 기능적으로 허용됩니다.
{% endalert %}

### 3단계: 앱 내 메시지 관리자 리스너를 사용하도록 Braze에 지시하세요.

`IInAppMessageManagerListener`가 생성되면 `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()`를 호출하여 `BrazeInAppMessageManager`에
기본 리스너 대신 커스텀 `IInAppMessageManagerListener`를 사용하도록 지시합니다.

Braze에 대한 다른 호출을 수행하기 전에 [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())에서 `IInAppMessageManagerListener`를 설정하는 것이 좋습니다. 이렇게 하면 인앱 메시지가 표시되기 전에 사용자 지정 리스너가 설정됩니다.

#### 표시 전 인앱 메시지 변경하기

새 인앱 메시지가 수신될 때 이미 표시 중인 인앱 메시지가 있는 경우 새 메시지가 스택 맨 위에 배치되고 나중에 표시될 수 있습니다.

그러나 인앱 메시지가 표시되지 않으면 `IInAppMessageManagerListener`의 다음 위임 메서드가 호출됩니다.

{% tabs %}
{% tab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessageBase) {
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessageBase: IInAppMessage): InAppMessageOperation {
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

`InAppMessageOperation()` 반환 값은 메시지 표시 시기를 제어할 수 있습니다. 제안된 방색으로 이 메서드를 사용하면 인앱 메시지가 사용자의 앱 경험을 방해할 경우 `DISPLAY_LATER`를 반환하여 앱의 특정 부분에서 메시지를 지연시킬 수 있습니다.

| `InAppMessageOperation` 반환 값 | 동작 |
| -------------------------- | -------- |
| `DISPLAY_NOW` | 메시지가 표시됩니다. |
| `DISPLAY_LATER` | 메시지는 스택으로 반환되어 다음 사용 가능한 기회에 표시됩니다. |
| `DISCARD` | 메시지가 삭제됩니다. |
| `null` | 메시지는 무시됩니다. 이 메서드는 `null`을 반환하지 **않아야** 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

자세한 내용은 [`InAppMessageOperation.java`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html)를 참조하세요.

{% alert tip %}
인앱 메시지에 대해 `DISCARD`를 선택하고 인앱 메시지 보기로 대체하는 경우 인앱 메시지 클릭 및 노출 횟수를 수동으로 기록해야 합니다.
{% endalert %}

Android에서는 인앱 메시지에서 `logClick` 및 `logImpression`을 호출하고 몰입형 인앱 메시지에서 `logButtonClick`을 호출하면 됩니다.

{% alert tip %}
인앱 메시지가 스택에 배치되면 언제든지 [`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html)를 호출하여 검색 및 표시를 요청할 수 있습니다. 이 메서드는 스택에서 사용 가능한 다음 인앱 메시지를 표시하도록 Braze에 요청합니다.
{% endalert %}

### 4단계: 어두운 테마 동작 사용자 지정(선택 사항) {#android-in-app-message-dark-theme-customization}

기본 `IInAppMessageManagerListener` 로직의 `beforeInAppMessageDisplayed()`에서 시스템 설정을 확인하고 다음 코드를 사용하여 메시지에서 다크 테마 스타일을 조건부로 활성화합니다.

{% tabs %}
{% tab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  if (inAppMessage instanceof IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(BrazeInAppMessageManager.getInstance().getApplicationContext())) {
    ((IInAppMessageThemeable) inAppMessage).enableDarkTheme();
  }
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  if (inAppMessage is IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(BrazeInAppMessageManager.getInstance().applicationContext!!)) {
    (inAppMessage as IInAppMessageThemeable).enableDarkTheme()
  }
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

고유한 조건 로직을 사용하려면 표시 전 프로세스 중 어느 단계에서든 [`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html)을 호출하면 됩니다.

## 커스텀 보기 팩토리

Braze 인앱 메시지 유형은 대부분의 커스텀 사용 사례를 포괄할 수 있을 만큼 유용합니다. 그러나 기본 유형을 사용하는 대신 인앱 메시지의 시각적 모양을 완전히 정의하고 싶다면 Braze에서 커스텀 보기 팩토리를 설정하면 됩니다.

### 1단계: 인앱 메시지 보기 팩토리 구현

[`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html)를 구현하는 클래스를 생성합니다.

{% tabs %}
{% tab JAVA %}
```java
public class CustomInAppMessageViewFactory implements IInAppMessageViewFactory {
  @Override
  public View createInAppMessageView(Activity activity, IInAppMessage inAppMessage) {
    // Uses a custom view for slideups, modals, and full in-app messages.
    // HTML in-app messages and any other types will use the Braze default in-app message view factories
    switch (inAppMessage.getMessageType()) {
      case SLIDEUP:
      case MODAL:
      case FULL:
        // Use a custom view of your choosing
        return createMyCustomInAppMessageView();
      default:
        // Use the default in-app message factories
        final IInAppMessageViewFactory defaultInAppMessageViewFactory = BrazeInAppMessageManager.getInstance().getDefaultInAppMessageViewFactory(inAppMessage);
        return defaultInAppMessageViewFactory.createInAppMessageView(activity, inAppMessage);
    }
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageViewFactory : IInAppMessageViewFactory {
  override fun createInAppMessageView(activity: Activity, inAppMessage: IInAppMessage): View {
    // Uses a custom view for slideups, modals, and full in-app messages.
    // HTML in-app messages and any other types will use the Braze default in-app message view factories
    when (inAppMessage.messageType) {
      MessageType.SLIDEUP, MessageType.MODAL, MessageType.FULL ->
        // Use a custom view of your choosing
        return createMyCustomInAppMessageView()
      else -> {
        // Use the default in-app message factories
        val defaultInAppMessageViewFactory = BrazeInAppMessageManager.getInstance().getDefaultInAppMessageViewFactory(inAppMessage)
        return defaultInAppMessageViewFactory!!.createInAppMessageView(activity, inAppMessage)
      }
    }
  }
}
```
{% endtab %}
{% endtabs %}

### 2단계: 인앱 메시지 보기 팩토리를 사용하도록 Braze에 지시

`IInAppMessageViewFactory`가 생성되면 `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()`를 호출하여 `BrazeInAppMessageManager`에
기본 보기 팩토리 대신 커스텀 `IInAppMessageViewFactory`를 사용하도록 지시합니다.

{% alert tip %}
Braze에 대한 다른 호출을 수행하기 전에 `Application.onCreate()`에서 `IInAppMessageViewFactory`를 설정하는 것이 좋습니다. 그러면 인앱 메시지가 표시되기 전에 커스텀 보기 팩토리가 설정됩니다.
{% endalert %}

#### Braze 보기 인터페이스 구현

`slideup` 인앱 메시지 보기는 [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html)를 구현합니다. `full` 및 `modal` 유형 메시지 보기는 [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html)를 구현합니다. 이러한 클래스 중 하나를 구현하면 Braze가 해당되는 경우 커스텀 보기에 클릭 리스너를 추가할 수 있습니다. 모든 Braze 뷰 클래스는 안드로이드의 [`View`](http://developer.android.com/reference/android/view/View.html) 클래스를 확장합니다.

`IInAppMessageView`를 구현하면 커스텀 보기의 특정 부분을 클릭 가능한 요소로 정의할 수 있습니다. [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html)를 구현하면 메시지 버튼 보기와 닫기 버튼 보기를 정의할 수 있습니다.

## 커스텀 애니메이션 팩토리

인앱 메시지에는 사전 설정된 애니메이션 동작이 있습니다. `Slideup` 메시지는 화면에서 슬라이드되고 `full` 및 `modal` 메시지는 페이드 인 및 페이드 아웃 처리됩니다. 인앱 메시지에 대한 커스텀 애니메이션 동작을 정의하려는 경우, Braze에서 커스텀 애니메이션 팩토리를 설정하면 됩니다.

### 1단계: 인앱 메시지 애니메이션 팩토리 구현하기

[`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html)를 구현하는 클래스를 생성합니다.

{% tabs %}
{% tab JAVA %}
```java
public class CustomInAppMessageAnimationFactory implements IInAppMessageAnimationFactory {

  @Override
  public Animation getOpeningAnimation(IInAppMessage inAppMessage) {
    Animation animation = new AlphaAnimation(0, 1);
    animation.setInterpolator(new AccelerateInterpolator());
    animation.setDuration(2000L);
    return animation;
  }

  @Override
  public Animation getClosingAnimation(IInAppMessage inAppMessage) {
    Animation animation = new AlphaAnimation(1, 0);
    animation.setInterpolator(new DecelerateInterpolator());
    animation.setDuration(2000L);
    return animation;
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageAnimationFactory : IInAppMessageAnimationFactory {
  override fun getOpeningAnimation(inAppMessage: IInAppMessage): Animation {
    val animation: Animation = AlphaAnimation(0, 1)
    animation.interpolator = AccelerateInterpolator()
    animation.duration = 2000L
    return animation
  }

  override fun getClosingAnimation(inAppMessage: IInAppMessage): Animation {
    val animation: Animation = AlphaAnimation(1, 0)
    animation.interpolator = DecelerateInterpolator()
    animation.duration = 2000L
    return animation
  }
}
```
{% endtab %}
{% endtabs %}

### 2단계: 인앱 메시지 보기 팩토리를 사용하도록 Braze에 지시

`IInAppMessageAnimationFactory`가 생성되면 `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()`를 호출하여 `BrazeInAppMessageManager`에
기본 애니메이션 팩토리 대신 커스텀 `IInAppMessageAnimationFactory`를 사용하도록 지시합니다.

Braze에 대한 다른 호출을 수행하기 전에 [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())에서 `IInAppMessageAnimationFactory`를 설정하는 것이 좋습니다. 그러면 인앱 메시지가 표시되기 전에 커스텀 애니메이션 팩토리가 설정됩니다.

## 사용자 지정 HTML 인앱 메시지 액션 리스너

Braze SDK에는 커스텀 리스너가 정의되어 있지 않은 경우 사용되는 기본 `DefaultHtmlInAppMessageActionListener` 클래스가 있으며 자동으로 적절한 조치가 수행됩니다. 사용자 지정 HTML 인앱 메시지 내에서 사용자가 다른 버튼과 상호 작용하는 방식을 더 잘 제어해야 하는 경우 사용자 지정 `IHtmlInAppMessageActionListener` 클래스를 구현하세요.

### 1단계: 사용자 지정 HTML 인앱 메시지 액션 리스너 구현하기

[`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html)를 구현하는 클래스를 생성합니다.

`IHtmlInAppMessageActionListener`의 콜백은 사용자가 HTML 인앱 메시지 내에서 다음 작업 중 하나를 시작할 때마다 호출됩니다.

- 닫기 버튼을 클릭합니다.
- 사용자 지정 이벤트를 실행합니다.
- HTML 인앱 메시지 내의 URL을 클릭합니다.

{% tabs %}
{% tab JAVA %}
```java
public class CustomHtmlInAppMessageActionListener implements IHtmlInAppMessageActionListener {
  private final Context mContext;

  public CustomHtmlInAppMessageActionListener(Context context) {
    mContext = context;
  }

  @Override
  public void onCloseClicked(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "HTML In App Message closed", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
  }

  @Override
  public boolean onCustomEventFired(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom event fired. Ignoring.", Toast.LENGTH_LONG).show();
    return true;
  }

  @Override
  public boolean onNewsfeedClicked(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Newsfeed button pressed. Ignoring.", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }

  @Override
  public boolean onOtherUrlAction(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom url pressed: " + url + " . Ignoring", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomHtmlInAppMessageActionListener(private val mContext: Context) : IHtmlInAppMessageActionListener {

    override fun onCloseClicked(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle) {
        Toast.makeText(mContext, "HTML In App Message closed", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
    }

    override fun onCustomEventFired(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom event fired. Ignoring.", Toast.LENGTH_LONG).show()
        return true
    }

    override fun onNewsfeedClicked(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Newsfeed button pressed. Ignoring.", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }

    override fun onOtherUrlAction(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom url pressed: $url . Ignoring", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }
}
```
{% endtab %}
{% endtabs %}

### 2단계: Braze가 HTML 인앱 메시지 액션 리스너를 사용하도록 지시하세요.

`IHtmlInAppMessageActionListener`가 생성되면 `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()`를 호출하여 `BrazeInAppMessageManager`에 기본 작업 리스너 대신 커스텀 `IHtmlInAppMessageActionListener`를 사용하도록 지시합니다.

Braze에 대한 다른 호출을 수행하기 전에 [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())에서 `IHtmlInAppMessageActionListener`를 설정하는 것이 좋습니다. 이렇게 하면 인앱 메시지가 표시되기 전에 사용자 지정 동작 리스너가 설정됩니다:

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(new CustomHtmlInAppMessageActionListener(context));
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(CustomHtmlInAppMessageActionListener(context))
```
{% endtab %}
{% endtabs %}

## 커스텀 보기 래퍼 팩토리

`BrazeInAppMessageManager`는 기본적으로 [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html)를 사용하여 인앱 메시지 모델을 기존 활동 보기 계층 구조에 배치하는 작업을 자동으로 처리합니다. 인앱 메시지가 보기 계층 구조에 배치되는 방식을 사용자 지정해야 하는 경우 커스텀 [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html)를 사용해야 합니다.

### 1단계: 인앱 메시지 보기 래퍼 팩토리 구현

[`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html)를 구현하고 [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html)를 반환하는 클래스를 생성합니다.

이 팩토리는 인앱 메시지 보기가 생성된 직후에 호출됩니다. 커스텀 [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html)를 구현하는 가장 쉬운 방법은 기본 [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html)를 확장하는 것입니다.

{% tabs %}
{% tab JAVA %}
```java
public class CustomInAppMessageViewWrapper extends DefaultInAppMessageViewWrapper {
  public CustomInAppMessageViewWrapper(View inAppMessageView,
                                       IInAppMessage inAppMessage,
                                       IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener,
                                       BrazeConfigurationProvider brazeConfigurationProvider,
                                       Animation openingAnimation,
                                       Animation closingAnimation, View clickableInAppMessageView) {
    super(inAppMessageView,
        inAppMessage,
        inAppMessageViewLifecycleListener,
        brazeConfigurationProvider,
        openingAnimation,
        closingAnimation,
        clickableInAppMessageView);
  }

  @Override
  public void open(@NonNull Activity activity) {
    super.open(activity);
    Toast.makeText(activity.getApplicationContext(), "Opened in-app message", Toast.LENGTH_SHORT).show();
  }

  @Override
  public void close() {
    super.close();
    Toast.makeText(mInAppMessageView.getContext().getApplicationContext(), "Closed in-app message", Toast.LENGTH_SHORT).show();
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageViewWrapper(inAppMessageView: View,
                                    inAppMessage: IInAppMessage,
                                    inAppMessageViewLifecycleListener: IInAppMessageViewLifecycleListener,
                                    brazeConfigurationProvider: BrazeConfigurationProvider,
                                    openingAnimation: Animation,
                                    closingAnimation: Animation, clickableInAppMessageView: View) : 
    DefaultInAppMessageViewWrapper(inAppMessageView, 
        inAppMessage, 
        inAppMessageViewLifecycleListener, 
        brazeConfigurationProvider, 
        openingAnimation, 
        closingAnimation, 
        clickableInAppMessageView) {

  override fun open(activity: Activity) {
    super.open(activity)
    Toast.makeText(activity.applicationContext, "Opened in-app message", Toast.LENGTH_SHORT).show()
  }

  override fun close() {
    super.close()
    Toast.makeText(mInAppMessageView.context.applicationContext, "Closed in-app message", Toast.LENGTH_SHORT).show()
  }
}
```
{% endtab %}
{% endtabs %}

### 2단계: 커스텀 보기 래퍼 팩토리를 사용하도록 Braze에 지시

[`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html)가 생성되면 [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html)를 호출하여 `BrazeInAppMessageManager`에 기본 보기 래퍼 팩토리 대신 커스텀 [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html)를 사용하도록 지시합니다.

Braze에 대한 다른 호출을 수행하기 전에 [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())에서 [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html)를 설정하는 것이 좋습니다. 이렇게 하면 인앱 메시지가 표시되기 전에 사용자 지정 보기 래퍼 팩토리가 설정됩니다:

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapper());
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapper())
```
{% endtab %}
{% endtabs %}

