---
nav_title: 오케스트레이션 설정하기
article_title: 오케스트레이션 설정하기
page_order: 2
description: "개인화된 커뮤니케이션을 인에이블하기 위해 디시전킹 스튜디오 프로 상담원을 위한 오케스트레이션을 구성하는 방법을 알아보세요."
toc_headers: h2
---

# 오케스트레이션 설정하기

> 의사 결정 에이전트는 고객 데이터를 수집하고 1:1 수준에서 개인화된 커뮤니케이션을 오케스트레이션하기 위해 고객 참여 플랫폼(CEP)에 연결해야 합니다. 이 문서에서는 지원되는 각 CEP에 대해 통합을 설정하는 방법을 설명합니다.

## 지원되는 CEP

디시전킹 스튜디오 프로는 다음과 같은 고객 참여 플랫폼을 지원합니다:

| CEP | 통합 유형 | 설정 복잡성 |
|-----|-----------------|------------------|
| **Braze** | 네이티브 API 통합 | 낮음(권장) |
| **Salesforce 마케팅 클라우드** | 네이티브 API 이벤트 + 여정 | 미디엄 |
| **클라비요** | 네이티브 API 이벤트 + 플로우 | 미디엄 |
| **기타 CEP** | 커스텀(추천 파일) | 높음 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

통합 설정을 시작하려면 아래에서 해당 CEP를 선택하세요.

{% tabs %}
{% tab Braze %}

## Braze 통합 설정하기

다음 단계에 따라 Braze 디시전 스튜디오 에이전트를 Braze의 오케스트레이션 기능과 통합하세요(Braze의 서비스 팀이 도움을 드릴 수 있습니다):

### 1단계: API 키 생성

**설정** > **API 키로** 이동한 다음 다음 권한으로 새 키를 만듭니다:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### 2단계: API 트리거 캠페인 설정하기

최적화된 모든 차원에 대한 API 트리거 속성을 사용하여 각 기본 템플릿에 대해 API 트리거 캠페인을 설정하세요.

기본 템플릿은 의사 결정 에이전트가 메시지를 오케스트레이션하는 데 사용할 수 있는 모든 템플릿입니다. 의사 결정 상담원은 기본 템플릿을 하나 또는 여러 개 가질 수 있으며, 이 경우 각 고객에게 적합한 기본 템플릿을 선택하는 것이 상담원이 개인화하는 의사 결정 중 하나가 됩니다.

### 3단계: 재적격성 구성

모든 API 트리거 캠페인에서 사용자가 15분 이내에 다시 자격을 얻을 수 있도록 하세요.

![의사 결정 프로 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
디시전킹 스튜디오 에이전트는 하루에 한 번 이상 같은 캠페인을 보내지 않지만, 테스트 목적으로 하루에 여러 번 같은 캠페인을 보낼 수 있는 기능을 원할 수 있습니다.
{% endalert %}

### 4단계: 동적 입력 안내자 추가하기

이는 Decisioning Studio 에이전트가 최적화 중인 의사 결정에 대한 동적 입력 안내 역할을 합니다.

#### 예 1: 이메일 캠페인

Decisioning Studio 상담원이 이메일 캠페인을 최적화하고 있다고 가정해 보겠습니다. 다음과 같이 구성할 수 있습니다:

![의사 결정 프로 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

에이전트가 선택한 템플릿과 CTA(클릭 유도 문안) 메시지에 최적화되어 있다고 가정하면 각 템플릿에 대해 API 트리거된 캠페인이 만들어져야 하며, 한 템플릿의 CTA 섹션은 다음과 같이 보일 수 있습니다:

![의사 결정 프로 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### 예 2: 푸시 캠페인

의사 결정 스튜디오 에이전트가 푸시 캠페인의 메시지를 최적화하고 있다고 가정해 보겠습니다. 다음과 같이 구성할 수 있습니다:

![의사 결정 프로 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![의사 결정 프로 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

다음 메시징이 표시됩니다:

![의사 결정 프로 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### 예 3: SMS 캠페인

Decisioning Studio 에이전트가 SMS 캠페인의 필드에 대해 최적화하고 있다고 가정해 보겠습니다. 다음과 같이 구성할 수 있습니다:

![의사 결정 프로 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![의사 결정 프로 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

다음 메시징이 표시됩니다:

![의사 결정 프로 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC 통합 설정하기

Decisioning Studio Pro는 Salesforce 마케팅 클라우드와의 기본 통합을 지원합니다. Decisioning Studio는 동적 요소를 채우는 데 필요한 데이터가 있는 여정으로 API 이벤트를 트리거합니다.

SFMC의 오케스트레이션 설정은 디시전킹 스튜디오 프로와 디시전킹 스튜디오 고 모두 비슷합니다. SFMC 통합을 구성하는 자세한 단계는 Decisioning Studio Go 설명서에 있는 [SFMC 지침을]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) 따르세요.

{% endtab %}
{% tab Klaviyo %}

## 클라비요 통합 설정하기

디시전킹 스튜디오 프로는 클라비요와의 기본 통합을 지원합니다. Decisioning Studio는 동적 요소를 채우는 데 필요한 데이터가 있는 흐름으로 API 이벤트를 트리거합니다.

클라비요의 오케스트레이션 설정은 디시전킹 스튜디오 프로와 디시전킹 스튜디오 고 모두 비슷합니다. 클라비요 통합을 구성하는 자세한 단계는 Decisioning Studio Go 설명서에 있는 [클라비요 지침을]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) 따르세요.

{% endtab %}
{% tab Other CEPs %}

## 다른 CEP 통합 설정하기

Decisioning Studio는 모든 고객 참여 플랫폼과 통합할 수 있습니다. 하지만 Decisioning Studio는 커뮤니케이션을 직접 트리거할 수 없으므로 팀의 커스텀 엔지니어링 작업이 필요할 수 있습니다.

이 시나리오에서는 상담원이 "추천 파일"을 전달합니다. 이 파일에는 각 고객에 대한 행과 해당 고객에 대한 모든 개인화된 결정을 나타내는 열이 포함되어 있습니다.

예를 들어 다음 권장 사항 파일이 있습니다:

![의사 결정 프로 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

다음과 같은 이메일 캠페인을 최적화하는 데 사용할 수 있습니다:

![의사 결정 프로 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## 다음 단계

오케스트레이션을 설정한 후 상담원 디자인을 진행합니다:

- [에이전트 설계]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

