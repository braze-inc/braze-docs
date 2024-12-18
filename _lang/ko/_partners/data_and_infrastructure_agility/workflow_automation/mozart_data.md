---
nav_title: Mozart Data
article_title: Mozart Data
description: "이 참조 문서에서는 올인원 최신 데이터 플랫폼인 Mozart Data와 Braze 간의 파트너십을 간략히 설명합니다. 이를 통해 Fivetran을 사용하여 데이터를 Snowflake에 가져오고, 변환을 생성하며, 데이터를 결합하는 등의 작업을 할 수 있습니다."
alias: /partners/mozartdata/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html ID="HU6dSOClcQ0" align="right" %}

> [Mozart Data](https://mozartdata.com/)는 Fivetran, Portable 및 Snowflake로 구동되는 올인원 최신 데이터 플랫폼입니다.

Braze 및 Mozart 데이터 통합을 통해 다음을 수행할 수 있습니다:
- Fivetran을 사용하여 Braze 데이터를 Snowflake로 가져오기
- Braze 데이터를 다른 애플리케이션 데이터와 결합하여 변환을 생성하고 효과적으로 사용자 행동 분석
- Snowflake에서 Braze로 데이터를 가져와 새로운 고객 참여 기회를 만드세요
- Braze 데이터를 다른 애플리케이션 데이터와 결합하여 사용자 행동에 대한 보다 전체적인 이해 기반 확보
- 비즈니스 인텔리전스 도구와 통합하여 Snowflake에 저장된 데이터를 추가로 탐색합니다

## 필수 조건

<style>
table th:nth-child(1) {
    width: 25%;
}
table th:nth-child(2) {
    width: 75%;
}
table td {
    word-break: break-word;
}
</style>

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Mozart 데이터 account | 이 파트너십을 활용하려면 Mozart Data 계정이 필요합니다. [여기에서 가입하세요.](https://app.mozartdata.com/signup)|
| Snowflake 계정<br>옵션 1: 새 계정 | Mozart Data 계정 생성 프로세스 중에 Mozart Data에서 새 Snowflake 계정을 프로비저닝하려면 **새 Snowflake 계정 생성**을 선택합니다. |
| Snowflake 계정<br>옵션 2: 기존 계정 | 조직에 이미 Snowflake 계정이 있는 경우 Mozart Data 연결 옵션을 사용할 수 있습니다.<br><br>**이미 Snowflake 계정이 있습니다** 옵션을 선택하여 기존 Snowflake 계정을 연결합니다. 이 옵션을 추구하려면 계정 수준 권한이 있는 사용자가 [다음 단계를 준수](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount)해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

통합은 [Braze에서 Mozart Data로](#syncing-data-from-braze-to-mozart-data) 및 [Mozart Data에서 Braze로](#syncing-data-from-mozart-data-to-braze) 데이터 동기화를 모두 지원합니다.

### Braze에서 Mozart Data로 데이터 동기화

#### 1단계: Braze 커넥터 설정

1. 모차르트 데이터에서 **커넥터**로 이동하여 **커넥터 추가**를 클릭합니다.
2. "Braze"를 검색하고 커넥터 카드를 선택하세요.
3. Braze에서 동기화된 모든 데이터를 저장할 대상 스키마 이름을 입력합니다. 기본 스키마 이름 `braze`을 사용하는 것을 권장합니다.
4. **커넥터 추가**를 클릭합니다.

#### 2단계: Fivetran 커넥터 양식을 작성하십시오

귀하는 Fivetran 커넥터 페이지로 리디렉션됩니다. 이 페이지에서 주어진 필드를 작성하세요. 다음으로, **계속** > **저장 및 테스트**를 클릭하여 Fivetran 커넥터를 완료합니다.

Fivetran은 Braze 계정의 데이터를 Snowflake 데이터 웨어하우스에 동기화하기 시작합니다. 커넥터가 동기화를 완료한 후 Mozart 데이터에서 쿼리 데이터에 액세스할 수 있습니다. 

### Mozart Data에서 Braze로 데이터 동기화

#### 1단계: Snowflake 데이터 웨어하우스를 설정하십시오

Snowflake 인터페이스에서 테이블, 사용자 및 권한을 설정하려면 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake) 지침을 따르세요. 이 단계는 관리자 수준의 Snowflake 액세스가 필요합니다.

#### 2단계: Braze에서 Snowflake 통합 설정

Snowflake 웨어하우스를 설정한 후, Mozart 데이터에서 **통합** 페이지로 이동하여 **Braze**를 선택합니다. 여기에서 Braze에 제공해야 하는 자격 증명을 찾을 수 있습니다.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

다음으로, Braze에 로그인한 상태에서 **통합 > 기술 파트너 > Snowflake**로 이동하여 통합 프로세스를 시작합니다. Mozart 데이터에서 자격 증명을 복사하여 Snowflake 데이터 가져오기 페이지에 추가합니다. **동기화 세부 정보 설정**을 클릭하고 Snowflake 계정과 소스 테이블 정보를 입력합니다. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

다음으로, 동기화의 이름을 선택하고, 연락처 이메일을 제공하며, 데이터 유형과 동기화 빈도를 선택합니다. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-importsync.png %}){: style="max-width:80%;"}

#### 3단계: Braze 사용자에게 공개 키 추가
이 시점에서 설정을 완료하려면 Snowflake로 돌아가야 합니다. Braze 대시보드에 표시된 공개 키를 Braze가 Snowflake에 연결할 수 있도록 생성한 사용자에게 추가합니다.

자세한 방법은 [Snowflake 설명서](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)를 참조하십시오. 키를 언제든지 순환하려면 Mozart Data에서 새 키 페어를 생성하고 새 공개 키를 제공할 수 있습니다.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### 4단계: 테스트 연결

사용자가 공개 키로 업데이트되면 Braze 대시보드로 돌아가 **연결 테스트**을 클릭하십시오. 성공하면 데이터 미리보기를 볼 수 있습니다. 어떠한 이유로 연결이 실패하면 문제를 해결하는 데 도움이 되는 오류 메시지가 표시됩니다.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
통합을 초안에서 활성 상태로 전환하기 전에 반드시 성공적으로 테스트해야 합니다. 생성 페이지를 닫아야 하는 경우, 통합이 저장되며, 세부 정보 페이지를 다시 방문하여 변경 및 테스트를 할 수 있습니다.  
{% endalert %}

## 이 통합 사용

### Mozart 데이터 사용자로서 Braze 데이터를 액세스하는 방법
Mozart Data 계정을 성공적으로 생성하면 Mozart Data에서 Snowflake 데이터 웨어하우스에 동기화된 Braze 데이터를 액세스할 수 있습니다.

#### 변환
Mozart Data는 사용자가 보기 또는 테이블을 생성할 수 있도록 SQL 변환 레이어를 제공합니다. 사용자 수준의 차원 테이블(예: `dim_users`)을 생성하여 각 사용자의 제품 사용 데이터, 거래 내역 및 Braze 메시지와의 참여 활동을 요약할 수 있습니다. 

#### 분석
Braze에서 동기화된 변환 모델 또는 원시 데이터를 사용하여 Braze 메시지에 대한 사용자의 참여를 분석할 수 있습니다. 또한 Braze 데이터를 다른 애플리케이션 데이터와 결합하여 사용자가 Braze 메시지와 상호 작용하면서 얻은 인사이트가 사용자가 보유하고 있을 수 있는 다른 데이터와 어떻게 관련되는지 분석할 수 있습니다. 예를 들어, 인구 통계 정보, 쇼핑 기록, 제품 사용 및 고객 서비스 인게이지먼트가 이에 해당합니다. 

사용자 유지를 개선하기 위한 인게이지먼트 전략에 대해 더 많은 정보를 바탕으로 결정을 내리는 데 도움이 될 수 있습니다. 이 모든 작업은 Mozart Data의 인터페이스 내에서 쿼리 툴을 사용하여 수행할 수 있으며, 결과를 Google 시트 또는 CSV로 내보내어 프레젠테이션을 준비할 수 있습니다.

#### 비즈니스 인텔리전스 (BI)
다른 팀원들과 통찰력을 시각화하고 공유할 준비가 되셨습니까? Mozart Data는 거의 모든 BI 툴과 통합됩니다. BI 툴이 아직 없는 경우, 무료 Metabase 계정을 설정하려면 Mozart Data에 문의하세요. 