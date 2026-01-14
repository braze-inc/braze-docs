---
nav_title: 예측 이탈률
article_title: 예측 이탈률
description: "이 랜딩 페이지에서는 비즈니스에 있어 이탈의 의미와 이탈을 방지하고자 하는 사용자를 정의할 수 있는 도구인 예측 이탈을 다룹니다."
page_order: 2.0
alias: /predictive_churn/
search_rank: 2
---

# 예측 이탈률

> 예측 이탈을 사용하면 비즈니스에 있어 이탈의 의미를 정의하고 유지하고자 하는 사용자를 식별할 수 있습니다. 예측을 생성하면 Braze는 [그라데이션 부스트 의사 결정 트리를](https://en.wikipedia.org/wiki/Gradient_boosting) 사용하여 머신 러닝 모델을 학습시켜 이탈한 사용자와 그렇지 않은 사용자 모두의 과거 행동 패턴을 분석하여 위험에 처한 사용자를 인식합니다.

{% alert tip %}
자세한 내용은 [이탈 정의]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) 및 [예측 오디언스를]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience) 참조하세요.
{% endalert %}

## 예측 이탈 정보

예측 모델이 구축되면 예측 오디언스에 속한 사용자에게는 정의에 따라 이탈 가능성을 나타내는 0~100 사이의 [이탈 위험 점수가]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score) 할당됩니다. 점수가 높을수록 사용자가 이탈할 가능성이 높습니다. 

예측 오디언스의 위험 점수 업데이트는 [사용자가 선택한 주기로]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions) 수행할 수 있습니다. 이렇게 하면 고객이탈 위험이 있는 사용자에게 실제로 이탈하기 전에 먼저 다가가서 이탈을 사전에 방지할 수 있습니다. 최대 3개의 활성 사용자 예측을 사용하여 예측 이탈을 활용하면 개별 모델을 맞춤화하여 가장 가치가 높다고 판단되는 특정 사용자 세그먼트 내에서 이탈을 방지할 수 있습니다.

과거 데이터로 학습한 과거 예측 오디언스를 포함한 고객이탈에 대한 개요 데이터입니다. 이는 현재 예측된 오디언스를 이탈 위험 점수로 측정하여 향후 발생할 수 있는 고객 이탈 위험을 예측하는 데 기여합니다.]({% image_buster /assets/img/churn/churn_overview.png %})

## 예측 이탈에 액세스하기

**예측** 페이지는 **분석** 섹션에 있습니다. 전체 액세스 권한을 얻으려면 계정 매니저에게 문의하세요.

이 기능을 구매하기 전에는 미리 보기 모드로 이용할 수 있습니다. 이를 통해 합성 데이터로 데모 이탈 예측을 확인하고 사용자 데이터를 기반으로 한 번에 하나의 이탈 예측 모델을 생성할 수 있습니다. 이 미리 보기에서는 고객이탈 위험에 따라 메시징 사용자를 타겟팅할 수 없으며 생성 후 정기적으로 업데이트되지 않습니다.

미리 보기를 사용하면 하나의 예측을 편집 및 재구축하거나 보관하고 다른 [예측을]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) 생성하여 다양한 [정의의]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) 예상 [예측 품질을]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) 테스트할 수도 있습니다.
