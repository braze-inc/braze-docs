---
nav_title: Amplitude
article_title: Amplitude 코호트 가져오기
description: "이 참조 문서에서는 제품 분석 및 비즈니스 인텔리전스 플랫폼인 Amplitude의 코호트 가져오기 기능을 간략히 설명합니다."
page_type: partner
search_tag: Partner
---

# Amplitude 코호트 가져오기

> 이 문서에서는 [Amplitude](https://amplitude.com/)에서 Braze로 사용자 코호트를 가져오는 방법을 다룹니다. Amplitude 및 기타 기능 통합에 대한 자세한 내용은 주요 [Amplitude 문서]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/)를 참조하세요.

## 데이터 가져오기 통합

설정한 모든 통합은 계정의 데이터 포인트 볼륨 계산에 포함됩니다.

### 1단계: Braze 데이터 가져오기 키 받기

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Amplitude**를 선택합니다. 여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성합니다. 

생성된 후에는 새 키를 만들거나 기존 키를 무효화할 수 있습니다. 데이터 가져오기 키와 REST 엔드포인트는 Amplitude의 대시보드에서 포스트백을 설정할 때 다음 단계에서 사용됩니다.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### 2단계: Amplitude에서 Braze 통합 설정

Amplitude에서 **소스 및 대상** > **[프로젝트 이름]** > **대상** > **Braze**로 이동합니다. 표시되는 프롬프트에서 Braze 데이터 가져오기 키와 REST 엔드포인트를 제공하고, **저장**을 클릭합니다.

![]({% image_buster /assets/img/amplitude.png %})

### 3단계: Amplitude 코호트를 Braze로 내보내기

먼저, Amplitude에서 Braze로 사용자를 내보내려면 내보내려는 사용자의 [코호트](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts)를 생성합니다. Amplitude는 다음 식별자를 사용하여 Braze에 코호트를 동기화할 수 있습니다:
- 사용자 별칭
- 기기 ID
- 사용자 ID (외부 ID)

코호트를 만든 후, **동기화...**을 클릭하여 이 사용자들을 Braze로 내보내세요.

{% alert important %}
Braze 내에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에서 새로운 사용자를 생성하지 않습니다.
{% endalert %}

#### 동기화 주기 정의

코호트 동기화는 일회성 동기화로 설정하거나, 매일 또는 매시간으로 예약하거나, 매분 업데이트되는 실시간으로도 설정할 수 있습니다. 비즈니스 요구 사항에 적합한 옵션을 선택하면서도 [데이터 포인트]({{site.baseurl}}/user_guide/data/data_points/)를 신중하게 소비하는 것을 잊지 마세요.

### 4단계: Braze에서 세그먼트 사용자

Braze에서 이러한 사용자의 세그먼트를 만들려면 **세그먼트**에서 **참여**로 이동하여 세그먼트 이름을 지정하고 필터로 **Amplitude 코호트**를 선택합니다. 다음으로, "포함" 옵션을 사용하고 Amplitude에서 생성한 코호트를 선택하십시오. 

![Braze 세그먼트 빌더에서 'amplitude_cohorts' 필터가 'includes_value' 및 'Amplitude cohort test'로 설정됩니다.]({% image_buster /assets/img/amplitude2.png %})

저장한 후에는 사용자 타겟팅 단계에서 캔버스 또는 캠페인을 생성하는 동안 이 세그먼트를 참조할 수 있습니다.

## 사용자 일치

식별된 사용자는 `external_id` 또는 `alias`로 일치할 수 있습니다. 익명 사용자는 `device_id`로 매칭될 수 있습니다. 익명 사용자로 처음 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.