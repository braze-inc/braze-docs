---
nav_title: 예측 이탈
article_title: 예측 이탈
description: "이 랜딩 페이지는 예측 이탈을 다루며, 고객이탈이 비즈니스에 어떤 의미인지 정의하고 고객이탈을 방지하고자 하는 사용자를 정의할 수 있는 도구입니다."
page_order: 2.0
alias: /predictive_churn/
search_rank: 2
---

# 예측 이탈

> 예측 이탈을 사용하면 이탈이 비즈니스에 미치는 영향을 정의하고 유지하려는 사용자를 식별할 수 있습니다. 예측을 생성하면 Braze는 [그라데이션 부스트 의사 결정 트리를](https://en.wikipedia.org/wiki/Gradient_boosting) 사용하여 머신 러닝 모델을 학습시켜 이탈한 사용자와 그렇지 않은 사용자 모두의 과거 행동 패턴을 분석하여 위험에 처한 사용자를 인식합니다.

{% alert tip %}
자세한 내용은 [이탈 정의]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) 및 [예측 대상을]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience) 참조하세요.
{% endalert %}

## 이탈 예측 정보

예측 모델이 구축되면 예측 대상에 속한 사용자에게는 정의에 따라 이탈 가능성을 나타내는 0~100 사이의 [이탈 위험 점수가]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score) 할당됩니다. 점수가 높을수록 사용자가 고객이탈할 가능성이 높습니다. 

예측 오디언스의 위험 점수를 업데이트하는 것은 [선택한 빈도]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions)로 수행할 수 있습니다. 이렇게 하면 고객이탈 위험이 있는 사용자에게 실제로 이탈하기 전에 연락하여 이를 방지할 수 있습니다. 최대 세 개의 활성 예측을 사용하여 예측 이탈을 활용하여 가장 가치 있다고 생각되는 특정 사용자 세그먼트 내에서 고객이탈을 방지하기 위해 개별 모델을 맞춤화할 수 있습니다.

![고객이탈의 개요는 과거 예측 오디언스를 포함하며, 역사적 데이터로 훈련합니다. 이는 이탈 위험 점수로 오늘의 예측 잠재고객을 측정하여 향후 이탈 위험을 예측하는 데 기여합니다.]({% image_buster /assets/img/churn/churn_overview.png %})

## 예측 이탈에 액세스하기

**예측** 페이지는 **분석** 섹션에 위치해 있습니다. 전체 액세스를 위해 계정 매니저에게 문의하세요.

이 기능을 구매하기 전에 미리보기 모드에서 사용할 수 있습니다. 이것은 데모 고객이탈 예측을 합성 데이터로 보고, 한 번에 사용자 데이터에 기반한 고객이탈 예측 모델을 만들 수 있게 해줍니다. 이 미리보기는 고객이탈 위험에 따라 메시징을 위해 사용자를 타겟팅할 수 없으며 생성 후 정기적으로 업데이트되지 않습니다.

미리보기를 통해 하나의 예측을 편집하고 다시 빌드하거나 보관하여 다른 [정의]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)의 예상 [예측 품질]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/)을 테스트하기 위해 다른 것을 만들 수 있습니다.
