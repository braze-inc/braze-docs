---
nav_title: 사용자 지정 스타일
article_title: Android 및 FireOS용 맞춤 뉴스피드 스타일링
page_order: 0
platform: 
  - Android
  - FireOS
description: "이 참고 문서에서는 Android 또는 FireOS 애플리케이션에서 커스텀 뉴스피드 스타일을 추가하는 방법을 다룹니다."
channel:
  - news feed
  
---

# 커스텀 스타일

> 이 참고 문서에서는 Android 또는 FireOS 애플리케이션에서 커스텀 뉴스피드 스타일을 추가하는 방법을 다룹니다. 

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Braze UI 요소는 Android 표준 UI 지침과 일치하는 기본 모양과 느낌으로 제공되며 원활한 경험을 제공합니다. 이러한 기본 스타일은 Braze SDK 배포의 `res/values/style.xml` 파일에서 확인할 수 있습니다.

```xml
  <style name="Braze"/>
  <!-- Feed -->
  <style name="Braze.Feed"/>
  <style name="Braze.Feed.List">
    <item name="android:background">@android:color/transparent</item>
    <item name="android:divider">@android:color/transparent</item>
    <item name="android:dividerHeight">16.0dp</item>
    <item name="android:paddingLeft">12.5dp</item>
    <item name="android:paddingRight">5.0dp</item>
    <item name="android:scrollbarStyle">outsideInset</item>
  </style>
  ...
  </style>
```

원하는 경우 이러한 스타일을 재정의하여 앱에 더 적합한 모양과 느낌을 만들 수 있습니다. 스타일을 재정의하려면 프로젝트의 `styles.xml` 파일에 전체 스타일을 복사한 후 수정합니다. 모든 속성을 올바르게 설정하려면 전체 스타일을 로컬 `styles.xml` 파일에 복사해야 합니다.

{% tabs local %}
{% tab 올바른 스타일 재정의 %}

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```
{% endtab %}
{% tab 잘못된 스타일 재정의 %}

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```
{% endtab %}
{% endtabs %}

## 피드 스타일 요소

다음은 스타일 목적으로 테마를 지정할 수 있는 Braze UI 요소와 해당 이름에 대한 설명입니다.

{% gallery %}{% image_buster /assets/img_archive/Image27Theming.png %}
{% image_buster /assets/img_archive/Image28Theming.png %}
{% image_buster /assets/img_archive/Image29Theming.png %}
{% image_buster /assets/img_archive/Image30Theming.png %}{% endgallery %}

## 사용자 정의 글꼴 설정

Braze에서는 [글꼴 패밀리 가이드를]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization) 사용하여 사용자 지정 글꼴을 설정할 수 있습니다. 이 기능을 사용하려면 카드의 스타일을 재정의하고 `fontFamily` 속성을 사용하여 사용자 지정 글꼴 패밀리를 사용하도록 Braze에 지시하세요.

예를 들어 짧은 뉴스 카드의 모든 제목에서 글꼴을 업데이트하려면 `Braze.Cards.ShortNews.Title` 스타일을 재정의하고 커스텀 글꼴 패밀리를 참조합니다. 속성 값은 `res/font` 디렉터리에 있는 글꼴 패밀리를 가리켜야 합니다.

다음은 마지막 줄에 참조된 사용자 정의 글꼴 모음( `my_custom_font_family`)을 사용한 잘린 예제입니다:

```
<style name="Braze.Cards.ShortNews.Title">
  <item name="android:layout_height">wrap_content</item>
  ...
  <item name="android:fontFamily">@font/my_custom_font_family</item>
  <item name="fontFamily">@font/my_custom_font_family</item>
</style>
```

