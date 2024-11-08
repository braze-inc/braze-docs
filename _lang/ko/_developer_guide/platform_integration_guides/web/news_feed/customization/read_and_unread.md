---
nav_title: 읽음 및 읽지 않음 표시기
article_title: 웹용 뉴스피드 읽기 및 읽지 않음 표시기
platform: Web
page_order: 2
page_type: reference
description: "이 문서에서는 Braze SDK를 통해 뉴스피드 카드에서 읽음 및 읽지 않음 표시기를 설정하는 방법에 대해 설명합니다."
channel: news feed

---

# 읽음 및 읽지 않음 표시기

> 이 문서에서는 Braze SDK를 통해 뉴스피드 카드에서 읽음 및 읽지 않음 표시기를 설정하는 방법에 대해 설명합니다.

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객에게 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요.
{% endalert %}

Braze는 다음 이미지와 같이 뉴스피드 카드에 읽지 않음 및 읽음 표시기를 제공합니다:

![텍스트와 함께 시계 이미지가 표시된 뉴스피드 카드입니다. 텍스트 상단 모서리에는 카드가 읽혔는지 여부를 나타내는 파란색 또는 회색 삼각형이 있습니다. 파란색 삼각형은 카드를 읽었음을 나타냅니다.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## 표시기 비활성화

이 기능을 비활성화하려면 다음 스타일을 CSS에 추가하십시오:

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

