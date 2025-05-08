---
nav_title: 고급 구현 가이드 (선택 사항)
article_title: Android용 인앱 메시지 구현 가이드(선택 사항)
platform: Android
page_order: 6
description: "이 고급 구현 가이드에서는 Android 및 FireOS 인앱 메시지 코드 고려사항, 저희 팀이 구축한 세 가지 사용 사례 및 관련 코드 스니펫을 다룹니다."
channel:
  - in-app messages
---
<br>
{% alert important %}
기본 인앱 메시지 개발자 통합 가이드를 찾고 계신가요? 여기에서 확인하세요[참조: ]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/#in-app-messaging-integration).
{% endalert %}

# 고급 구현 가이드

> 이 고급 구현 가이드(선택 사항)에서는 인앱 메시지 코드 고려사항, 저희 팀이 구축한 세 가지 커스텀 사용 사례 및 관련 코드 스니펫을 다룹니다. [여기](https://github.com/braze-inc/braze-growth-shares-android-demo-app)에서 Braze 데모 리포지토리를 확인하세요! 이 구현 가이드는 Kotlin 구현을 중심으로 하지만 관심 있는 사람을 위해 Java 스니펫도 제공됩니다. HTML 구현을 찾고 계신가요? [HTML 템플릿 리포지토리를](https://github.com/braze-inc/in-app-message-templates) 살펴보세요!

## 코드 고려 사항

다음 가이드에서는 기본 인앱 메시지 외에 사용할 수 있는 사용자 지정 개발자 통합 옵션에 대해 설명합니다. 커스텀 보기 구성요소 및 팩토리는 필요한 경우 각 사용 사례에 포함되어 기능을 확장하고 인앱 메시지의 모양과 느낌을 기본적으로 사용자 지정하는 예제를 제공합니다. 경우에 따라 비슷한 결과를 얻을 수 있는 여러 가지 방법이 있습니다. 최적의 구현은 특정 사용 사례에 따라 달라집니다.

### 커스텀 팩토리

Braze SDK를 사용하면 개발자는 커스텀 팩토리 오브젝트를 통해 여러 기본값을 재정의할 수 있습니다. 원하는 결과를 얻기 위해 필요한 경우 Braze SDK에 등록할 수 있습니다. 그러나 대부분의 경우 팩토리를 재정의하려면 기본값을 명시적으로 지연하거나 Braze 기본값에서 제공하는 기능을 다시 구현해야 합니다. 다음 코드 스니펫은 `IInAppMessageViewFactory` 및 `IInAppMessageViewWrapperFactory` 인터페이스의 커스텀 구현을 제공하는 방법을 보여줍니다. 기본 팩토리 재정의와 관련된 개념을 확실히 이해했다면 [사용 사례](#sample-use-cases)를 확인하여 커스텀 인앱 메시징 기능 구현을 시작하세요.

{% tabs %}
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

## 사용 사례

아래에 세 가지 사용 사례를 제공했습니다. 각 사용 사례는 코드 스니펫 및 Braze 대시보드에서 인앱 메시지의 모양과 느낌에 대한 인상을 제공합니다.
- [사용자 지정 슬라이드업 인앱 메시지](#custom-slideup-in-app-message)
- [커스텀 Modal 인앱 메시지](#custom-modal-in-app-message)
- [커스텀 전체 인앱 메시지](#custom-full-in-app-message)

### 사용자 지정 슬라이드업 인앱 메시지

슬라이드업 인앱 메시지를 작성하는 동안 기본 방법을 사용하여 메시지의 위치를 수정할 수 없다는 점을 알아차렸습니다. 이와 같은 수정은 `DefaultInAppMessageViewWrapper` 클래스를 서브클래스로 설정하여 레이아웃 매개변수를 조정하면 가능합니다. 수정된 `LayoutParams`를 커스텀 위치 지정 값으로 반환하는 `getLayoutParams` 메서드를 재정의하여 화면의 최종 위치를 조정할 수 있습니다. 시작하려면 [CustomSlideUpInAppMessageViewWrapper](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/slideup/CustomSlideUpInAppMessageViewWrapper.kt)를 참조하세요.

#### 사용자 지정 뷰 래퍼<br><br>

{% tabs %}
{% tab Kotlin %}
**사용자 정의 레이아웃 매개변수 재정의 및 반환**<br>
`getLayoutParams` 메서드 내에서 슈퍼클래스 메서드를 사용하여 인앱 메시지의 원본 `LayoutParameters` 에 액세스할 수 있습니다. 그런 다음, 원하는 대로 더하거나 빼서 위치를 조정할 수 있습니다.

```kotlin
class CustomSlideUpInAppMessageViewWrapper(inAppMessageView: View?,
                                           inAppMessage: IInAppMessage?,
                                           inAppMessageViewLifecycleListener: IInAppMessageViewLifecycleListener?,
                                           configurationProvider: BrazeConfigurationProvider?,
                                           openingAnimation: Animation?,
                                           closingAnimation: Animation?,
                                           clickableInAppMessageView: View?) : DefaultInAppMessageViewWrapper(inAppMessageView,
    inAppMessage,
    inAppMessageViewLifecycleListener,
    configurationProvider,
    openingAnimation,
    closingAnimation,
    clickableInAppMessageView) {

    override fun getLayoutParams(inAppMessage: IInAppMessage?): ViewGroup.LayoutParams {
        val params = super.getLayoutParams(inAppMessage) as FrameLayout.LayoutParams
        params.bottomMargin = params.bottomMargin + 500 //move the view up by 500 pixels
        return params
    }
}
```
{% endtab %}
{% tab Java %}
**사용자 정의 레이아웃 매개변수 재정의 및 반환**<br>
`getLayoutParams` 메서드 내에서 슈퍼클래스 메서드를 사용하여 인앱 메시지의 원본 `LayoutParameters` 에 액세스할 수 있습니다. 그런 다음, 원하는 대로 더하거나 빼서 위치를 조정할 수 있습니다.

```java
class CustomSlideUpInAppMessageViewWrapper extends DefaultInAppMessageViewWrapper {

    public CustomInAppMessageViewWrapper(View inAppMessageView,
                                           IInAppMessage inAppMessage,
                                           IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener,
                                           BrazeConfigurationProvider configurationProvider,
                                           Animation openingAnimation,
                                           Animation closingAnimation,
                                           View clickableInAppMessageView){
        super(inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView)

    }
    
    @Override
    public ViewGroup.LayoutParams getLayoutParams(IInAppMessage inAppMessage){
        FrameLayout.LayoutParams params = (FrameLayout.LayoutParams)super.getLayoutParams(inAppMessage)
        params.bottomMargin = params.bottomMargin + 500 //move the view up by 500 pixels
        return params
    }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
**커스텀 팩토리를 제공하여 커스텀 래퍼 반환**<br>
Braze SDK에서 커스텀 래퍼를 사용하려면 커스텀 래퍼를 반환하는 커스텀 `IInAppMessageViewWrapperFactory` 구현도 제공해야 합니다. `IInAppMessageViewWrapperFactory`를 직접 구현하거나 `BrazeInAppMessageViewWrapperFactory` 서브클래스를 구현하고 `createInAppMessageViewWrapper` 메서드만 재정의할 수 있습니다.

```kotlin
class CustomInAppMessageViewWrapperFactory : BrazeInAppMessageViewWrapperFactory() {

    override fun createInAppMessageViewWrapper(
        inAppMessageView: View?,
        inAppMessage: IInAppMessage?,
        inAppMessageViewLifecycleListener: IInAppMessageViewLifecycleListener?,
        configurationProvider: BrazeConfigurationProvider?,
        openingAnimation: Animation?,
        closingAnimation: Animation?,
        clickableInAppMessageView: View?
    ): IInAppMessageViewWrapper {
        return if (inAppMessage is InAppMessageSlideup) {
            CustomSlideUpInAppMessageViewWrapper( //return our custom view wrapper only for slideups
                inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView
            )
        } else {
            super.createInAppMessageViewWrapper( //defer to the default implementation for all other IAM types
                inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView
            )
        }
    }
}
```
{% endtab %}
{% tab Java %}
**커스텀 팩토리를 제공하여 커스텀 래퍼 반환**<br>
Braze SDK에서 커스텀 래퍼를 사용하려면 커스텀 래퍼를 반환하는 커스텀 `IInAppMessageViewWrapperFactory` 구현을 제공해야 합니다. `IInAppMessageViewWrapperFactory`를 직접 구현하거나 `BrazeInAppMessageViewWrapperFactory` 서브클래스를 구현하고 `createInAppMessageViewWrapper` 메서드만 재정의할 수 있습니다.

```java
class CustomInAppMessageViewWrapperFactory extends BrazeInAppMessageViewWrapperFactory {
    @Override
    public IInAppMessageViewWrapper createInAppMessageViewWrapper(View inAppMessageView, 
        IInAppMessage inAppMessage, 
        IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener, 
        BrazeConfigurationProvider configurationProvider, 
        Animation openingAnimation, 
        Animation closingAnimation, 
        View clickableInAppMessageView){
        if (inAppMessage instanceof InAppMessageSlideup){
            return new CustomSlideUpInAppMessageViewWrapper( //return our custom view wrapper only for slideups
                inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView);
        }else{
            return super.createInAppMessageViewWrapper(//defer to the default implementation for all other IAM types
                inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView);
        }
    }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
**Braze에 공장 등록하기**<br>
커스텀 래퍼 팩토리를 생성한 후에는 `BrazeInAppMessageManager`를 통해 Braze SDK에 등록합니다.

```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
```
{% endtab %}
{% tab Java %}
**Braze에 공장 등록하기**<br>
커스텀 래퍼 팩토리를 생성한 후에는 `BrazeInAppMessageManager`를 통해 Braze SDK에 등록합니다.

```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
```
{% endtab %}
{% endtabs %}

### 커스텀 Modal 인앱 메시지

소중한 사용자 속성을 수집하는 매력적인 방법을 제공하기 위해 `BrazeInAppMessageModalView`는 `Spinner`를 활용하여 서브클래스로 만들 수 있습니다. 다음 예는 커넥티드 콘텐츠를 사용하여 동적 항목 목록에서 사용자 지정 속성을 캡처하는 방법을 보여줍니다. 시작하려면 [`TeamPickerView`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/modal/TeamPickerView.kt)를 참조하세요.

{% tabs %}
{% tab Kotlin %}
**UI 표시 동작에 `view_type` 사용**<br>
`IInAppMessage` 오브젝트에는 `extras` 사전이 있습니다. 이 사전을 쿼리하여 `view_type` 키(있는 경우)를 찾고 올바른 보기 유형을 표시할 수 있습니다. 인앱 메시지는 메시지별로 구성되므로 커스텀 및 기본값 Modal 보기가 조화를 이룰 수 있습니다.

```kotlin
override fun createInAppMessageView(activity: Activity, inAppMessage: IInAppMessage): View {
  return when {
      inAppMessage.extras?.get("view_type") == "picker" -> {
          getCustomPickerView(activity, inAppMessage)
      }
      //...
      else -> {
          //Defer to default
          BrazeInAppMessageManager
              .getInstance()
              .getDefaultInAppMessageViewFactory(inAppMessage).createInAppMessageView(activity, inAppMessage)
      }
  }
}
```
{% endtab %}
{% tab Java %}
**UI 표시 동작에 `view_type` 사용**<br>
`IInAppMessage` 오브젝트에는 `extras` 사전이 있습니다. 이 사전을 쿼리하여 `view_type` 키(있는 경우)를 찾고 올바른 보기 유형을 표시할 수 있습니다. 인앱 메시지는 메시지별로 구성되므로 커스텀 및 기본값 Modal 보기가 조화를 이룰 수 있습니다.

```java
@Override
public View createInAppMessageView(Activity activity, IInAppMessage inAppMessage) {
    if("picker".equals(inAppMessage.getExtras().get("view_type"))){
        return getCustomPickerView(activity, inAppMessage);
    } else {
        //Defer to default
        BrazeInAppMessageManager
          .getInstance()
          .getDefaultInAppMessageViewFactory(inAppMessage)
          .createInAppMessageView(activity, inAppMessage);
    }
}
```
{% endtab %}
{% endtabs %}

**사용자 지정 보기 재정의 및 제공**<br>
표준 Modal 인앱 메시지를 모방하는 레이아웃을 제공합니다. 단, 보기를 루트 요소로 제공한 다음, 해당 레이아웃을 확장합니다. 
```xml
<com.braze.advancedsamples.inapp.modal.TeamPickerView xmlns:android="http://schemas.android.com/apk/res/android"
                                                      xmlns:tools="http://schemas.android.com/tools"
                                                      android:layout_width="match_parent"
                                                      android:layout_height="match_parent"
                                                      android:padding="0.0dp"
                                                      android:id="@+id/team_picker_view">
    <!-- ... -->
    <Spinner android:layout_width="match_parent" android:layout_height="wrap_content"
                     android:id="@+id/team_spinner"/>
    <!-- ... -->                                                      
</com.braze.advancedsamples.inapp.modal.TeamPickerView>
```

{% tabs %}
{% tab Kotlin %}
**뷰 부풀리기 및 사용자 지정**<br>
`Spinner` 구성요소를 다시 로드하기 전에 `inAppMessage` 메시지 변수가 문자열로 출력됩니다. 이 메시지를 올바르게 표시하려면 이 메시지의 형식이 항목 배열로 지정되어야 합니다. 예를 들어 `String.split(",")`을 사용하면 됩니다.

```kotlin
private fun getCustomView(activity: Activity, inAppMessage: IInAppMessage): TeamPickerView {
        val view = activity.layoutInflater.inflate(R.layout.team_picker_dialog, null) as TeamPickerView
        val teams = inAppMessage.message.split(",")
        view.setTeams(teams)
        return view
    }
```
{% endtab %}
{% tab Java %}
**뷰 부풀리기 및 사용자 지정**<br>
`Spinner` 컴포넌트를 다시 로드하기 전에 `inAppMessage` 메시지 변수가 _문자열로_ 출력됩니다. 이 메시지를 올바르게 표시하려면 이 메시지의 형식이 항목 배열로 지정되어야 합니다. 예를 들어 `String.split(",")`을 사용하면 됩니다.

```java
private TeamPickerView getCustomView(Activity activity, IInAppMessage inAppMessage) {
        TeamPickerView view = (TeamPickerView) activity.getLayoutInflater().inflate(R.layout.team_picker_dialog, null);
        String[] teams = inAppMessage.getMessage().split(",");
        view.setTeams(teams);
        return view
    }
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
**커스텀 속성 할당**<br>
보기 서브클래스를 사용하여 사용자가 제출을 누른 후 속성과 이에 대응하는 선택된 값을 Braze에 전달하고 `messageClickableView.performClick()`을 호출하여 인앱 메시지를 해제합니다.

```kotlin
    override fun onClick(v: View?) {
        val selectedTeam = spinner.selectedItem as String
        messageClickableView.performClick()
        Braze.getInstance(ctx).getCurrentUser { brazeUser ->
            brazeUser?.setCustomUserAttribute("FavoriteTeam", selectedTeam)
        }
    }
```
{% endtab %}
{% tab Java %}
**커스텀 속성 할당**<br>
보기 서브클래스를 사용하여 사용자가 제출을 누른 후 속성과 이에 대응하는 선택된 값을 Braze에 전달하고 `messageClickableView.performClick()`을 호출하여 인앱 메시지를 해제합니다.

```java
    @Override
    public void onClick(View v) {
        String selectedTeam = (String) spinner.getSelectedItem();
        messageClickableView.performClick();
        Braze.getInstance(ctx).getCurrentUser(brazeUser -> {
            brazeUser.setCustomUserAttribute("FavoriteTeam", selectedTeam);
        });
    }
```
{% endtab %}
{% endtabs %}

### 커스텀 전체 인앱 메시지
완전 맞춤형 몰입형(전체 화면) 인앱 메시지를 구현하려면 [맞춤형 모달 인앱 메시지](#custom-modal-in-app-message) 구현하기 섹션에 설명된 것과 유사한 접근 방식이 필요합니다. 하지만 이 경우에는 `BrazeInAppMessageFullView`를 확장하고 필요한 경우 사용자 지정합니다. 보기는 애플리케이션 UI 위에 표시되며, Android에서 보기는 기본적으로 투명합니다. 즉, 인앱 메시지가 뒤에 있는 콘텐츠를 가릴 수 있도록 배경을 정의해야 합니다. `BrazeInAppMessageFullView`를 확장하면 Braze SDK가 보기에서 터치 이벤트 가로채기를 처리하고 적절한 조치를 취합니다. 모달 예시와 마찬가지로 특정 컨트롤(예: `Switch` 컨트롤)에 대해 이 동작을 재정의하여 사용자로부터 피드백을 수집할 수 있습니다.

{% tabs %}
{% tab Kotlin %}
**UI 표시 동작에 `view_type` 사용**<br>
새로운 몰입형 사용자 지정을 위해 다른 `view_type`을 더 추가할 예정입니다. `createInAppMessageView` 메소드를 다시 참조하여 '스위치' UI에 대한 옵션을 추가합니다.

```kotlin
override fun createInAppMessageView(activity: Activity, inAppMessage: IInAppMessage): View {
    return when {
        inAppMessage.extras?.get("view_type") == "picker" -> {
            getCustomPickerView(activity, inAppMessage)
        }
        inAppMessage.extras?.get("view_type") == "switches" -> {
            getCustomImmersiveView(activity, inAppMessage) // new customization
        }
        else -> {
            //Defer to default
            BrazeInAppMessageManager
                .getInstance()
                .getDefaultInAppMessageViewFactory(inAppMessage).createInAppMessageView(activity, inAppMessage)
        }
    }
}
```
{% endtab %}
{% tab Java %}
**UI 표시 동작에 `view_type` 사용**<br>
새로운 몰입형 사용자 지정을 위해 다른 `view_type`을 더 추가할 예정입니다. `createInAppMessageView` 메소드를 다시 참조하여 '스위치' UI에 대한 옵션을 추가합니다.

```java
@Override
public View createInAppMessageView(Activity activity, IInAppMessage inAppMessage) {
    if("picker".equals(inAppMessage.getExtras().get("view_type"))){
        return getCustomPickerView(activity, inAppMessage);
    } else if ("switches".equals(inAppMessage.getExtras().get("view_type"))) {
        return getCustomImmersiveView(activity, inAppMessage); // new customization
    } else {
        //Defer to default
        BrazeInAppMessageManager
          .getInstance()
          .getDefaultInAppMessageViewFactory(inAppMessage)
          .createInAppMessageView(activity, inAppMessage);
    }
}
```
{% endtab %}
{% endtabs %}

**사용자 지정 보기 재정의 및 제공**<br>
표준 Modal 인앱 메시지를 모방하는 레이아웃을 제공합니다. 단, 보기를 루트 요소로 제공한 다음, 해당 레이아웃을 확장합니다. 
```xml
<?xml version="1.0" encoding="utf-8"?>
<com.braze.advancedsamples.immersive.CustomImmersiveInAppMessage
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
        android:layout_height="wrap_content">
    <!-- giving the parent layout a white backround color will obscure the app behind the IAM. You could also do this within your custom view -->
    <LinearLayout android:background="@color/white" android:layout_width="match_parent" android:layout_height="match_parent" android:gravity="center"> 
        <!-- ... -->
        <androidx.recyclerview.widget.RecyclerView android:layout_width="match_parent"
                                                       android:layout_height="wrap_content"
                                                       android:id="@+id/option_list"/>
        <!-- ... -->
    </LinearLayout>
</com.braze.advancedsamples.immersive.CustomImmersiveInAppMessage>
```

{% tabs %}
{% tab Kotlin %}
**뷰 부풀리기 및 사용자 지정**<br>
`RecyclerView` 컴포넌트에 대한 옵션을 설정하기 전에 `inAppMessage` 메시지 변수가 _문자열로_ 출력됩니다. 이 메시지를 올바르게 표시하려면 이 메시지의 형식이 항목 배열로 지정되어야 합니다. 예를 들어 `String.split(",")`을 사용하면 됩니다. `title` 및 `subtitle` 역시 `extras` 번들에서 추출됩니다.

```kotlin
private fun getCustomImmersiveView(activity: Activity, inAppMessage: IInAppMessage): CustomImmersiveInAppMessage{
    val view = activity.layoutInflater.inflate(R.layout.full_screen_iam, null) as CustomImmersiveInAppMessage
    val options = inAppMessage.message.split(",")
    view.setOptions(options)
    inAppMessage.extras?.get("title").let { view.setTitle(it) }
    inAppMessage.extras?.get("subtitle").let {view.setSubtitle(it) }
    return view
}
```
{% endtab %}
{% tab Java %}
**뷰 부풀리기 및 사용자 지정**<br>
`RecyclerView` 컴포넌트에 대한 옵션을 설정하기 전에 `inAppMessage` 메시지 변수가 _문자열로_ 출력됩니다. 이 메시지를 올바르게 표시하려면 이 메시지의 형식이 항목 배열로 지정되어야 합니다. 예를 들어 `String.split(",")`을 사용하면 됩니다. `title` 및 `subtitle` 역시 `extras` 번들에서 추출됩니다.

```java
private CustomImmersiveInAppMessage getCustomImmersiveView(Activity activity, IInAppMessage inAppMessage) {
    CustomImmersiveInAppMessage view = (CustomImmersiveInAppMessage) activity.layoutInflater.inflate(R.layout.full_screen_iam, null);
    String[] options = inAppMessage.message.split(",");
    view.setOptions(options);
    String title = inAppMessage.getExtras().get("title");
    view.setTitle(title);
    String subtitle = inAppMessage.getExtras().get("subtitle"); 
    view.setSubtitle(subtitle);
    return view;
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
**커스텀 속성 할당**<br>
보기 서브클래스를 사용하여 사용자가 스위치 중 하나를 토글한 후 관련 속성과 토글 상태를 Braze에 전달합니다.

```kotlin
fun logClick(value:String, checked:Boolean){
    Braze.getInstance(ctx).logCustomEvent("SwitchChanged", BrazeProperties())
}

inner class OptionViewHolder(item: View): RecyclerView.ViewHolder(item), View.OnClickListener{

    var value: String = ""

    override fun onClick(p0: View?) {
        if (p0 is Switch){
            val checked = p0.isChecked
            p0.isChecked = !p0.isChecked
            logClick(value, checked)
        }
    }
}
override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): OptionViewHolder {
    return OptionViewHolder(mInflater.inflate(R.layout.switch_cell, null))
}

override fun onBindViewHolder(holder: OptionViewHolder, position: Int) {
    holder.itemView.findViewById<TextView>(R.id.label).text = options[position]
    holder.value = options[position]
}
```
{% endtab %}
{% tab Java %}
**커스텀 속성 할당**<br>
보기 서브클래스를 사용하여 사용자가 스위치 중 하나를 토글한 후 관련 속성과 토글 상태를 Braze에 전달합니다.

```java
private void logClick(String value, boolean checked){
    Braze.getInstance(ctx).logCustomEvent("SwitchChanged", new BrazeProperties());
}

private class OptionViewHolder extends RecyclerView.ViewHolder, implements View.OnClickListener{

    private String value = "";

    public OptionViewHolder(View item){
        super(item);
    }

   
    @Override
    public void onClick(View view) {
        if (view instanceof Switch){
            Switch switchView = (Switch) view;
            boolean checked = switchView.isChecked;
            switchView.isChecked = !switchView.isChecked;
            logClick(value, checked)
        }
    }
}

@Override
public OptionViewHolder onCreateViewHolder(ViewGroup parent, Int viewType) {
    return new OptionViewHolder(mInflater.inflate(R.layout.switch_cell, null));
}

@Override
public void onBindViewHolder(OptionViewHolder holder, Int position) {
    ((TextView)holder.getItemView().findViewById(R.id.label)).setText(options.get(position));
    holder.value = options.get(position);
}
```
{% endtab %}
{% endtabs %}

#### 인앱 메시지 터치 가로채기
![설정 및 토글 행을 표시하는 안드로이드 기기입니다. 사용자 지정 보기가 버튼을 처리하며, 버튼 컨트롤 이외의 모든 터치는 앱 내 메시지에 의해 처리되어 해제됩니다.]({% image_buster /assets/img/iam_implementation_guide_android.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
인앱 메시지 터치를 가로채는 작업은 커스텀 전체 인앱 메시지 버튼이 올바르게 작동하도록 하는 데 매우 중요합니다. 기본적으로 모든 인앱 메시지 보기는 메시지에 `onClick` 리스너를 추가하므로 사용자는 버튼 없이 메시지를 해제할 수 있습니다. 커스텀 버튼과 같이 사용자 입력에 응답해야 하는 커스텀 컨트롤을 추가하는 경우 평소처럼 `onClick` 리스너를 보기에 등록할 수 있습니다. 커스텀 컨트롤 외부를 터치하면 평소와 같이 인앱 메시지가 해제되고, 커스텀 컨트롤에서 수신하는 터치는 `onClick` 리스너를 호출합니다. 

