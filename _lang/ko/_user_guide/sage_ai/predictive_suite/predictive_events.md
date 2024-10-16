---
nav_title: 예측 이벤트
article_title: 예측 이벤트
page_order: 6.4
layout: featured
alias: /predictive_purchases/
search_rank: 1
guide_top_header: "예측 이벤트"
guide_top_text: "어떤 사용자가 특정 이벤트(예: 구매)를 수행할 가능성이 있는지 아는 것은 성장하는 비즈니스에 중요한 인사이트입니다. 그것 없이, 어떤 캠페인을 구축할지 어떻게 결정합니까? 누가 할인과 프로모션을 받아야 합니까? 한정된 예산을 어디에 쓸까? Braze는 마케팅 팀이 미래 행동을 이해하고 자원을 참여 및 매출 극대화 캠페인에 집중할 수 있도록 돕는 머신 러닝 모델인 Predictive Events(이전의 Predictive Purchases)를 통해 이러한 질문에 답하는 데 도움을 줍니다."
description: "이 문서에서는 마케터가 이벤트를 수행할 가능성에 따라 사용자를 식별하고 메시지할 수 있는 도구인 Predictive Events(이전의 Predictive Purchases)에 대해 다룹니다."

guide_featured_title: "주제"
guide_featured_list:
- name: 예측 생성
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_events/creating_an_event_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: 예측 분석
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_events/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: 메시징 사용자
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_events/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg

---

## 개요

![예측 이벤트 작동 방식이라는 제목의 그래픽. 왼쪽에는 사용자 데이터가 머신 러닝 모델로 유입되는 모습이 표시됩니다. 라벨에는 "역사적 데이터를 사용하여 훈련하고, 특정 기간 동안 이벤트를 수행한 사용자와 수행하지 않은 사용자의 행동을 비교합니다."라고 적혀 있습니다. 오른쪽에는 머신 러닝의 결과가 표시되며, 사용자가 이벤트를 수행할 가능성이 적은 순서에서 높은 순서로 순위가 매겨집니다. 라벨에는 "미래 사건의 가능성을 예측하고, 정확하고 편리한 타겟팅을 위해 사용자에게 가능성 점수를 할당합니다."][1]라고 적혀 있습니다.

> 예측 이벤트는 마케터에게 이벤트를 수행할 가능성에 따라 사용자를 식별하고 메시징할 수 있는 강력한 도구를 제공합니다. 이벤트 예측을 생성하면 Braze는 [그라디언트 부스팅 결정 트리](https://en.wikipedia.org/wiki/Gradient_boosting)를 사용하여 머신 러닝 모델을 훈련시켜 이전 활동에서 학습하고 미래 활동을 예측합니다.

예측이 완료되면 사용자는 선택한 이벤트를 수행할 가능성을 나타내는 0에서 100 사이의 [가능성 점수]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/prediction_analytics/#purchase_score)를 받습니다. 점수가 높을수록 사용자가 해당 이벤트를 수행할 가능성이 높아집니다. 사용자는 낮음, 중간 및 높음 가능성 범주로도 분류됩니다.

Predictive Events의 실제 가치는 예측 결과를 사용하여 세그먼트 또는 캠페인을 만드는 데 있습니다. 마케터는 즉각적인 매출 증대 결과를 위해 **예측** 페이지에서 직접 타겟팅된 캠페인을 구축하거나, 향후 캠페인 또는 캔버스를 위해 세그먼트를 저장할 수 있습니다. 누구를 먼저 목표로 삼아야 할지 모르겠나요? 메시징 사용자의 가능성 점수를 기반으로 한 [전략적 고려 사항]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/messaging_users/#strategy)을 읽어보십시오.

## 예측 이벤트에 액세스

예측 페이지는 분석 섹션에 있습니다. 전체 액세스를 위해 계정 매니저에게 문의하십시오.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **예측**을 **참여** 아래에서 찾을 수 있습니다.
{% endalert %}

이 기능을 구매하기 전에 미리보기 모드에서 사용할 수 있습니다. 이렇게 하면 예측을 통해 합성 데이터를 볼 수 있을 뿐만 아니라 한 번에 하나의 예측 모델을 미리 볼 수 있습니다. 이 예측은 실제 사용자 데이터를 기반으로 생성되지만, 사용자의 가능성 점수에 따라 메시징 대상으로 설정할 수는 없습니다. 생성 후에는 정기적으로 업데이트되지 않습니다.

미리보기를 사용하면 이 예측을 편집하고 다시 빌드하거나 보관하고 다른 예측을 만들어 예상되는 [예측 품질]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/prediction_analytics/#prediction_quality)을 [다른 청중<2>에 대해 테스트하고 분석에 익숙해질 수 있습니다.

<br><br>

[1]: {% image_buster /assets/img/how_predictive_events_works.png %}

