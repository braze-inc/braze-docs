---
nav_title: Heap
article_title: "Heap 분석"
description: "이 참조 문서는 Braze 커런츠를 사용하여 디지털 인사이트 플랫폼인 Heap과 함께 참여 이벤트를 자동으로 분석하는 방법을 설명합니다. 이를 통해 Heap 데이터를 Braze로 가져오고, 사용자 코호트를 생성하며, Braze 데이터를 Heap으로 내보내어 세그먼트를 생성할 수 있습니다."
page_type: partner
search_tag: Partner


---

# Heap 분석

> 이 문서에서는 Braze에서 Heap으로 인게이지먼트 이벤트를 자동으로 전송하여 분석하는 방법을 설명합니다. Heap 및 기타 기능(예: [Heap 코호트 동기화]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/#data-import-integration)를 Braze에 연결)에 대한 자세한 내용은 주요 [Heap 기사]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/)를 참조하세요.

## 데이터 내보내기 통합

Braze 커런츠를 사용하여 분석을 위해 Braze에서 Heap으로 인게이지먼트 이벤트(예: 이메일 전송, 푸시 전송)를 자동으로 전송합니다.

### 1단계: 힙 자격 증명 얻기

이 통합을 구성하려면 웹훅 엔드포인트 URL이 필요하며, 이 URL은 Heap 계정 매니저로부터 받을 수 있습니다.

### 2단계: Braze 커런츠 구성

Braze에서 **파트너 통합** > **데이터 내보내기**로 이동하여 **새 현재 만들기**를 클릭하고 **Heap 내보내기**를 선택합니다. 

내보내기에 이름을 지정한 다음 **현재 세부 정보** 페이지로 이동하십시오. 이 페이지에서 엔드포인트와 선택적 베어러 토큰(제공된 경우)을 입력하세요.

통합의 자격 증명을 구성한 후, Heap에 내보내고자 하는 모든 메시지 인게이지먼트, 고객 행동 및 사용자 이벤트를 확인하고 **커런츠 시작**을 클릭합니다.

![][5]{: style="max-width:90%;"}

[5]: {% image_buster /assets/img/heap/heap4.png %} 
