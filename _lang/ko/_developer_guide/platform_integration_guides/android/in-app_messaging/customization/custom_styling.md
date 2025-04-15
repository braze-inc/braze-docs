---
nav_title: 사용자 지정 스타일
article_title: Android 및 FireOS용 인앱 메시지 사용자 지정 스타일링
platform: 
  - Android
  - FireOS
page_order: 2
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션의 커스텀 인앱 메시징 스타일을 다룹니다."
channel:
  - in-app messages

---

# 커스텀 스타일

> Braze UI 요소는 Android 표준 UI 지침과 일치하는 기본 모양과 느낌으로 제공되며 원활한 경험을 제공합니다. 이 참조 문서에서는 Android 또는 FireOS 애플리케이션의 커스텀 인앱 메시징 스타일을 다룹니다.

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

## 사용자 지정 글꼴

Braze에서는 [글꼴 패밀리 가이드를]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization) 사용하여 사용자 지정 글꼴을 설정할 수 있습니다. 이를 사용하려면 메시지 텍스트, 헤더 및 버튼 텍스트의 스타일을 재정의하고 `fontFamily` 속성을 사용하여 사용자 지정 폰트 패밀리를 사용하도록 Braze에 지시하세요.

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

## 고정 방향 설정

인앱 메시지의 고정 방향을 설정하려면 먼저 [커스텀 인앱 메시지 관리자 리스너]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/)를 설정합니다. 그런 다음, `beforeInAppMessageDisplayed()` 위임 메서드의 `IInAppMessage` 오브젝트에서 `setOrientation()`을 호출합니다.

{% tabs %}
{% tab JAVA %}
```java
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Set the orientation to portrait
  inAppMessage.setOrientation(Orientation.PORTRAIT);
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
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

