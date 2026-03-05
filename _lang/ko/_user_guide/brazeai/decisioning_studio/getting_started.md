---
nav_title: 시작하기
article_title: 의사 결정 스튜디오 시작하기
layout: dev_guide
guide_top_header: "의사 결정 스튜디오 시작하기"
guide_top_text: "의사 결정 에이전트를 만들기 전에 다음 문서를 참조하여 의사 결정 스튜디오에 대한 계획을 세우고 이해하세요."
page_order: 0
search_rank: 2
page_type: landing
description: "이 섹션에서는 의사 결정 스튜디오에 대한 소개와 이를 사용하여 모든 비즈니스 측정기준을 최적화하는 의사 결정 에이전트를 디자인하고 배포하는 방법에 대해 설명합니다."

guide_featured_title: "섹션 기사"
guide_featured_list:
  - name: 데이터 소스 준비하기
    link: /docs/user_guide/brazeai/decisioning_studio/preparing_your_data_sources/
    image: /assets/img/braze_icons/database-01.svg
  - name: 오케스트레이션 준비하기
    link: /docs/user_guide/brazeai/decisioning_studio/preparing_your_orchestration/
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: 의사 결정 에이전트 설계
    link: /docs/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/
    image: /assets/img/braze_icons/settings-01.svg

guide_menu_title: "Additional resources"
guide_menu_list:
  - name: 디시전 스튜디오 정보
    link: /docs/user_guide/brazeai/decisioning_studio/about/
    image: /assets/img/braze_icons/info-circle.svg
  - name: 의사 결정 스튜디오 FAQ
    link: /docs/user_guide/brazeai/decisioning_studio/faq/
    image: /assets/img/braze_icons/annotation-question.svg
---

# 의사 결정 스튜디오 시작하기

> 이 참조 자료에서는 데이터 소스 연결, 오케스트레이션 설정, 의사 결정 에이전트 디자인 등 Decisioning Studio 설정에 관련된 단계에 대한 개요를 제공합니다.

BrazeAI Decisioning Studio™를 사용하면 모든 비즈니스 측정기준을 최적화하는 의사 결정 에이전트를 설계하고 배포할 수 있습니다. 의사 결정 에이전트는 특정 비즈니스 목표를 달성하기 위해 맞춤화된 커스텀 구성입니다.

이를 위해서는 데이터 소스를 연결하고, 오케스트레이션을 설정하고, 의사 결정 에이전트를 디자인해야 합니다.

{% alert tip %}
디시전킹 스튜디오 프로 고객의 경우, AI 전문가 서비스 팀이 최적의 성능/성과를 위해 디시전킹 스튜디오를 설정할 수 있도록 지원합니다.
{% endalert %}

## 의사 결정 스튜디오 설정

Decisioning Studio를 설정하려면 다음 단계를 완료합니다:

### 1단계: 데이터 소스 연결

고객 프로필과 고객 참여 데이터를 연결하여 생성한 의사 결정 에이전트가 각 고객이 누구인지, 어떻게 행동하는지 이해할 수 있도록 하세요.

일반적으로 데이터 소스는 Decisioning Studio를 처음 설정하는 동안 한 번만 연결하면 됩니다. 나중에 사용 사례를 확장하는 경우 새 데이터 소스를 추가해야 할 수도 있습니다.

{% alert tip %}
이미 [Braze 데이터 플랫폼에]({{site.baseurl}}/user_guide/data/braze_data_platform) 있는 모든 데이터는 Decisioning Studio에서 자동으로 사용할 수 있습니다.
{% endalert %}

자세한 지침은 해당 Decisioning Studio 티어에 대한 설명서를 참조하세요:
- [의사 결정 스튜디오 이동: 데이터 소스 연결]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [디시전 스튜디오 프로: 데이터 소스 연결]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)

### 2단계: 오케스트레이션 설정하기

Decisioning Studio를 고객 참여 플랫폼(CEP)과 통합하여 상담원이 작업을 오케스트레이션할 수 있도록 하세요. CEP는 상담원의 결정에 따라 고객에게 개인화된 경험을 제공하는 데 사용되는 플랫폼입니다.

일반적으로 이 오케스트레이션은 한 번만 설정하면 됩니다.

자세한 지침은 해당 Decisioning Studio 티어에 대한 설명서를 참조하세요:
- [의사 결정 스튜디오 이동: 오케스트레이션 설정하기]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [디시전 스튜디오 프로: 오케스트레이션 설정하기]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

### 3단계: 상담원 디자인

의사 결정 에이전트를 구성하여 최대화하려는 결과와 이를 달성하기 위해 에이전트가 취할 수 있는 조치를 정의하세요. 상담원 디자인에 대한 자세한 안내는 [의사 결정 상담원 디자인]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/) 하기를 참조하세요.

티어별 안내를 참조하세요:
- [의사 결정 스튜디오 이동: 에이전트 디자인]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
- [디시전 스튜디오 프로: 에이전트 디자인]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

{% alert tip %}
의사 결정 스튜디오 프로 고객의 경우 AI 의사 결정 서비스 팀이 의사 결정 에이전트를 설계하고 출시할 수 있도록 지원합니다.
{% endalert %}

### 4단계: 의사 결정 에이전트 시작

의사 결정 에이전트를 실행하여 비즈니스 결과에 맞게 지속적으로 학습하고 최적화하도록 하세요.

자세한 지침은 해당 Decisioning Studio 티어에 대한 설명서를 참조하세요:
- [의사 결정 스튜디오 이동: 상담원 시작하기]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)
- [디시전 스튜디오 프로: 상담원 시작하기]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)

## 다음 단계

이제 의사 결정 스튜디오의 주요 개념을 기본적으로 이해했으므로 이제 의사 결정 에이전트 디자인을 시작할 수 있습니다.

- [의사 결정 에이전트 설계]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/)
