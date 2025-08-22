---
nav_title: 예측 이벤트
article_title: 예측 이벤트
description: "이 기사는 마케터가 사용자가 이벤트를 수행할 가능성에 따라 사용자를 식별하고 메시지를 보낼 수 있는 도구인 예측 이벤트(이전에는 예측 구매)를 다룹니다."
page_order: 2.1
alias: /predictive_purchases/
search_rank: 1
---

# 예측 이벤트

> 예측 이벤트는 마케터에게 사용자가 이벤트를 수행할 가능성에 따라 식별하고 메시징할 수 있는 강력한 도구를 제공합니다. 이벤트 예측을 생성할 때, Braze는 [그레디언트 부스티드 결정 트리](https://en.wikipedia.org/wiki/Gradient_boosting)를 사용하여 이전 활동을 학습하고 미래 활동을 예측하기 위해 머신 러닝 모델을 훈련시킵니다.

## 예측 이벤트 정보

예측이 생성된 후, 사용자에게 0에서 100 사이의 [가능성 점수]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score)이 할당되어 선택한 이벤트를 수행할 가능성을 나타냅니다. 점수가 높을수록 사용자가 해당 이벤트를 수행할 가능성이 높습니다. 사용자는 낮음, 중간, 높음 가능성 범주로도 분류됩니다.

예측 이벤트의 진정한 가치는 예측 결과를 사용하여 세그먼트 또는 캠페인을 만드는 데 있습니다. 마케터는 **예측** 페이지에서 직접 타겟팅된 캠페인을 구축하여 즉각적인 매출 증대 결과를 얻거나, 향후 캠페인 또는 캔버스를 위해 세그먼트를 저장할 수 있습니다. 누구를 먼저 목표로 삼아야 할지 모르겠나요? 메시징 사용자에 대한 [전략적 고려사항]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy)을 읽어보세요. 이는 해당 사용자의 가능성 점수에 기반합니다.

!["예측 이벤트의 작동 방식"이라는 제목의 그래픽으로, 머신 러닝 모델에 유입되는 사용자 데이터를 표시합니다. 라벨에는 "과거 데이터를 사용하여 이벤트를 특정 기간 동안 수행한 사용자와 수행하지 않은 사용자의 행동을 비교합니다."라고 적혀 있습니다. 또한 이벤트를 수행할 가능성이 가장 낮은 사용자부터 가장 높은 사용자까지 순위가 매겨진 머신 러닝 결과도 보여줍니다. 라벨에는 "미래 이벤트의 가능성을 예측하고, 사용자에게 정확하고 편리한 타겟팅을 위해 가능성 점수를 할당합니다."]({% image_buster /assets/img/how_predictive_events_works.png %})

## 예측 이벤트에 접근하기

**예측** 페이지는 **분석** 섹션에 위치해 있습니다. 전체 액세스를 위해 계정 매니저에게 문의하세요.

이 기능을 구매하기 전에 미리보기 모드에서 사용할 수 있습니다. 이것은 합성 데이터를 사용한 데모 예측을 볼 수 있게 해주며, 한 번에 하나의 미리보기 예측 모델을 생성할 수 있게 해줍니다. 이 예측은 실제 사용자 데이터를 기반으로 생성되지만, 사용자의 가능성 점수에 따라 메시징 대상으로 설정할 수는 없습니다. 생성 후에는 정기적으로 업데이트되지 않습니다.

미리보기를 사용하면 이 예측을 편집하고 다시 빌드하거나 보관하여 다른 [예측 품질]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality)을 테스트하고 [다양한 오디언스]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience)와 친숙해지며 분석에 익숙해질 수 있습니다.
