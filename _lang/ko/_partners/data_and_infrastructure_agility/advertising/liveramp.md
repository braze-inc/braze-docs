---
nav_title: LiveRamp
article_title: LiveRamp
description: "LiveRamp, Snowflake, Braze를 연결하여 고도로 개인화되고 관련성 높은 마케팅 캠페인을 생성하는 방법을 알아보세요."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# LiveRamp, Snowflake, Braze 연결

> 인사이트 도출 시간을 단축하고 데이터 사일로를 허물며 고객 참여를 최적화하여 고도로 개인화되고 관련성 높은 마케팅 캠페인을 생성할 수 있도록 LiveRamp, Snowflake, Braze를 연결하는 방법을 알아보세요. 이 통합은 더 나은 오디언스 세분화 및 시기 적절한 캠페인을 위해 실행 가능한 개인 기반 인사이트를 제공하고 소비자 터치포인트를 통합하여 데이터 기반 마케팅을 강화합니다. 또한 Snowflake에서 제공하는 벤치마크를 활용하여 업계 표준에 맞춰 마케팅 전략을 개선할 수 있습니다.

{% alert important %}
Snowflake의 [보안 데이터 공유](https://docs.snowflake.com/en/user-guide/data-sharing-intro)는 LiveRamp, Snowflake, Braze 간에 데이터를 전송하지 않습니다. 데이터는 Snowflake의 서비스와 메타데이터 저장소를 통해서만 공유되므로 데이터가 복사되지 않으며 추가 스토리지 요금도 발생하지 않습니다. 공유 데이터에 대한 액세스는 Snowflake 계정의 액세스 제어를 통해 제어 및 관리됩니다.
{% endalert %}

## 사용 사례

- **데이터 최소화:** LiveRamp의 활성화 앱은 Snowflake의 보안 데이터 공유 기능을 사용하여 인스턴스에서 직접 테이블을 효과적으로 읽을 수 있습니다. Snowflake에서 다운스트림 파트너로 전달 시점까지 데이터는 이동되지 않습니다.
- **보안 퍼스트파티 활성화:** 위의 ID 확인 애플리케이션을 사용하면 LiveRamp의 활성화 애플리케이션은 Snowflake 인스턴스에서 RampID 기반 테이블만 활용하므로 PII가 유출되지 않습니다.
- **TTL 단축:** 사용자 환경에서 직접 RampID로 데이터를 확인하면 LiveRamp가 제공하던 기존의 파일 기반 방식을 사용할 때 며칠이 걸렸던 것과 달리, 최종 대상으로 몇 시간 안에 전달할 수 있습니다. 이를 통해 캠페인 성과를 적시에 최적화할 수 있는 능력이 크게 향상됩니다.
- **운영 비용 절감:** 위와 마찬가지로, 고객은 Snowflake의 보안 데이터 공유 기능을 사용하여 LiveRamp로 파일 발신을 조정하거나 최종 목적지로 직접 전송할 때보다 시간과 비용을 절약할 수 있습니다.

## 전제 조건

| 전제 조건       | 설명                                                                                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Snowflake 계정 | 관리자 수준의 권한이 있는 Snowflake 계정이 필요합니다.                                                                                                                                      |
| LiveRamp 계정  | LiveRamp 계정 팀 또는 [snowflake@liveramp.com](mailto:snowflake@liveramp.com) 에 문의하여 Snowflake 내에서 필요한 LiveRamp 애플리케이션에 대해 논의하세요.                              |
{: .reset-td-br-1 .reset-td-br-2 }

## 연동 설정하기

### 1단계: Braze에 데이터 공유 요청하기

먼저, Braze 계정 매니저 또는 고객 성공 매니저에게 연락하여 Braze 계정에 대한 Snowflake 데이터 공유 커넥터를 구입합니다. 데이터 공유를 요청하면 Braze는 공유를 구매한 워크스페이스에서 공유를 프로비저닝합니다. 공유가 프로비저닝되면 모든 데이터는 Snowflake 인스턴스 내에서 들어오는 데이터 공유의 형태로 즉시 액세스할 수 있습니다. 인스턴스에 공유가 표시되면 공유에서 데이터베이스를 만들어 테이블을 보고 쿼리할 수 있습니다.

전체 안내는 [Snowflake 및 Braze 통합 가이드]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/)를 참조하세요.

### 2단계: Snowflake에서 LiveRamp 앱 설정 

번역 및 ID 확인 기능은 계정에 대한 공유를 생성하는 LiveRamp ID 확인 및 번역 기본 앱을 통해 Snowflake 환경 내에서 사용 가능합니다. 이 기능을 사용하면 자체 Snowflake 환경에서 참조 데이터 세트를 쿼리할 수 있는 보기가 열립니다.

기본 앱을 설정하려면 LiveRamp 설명서에서 다음 단계를 따르세요. [Snowflake에서 LiveRamp 기본 앱을 설정합니다](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html). 완료했으면 다음 단계로 넘어갑니다.

### 3단계: 데이터 테이블 만들기

{% alert warning %}
PII 기반 테이블을 준비하기 전에, 입력 테이블의 속성 열(비식별자)에 너무 고유한 값이 포함되지 않도록 작업 중에 실행되는 [LiveRamp의 개인정보 보호 필터를](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) 이해해야 합니다. 이는 소비자의 개인정보를 보호하고 재식별을 방지하는 데 매우 중요합니다.
{% endalert %}

다음으로, LiveRamp 기본 앱에 대해 호출할 [필수 형식](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html)으로 데이터 테이블을 생성합니다. 다음 카테고리를 참조하여 어떤 식별정보가 해결 대상인지 확인하세요:

| 식별자 유형 | 설명  |
|-----------------|--------------|
| 전체 PII        | 개인 식별 정보(PII)로는 사용자의 이름, 우편 주소, 이메일 및 전화번호가 포함됩니다. **참고:** 모든 기록에 모든 식별자가 필요한 것은 아닙니다. |
| 이메일 전용      | 사용자의 이메일 주소(예: `alex-lee@email.com`. |
| 기기          | 여기에는 서드파티 쿠키, 모바일 광고 ID(MAID), 커넥티드 TV ID(CTV ID), RampID(가정용 RampID로 확인됨)가 포함됩니다. |
| CID            | 플랫폼 파트너의 식별자 또는 내부 고객 ID와 같이 LiveRamp와 동기화된 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 브레이즈 식별자

Braze의 이벤트 로그에는 LiveRamp 기본 앱 내에서 사용할 수 있는 식별자가 포함되어 있습니다. 각 이벤트 유형에 사용 가능한 식별자의 전체 목록을 보려면 [Braze 이벤트 스키마 및 식별자]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt)를 다운로드합니다.

| 식별자 유형 | 설명  |
|-----------------|--------------|
| `AD_ID` | 특정 이벤트 유형 내에서 캡처된 광고 ID(`ios_idfa`, `google_ad_id`, `roku_ad_id`)는 LiveRamp의 기기 확인 서비스와 함께 사용할 수 있습니다. 기본적으로 광고 ID는 수집되지 않지만, [Braze 설명서를]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default) 따라 추적을 활성화할 수 있습니다. |
| `EMAIL_ADDRESS`   | LiveRamp의 이메일 전용 확인 서비스와 함께 사용할 수 있는 이메일 주소 |
| `TO_PHONE_NUMBER` | LiveRamp의 PII 확인 서비스와 함께 사용할 수 있는 전화번호. |
| `EXTERNAL_USER_ID` | 사용자와 연결된 외부 ID로, LiveRamp의 디바이스 확인 서비스(CID)와 함께 사용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
LiveRamp 애플리케이션 내에서 클라이언트 또는 브랜드별 커스텀 식별자를 사용하려면 [LiveRamp와 ID를 동기화](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html)해야 합니다.
{% endalert %}

### 4단계: 변수 설정

그런 다음, 앱에서 제공되는 실행 단계 워크시트에서 작업에 대한 변수를 설정합니다. 여기에는 대상 데이터베이스, 연결된 테이블(입력 데이터, 측정기준, 로깅), 출력 테이블 이름 정의와 같은 세부 정보가 포함됩니다. 전체 안내는 [LiveRamp를 참조하세요: 변수 지정](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727)을 참조하세요.

### 5단계: PII 확인을 위한 메타데이터 테이블 만들기

변수가 설정되었으므로 PII 확인을 위한 메타데이터 테이블을 생성합니다. 그러면 관련된 식별자 범주에 따라 실행할 특정 작업 유형에 대한 세부 정보가 제공됩니다. 전체 안내는 [LiveRamp를 참조하세요: 메타데이터 테이블 만들기](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43).

### 6단계: ID 확인 작업 수행

마지막으로, ID 확인 작업을 수행합니다. 전체 안내는 [LiveRamp를 참조하세요: ID 확인 작업 수행](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation)을 참조하세요.

{% tabs local %}
{% tab 입력 예제 %}
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
{% endtab %}

{% tab 출력 예제 %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### 다음 단계

이제 데이터를 가명화하여 전용 RampID 인코딩으로 변환하면, RampID 기반 테이블을 LiveRamp의 관리형 활성화 애플리케이션에 공유하여 주요 광고 플랫폼 파트너에게 간소화된 주문 처리를 제공할 수 있습니다. 활성화 애플리케이션에는 추가 세분화 및 다운스트림 대상 파트너의 선택/구성을 위한 비즈니스 사용자 친화적인 인터페이스가 포함되어 있습니다. 애플리케이션에 대한 자세한 내용은 LiveRamp 계정 팀 또는 [snowflake@liveramp.com](mailto:snowflake@liveramp.com)로 문의하시기 바랍니다.

## 문제 해결

{% alert note %}
보다 구체적인 문제나 질문이 있는 경우 [martech@liveramp.com](mailto:martech@liveramp.com) 으로 문의하세요.
{% endalert %}

### Snowflake 리전

현재 이 애플리케이션은 다음 미국 기반 지역에서만 사용할 수 있습니다:

  - AWS-US-EAST-1: POA18931
  - aws-us-west-2: FAA28932
  - azure-east-us-2: BL60425

### 개인 정보 보호 및 열 값

이 프로세스는 고유한 값이 있는지 행 단위로 모든 열 값의 조합을 평가합니다. 열 값의 특정 조합이 3회 이하로 발생하는 경우 해당 열 값이 포함된 행은 일치하지 않으며 출력 테이블에 반환되지 않습니다. 마찬가지로 개인정보 보호를 위해 LiveRamp 서비스는 열 값 조합의 고유성을 평가하여 드문 조합으로 인해 파일 행의 5% 넘게 일치할 수 없는 경우 작업이 실패합니다.

### 과거 데이터

Snowflake의 과거 데이터는 2019년 4월까지 거슬러 올라가지만, 제품 변경으로 인해 2019년 8월 이전 데이터와 약간의 차이가 있을 수 있습니다.

### 속도, 성능, 비용

쿼리 속도와 비용은 사용되는 웨어하우스 규모에 따라 달라집니다. 웨어하우스 크기를 선택할 때 데이터 액세스 요구 사항을 고려하세요.

### Braze 벤치마크

벤치마크를 사용하면 Snowflake 데이터 교환에서 바로 사용할 수 있는 업계 표준과 측정기준을 비교할 수 있습니다.

### 파괴적 변경 사항 및 비파괴적 변경 사항

통합에 영향을 줄 수 있는 변경 사항에 유의하세요. 파괴적 변경 사항은 공지와 마이그레이션 기간이 선행됩니다.
