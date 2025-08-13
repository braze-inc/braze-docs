---
nav_title: 전환 상관관계
article_title: 전환 상관관계
alias: /conversion_correlation/
page_order: 3

page_type: reference
description: "이 참조 문서에서는 캠페인 분석 페이지의 전환 상관관계 분석에 대해 설명합니다."
tool: 
  - Reports
  
---

# 전환 상관관계

> **캠페인 분석** 페이지의 전환 상관관계 분석을 통해 어떤 사용자 속성과 행동이 캠페인에 대해 설정한 결과에 도움이 되거나 해가 되는지에 대한 인사이트를 얻을 수 있습니다. 

## 개요

For every campaign, Braze checks a list of attributes and user behaviors and computes whether users are statistically significantly associated with increases or decreases in each of the [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) you've chosen for the campaign. 또한 특정 속성이나 행동을 가진 사용자가 전환할 가능성이 얼마나 높은지 또는 낮은지도 계산하여 유의미한 경우 표의 해당 면에 표시합니다. 각 속성 또는 관심 행동을 가진 사용자를 전체 캠페인 오디언스 전체의 비율과 비교합니다. 전환과 유의미한 상관관계가 없는 행동 및 속성은 표에 표시되지 않습니다.

전환 상관관계 분석을 실행하려면 드롭다운 메뉴에서 관심 있는 전환 이벤트를 선택합니다.

![Conversion Correlation panel that shows an example with "Select a conversion event" set to "Primary Conversion Event - A" with the Event Setting as "Made Purchase within 12 hours (Any product)".]({% image_buster /assets/img/convcorr.png %})

## 무엇을 확인하나요?

다음 속성을 범주형 변수로 처리하여 확인합니다. 즉, 사용자가 이러한 속성의 각 가능한 값을 가지고 있거나 가지고 있지 않은 경우, 해당 속성이 전환율에 영향을 미치는지 테스트합니다.

-  국가
-  언어
-  성별

또한 다음 사항이 전환율에 영향을 미치는지 확인합니다:

- 사용자 지정 이벤트 수행
- 지난 30일 동안 접수된 캠페인 및 캔버스(현재 평가 중인 캠페인 제외)

마지막으로 여러 값을 가질 수 있는 여러 행동 변수를 확인합니다. 다음을 4개의 버킷 또는 사분위수로 나눈 다음, 해당 사분위수에 속하는 것과 전환율의 증가 또는 감소 간의 연관성을 측정합니다:

- 연령
- 총 소비 금액(달러)
- 세션 수

## 이 분석은 언제 확인할 수 있나요?

이 분석은 캠페인 전송이 시작된 후 최소 24시간이 지나면 사용할 수 있으며 지난 30일 동안 발생한 전송만 살펴봅니다. 캠페인의 전환 이벤트와 유의미한 상관 관계가 있는 행동이나 속성이 없는 경우, 드롭다운 메뉴가 비활성화되고 이를 알리는 메시지가 표시됩니다.

## Braze가 중요도를 확인하는 방법

[윌슨 신뢰 구간](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval)을 사용하여 통계적 중요성을 확인합니다. 전체 캠페인 오디언스의 전환율을 95% 신뢰도로 결정합니다. 이를 기본 요율이라고 합니다. 

그런 다음 각 변수에 대해 해당 특정 속성 또는 관심 행동을 가진 사용자가 95% 신뢰도로 전환한 비율도 계산합니다. 이를 기본 이자율로 나누면 비율을 측정할 수 있습니다. 이 값이 1보다 훨씬 크면 해당 속성이나 행동을 가진 사용자가 전환할 가능성이 높다는 뜻입니다. 그보다 훨씬 적으면 가능성이 적습니다. 비율 자체의 값을 표에 표시합니다. 이 값은 95% 신뢰 수준에서 유의미할 정도로 1에서 충분히 멀리 떨어져 있는 경우에만 표시됩니다.

