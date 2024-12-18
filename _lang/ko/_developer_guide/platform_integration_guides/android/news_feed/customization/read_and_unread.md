---
nav_title: 읽음 및 미열람 표시기
article_title: Android 및 FireOS용 뉴스피드 읽기 및 읽지 않음 표시기
page_order: 3.1
platform: 
  - Android
  - FireOS
description: "이 참고 문서에서는 Android 또는 FireOS 애플리케이션의 뉴스피드 읽기 및 읽지 않음 표시기에 대해 설명합니다."
channel:
  - news feed
  
---

# 열람 및 미열람 표시기

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객에게 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요.
{% endalert %}

> Braze를 사용하면 뉴스피드 카드에서 읽지 않음 및 읽음 표시기를 선택적으로 켤 수 있습니다.

![텍스트와 함께 시계 이미지가 표시된 뉴스피드 카드입니다. 텍스트 상단 모서리에는 카드가 읽혔는지 여부를 나타내는 파란색 또는 회색 삼각형이 있습니다. 파란색 삼각형은 카드를 읽었음을 나타냅니다.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## 표시기 활성화

이 기능을 사용하려면 `braze.xml` 파일에 다음 줄을 추가하세요:

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## 표시기 사용자 지정하기

이러한 표시기는 `icon_read` 및 `icon_unread` 드로어블을 변경하여 사용자 지정할 수 있습니다.

