---
nav_title: 배지
article_title: 뉴스피드 배지 Android 및 FireOS용
page_order: 3.2
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 뉴스피드 배지를 추가하고 미열람 뉴스피드 카드 수를 요청하는 방법을 다룹니다."
channel:
  - news feed
  
---

# 배지

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 뉴스피드 배지를 추가하고 미열람 뉴스피드 카드 수를 요청하는 방법을 다룹니다.

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객에게 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요.
{% endalert %}

## 미열람 뉴스피드 카드 수 요청

언제든지 다음 번호로 전화하여 읽지 않은 카드의 수를 요청할 수 있습니다:

```java
getUnreadCardCount()
```

자세한 내용은 [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-feed-updated-event/get-unread-card-count.html)을 참조하십시오.

