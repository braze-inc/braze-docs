---
nav_title: Census
article_title: Census 코호트 가져오기
description: "이 참조 문서에서는 클라우드 창고의 데이터를 사용하여 대상 사용자 세그먼트를 동적으로 생성할 수 있는 데이터 통합 플랫폼인 Census의 코호트 가져오기 기능을 설명합니다."
page_type: partner
search_tag: Partner

---

# Census 코호트 가져오기

> 이 문서에서는 [Census][1]에서 Braze로 사용자 코호트를 가져오는 방법을 설명합니다. Census 통합에 대한 자세한 내용은 기본 [Census 문서]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/census/)를 참조하세요.

## 코호트 가져오기 통합

### 1단계: Braze 서비스 연결 만들기

Census 플랫폼에 Census를 통합하려면 **연결** 탭으로 이동하고 **새 대상**을 선택하여 새 Braze 서비스 연결을 생성합니다.

표시되는 프롬프트에서 이 연결의 이름을 지정하고 Braze 엔드포인트 URL, Braze REST API 키 및 데이터 가져오기 키를 제공합니다. 데이터 가져오기 키는 코호트를 동기화하는 데 필요하며 **파트너 통합** > **기술 파트너** > **Census**에서 Braze에서 찾을 수 있습니다.

![][8]{: style="max-width:60%;"}

### 2단계: 인구조사 동기화 만들기

고객을 Braze에 동기화하려면 동기화를 구축해야 합니다. 여기에서 데이터 동기화 위치와 두 플랫폼 간 필드 매핑 방법을 정의합니다.

1. **동기화** 탭으로 이동하여 **새 동기화를** 선택합니다.<br><br> 
2. 작성기에서 데이터 웨어하우스의 소스 데이터 모델을 선택합니다.<br><br>
3. 모델이 동기화될 위치를 구성합니다. **Braze**를 대상으로 선택하고 **User & 코호트**를 동기화할 객체로 선택합니다.<br>!['대상 선택' 프롬프트에서 'Braze'가 연결로 선택되고 다양한 오브젝트가 나열됩니다.][10]{: style="max-width:80%;"}<br><br>
4. **소스 열**을(를) 선택하여 코호트에 추가할 사용자를 식별하고, **외부 사용자 ID**를 **식별자 유형**으로 선택합니다.<br><br>
5. **코호트 이름** 드롭다운에서 코호트를 선택하거나, 코호트를 생성하거나, 코호트 이름을 채우기 위해 소스 열을 선택하십시오.<br><br>
6. **소스 데이터에서 레코드가 제거될 때** 드롭다운을 사용하여 소스 데이터 세트에서 제거될 때 사용자에게 나타나는 현상을 선택합니다. 예를 들어, **아무 작업도 안 함** 또는 **코호트에서 일치하는 레코드 제거**와 같은 옵션이 있습니다.<br><br>
7. 마지막으로, Census 데이터 필드를 해당하는 Braze 필드에 매핑합니다.<br>![인구조사 매핑][11]{: style="max-width:80%;"}<br><br>
8. 세부 사항을 확인하고 동기화를 만드십시오. 

이제 동기화를 실행할 수 있습니다!

동기화 중에 매핑한 모든 필드는 먼저 사용자 오브젝트에 동기화되어 Braze에 이미 존재하는 항목을 업데이트합니다. 그 후, 업데이트된 사용자가 지정된 코호트에 추가됩니다.

동기화 후, Braze 세그먼트를 생성하고 Census 코호트 필터와 함께 추가하여 향후 Braze 캠페인 및 캔버스에서 해당 사용자를 타겟팅할 수 있습니다. 

{% alert note %}
Census 및 Braze 통합을 사용할 때, Census는 각 동기화에서 Braze에 델타(변경 데이터)만 전송합니다.
{% endalert %}

{% alert important %}
Braze 내에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에서 새로운 사용자를 생성하지 않습니다.
{% endalert %}

## 사용자 매칭

식별된 사용자는 `external_id` 또는 `alias` 으로 일치시킬 수 있습니다. 익명 사용자는 `device_id`. 원래 익명 사용자로 생성된 식별된 사용자는 `device_id` 으로 식별할 수 없으며 `external_id` 또는 `alias` 으로 식별해야 합니다.

[1]: https://www.getcensus.com/
[8]: {% image_buster /assets/img/census/add_service.png %}
[10]: {% image_buster /assets/img/census/census_2.png %}
[11]: {% image_buster /assets/img/census/census_3.png %}