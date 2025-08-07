---
nav_title: 예측 이탈
article_title: 예측 이탈
page_order: 6.4
layout: dev_guide
alias: /predictive_churn/
search_rank: 2
guide_top_header: "예측 이탈"
guide_top_text: "고객 이탈 또는 클라이언트 손실로도 알려진 고객이탈은 성장하는 기업이 고려해야 할 가장 중요한 측정기준 중 하나입니다. 고객이탈을 해결하기 위한 적절한 도구를 갖추는 것은 손실을 최소화하고 고객 유지를 극대화하는 데 중요합니다. 이탈할 가능성이 있는 사용자에게 선제적으로 대응하기 위해, Braze는 예측 이탈을 제공하여 미래의 고객이탈을 최소화하는 데에 적극적인 접근 방식을 제공합니다."
description: "이 랜딩 페이지는 예측 이탈을 다루며, 고객이탈이 비즈니스에 어떤 의미인지 정의하고 고객이탈을 방지하고자 하는 사용자를 정의할 수 있는 도구입니다."

guide_featured_title: "주제"
guide_featured_list:
- name: 고객이탈 예측 생성
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: 예측 분석
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: 메시징 사용자
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg
- name: 문제 해결
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/prediction_faq/
  image: /assets/img/braze_icons/annotation-question.svg

---

## 개요

![고객이탈의 개요는 과거 예측 오디언스를 포함하며, 역사적 데이터로 훈련합니다. 이는 오늘의 예측된 오디언스를 고객이탈 위험 점수로 측정하여 미래의 고객이탈 위험을 예측하는 데 기여합니다.][1]

> 예측 이탈을 통해 비즈니스에 있어 고객이탈이 무엇을 의미하는지 정의할 수 있으며 ([고객이탈 정의]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)), 고객이탈([예측 오디언스]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience))을 방지하고자 하는 사용자들을 지정할 수 있습니다. 예측을 생성하면 Braze는 [그레디언트 부스티드 결정 트리](https://en.wikipedia.org/wiki/Gradient_boosting)를 사용하여 머신 러닝 모델을 훈련시켜 고객이탈 위험이 있는 사용자를 식별합니다. 이는 고객이탈한 사용자와 고객이탈하지 않은 사용자의 활동 패턴을 귀하의 정의에 따라 학습하여 이루어집니다.

예측 모델이 구축되면, 예측 오디언스의 사용자에게는 사용자의 정의에 따라 고객이탈 가능성을 나타내는 0에서 100 사이의 [고객이탈 위험 점수]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score)가 할당됩니다. 점수가 높을수록 사용자가 고객이탈할 가능성이 높습니다. 

예측 오디언스의 위험 점수를 업데이트하는 것은 [선택한 빈도]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions)로 수행할 수 있습니다. 이렇게 하면 고객이탈 위험이 있는 사용자에게 실제로 이탈하기 전에 연락하여 이를 방지할 수 있습니다. 최대 세 개의 활성 예측을 사용하여 예측 이탈을 활용하여 가장 가치 있다고 생각되는 특정 사용자 세그먼트 내에서 고객이탈을 방지하기 위해 개별 모델을 맞춤화할 수 있습니다.

## 액세스 예측 이탈

**예측** 페이지는 **분석** 섹션에 위치해 있습니다. 전체 액세스를 위해 계정 매니저에게 문의하세요.

이 기능을 구매하기 전에 미리보기 모드에서 사용할 수 있습니다. 이것은 데모 고객이탈 예측을 합성 데이터로 보고, 한 번에 사용자 데이터에 기반한 고객이탈 예측 모델을 만들 수 있게 해줍니다. 이 미리보기는 고객이탈 위험에 따라 메시징을 위해 사용자를 타겟팅할 수 없으며 생성 후 정기적으로 업데이트되지 않습니다.

미리보기를 통해 하나의 예측을 편집하고 다시 빌드하거나 보관하여 다른 [정의]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)의 예상 [예측 품질]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/)을 테스트하기 위해 다른 것을 만들 수 있습니다.

<br><br>

[1]: {% image_buster /assets/img/churn/churn_overview.png %}
