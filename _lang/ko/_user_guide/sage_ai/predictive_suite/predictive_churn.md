---
nav_title: Predictive Churn
article_title: Predictive Churn
page_order: 6.4
layout: dev_guide
alias: /predictive_churn/
search_rank: 2
guide_top_header: "Predictive Churn"
guide_top_text: "고객 이탈률 또는 고객 손실이라고도 하는 고객 이탈은 성장하는 비즈니스가 고려해야 할 가장 중요한 지표 중 하나입니다. 이탈을 해결할 수 있는 올바른 도구를 갖추는 것은 손실을 최소화하고 고객 유지율을 극대화하는 데 매우 중요합니다. 잠재적으로 이탈할 가능성이 있는 사용자를 확보하기 위해 Braze는 향후 이탈을 최소화하기 위한 사전 예방적 접근 방식을 제공하는 예측 이탈 기능을 제공합니다."
description: "이 랜딩 페이지에서는 이탈이 비즈니스에 미치는 영향과 이탈을 방지하고자 하는 사용자를 정의할 수 있는 도구인 예측 이탈에 대해 설명합니다."

guide_featured_title: "주제"
guide_featured_list:
- name: 이탈 예측 생성
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_churn/creating_a_churn_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: 예측 분석
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_churn/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: 사용자 메시징
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_churn/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg
- name: 문제 해결
  link: /docs/user_guide/sage_ai/predictive_suite/predictive_churn/prediction_faq/
  image: /assets/img/braze_icons/annotation-question.svg

---

## 개요

![과거 데이터로 학습한 과거 예측 잠재고객을 포함한 이탈에 대한 개요입니다. 이는 이탈 위험 점수로 오늘의 예측 잠재고객을 측정하여 향후 이탈 위험을 예측하는 데 기여합니다.][1]

> 예측 이탈을 사용하면 비즈니스에 있어 이탈의 의미[(이탈 정의)]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)와 이탈을 방지하고자 하는 사용자[(예측 대상)를]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience) 정의할 수 있습니다. 예측을 생성하면 Braze는 [그라데이션 부스트 의사 결정 트리를](https://en.wikipedia.org/wiki/Gradient_boosting) 사용하여 머신 러닝 모델을 학습시켜 정의에 따라 이탈한 사용자와 그렇지 않은 과거 사용자의 활동 패턴을 학습하여 이탈 위험이 있는 사용자를 식별합니다.

예측 모델이 구축되면 예측 대상에 속한 사용자에게는 정의에 따라 이탈 가능성을 나타내는 0~100 사이의 [이탈 위험 점수가]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/#churn_score) 할당됩니다. 점수가 높을수록 사용자가 이탈할 가능성이 높습니다. 

예측 대상의 위험 점수를 업데이트하는 것은 [사용자가 선택한 주기로]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions) 수행할 수 있습니다. 이렇게 하면 이탈할 위험이 있는 사용자에게 실제로 이탈하기 전에 먼저 다가가서 이탈을 사전에 방지할 수 있습니다. 최대 3개의 활성 예측을 사용하여 이탈 예측을 활용하면 개별 모델을 맞춤화하여 가장 가치가 있다고 판단되는 특정 사용자 세그먼트 내에서 이탈을 방지할 수 있습니다.

## 이탈 예측에 액세스

**예측** 페이지는 **애널리틱스** 섹션에 있습니다. 전체 액세스 권한을 얻으려면 계정 관리자에게 문의하세요.

{% alert note %}
[이전 탐색을]({{site.baseurl}}/navigation) 사용하는 경우 **참여도** 아래에서 **예측을** 찾을 수 있습니다.
{% endalert %}

이 기능을 구매하기 전에는 미리 보기 모드로 이용할 수 있습니다. 이를 통해 합성 데이터를 사용한 데모 이탈 예측을 확인하고 사용자 데이터를 기반으로 한 번에 하나의 이탈 예측 모델을 만들 수 있습니다. 이 미리 보기에서는 이탈 위험에 따라 메시징 대상 사용자를 지정할 수 없으며, 생성 후 정기적으로 업데이트되지 않습니다.

미리 보기를 사용하면 하나의 예측을 편집 및 재구축하거나 보관하고 다른 [예측을]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) 생성하여 다양한 [정의의]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) 예상 [예측 품질을]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) 테스트할 수도 있습니다.

<br><br>

[1]: {% image_buster /assets/img/churn/churn_overview.png %}
