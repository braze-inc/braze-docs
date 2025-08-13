---
nav_title: Hightouch
article_title: 하이터치 코호트 가져오기
description: "이 참조 문서에서는 고객 데이터를 웨어하우스에서 비즈니스 툴로 동기화하는 플랫폼인 Hightouch의 코호트 가져오기 기능을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---
# 하이터치 코호트 가져오기

> 이 문서에서는 웨어하우스에만 존재할 수 있는 데이터를 기반으로 타겟팅 캠페인을 보낼 수 있도록 [Hightouch][1]에서 Braze로 사용자 코호트를 가져오는 방법을 설명합니다. Hightouch 및 기타 기능 통합에 대한 자세한 내용은 주요 [Hightouch 문서]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/hightouch/)를 참조하세요.

## 데이터 가져오기 통합

### 1단계: Braze 데이터 가져오기 키 받기
Braze에서 **파트너 통합** > **기술 파트너**로 이동하고 **Hightouch**를 선택합니다. 

여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성합니다. 키가 생성된 후에는 새 키를 생성하거나 기존 키를 무효화할 수 있습니다.<br><br>![][6]{: style="max-width:90%;"} 

### 2단계: Hightouch에서 Braze 코호트를 대상으로 추가
하이터치 작업 공간에서 **대상** 페이지로 이동하여 **Braze 코호트를** 검색한 다음 **계속을** 클릭합니다. 여기에서 REST 엔드포인트와 데이터 가져오기 키를 가져오고 **계속**을 클릭합니다.<br><br>![][7]{: style="max-width:90%;"}

### 3단계: 모델(또는 대상)을 Braze 코호트에 동기화하기
Hightouch에서 생성한 [모델](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) 또는 [오디언스](https://hightouch.io/docs/audiences/usage/)를 사용하여 새 동기화를 생성합니다. 다음으로, 이전 단계에서 생성한 Braze 코호트 대상을 선택합니다. 마지막으로, Braze 코호트 대상 구성에서 일치시킬 식별자를 선택하고 Hightouch가 새 Braze 코호트를 생성할지, 기존 코호트를 업데이트할지 여부를 결정합니다.<br><br>![][8]{: style="max-width:90%;"}

{% alert important %}
Braze 내에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에서 새로운 사용자를 생성하지 않습니다.
{% endalert %}

### 4단계: Hightouch 커스텀 오디언스에서 Braze 세그먼트 생성
Braze에서 **세그먼트로** 이동하여 새 세그먼트를 생성하고 필터로 **하이터치 코호트를** 선택합니다. 여기에서 포함할 Hightouch 코호트를 선택할 수 있습니다. 하이터치 코호트 세그먼트가 생성된 후에는 캠페인이나 캔버스를 만들 때 오디언스 필터로 선택할 수 있습니다.<br><br>![][9]{: style="max-width:90%;"}

### 이 통합 사용
하이터치 세그먼트를 사용하려면 Braze 캠페인 또는 캔버스를 생성하고 세그먼트를 타겟 오디언스로 선택합니다.<br><br>![][10]{: style="max-width:90%;"}

## 사용자 일치

식별된 사용자는 `external_id` 또는 `alias`로 일치할 수 있습니다. 익명 사용자는 `device_id`로 매칭될 수 있습니다. 익명 사용자로 처음 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.

[1]: https://hightouch.io
[6]: {% image_buster /assets/img/hightouch/data_import_key.png %}
[7]: {% image_buster /assets/img/hightouch/cohort1.png %}
[8]: {% image_buster /assets/img/hightouch/cohort2.png %}  
[9]: {% image_buster /assets/img/hightouch/cohort3.png %}  
[10]: {% image_buster /assets/img/hightouch/cohort4.png %}  