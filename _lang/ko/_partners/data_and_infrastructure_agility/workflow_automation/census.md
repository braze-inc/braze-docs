---
nav_title: Census
article_title: Census
description: "이 참조 문서에서는 클라우드 웨어하우스의 데이터로 타겟 사용자 세그먼트를 동적으로 생성할 수 있는 데이터 통합 플랫폼인 Braze와 Census 간의 파트너십에 대해 설명합니다."
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# Census

> [Census][1]는 데이터 활성화 플랫폼으로 Snowflake, BigQuery 등의 클라우드 데이터 웨어하우스를 Braze에 연결합니다. 이를 통해 마케팅 팀은 퍼스트파티 데이터의 강점을 인지하여 동적 오디언스 세그먼트를 구축하고, 캠페인 개인화를 위해 고객 속성을 동기화하며, Braze의 모든 데이터를 최신 상태로 유지할 수 있습니다. 또한 CSV 업로드나 엔지니어링 관련 요청을 하지 않아도 되므로, 신뢰할 수 있고 실행 가능한 데이터로 조치를 취하기가 그 어느 때보다도 쉬워졌습니다.

Braze와 Census의 통합을 통해 오디언스 또는 제품 데이터를 Braze로 동적으로 가져와 개인화된 캠페인을 전송할 수 있습니다. 예를 들어, Braze에서 높은 가치의 고객을 타겟팅하기 위해 'CLV가 1,000이 넘는 뉴스레터 가입자'에 대한 코호트를 생성하거나 향후 베타 기능을 테스트할 특정 사용자를 타겟팅하기 위해 '지난 30일 동안 활성 사용자'에 대한 코호트를 생성할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| --- | --- |
| 인구조사 계정 | 이 파트너십을 활용하려면 [Census 계정][1]이 필요합니다. |
| Braze REST API 키 | 모든 사용자 데이터 권한(`users.delete`) 및 `segments.list` 권한이 있는 Braze REST API 키. Census가 더 많은 Braze 개체에 대한 지원을 추가함에 따라 권한 세트가 변경될 수 있으므로 지금 더 많은 권한을 부여하거나 향후에 이러한 권한을 업데이트할 계획을 세울 수 있습니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트  | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에][2] 따라 달라집니다. |
| 데이터 웨어하우스 및 데이터 모델 | 통합을 시작하기 전에 Census에 데이터 웨어하우스가 설정되어 있어야 하며, Braze에 동기화하려는 데이터 하위 집합의 모델을 정의해야 합니다. 사용 가능한 데이터 소스 목록과 모델 생성에 대한 지침은 [인구주택총조사 설명서를](https://docs.getcensus.com/destinations/braze) 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 통합

### 1단계: Braze 서비스 연결 만들기

Census 플랫폼에 Census를 통합하려면 **연결** 탭으로 이동하고 **새 대상**을 선택하여 새 Braze 서비스 연결을 생성합니다.

표시되는 프롬프트에서 이 연결의 이름을 지정하고 Braze 엔드포인트 URL, Braze REST API 키 및 선택적으로 코호트를 동기화할 데이터 가져오기 키를 제공합니다.

![][8]{: style="max-width:60%;"}

### 2단계: 인구조사 동기화 만들기

고객을 Braze에 동기화하려면 동기화를 구축해야 합니다. 여기에서 데이터 동기화 위치와 두 플랫폼 간 필드 매핑 방법을 정의합니다.

1. **동기화** 탭으로 이동하여 **새 동기화를** 선택합니다.<br><br> 
2. 작성기에서 데이터 웨어하우스의 소스 데이터 모델을 선택합니다.<br><br>
3. 모델을 동기화할 위치를 구성합니다. 대상으로 **Braze**를 선택하고 동기화할 [지원되는 오브젝트 유형](#supported-objects)을 선택합니다.<br>!['대상 선택' 프롬프트에서 'Braze'가 연결로 선택되고 다양한 오브젝트가 나열됩니다.][10]{: style="max-width:80%;"}<br><br>
4. 적용할 동기화 규칙을 선택합니다. **업데이트 또는 생성**이 가장 일반적인 선택이지만, 데이터 삭제 등을 처리하기 위해 고급 규칙을 선택할 수도 있습니다.<br><br>
5. 다음으로, 레코드 매칭을 위해 동기화 키를 선택하여 Braze 개체를 모델 필드에 [매핑합니다](#supported-objects).<br>!['동기화 키 선택' 프롬프트에서 Braze의 '외부 사용자 ID'를 소스의 'user_id'와 일치시킵니다.][9]{: style="max-width:80%;"}<br><br>
6. 마지막으로, Census 데이터 필드를 동등한 Braze 필드에 매핑합니다.<br>![인구조사 매핑][11]{: style="max-width:80%;"}<br><br>
7. 세부 정보를 확인하고 동기화를 생성합니다. 

동기화가 실행되면 Braze에서 사용자 데이터를 찾을 수 있습니다. 이제 Braze 세그먼트를 생성하고 향후 Braze 캠페인 및 캔버스에 추가하여 이러한 사용자를 타겟팅할 수 있습니다. 

{% alert note %}
Census 및 Braze 통합을 사용할 때, Census는 각 동기화에서 Braze에 델타(변경 데이터)만 전송합니다.
{% endalert %}

## 지원되는 개체

Census는 현재 다음과 같은 Braze 오브젝트의 동기화를 지원합니다:

| 개체 이름 | 동기화 동작 |
| --- | --- |
| 사용자 | 업데이트, 생성, 미러링, 삭제 |
| 코호트 | 업데이트, 만들기, 미러링 | 
| 카탈로그 | 업데이트, 만들기, 미러링 |
| 정기구독 그룹 멤버십 | 거울 |
| 이벤트 | 추가 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

또한 Census는 Braze에 [구조화된 데이터](https://docs.getcensus.com/destinations/braze#supported-objects) 전송을 지원합니다: 
- 사용자 푸시 토큰: 푸시 토큰을 보내려면 데이터는 2~3개의 값(`app_id`, `token`)과 선택적 `device_id`를 포함하는 오브젝트 배열로 구성되어야 합니다.
- 중첩된 사용자 지정 속성: 객체와 배열이 모두 지원됩니다. 2022년 4월 기준, 이 기능은 아직 얼리 액세스에서 제공합니다. 액세스하려면 Braze 계정 관리자에게 문의해야 할 수도 있습니다.

[1]: https://www.getcensus.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[8]: {% image_buster /assets/img/census/add_service.png %}
[9]: {% image_buster /assets/img/census/census_1.png %}
[10]: {% image_buster /assets/img/census/census_2.png %}
[11]: {% image_buster /assets/img/census/census_3.png %}