---
nav_title: Mixpanel
article_title: Mixpanel 코호트 가져오기
description: "이 참조 문서에서는 비즈니스 분석 플랫폼인 Mixpanel의 코호트 가져오기 기능을 설명하며, Mixpanel 코호트를 Braze로 가져와서 향후 Braze 캠페인 또는 캔버스에서 사용자를 타겟팅하는 데 사용할 수 있는 Braze 세그먼트를 생성할 수 있습니다."
page_type: partner
search_tag: Partner
---

# Mixpanel 코호트 가져오기

> 이 문서에서는 [Mixpanel](https://mixpanel.com/)에서 Braze로 사용자 코호트를 가져오는 방법을 설명합니다. Mixpanel 및 기타 기능 통합에 대한 자세한 내용은 주요 [Mixpanel 문서]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/mixpanel_for_currents/)를 참조하세요.

## 데이터 가져오기 통합

설정한 모든 통합은 계정의 데이터 포인트 볼륨 계산에 포함됩니다.

{% alert important %}
Mixpanel의 데이터 유지 정책에 따라 2010년 1월 1일 이전에 전송된 이벤트는 가져오는 중에 제거됩니다.
{% endalert %}

### 1단계: Braze 데이터 가져오기 키 가져오기

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Mixpanel**을 선택합니다. 여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성합니다. 

생성된 후에는 새 키를 만들거나 기존 키를 무효화할 수 있습니다. 데이터 가져오기 키와 REST 엔드포인트는 Mixpanel의 대시보드에서 포스트백을 설정할 때 다음 단계에서 사용됩니다.<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### 2단계: Mixpanel에서 Braze 통합 설정

Mixpanel에서 **데이터 관리 > 통합**로 이동합니다. 다음으로, Braze 통합 탭을 선택하고 **연결**을 클릭하세요. 표시되는 프롬프트에서 Braze 데이터 가져오기 키와 REST 엔드포인트를 제공하고, **계속**을 클릭합니다.

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### 3단계: Mixpanel 코호트를 Braze로 내보내기

Mixpanel에서 **데이터 관리 > 코호트**로 이동합니다. Braze로 보낼 코호트를 선택한 다음 **Braze로 내보내기**를 선택합니다. 마지막으로 일회성 동기화 또는 동적 동기화를 선택하십시오. 동적 동기화를 선택하면 Braze 코호트가 15분마다 Mixpanel의 사용자와 일치하도록 동기화됩니다. 

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

{% alert important %}
Braze 내에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에서 새로운 사용자를 생성하지 않습니다.
{% endalert %}

### 4단계: Braze에서 세그먼트 사용자

Braze에서 이러한 사용자의 세그먼트를 만들려면 **오디언스** > **세그먼트로** 이동하여 세그먼트의 이름을 지정하고 필터로 **Mixpanel_Cohorts를** 선택합니다. 다음으로, '포함' 옵션을 사용하고 Mixpanel에서 생성한 코호트를 선택합니다. 

![Braze 세그먼트 빌더에서 사용자 속성 필터 'Mixpanel 코호트'가 '포함' 및 'Braze 코호트'로 설정됩니다.]({% image_buster /assets/img_archive/mixpanel1.png %})

저장한 후에는 사용자 타겟팅 단계에서 캔버스 또는 캠페인을 생성하는 동안 이 세그먼트를 참조할 수 있습니다.

## 사용자 일치

식별된 사용자는 `external_id` 또는 `alias`로 일치할 수 있습니다. 익명 사용자는 `device_id`로 매칭될 수 있습니다. 익명 사용자로 처음 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.