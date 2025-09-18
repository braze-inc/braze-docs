---
nav_title: Kubit
article_title: Kubit 코호트 가져오기
description: "이 참조 문서에서는 즉각적인 제품 인사이트를 제공하는 코드 없는 셀프 서비스 분석 플랫폼인 Kubit의 코호트 가져오기 기능에 대해 설명하며, 이를 통해 Kubit 사용자 코호트를 가져와서 Braze 메시징에서 타겟팅할 수 있습니다."
page_type: partner
search_tag: Partner
---

# Kubit 코호트 가져오기

> 이 문서에서는 [Kubit에서](https://kubit.ai/) Braze로 사용자 코호트를 가져오는 방법에 대해 설명합니다. Kubit 및 기타 기능 통합에 대한 자세한 내용은 주요 [Kubit 문서]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/kubit/)를 참조하세요.

## 데이터 가져오기 통합

### 1단계: Braze 데이터 가져오기 키 받기

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Kubit**를 선택합니다. 여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성합니다. 

생성된 후에는 새 키를 생성하거나 기존 키를 무효화할 수 있습니다. 데이터 가져오기 키와 REST 엔드포인트는 Kubit의 대시보드에서 포스트백을 설정할 때 다음 단계에서 사용됩니다.

![Braze의 Kubit 기술 파트너 페이지]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### 2단계: Kubit에서 Braze 구성

Braze 데이터 가져오기 키와 Braze REST 엔드포인트를 Kubit 지원 담당자에게 제공합니다. 파트너 측에서 통합을 구성하고 통합이 활성화되면 알림을 제공합니다.  

### 3단계: Braze로 코호트 가져오기

#### Kubit에서 코호트 만들기
Kubit에서 [코호트를 생성](https://www.kubit.ai/doc/fundamentals#cohort)하고 타겟 사용자의 기준을 정의합니다.<br><br>![]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### 사용자를 Braze로 가져오기
코호트를 저장한 후에는 Braze로 가져와서 Braze 세그먼트에서 사용할 수 있습니다. 그런 다음 이러한 세그먼트를 사용하여 타겟 이메일 또는 푸시 캠페인과 캔버스를 만들 수 있습니다.

이를 위해 기존 코호트로 이동하여 **코호트 관리**에서 **Braze로 가져오기**를 선택합니다.

![]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

다음으로 원하는 가져오기 케이던스를 선택합니다. 이제 일회성 가져오기를 통해 한 번만 가져올 수 있습니다. 예약 가져오기를 사용하면 매일, 매주 또는 매월 특정 시간에 가져오기를 수행할 수 있습니다. 각 코호트에는 하나의 라이브 가져오기 스케줄만 포함될 수 있습니다. 

![]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

{% alert important %}
Braze 내에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에서 새로운 사용자를 생성하지 않습니다.
{% endalert %}

#### 가져오기 상태 확인
가져오기가 완료되면 가져오기 스케줄에 지정된 수신자에게 이메일 알림이 전송됩니다. Kubit의 **스케줄**에서 코호트의 가져오기 상태를 확인할 수도 있습니다. 스케줄 기록에는 모든 가져오기 실행 시간, 결과 및 Braze로 가져온 코호트의 총 사용자 수가 표시됩니다.<br><br>![]({% image_buster /assets/img/kubit/import_history.png %})<br><br>해당 가져오기 스케줄에 대해 **Braze로 가져오기** 아이콘을 클릭하여 가져오기를 수동으로 트리거할 수 있습니다.

### 4단계: Kubit 코호트로 Braze 세그먼트 만들기
코호트를 Braze로 가져온 후, 이를 필터로 사용하여 Braze 세그먼트를 생성하고 Braze 캠페인이나 캔버스에 포함할 수 있습니다. [Braze 세그먼트를 생성하는 방법]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment)에 대해 자세히 알아보려면 세그먼트 설명서를 참조하세요.

![Braze 세그먼트 빌더에서 사용자 속성 'Kubit 코호트'가 'includes_value'로 설정되어 있으며, 사용 가능한 코호트 목록을 표시합니다.]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## 사용자 일치

식별된 사용자는 `external_id` 또는 `alias`로 일치할 수 있습니다. 익명 사용자는 `device_id`로 매칭될 수 있습니다. 익명 사용자로 처음 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.