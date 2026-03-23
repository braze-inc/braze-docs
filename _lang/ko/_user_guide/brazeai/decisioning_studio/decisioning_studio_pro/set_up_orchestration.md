---
nav_title: 오케스트레이션 설정
article_title: 오케스트레이션 설정
page_order: 2
description: "Decisioning Studio Pro 에이전트에 대한 오케스트레이션 구성을 통해 개인화된 커뮤니케이션을 인에이블먼트하는 방법을 알아보세요."
toc_headers: h2
---

# 오케스트레이션 설정

> 결정 에이전트는 고객 데이터를 수집하고 1:1 수준으로 개인화한 후 커뮤니케이션을 오케스트레이션하기 위해 고객 참여 플랫폼(CEP)에 연결해야 합니다. 이 문서는 지원되는 각 CEP에 대한 통합 설정 방법을 설명합니다.

## 지원되는 CEP

Decisioning Studio Pro는 다음 고객 참여 플랫폼을 지원합니다:

| CEP | 통합 유형 | 설정 복잡성 |
|-----|-----------------|------------------|
| **Braze** | 네이티브 API 통합 | 낮음 (권장) |
| **세일즈포스 마케팅 클라우드** | 네이티브 API 이벤트 + 여정 | 미디엄 |
| **클라비요** | 네이티브 API 이벤트 + 플로우 | 미디엄 |
| **기타 CEP** | 커스텀 (추천 파일) | 높음 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

아래에서 CEP를 선택하여 통합 설정을 시작하세요.

{% tabs %}
{% tab Braze %}

## Braze 통합 설정

다음 단계를 따라 Braze Decisioning Studio 에이전트를 Braze의 오케스트레이션 기능과 통합하십시오(Braze 서비스 팀이 지원해 드립니다):

### 1단계: API 키 생성

**설정** > **API 키**로 이동한 후, 다음 권한으로 새 키를 생성하세요:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### 2단계: API 트리거 캠페인 설정

각 기본 템플릿에 대해 모든 최적화된 차원에 대한 API 트리거 속성을 사용하여 API 트리거 캠페인을 설정하십시오.

기본 템플릿은 의사 결정 에이전트가 메시지 오케스트레이션을 위해 사용할 수 있는 모든 템플릿을 의미합니다. 결정 에이전트는 하나의 기본 템플릿을 가질 수도 있고 여러 개를 가질 수도 있습니다. 후자의 경우, 각 고객에게 적합한 기본 템플릿을 선택하는 것이 에이전트가 개인화하는 결정 사항 중 하나가 될 것입니다.

### 3단계: 재자격 부여 설정

모든 API 트리거 캠페인은 사용자가 15분 이내에 재적격 상태가 될 수 있도록 보장하십시오.

![결정 프로세스 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Decisioning Studio 에이전트는 동일한 캠페인을 하루에 한 번 이상 전송하지 않지만, 테스트 목적으로 동일한 캠페인을 하루에 여러 번 전송할 수 있는 기능이 필요합니다.
{% endalert %}

### 4단계: 동적 입력 안내 추가

이들은 Decisioning Studio 에이전트가 최적화하는 결정에 대한 동적 입력 안내 역할을 합니다.

#### 예시 1: 이메일 캠페인

Decisioning Studio 에이전트가 이메일 캠페인을 최적화하고 있다고 가정해 보자. 이렇게 구성할 수 있습니다:

![결정 프로세스 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

에이전트가 템플릿 선택과 행동 유도(CTA) 메시지 최적화를 목표로 한다면, 각 템플릿별로 API 트리거 캠페인을 생성해야 하며, 한 템플릿의 CTA 섹션은 다음과 같이 구성될 수 있습니다:

![결정 프로세스 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### 예시 2: 푸시 캠페인

결정 스튜디오 에이전트가 푸시 캠페인의 메시지를 최적화하고 있다고 가정해 보자. 이렇게 구성할 수 있습니다:

![결정 프로세스 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![결정 프로세스 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

다음과 같은 메시지가 표시됩니다:

![결정 프로세스 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### 예시 3: SMS 캠페인

Decisioning Studio 에이전트가 SMS 캠페인 내 필드에 대해 최적화를 수행한다고 가정합니다. 이렇게 구성할 수 있습니다:

![결정 프로세스 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![결정 프로세스 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

다음과 같은 메시지가 표시됩니다:

![결정 프로세스 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC 통합 설정

Decisioning Studio Pro는 Salesforce Marketing Cloud와의 네이티브 통합을 지원합니다. Decisioning Studio는 동적 요소를 채우기 위해 필요한 데이터와 함께 API 이벤트를 여정으로 트리거합니다.

SFMC의 오케스트레이션 설정은 Decisioning Studio Pro와 Decisioning Studio Go 모두에서 유사합니다. SFMC 통합을 구성하는 자세한 단계는 Decisioning Studio Go 설명서의 [SFMC 지침을]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) 따르십시오.

{% endtab %}
{% tab Klaviyo %}

## Klaviyo 통합 설정

Decisioning Studio Pro는 Klaviyo와의 네이티브 통합을 지원합니다. Decisioning Studio는 동적 요소를 채우기 위해 필요한 데이터와 함께 API 이벤트를 플로우로 트리거합니다.

Klaviyo의 오케스트레이션 설정은 Decisioning Studio Pro와 Decisioning Studio Go 모두에서 유사합니다. Klaviyo 통합을 구성하는 자세한 단계는 Decisioning Studio Go 설명서의 [Klaviyo 지]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)침을 따르십시오.

{% endtab %}
{% tab Other CEPs %}

## 기타 CEP 통합 설정

디시전닝 스튜디오는 모든 고객 참여 플랫폼과 통합할 수 있습니다. 그러나 Decisioning Studio는 직접 커뮤니케이션을 트리거할 수 없기 때문에, 이를 위해서는 귀사 팀의 커스텀 엔지니어링 작업이 필요할 수 있습니다.

이 시나리오에서 에이전트는 "추천 파일"을 전달할 것입니다. 이 파일에는 각 고객에게 대한 행이 포함되어 있으며, 해당 고객에게 대한 모든 개인화된 결정을 나타내는 열이 있습니다.

예를 들어, 다음 추천 파일:

![결정 프로세스 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

다음과 같은 이메일 캠페인을 최적화하는 데 사용될 수 있습니다:

![결정 프로세스 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## 다음 단계

오케스트레이션을 설정한 후 에이전트 설계를 진행하십시오:

- [에이전트 설계]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

