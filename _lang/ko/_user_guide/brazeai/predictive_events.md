---
nav_title: 예측 이벤트
article_title: 예측 이벤트
description: "이 문서에서는 마케터가 이벤트 수행 가능성에 따라 사용자를 식별하고 메시지를 보낼 수 있는 도구인 예측 이벤트(이전의 예측 구매)에 대해 다룹니다."
page_order: 2.1
alias: /predictive_purchases/
search_rank: 1
---

# 예측 이벤트

> 예측 이벤트는 마케터에게 이벤트 수행 가능성을 기반으로 사용자를 식별하고 메시징할 수 있는 강력한 툴을 제공합니다. 이벤트 예측을 생성하면 Braze는 [그라데이션 부스트 의사 결정 트리를](https://en.wikipedia.org/wiki/Gradient_boosting) 사용하여 머신 러닝 모델을 학습시켜 이전 활동에서 학습하고 향후 활동을 예측합니다.

## 예측 이벤트 정보

예측이 구축되면 사용자에게 선택한 이벤트를 수행할 가능성을 나타내는 0에서 100 사이의 [가능성 점수가]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score) 할당됩니다. 점수가 높을수록 사용자가 해당 이벤트를 수행할 가능성이 높습니다. 또한 사용자는 가능성이 낮음, 중간, 높음 카테고리별로 정렬됩니다.

예측 이벤트의 진정한 가치는 예측 결과를 사용하여 세그먼트 또는 캠페인을 생성하는 데 있습니다. 마케터는 **예측** 페이지에서 바로 타겟팅 캠페인을 구축하여 즉각적인 매출 증대 결과를 확인하거나 향후 캠페인 또는 캔버스를 위해 세그먼트를 저장할 수 있습니다. 누구를 먼저 타겟팅해야 할지 잘 모르시겠어요? 가능성 점수를 기반으로 사용자에게 메시지를 보낼 때 [고려해야 할 전략적 사항을]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) 읽어보세요.

"이벤트 예측의 작동 방식"이라는 제목의 그래픽으로, 사용자 데이터가 머신 러닝 모델에 퍼널링되는 모습을 보여줍니다. 라벨에는 "과거 데이터로 훈련하고, 특정 기간에 이벤트를 수행한 사용자와 그렇지 않은 사용자의 행동을 비교하세요."라는 문구가 적혀 있습니다. 또한 이벤트 수행 가능성이 가장 낮은 사용자부터 가장 높은 사용자까지 순위가 매겨진 머신 러닝 결과도 표시됩니다. 라벨에는 "향후 이벤트의 가능성을 예측하고 사용자에게 가능성 점수를 할당하여 정확하고 편리한 타겟팅"이라는 문구가 적혀 있습니다.]({% image_buster /assets/img/how_predictive_events_works.png %})

## 예측 이벤트에 액세스하기

**예측** 페이지는 **분석** 섹션에 있습니다. 전체 액세스 권한을 얻으려면 계정 매니저에게 문의하세요.

이 기능을 구매하기 전에는 미리 보기 모드로 이용할 수 있습니다. 이렇게 하면 합성 데이터로 데모 예측을 볼 수 있을 뿐만 아니라 한 번에 하나의 미리보기 예측 모델을 만들 수 있습니다. 이 예측은 실제 사용자 데이터를 기반으로 만들어지지만, 가능성 점수에 따라 메시징을 보낼 사용자를 타겟팅할 수는 없습니다. 또한 생성 후에는 정기적으로 업데이트되지 않습니다.

미리 보기를 사용하면 이 하나의 예측을 편집 및 재구축하거나 보관하고 다른 [예측을]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality) 생성하여 [다양한 오디언스의]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) 예상 [예측 품질을]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality) 테스트하고 분석에 익숙해질 수도 있습니다.
