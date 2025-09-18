---
nav_title: Heap
article_title: Heap
description: "이 참조 문서에서는 디지털 인사이트 플랫폼인 Heap과 Braze 간의 통합을 자세히 설명합니다. 이를 통해 Heap 데이터를 Braze로 가져오고, 사용자 코호트를 생성하며, Braze 데이터를 Heap으로 내보내 세그먼트를 생성할 수 있습니다."
alias: /partners/heap/
page_type: partner
search_tag: Partner

---

# Heap

> 디지털 인사이트 플랫폼인 [Heap은](https://heap.io/) 디지털 경험에서 비즈니스에 가장 큰 영향을 미치는 기회에 집중하여 마찰을 없애고 고객을 만족시키며 수익을 가속화합니다.

Braze와 Heap의 통합을 통해 [Heap 데이터를 Braze로 가져오고](#data-import-integration), 사용자 코호트를 생성할 수 있을 뿐만 아니라, [Braze 데이터를 Heap으로 내보내]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/heap/) 세그먼트를 생성할 수도 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Heap 계정 | 이 파트너십을 이용하려면 [Heap](https://heap.io/about) 계정이 필요합니다. |
| Braze 데이터 가져오기 키 | 이 정보는 Braze 대시보드의 **파트너 통합** > **기술 파트너**에서 **Heap**을 선택하여 캡처할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][1]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
| Braze 커런츠 | Braze에서 Heap으로 데이터를 내보내려면 계정에서 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)가 활성화되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례
- 퍼널을 이탈한 사용자의 재참여를 유도하세요: 사용자가 구매 또는 구독 퍼널을 포기하면 재참여 메시지를 트리거합니다.
- 평가판 환경 개인화: 평가판 경험의 마찰 지점을 파악하고 정확한 타이밍에 알림을 보내 평가판 기간 동안 사용자의 재참여를 유도하고 가치를 실현할 수 있도록 도와주세요.
- 공지사항과 오퍼에 대한 참여도를 높이세요: 프로모션, 업데이트 및 새로운 서비스 공지를 관련 오디언스에 타겟팅합니다.

## 데이터 가져오기 통합

Braze로 Heap 통합을 사용하여 Heap에 정의된 코호트를 Braze에 자동으로 동기화할 수 있습니다.

### 1단계: Braze 데이터 가져오기 키 가져오기

Braze에서 **파트너 통합** > **기술 파트너**로 이동한 다음, **Heap**을 선택합니다. 

이 페이지에서 데이터 가져오기 키와 REST 엔드포인트를 찾을 수 있습니다. 이 두 값을 모두 기록해 두었다가 Heap 계정 매니저에게 제공하면 통합 설정을 완료할 수 있습니다.

![][3]{: style="max-width:90%;"}

### 2단계: Braze에서 가져온 사용자 세분화

Braze에서 **세그먼트**로 이동하고 Heap 코호트 세그먼트의 이름을 지정한 후 **Heap 코호트**를 필터로 선택합니다. 여기에서 포함할 힙 코호트를 선택할 수 있습니다. 힙 코호트 세그먼트가 생성된 후에는 캠페인이나 캔버스를 만들 때 오디언스 필터로 선택할 수 있습니다.

![Braze 세그먼트 빌더에서 사용자 속성 필터 'Heap 코호트'는 '포함' 및 'Heap 테스트 코호트'로 설정되어 있습니다.][2]{: style="max-width:90%;"}

### 이 통합 사용

힙 세그먼트를 사용하려면 Braze 캠페인 또는 캔버스를 생성하고 세그먼트를 타겟 오디언스로 선택합니다.

![타겟팅 단계의 Braze 캠페인 빌더에서 '세그먼트별 타겟 사용자' 필터가 'Heap 코호트'로 설정되어 있습니다.][4]{: style="max-width:90%;"}

{% alert important %}
Braze 내에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에서 새로운 사용자를 생성하지 않습니다.
{% endalert %}

## 통합 세부 정보

내보낸 데이터의 페이로드 구조는 커스텀 HTTP 커넥터의 페이로드 구조와 동일하며, [커스텀 HTTP 커넥터의 예제 리포지토리](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)에서 확인할 수 있습니다.

## 사용자 일치

식별된 사용자는 `external_id` 또는 `alias`로 일치할 수 있습니다. 익명 사용자는 `device_id`로 매칭될 수 있습니다. 익명 사용자로 처음 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/heap/heap1.png %}
[3]: {% image_buster /assets/img/heap/heap2.png %}
[4]: {% image_buster /assets/img/heap/heap3.png %} 
