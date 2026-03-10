---
nav_title: Intelligent Selection
article_title: Intelligent Selection
page_order: 1.0
description: "이 문서는 반복 캠페인 또는 Canvas의 성과를 하루 두 번 분석하고 각 메시지 변형을 받는 사용자 비율을 자동으로 조정하는 Intelligent Selection 기능을 설명합니다."
search_rank: 10
toc_headers: h2
---

# Intelligent Selection {#intelligent-selection}

> Intelligent Selection은 반복 캠페인 또는 Canvas의 성과를 하루 두 번 분석하고 각 메시지 변형을 받는 사용자 비율을 자동으로 조정하는 기능입니다.

## Intelligent Selection 정보

성과가 더 좋아 보이는 변형은 더 많은 사용자에게 전송되고, 성과가 낮은 변형은 더 적은 사용자에게 전송됩니다. 각 조정은 [통계 알고리즘](https://en.wikipedia.org/wiki/Multi-armed_bandit)으로 수행되어 Braze가 우연이 아닌 실제 성과 차이에 반응하도록 합니다.

![Intelligent Selection이 활성화된 캠페인의 A/B 테스트 영역.]({% image_buster /assets/img/intelligent_selection1.png %})

Intelligent Selection은 다음을 수행합니다.

- 성과 데이터를 반복 검토하고 캠페인 트래픽을 점진적으로 우승 변형으로 이동합니다.
- 통계적 신뢰를 해치지 않으면서 더 많은 사용자가 최고 변형을 받도록 합니다.
- [전통적인 A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)보다 성과가 낮은 변형을 더 빨리 제거하고 성과가 높은 변형을 더 빨리 식별합니다.
- 더 자주 테스트하고 사용자가 최고 메시지를 볼 확신을 높입니다.

Intelligent Selection은 한 번 이상 전송하는 캠페인에 가장 적합합니다. 단일 전송 캠페인에는 [A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)를 권장합니다.

## 사전 요구 사항

캠페인에 Intelligent Selection을 추가하기 전에 다음을 확인하세요.

- 캠페인이 반복 일정으로 전송됩니다(단일 전송은 지원되지 않음).
- 메시지 변형이 최소 두 개 있습니다.
- 변형 간 성과를 측정할 전환 이벤트가 정의되어 있습니다.
- 재자격 창이 24시간 이상입니다(더 짧은 창은 컨트롤 변형 무결성에 영향을 주어 지원되지 않음).

Canvas의 경우: 메시지 단계에 최소 두 개의 변형과 최소 하나의 전환 이벤트가 포함되어 있습니다.

캠페인 및 Canvas에 추가하는 단계, 실행 시간, 변형 분포 및 FAQ는 왼쪽 목차 또는 Braze 대시보드 도움말의 전체 문서를 참조하세요.
