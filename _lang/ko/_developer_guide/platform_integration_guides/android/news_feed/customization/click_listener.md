---
nav_title: 수동으로 클릭 처리하기
article_title: Android 및 FireOS용 뉴스피드 클릭 수동 처리하기
page_order: 3
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션에서 뉴스피드 클릭을 수동으로 처리하는 방법을 다룹니다."
channel:
  - news feed
  
---

# 수동으로 클릭 처리

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에서 뉴스피드 클릭을 수동으로 처리하는 방법을 다룹니다.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

커스텀 뉴스피드 클릭 리스너를 설정하여 뉴스피드 클릭을 수동으로 처리할 수 있습니다. 이를 통해 기본 웹 브라우저를 선택적으로 사용하여 웹 링크를 여는 등의 사용 사례를 지원합니다.

## 1단계: 뉴스피드 클릭 리스너 구현하기

[`IFeedClickActionListener`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/feed/listeners/IFeedClickActionListener.java)를 구현하는 클래스를 생성합니다. 사용자가 뉴스피드 카드를 클릭할 때 호출되는 `onFeedCardClicked()` 메서드를 구현합니다.

## 2단계: Braze가 뉴스피드 클릭 리스너를 사용하도록 지시하기

`IFeedClickActionListener`가 생성되면 `BrazeFeedManager.getInstance().setFeedCardClickActionListener()`를 호출하여 `BrazeFeedManager`에 커스텀 `IFeedClickActionListener`를 사용하도록 지시합니다.

