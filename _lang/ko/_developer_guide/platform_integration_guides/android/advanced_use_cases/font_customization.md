---
nav_title: 글꼴 사용자 지정
article_title: Android 및 FireOS용 글꼴 사용자 지정
platform: 
  - Android
  - FireOS
page_order: 7
description: "이 참조 문서에서는 글꼴 패밀리 정의와 같은 글꼴 사용자 지정 옵션을 다루고 Android 또는 FireOS 애플리케이션 전체에서 이를 참조하는 방법을 보여줍니다."

---

# 글꼴 사용자 지정

> 이 참조 문서에서는 글꼴 패밀리 정의와 같은 글꼴 사용자 지정 옵션을 다루고 Android 또는 FireOS 애플리케이션 전체에서 이를 참조하는 방법을 보여줍니다.

Braze SDK의 글꼴은 [XML의 글꼴](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html)에 따라 AndroidX 라이브러리를 사용하여 XML을 통해 설정할 수 있습니다. 커스텀 글꼴을 Braze SDK에서 사용하려면 먼저 글꼴 패밀리를 생성해야 합니다.

## 글꼴 패밀리 만들기

다음은 [글꼴 패밀리 가이드를](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html#font-family) 사용한 사용자 정의 글꼴 패밀리 정의 예시입니다. 이 예제에서는 [Bungee Shade 글꼴](https://fonts.google.com/specimen/Bungee+Shade)을 사용합니다.

```XML
<?xml version="1.0" encoding="utf-8"?>
<font-family xmlns:android="http://schemas.android.com/apk/res/android"
             xmlns:app="http://schemas.android.com/apk/res-auto">

  <!--Note: You must declare both sets of attributes
      so that your fonts load on devices running Android 8.0 (API level 26) or lower.
      See https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html -->

  <font android:fontStyle="normal"
        android:fontWeight="400"
        android:font="@font/bungeeshade"

        app:fontStyle="normal"
        app:fontWeight="400"
        app:font="@font/bungeeshade"/>
</font-family>
```

글꼴 패밀리 정의를 `/res/font/bungee_font_family.xml`에 저장한 후 XML에서 `@font/bungee_font_family`로 참조할 수 있습니다.

## 글꼴 패밀리 참조

이제 글꼴 패밀리가 생성되었으므로 `styles.xml` 에서 Braze 스타일 기본값을 재정의하여 글꼴 패밀리에 대한 참조를 포함할 수 있습니다.

예를 들어, 다음 스타일 재정의는 모든 Braze 인앱 메시지에 대해 `bungee` 글꼴 패밀리를 사용합니다.

```
<style name="Braze.InAppMessage">
  <item name="android:fontFamily">@font/bungee_font_family</item>
  <item name="fontFamily">@font/bungee_font_family</item>
</style>

<style name="Braze.Cards">
  <item name="android:fontFamily">@font/another_custom_font_family</item>
  <item name="fontFamily">@font/another_custom_font_family</item>
</style>
```

{% alert warning %}
모든 SDK 버전에서 호환성을 유지하려면 `android:fontFamily` 및 `fontFamily` 스타일 속성을 모두 설정해야 합니다.
{% endalert %}

