---
nav_title: 뉴스피드에서 마이그레이션
article_title: 뉴스피드에서 마이그레이션
page_order: 10
description: "이 참고 문서는 뉴스피드에서 Braze 콘텐츠 카드로 마이그레이션하는 방법에 대한 지침을 제공합니다."
channel:
  - content cards
  - news feed
  
---

# 뉴스피드에서 콘텐츠 카드로 이동

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객들이 더 유연하고, 맞춤화 가능하며, 신뢰할 수 있는 콘텐츠 카드 메시징 채널로 이동할 것을 권장합니다.
{% endalert %}

> 뉴스피드에서 콘텐츠 카드로 이동하는 데 시간이 걸리지만, 쉽게 적응할 수 있습니다! 콘텐츠를 뉴스피드에서 콘텐츠 카드로 자동으로 마이그레이션할 수 없습니다. 콘텐츠 카드를 처음부터 통합해야 합니다. 하지만 콘텐츠 카드의 새로운 유연성 덕분에 그것을 놓치거나 신경 쓰지 않을 것이라고 생각합니다.

자세한 내용은 Braze 계정 매니저에게 문의하십시오.

## 특징 및 기능

콘텐츠 카드에는 뉴스피드에서 지원하지 않는 많은 기능이 포함되어 있습니다. 예를 들어, 실행 기반 및 API 전달과 같은 추가 전달 옵션과 전환 추적과 같은 향상된 분석 기능이 있습니다.

뉴스피드에서 콘텐츠 카드로 마이그레이션을 계획할 때, 콘텐츠 카드와 뉴스피드 간의 주요 차이점을 주목하는 것이 중요합니다:

- **세분화:** 콘텐츠 카드 세분화는 메시지가 전송될 때 또는 카드가 처음 조회될 때 평가될 수 있습니다. 뉴스피드 세분화는 뉴스피드 카드가 조회될 때 평가됩니다.
- **개인화:** 콘텐츠 카드 개인화는 메시지가 전송될 때 또는 카드가 처음 조회될 때 템플릿화될 수 있습니다. 뉴스피드 카드 개인화는 뉴스피드 카드가 조회될 때 템플릿화됩니다.

다음 표는 뉴스피드와 콘텐츠 카드 간의 지원되는 기능의 차이를 자세히 설명합니다.

| 기능 | 뉴스피드 | 콘텐츠 카드 |
|---|---|---|
| 다변량 및 다채널 캠페인 | <i class="fas fa-times" title="지원되지 않음"></i> | <i class="fas fa-check" title="지원됨"></i> |
| 예약된, 실행 기반 및 API 기반 전달 | <i class="fas fa-times" title="지원되지 않음"></i> | <i class="fas fa-check" title="지원됨"></i> |
| API로 생성된 메시지 | <i class="fas fa-times" title="지원되지 않음"></i> | <i class="fas fa-check" title="지원됨"></i> |
| A/B 테스트 | <i class="fas fa-times" title="지원되지 않음"></i> | <i class="fas fa-check" title="지원됨"></i> |
| [카드 해제 및 고정][4] | <i class="fas fa-times" title="지원되지 않음"></i> | <i class="fas fa-check" title="지원됨"></i> |
| [풍부한 분석][3] (예: 전환 추적) | <i class="fas fa-times" title="지원되지 않음"></i> | <i class="fas fa-check" title="지원됨"></i> |
| [캔버스에서 사용 가능][2] | <i class="fas fa-times" title="지원되지 않음"></i> | <i class="fas fa-check" title="지원됨"></i> |
| [연결된 콘텐츠][5] | <i class="fas fa-times" title="지원되지 않음"></i> | <i class="fas fa-check" title="지원됨"></i> |
| 개인화와 세분화 | 템플릿된 노출 횟수 | 전송 시 또는 첫 노출 횟수에 템플릿화됨 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 구현

- 콘텐츠 카드와 뉴스피드는 별개의 제품이므로 콘텐츠 카드를 사용하려면 앱 또는 웹사이트에 대한 간단한 통합이 필요합니다.
- 원하는 경우 전환 시 기존 뉴스피드 카드를 콘텐츠 카드 캠페인으로 수동으로 마이그레이션해야 합니다.
- 콘텐츠 카드는 뉴스피드의 대체물로, 뉴스피드와 동시에 사용하도록 의도되지 않았습니다.
- 콘텐츠 카드는 현재 카테고리를 지원하지 않습니다. 카테고리는 [사용자 정의 및 키-값 쌍][1]을 통해 달성할 수 있습니다.


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/content-cards_in_canvas/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#step-2-compose-a-content-card
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
