{% multi_lang_include developer_guide/prerequisites/android.md %} 또한 [인앱 메시지를 설정해야]({{site.baseurl}}/developer_guide/in_app_messages) 합니다.

## 커스텀 매니저 리스너 설정하기

{% tabs %}
{% tab 글로벌 리스너 %}
`BrazeInAppMessageManager` 리스너는 인앱 메시지의 표시 및 생애주기를 자동으로 처리할 수 있지만, 메시지를 완전히 커스텀하려면 커스텀 매니저 리스너를 구현해야 합니다.
{% endtab %}

{% tab HTML 리스너 %}
Braze SDK에는 커스텀 리스너가 정의되어 있지 않은 경우 사용되는 기본 `DefaultHtmlInAppMessageActionListener` 클래스가 있으며 자동으로 적절한 조치가 수행됩니다. 사용자 지정 HTML 인앱 메시지 내에서 사용자가 다른 버튼과 상호 작용하는 방식을 더 잘 제어해야 하는 경우 사용자 지정 `IHtmlInAppMessageActionListener` 클래스를 구현하세요.
{% endtab %}
{% endtabs %}

### 1단계: 커스텀 매니저 리스너 구현하기

{% tabs %}
{% tab 글로벌 리스너 %}
#### 1.1단계: 구현 `IInAppMessageManagerListener` 

[`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html)를 구현하는 클래스를 생성합니다.

`IInAppMessageManagerListener` 의 콜백은 인앱 메시지 라이프사이클의 다양한 지점에서 호출됩니다. 예를 들어, Braze에서 인앱 메시지를 수신할 때 커스텀 매니저 리스너를 설정하면 [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html) 메서드가 호출됩니다. 이 메서드의 구현이 [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html)를 반환하면, 인앱 메시지가 호스트 앱에서 처리되며 Braze에서 표시해서는 안 됨을 Braze에 알립니다. 가 반환되면 [`InAppMessageOperation.DISPLAY_NOW`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-p-l-a-y_-n-o-w/index.html) 가 반환되면 Braze는 인앱 메시지를 표시하려고 시도합니다. 이 방법은 인앱 메시지를 사용자 지정 방식으로 표시하도록 선택한 경우에 사용해야 합니다.

`IInAppMessageManagerListener` 에는 메시지 클릭 및 버튼에 대한 델리게이트 메서드도 포함되어 있어 추가 처리를 위해 버튼이나 메시지를 클릭할 때 메시지를 가로채는 등의 경우에 사용할 수 있습니다.

#### 1.2단계: IAM 보기 수명 주기 메서드에 연결(선택 사항)

[`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) 인터페이스에는 인앱 메시지 보기 생애주기의 특정 지점에서 호출되는 인앱 메시지 보기 메서드가 있습니다. 이러한 메서드는 다음 순서로 호출됩니다:

1. [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html): 인앱 메시지가 활동의 보기에 추가되기 직전에 호출됩니다. 현재 인앱 메시지는 아직 사용자에게 표시되지 않습니다.
2. [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html): 인앱 메시지가 활동의 보기에 추가된 직후에 호출됩니다. 이제 인앱 메시지가 사용자에게 표시됩니다.
3. [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html): 인앱 메시지가 활동의 보기에서 제거되기 직전에 호출됩니다. 현재 인앱 메시지는 사용자에게 계속 표시됩니다.
4. [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html): 인앱 메시지가 활동 보기에서 제거된 직후에 호출됩니다. 현재 인앱 메시지는 더 이상 사용자에게 표시되지 않습니다.

사이의 시간은 [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) 과 [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) 사이의 시간은 인앱 메시지 보기가 화면에 표시되어 사용자에게 보이는 시간입니다.

{% alert note %}
이러한 방법을 구현할 필요는 없습니다. 인앱 메시지 보기 라이프사이클을 추적하고 알리기 위해서만 제공됩니다. 이러한 메서드 구현은 비워둘 수 있습니다.
{% endalert %}
{% endtab %}

{% tab HTML 리스너 %}
[`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html)를 구현하는 클래스를 생성합니다.

`IHtmlInAppMessageActionListener`의 콜백은 사용자가 HTML 인앱 메시지 내에서 다음 작업 중 하나를 시작할 때마다 호출됩니다.

- 닫기 버튼을 클릭합니다.
- 사용자 지정 이벤트를 실행합니다.
- HTML 인앱 메시지 내의 URL을 클릭합니다.

{% subtabs %}
{% subtab JAVA %}
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
  public boolean onOtherUrlAction(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom url pressed: " + url + " . Ignoring", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }
}
```
{% endsubtab %}
{% subtab KOTLIN %}
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

    override fun onOtherUrlAction(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom url pressed: $url . Ignoring", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 2단계: Braze에 커스텀 매니저 리스너를 사용하도록 지시하세요.

{% tabs %}
{% tab 글로벌 리스너 %}
`IInAppMessageManagerListener` 를 만든 후 `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` 으로 전화하여 지시하세요. `BrazeInAppMessageManager`
기본 리스너 대신 커스텀 `IInAppMessageManagerListener`를 사용하도록 지시합니다. 이 작업을 수행하면 [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) 를 호출하여 인앱 메시지가 표시되기 전에 커스텀 리스너가 설정되도록 합니다.

#### 표시 전 인앱 메시지 변경하기

새 인앱 메시지가 수신될 때 이미 표시 중인 인앱 메시지가 있는 경우 새 메시지가 스택 맨 위에 배치되고 나중에 표시될 수 있습니다.

그러나 인앱 메시지가 표시되지 않으면 `IInAppMessageManagerListener`의 다음 위임 메서드가 호출됩니다.

{% subtabs %}
{% subtab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endsubtab %}
{% endsubtabs %}

`InAppMessageOperation()` 반환 값은 메시지 표시 시기를 제어할 수 있습니다. 제안된 방색으로 이 메서드를 사용하면 인앱 메시지가 사용자의 앱 경험을 방해할 경우 `DISPLAY_LATER`를 반환하여 앱의 특정 부분에서 메시지를 지연시킬 수 있습니다.

| `InAppMessageOperation` 반환 값 | 동작 |
| -------------------------- | -------- |
| `DISPLAY_NOW` | 메시지가 표시됩니다. |
| `DISPLAY_LATER` | 메시지는 스택으로 반환되어 다음 사용 가능한 기회에 표시됩니다. |
| `DISCARD` | 메시지가 삭제됩니다. |
| `null` | 메시지는 무시됩니다. 이 메서드는 `null`을 반환하지 **않아야** 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

자세한 내용은 [`InAppMessageOperation`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html)를 참조하세요.

{% alert tip %}
인앱 메시지에 대해 `DISCARD`를 선택하고 인앱 메시지 보기로 대체하는 경우 인앱 메시지 클릭 및 노출 횟수를 수동으로 기록해야 합니다.
{% endalert %}

Android에서는 인앱 메시지에서 `logClick` 및 `logImpression`을 호출하고 몰입형 인앱 메시지에서 `logButtonClick`을 호출하면 됩니다.

{% alert tip %}
인앱 메시지가 스택에 배치되면 언제든지 [`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html)를 호출하여 검색 및 표시를 요청할 수 있습니다. 이 메서드는 스택에서 사용 가능한 다음 인앱 메시지를 표시하도록 Braze에 요청합니다.
{% endalert %}
{% endtab %}

{% tab HTML 리스너 %}
`IHtmlInAppMessageActionListener` 을 만든 후 `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` 으로 전화하여 `BrazeInAppMessageManager` 에 기본값 대신 커스텀 작업 리스너 `IHtmlInAppMessageActionListener` 를 사용하도록 지시합니다.

Braze에 대한 다른 호출을 수행하기 전에 [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())에서 `IHtmlInAppMessageActionListener`를 설정하는 것이 좋습니다. 이렇게 하면 인앱 메시지가 표시되기 전에 사용자 지정 동작 리스너가 설정됩니다:

{% subtabs %}
{% subtab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(new CustomHtmlInAppMessageActionListener(context));
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(CustomHtmlInAppMessageActionListener(context))
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 커스텀 공장 설정하기

커스텀 팩토리 오브젝트를 통해 여러 기본값을 재정의할 수 있습니다. 원하는 결과를 얻기 위해 필요한 경우 Braze SDK에 등록할 수 있습니다. 그러나 팩토리를 재정의하려면 기본값을 명시적으로 재정의하거나 Braze 기본값에서 제공하는 기능을 다시 구현해야 할 수 있습니다. 다음 코드 스니펫은 `IInAppMessageViewFactory` 및 `IInAppMessageViewWrapperFactory` 인터페이스의 커스텀 구현을 제공하는 방법을 보여줍니다.

{% tabs local %}
{% tab Kotlin %}
**인앱 메시지 유형**<br>

```kotlin
class BrazeDemoApplication : Application(){
 override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(true, true))
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(CustomInAppMessageViewFactory())
  }
}
```
{% endtab %}
{% tab Java %}
**인앱 메시지 유형**<br> 

```java
public class BrazeDemoApplication extends Application {
  @Override
  public void onCreate{
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(true, true));
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(new CustomInAppMessageViewFactory());
  }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab 보기 %}
Braze 인앱 메시지 유형은 대부분의 커스텀 사용 사례를 포괄할 수 있을 만큼 유용합니다. 그러나 기본 유형을 사용하는 대신 인앱 메시지의 시각적 모양을 완전히 정의하고 싶다면 Braze에서 커스텀 보기 팩토리를 설정하면 됩니다.
{% endtab %}

{% tab 래퍼 보기 %}
`BrazeInAppMessageManager`는 기본적으로 [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html)를 사용하여 인앱 메시지 모델을 기존 활동 보기 계층 구조에 배치하는 작업을 자동으로 처리합니다. 인앱 메시지가 보기 계층 구조에 배치되는 방식을 사용자 지정해야 하는 경우 커스텀 [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html)를 사용해야 합니다.
{% endtab %}

{% tab 애니메이션 %}
인앱 메시지에는 사전 설정된 애니메이션 동작이 있습니다. `Slideup` 메시지는 화면에서 슬라이드되고 `full` 및 `modal` 메시지는 페이드 인 및 페이드 아웃 처리됩니다. 인앱 메시지에 대한 커스텀 애니메이션 동작을 정의하려는 경우, Braze에서 커스텀 애니메이션 팩토리를 설정하면 됩니다.
{% endtab %}
{% endtabs %}

### 1단계: 공장 구현

{% tabs %}
{% tab 보기 %}
[`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html)를 구현하는 클래스를 생성합니다.

{% subtabs %}
{% subtab JAVA %}
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
{% endsubtab %}
{% subtab KOTLIN %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 래퍼 보기 %}
[`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html)를 구현하고 [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html)를 반환하는 클래스를 생성합니다.

이 팩토리는 인앱 메시지 보기가 생성된 직후에 호출됩니다. 커스텀 [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html)를 구현하는 가장 쉬운 방법은 기본 [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html)를 확장하는 것입니다.

{% subtabs %}
{% subtab JAVA %}
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
{% endsubtab %}
{% subtab KOTLIN %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 애니메이션 %}
[`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html)를 구현하는 클래스를 생성합니다.

{% subtabs %}
{% subtab JAVA %}
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
{% endsubtab %}
{% subtab KOTLIN %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 2단계: Braze에게 공장 사용 지시하기

{% tabs %}
{% tab 보기 %}
`IInAppMessageViewFactory` 을 생성한 후 `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` 으로 전화하여 다음과 같이 지시하세요. `BrazeInAppMessageManager`
기본 보기 팩토리 대신 커스텀 `IInAppMessageViewFactory`를 사용하도록 지시합니다.

{% alert tip %}
Braze에 대한 다른 호출을 수행하기 전에 `Application.onCreate()`에서 `IInAppMessageViewFactory`를 설정하는 것이 좋습니다. 그러면 인앱 메시지가 표시되기 전에 커스텀 보기 팩토리가 설정됩니다.
{% endalert %}

#### 작동 방식

`slideup` 인앱 메시지 보기는 [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html)를 구현합니다. `full` 및 `modal` 유형 메시지 보기는 [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html)를 구현합니다. 이러한 클래스 중 하나를 구현하면 Braze가 해당되는 경우 커스텀 보기에 클릭 리스너를 추가할 수 있습니다. 모든 Braze 뷰 클래스는 안드로이드의 [`View`](http://developer.android.com/reference/android/view/View.html) 클래스를 확장합니다.

`IInAppMessageView`를 구현하면 커스텀 보기의 특정 부분을 클릭 가능한 요소로 정의할 수 있습니다. [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html)를 구현하면 메시지 버튼 보기와 닫기 버튼 보기를 정의할 수 있습니다.
{% endtab %}

{% tab 래퍼 보기 %}
가 생성된 후 [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) 가 생성된 후 [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) 을 호출하여 `BrazeInAppMessageManager` 에 기본 뷰 래퍼 팩토리 대신 커스텀을 사용하도록 지시합니다. [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) 기본값인 뷰 래퍼 팩토리 대신 사용하도록 지시합니다.

Braze에 대한 다른 호출을 수행하기 전에 [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())에서 [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html)를 설정하는 것이 좋습니다. 이렇게 하면 인앱 메시지가 표시되기 전에 사용자 지정 보기 래퍼 팩토리가 설정됩니다:

{% subtabs %}
{% subtab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapper());
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapper())
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 애니메이션 %}
`IInAppMessageAnimationFactory`가 생성되면 `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()`를 호출하여 `BrazeInAppMessageManager`에
기본 애니메이션 팩토리 대신 커스텀 `IInAppMessageAnimationFactory`를 사용하도록 지시합니다.

Braze에 대한 다른 호출을 수행하기 전에 [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())에서 `IInAppMessageAnimationFactory`를 설정하는 것이 좋습니다. 그러면 인앱 메시지가 표시되기 전에 커스텀 애니메이션 팩토리가 설정됩니다.
{% endtab %}
{% endtabs %}

## 커스텀 스타일

Braze UI 요소는 Android 표준 UI 지침과 일치하는 기본 모양과 느낌으로 제공되며 원활한 경험을 제공합니다. 이 참조 문서에서는 Android 또는 FireOS 애플리케이션의 커스텀 인앱 메시징 스타일을 다룹니다.

### 기본값 스타일 설정하기

기본 스타일은 Braze SDK의 [`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) 파일에서 확인할 수 있습니다:

```xml
  <style name="Braze"/>
  <style name="Braze.InAppMessage"/>
  <style name="Braze.InAppMessage.Header">
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:padding">0.0dp</item>
    <item name="android:background">@android:color/transparent</item>
    <item name="android:textColor">@color/com_braze_inappmessage_header_text</item>
    <item name="android:textSize">20.0sp</item>
    <item name="android:lineSpacingMultiplier">1.3</item>
    <item name="android:gravity">center</item>
    <item name="android:textStyle">bold</item>
    <item name="android:layout_centerHorizontal">true</item>
  </style>
```

원하는 경우 이러한 스타일을 재정의하여 앱에 더 적합한 모양과 느낌을 만들 수 있습니다.

스타일을 재정의하려면 프로젝트의 `styles.xml` 파일에 전체 스타일을 복사한 후 수정합니다. 모든 속성을 올바르게 설정하려면 전체 스타일을 로컬 `styles.xml` 파일에 복사해야 합니다. 이러한 커스텀 스타일은 레이아웃을 일괄적으로 변경하는 것이 아니라 개별 UI 요소를 변경하기 위한 기능입니다. 레이아웃 수준 변경은 사용자 지정 보기로 처리해야 합니다.

{% alert note %}
XML을 수정하지 않고도 Braze 캠페인에서 직접 일부 색상을 사용자 지정할 수 있습니다. Braze 대시보드에서 설정한 색상은 다른 곳에서 설정한 색상보다 우선한다는 점을 기억하세요.
{% endalert %}

### 글꼴 커스텀하기

`res/font` 디렉토리에서 서체를 찾아 커스텀 글꼴을 설정할 수 있습니다. 이를 사용하려면 메시지 텍스트, 헤더 및 버튼 텍스트의 스타일을 재정의하고 `fontFamily` 속성을 사용하여 사용자 지정 폰트 패밀리를 사용하도록 Braze에 지시하세요.

예를 들어 인앱 메시지 버튼 텍스트의 글꼴을 업데이트하려면 `Braze.InAppMessage.Button` 스타일을 재정의하고 커스텀 글꼴 패밀리를 참조합니다. 속성 값은 `res/font` 디렉터리에 있는 글꼴 패밀리를 가리켜야 합니다.

다음은 마지막 줄에 참조된 사용자 정의 글꼴 모음( `my_custom_font_family`)을 사용한 잘린 예제입니다:

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

버튼 텍스트의 스타일은 `Braze.InAppMessage.Button`이며, 메시지 텍스트의 스타일은 `Braze.InAppMessage.Message`이고, 메시지 헤더의 스타일은 `Braze.InAppMessage.Header`입니다. 가능한 모든 인앱 메시지 텍스트에 커스텀 글꼴 패밀리를 사용하려면 모든 인앱 메시지의 상위 스타일인 `Braze.InAppMessage` 스타일에서 글꼴 패밀리를 설정하면 됩니다.

{% alert important %}
다른 사용자 정의 스타일과 마찬가지로 모든 속성을 올바르게 설정하려면 전체 스타일을 로컬 `styles.xml` 파일에 복사해야 합니다.
{% endalert %}

## 메시지 해고

### 뒤로 버튼 해고 비활성화하기

기본적으로 하드웨어의 뒤로 버튼은 Braze 인앱 메시지를 해제합니다. 이 동작은 메시지별로 [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html)를 통해 비활성화할 수 있습니다. 

다음 예제에서 `disable_back_button`은 인앱 메시지에 설정된 커스텀 키-값 페어로, 메시지에서 뒤로 버튼을 사용하여 메시지를 해제할 것인지 여부를 나타냅니다.

{% tabs %}
{% tab 자바 %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(new DefaultInAppMessageManagerListener() {
  @Override
  public void beforeInAppMessageViewOpened(View inAppMessageView, IInAppMessage inAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage);
    final Map<String, String> extras = inAppMessage.getExtras();
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false);
    }
  }

  @Override
  public void afterInAppMessageViewClosed(IInAppMessage inAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage);
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true);
  }
});
```
{% endtab %}
{% tab 코틀린 %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : DefaultInAppMessageManagerListener() {
  override fun beforeInAppMessageViewOpened(inAppMessageView: View, inAppMessage: IInAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage)
    val extras = inAppMessage.extras
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false)
    }
  }

  override fun afterInAppMessageViewClosed(inAppMessage: IInAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage)
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true)
  }
})
```
{% endtab %}
{% endtabs %}

{% alert note %}
이 기능을 비활성화하면 호스트 활동의 하드웨어 뒤로 가기 버튼 기본 동작이 대신 사용됩니다. 이 경우 표시되는 인앱 메시지 대신 뒤로 버튼으로 애플리케이션을 닫을 수 있습니다.
{% endalert %}

### 외부 탭 해고 인에이블먼트

기본적으로 외부 탭을 사용하여 모달을 해제하는 기본값은 `false` 으로 설정되어 있습니다. 이 값을 `true`로 설정하면 사용자가 인앱 메시지 외부를 탭할 때 Modal 인앱 메시지가 해제됩니다. 이 동작은 호출을 통해 토글할 수 있습니다.

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

## 오리엔테이션 커스텀하기

인앱 메시지의 고정 방향을 설정하려면 먼저 [커스텀 인앱 메시지 관리자 리스너]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners)를 설정합니다. 그런 다음 `beforeInAppMessageDisplayed()` 델리게이트 메서드에서 `IInAppMessage` 객체의 오리엔테이션을 업데이트합니다:

{% tabs %}
{% tab 자바 %}
```java
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Set the orientation to portrait
  inAppMessage.setOrientation(Orientation.PORTRAIT);
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab 코틀린 %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  // Set the orientation to portrait
  inAppMessage.orientation = Orientation.PORTRAIT
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

태블릿 기기의 경우 인앱 메시지는 실제 화면 방향과 관계없이 사용자가 선호하는 방향 스타일로 표시됩니다.

## 어두운 테마 비활성화하기 {#android-in-app-message-dark-theme-customization}

기본값은 `IInAppMessageManagerListener` 의 `beforeInAppMessageDisplayed()` 에서 시스템 설정을 확인하고 다음 코드를 사용하여 메시징에 어두운 테마 스타일링을 조건부로 인에이블먼트합니다:

{% tabs %}
{% tab 자바 %}
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
{% tab 코틀린 %}
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

이를 변경하려면 사전 표시 프로세스의 어느 단계에서든 [`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html) 을 호출하여 고유한 조건 로직을 구현할 수 있습니다.

## Google Play 리뷰 프롬프트 커스텀하기

Google이 설정한 제한 사항으로 인해 현재 Braze에서는 커스텀 Google Play 리뷰 프롬프트를 지원하지 않습니다. 일부 사용자는 이러한 프롬프트를 성공적으로 통합할 수 있었지만, [Google Play 할당량](https://developer.android.com/guide/playcore/in-app-review#quotas)으로 인해 성공률이 낮은 사용자도 있습니다. 위험을 감수하고 통합해 보세요. [Google Play 인앱 리뷰 프롬프트](https://developer.android.com/guide/playcore/in-app-review)에 대한 설명서를 참조하십시오.
