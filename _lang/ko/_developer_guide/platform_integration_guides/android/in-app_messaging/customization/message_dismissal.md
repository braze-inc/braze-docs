---
nav_title: 메시지 삭제
article_title: Android 및 FireOS용 인앱 메시지 삭제
platform: 
  - Android
  - FireOS
page_order: 5
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션의 인앱 메시징 해제를 다룹니다."
channel:
  - in-app messages

---

# 메시지 삭제

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션의 인앱 메시징 해제를 다룹니다.

## 뒤로 버튼 해제 비활성화

기본적으로 하드웨어의 뒤로 버튼은 Braze 인앱 메시지를 해제합니다. 이 동작은 메시지별로 [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html)를 통해 비활성화할 수 있습니다. 

다음 예제에서 `disable_back_button`은 인앱 메시지에 설정된 커스텀 키-값 페어로, 메시지에서 뒤로 버튼을 사용하여 메시지를 해제할 것인지 여부를 나타냅니다.

{% tabs %}
{% tab JAVA %}
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
{% tab KOTLIN %}
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

## 외부 탭에서 모달 해제

기본값 및 기록 값은 `false`로, Modal 외부를 클릭해도 Modal이 닫히지 않습니다. 이 값을 `true`로 설정하면 사용자가 인앱 메시지 외부를 탭할 때 Modal 인앱 메시지가 해제됩니다. 이 동작은 호출을 통해 토글할 수 있습니다.

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

