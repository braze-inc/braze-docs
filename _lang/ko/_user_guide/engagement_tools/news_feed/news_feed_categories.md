---
nav_title: 뉴스피드 카테고리
page_order: 9

page_type: reference
description: "이 참조 문서에서는 뉴스피드 카테고리에 대해 설명하며, 이를 통해 뉴스피드의 여러 인스턴스를 애플리케이션에 통합할 수 있습니다."
tool: Dashboard
channel: news feed
hidden: true

---

# 뉴스피드 카테고리

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> 뉴스피드 카테고리를 사용하면 뉴스피드의 여러 인스턴스를 애플리케이션에 통합할 수 있습니다. 다양한 창 내에서 특정 카테고리의 뉴스피드 카드를 표시하는 피드를 통합하는 것이 가능합니다.

![뉴스피드 패널에 "Sweet Teeth - 대량으로 사탕을 구매하세요!"라는 제목의 뉴스피드 항목에 대한 캡션이 있는 이미지 카드 미리보기와 "단맛 욕구를 충족시키고 우리 가게에 들러보세요!"라는 메시지가 있습니다. 이 광고를 언급하면 첫 번째 사탕 가방에서 50% 할인을 받으세요. 뉴스피드 카테고리 확인란이 네 가지 있습니다: 뉴스, 공지사항, 광고, 소셜. 카테고리가 선택되지 않았습니다.][1]

뉴스피드를 특정 카테고리로 표시하는 것은 최종사용자에게 보이지 않습니다. 앱 코드에서 특정 카테고리를 표시하도록 피드를 특별히 구성하지 않는 한 기본값으로, Braze 뉴스피드는 모든 카테고리의 카드를 표시합니다. 자세한 앱 코드 구성 정보는 [뉴스피드 카테고리 정의][2]을 참조하세요.

[1]: {% image_buster /assets/img_archive/Newsfeed_category.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/defining_a_news_feed_category/
