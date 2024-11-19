---
nav_title: Treasure Data
article_title: Treasure Data
description: "이 참조 문서에서는 작업 결과를 Braze에 직접 작성할 수 있는 기업 고객 데이터 플랫폼인 Treasure Data와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/treasure_data/
page_type: partner
search_tag: Partner

---

# Treasure Data

> [Treasure Data][4]는 여러 소스로부터 정보를 수집하여 마케팅 스택의 다양한 위치로 라우팅하는 고객 데이터 플랫폼(CDP)입니다.

Braze와 Treasure Data의 통합을 통해 Treasure Data의 작업 결과를 바로 Braze에 기록함으로써 다음 작업이 가능합니다.
* **외부 ID 매핑**: CRM 시스템에서 Braze 사용자 계정에 ID를 매핑합니다. 
* **옵트아웃 관리**: 최종 사용자가 참여하지 않기로 선택하여 동의를 업데이트하는 경우.
* **이벤트, 구매 또는 사용자 지정 프로필 속성에 대한 추적 정보를 업로드합니다**. 이 정보는 캠페인의 사용자 경험을 향상시키는 정확한 고객 세그먼트를 구축하는 데 도움이 될 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| --- | --- |
| Treasure Data 계정 | 이 파트너십을 활용하려면 [Treasure Data 계정](https://www.treasuredata.com/custom-demo/)이 필요합니다. |
| Braze REST API 키 | `users.track`, `users.delete`, `users.alias.new`, `users.identify` 권한이 있는 Braze REST API 키.<br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트  | 귀하의 REST 엔드포인트 URL. 사용자의 엔드포인트는 [인스턴스를 위한 Braze URL][1]에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 사용 사례

Treasure Data의 통합된 고객 프로필을 Braze에 동기화하여 타겟 세그먼트를 구축할 수 있습니다. Treasure Data는 퍼스트파티 쿠키 데이터, 모바일 ID, CRM과 같은 서드파티 시스템 등을 지원합니다.

## 통합

### 1단계: 새 연결 만들기

Treasure Data에서 **통합 허브** 아래의 **카탈로그**로 이동하여 **Braze**를 검색하고 선택합니다. 

**새 인증** 프롬프트가 표시되면 연결 이름을 지정하고 Braze REST API 키와 REST 엔드포인트를 입력합니다. 완료되면 **완료**를 선택합니다.

![][2]{: style="max-width:80%;"}

### 2단계: 쿼리 정의

보물 데이터에서 **데이터 워크벤치** 아래의 **쿼리로** 이동하여 데이터를 내보낼 쿼리를 선택합니다. 이 쿼리를 실행하여 결과 집합의 유효성을 검사합니다.

{% alert note %}
HIVE를 사용하여 쿼리를 구축하는 사용자의 경우, 밑줄로 시작하는 열이나 테이블을 모두 역따옴표로 묶어야 합니다. 예: `_merge_objects`.
{% endalert %}

다음으로, **결과 내보내기**를 선택하고 기존 통합 인증을 선택합니다.

![][11]{: style="max-width:80%;"}

다음 [사용자 지정 섹션](#customization)에 설명된 대로 추가 내보내기 결과 매개변수를 정의합니다. 내보내기 연동 콘텐츠에서 연동 매개변수를 검토합니다.

!['결과 내보내기' 페이지입니다. 이 페이지에는 '모드', '추적 레코드 유형' 및 '미리 서식 지정된 필드'에 대한 필드가 있습니다. 이 예제에서는 '사용자 추적' 및 '커스텀 이벤트'가 각각 이 필드에 설정되어 있습니다.][3]{: style="max-width:80%;"}

마지막으로, **완료**를 선택하고 쿼리를 실행한 다음, 데이터가 Braze로 이동했는지 확인합니다.

### 사용자 지정

내보내기 결과 매개변수는 다음 표에 포함되어 있습니다:

| 매개변수                 | 값 | 설명 |
|---------------------------|---|---|
| `mode`                    | 사용자 - 새 별칭<br>사용자 - 식별<br>사용자 - 추적<br>사용자 - 삭제 | 커넥터 모드 |
| `pre_formatted_fields`    | 문자열 | 형식을 유지하려면 배열 또는 JSON 열에 사용합니다. |
| `track_record_type`       | 사용자 지정 이벤트<br>구매<br>사용자 프로필 속성| **사용자 - 추적** 모드의 레코드 유형 |
| `skip_on_invalid_records` | 부울 | 활성화된 경우 계속 진행하며 JSON 열에 대한 유효하지 않은 레코드를 모두 무시합니다. <br> 그렇지 않으면 작업이 중지됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
미리 서식이 지정된 필드, 쿼리 예제, 매개변수 세부 정보 및 쿼리 내보내기 작업 예약에 대한 자세한 내용은 [Treasure Data](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration)를 참조하세요.
{% endalert %}

## 웹훅

Treasure Data 사용자는 공개 REST API를 통해 데이터를 수집할 수 있습니다. Treasure Data를 사용하여 데이터에 커스텀 웹훅을 생성할 수 있습니다. 자세하 알아보려면 [Treasure Data][6]를 방문하세요.

[6]: https://docs.treasuredata.com/display/public/PD/Postback+API
[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: {% image_buster /assets/img/treasure_data/braze_authentication.png %}
[3]: {% image_buster /assets/img/treasure_data/braze_export_configuration.png %}
[4]:https://www.treasuredata.com/
[5]:https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration
[10]: {% image_buster /assets/img/treasure_data/query_1.png %}
[11]: {% image_buster /assets/img/treasure_data/query_2.png %}
