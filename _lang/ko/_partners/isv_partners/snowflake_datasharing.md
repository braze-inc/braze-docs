---
nav_title: Snowflake 데이터 공유
hidden: true
---

# Snowflake 데이터 공유 통합

> Snowflake 데이터 공유를 통합 방법으로 사용하는 경우, Braze는 고객을 대신하여 Snowflake 인스턴스에 공유를 프로비저닝합니다. 이 공유에는 모든 메시지 참여 및 사용자 행동 이벤트가 자동으로 포함됩니다.

공유는 고객이 Snowflake 데이터 공유 자격을 구매한 후 고객별로 프로비저닝됩니다. 고객이 데이터 공유를 요청하면 Braze는 고객의 워크스페이스에 공유를 추가하고, 고객은 셀프서비스 UI를 사용하여 관련 파트너 Snowflake 계정 데이터를 추가할 수 있습니다.

![]({% image_buster /assets/img/snowflake.png %})

공유가 프로비저닝되면 모든 데이터는 Snowflake 인스턴스 내에서 들어오는 데이터 공유로 즉시 액세스할 수 있습니다.

![]({% image_buster /assets/img/snowflake2.png %})

Snowflake 인스턴스 내에는 리전당 하나의 공유가 표시됩니다. 각 테이블에는 사실상 Braze의 테넌트 키인 `app_group_id` 열이 있습니다. 동일한 리전 내 공유에 새 고객이 추가되면 기존 테이블 내에서는 다른 `app_group_ids`로 표시됩니다.

{% alert important %}
Braze는 현재 모든 사용자 수준 데이터를 Snowflake AWS US East-1 및 EU-Central(프랑크푸르트) 리전에 호스팅합니다. Braze는 리전 간 공유가 가능하지만, `US-EAST-1` 및/또는 `EU-CENTRAL-1`과 공유하는 것이 고객에게 가장 비용 효율적입니다.
{% endalert %}

{% alert tip %}
여기에서 [원시 테이블 스키마]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df)를 다운로드하거나 Snowflake 마켓플레이스에서 제공되는 이 [샘플 이벤트 데이터](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset) 세트를 사용하여 공유된 이벤트에 익숙해지세요.
{% endalert %}

## 중복 이벤트 처리하기

중복이 예상되지만 모든 이벤트에는 고유 식별자인 ID 열이 있습니다. `select distinct(id)`를 수행하여 중복을 제거할 수 있습니다.

## 파괴적 변경 사항 및 비파괴적 변경 사항

### 비파괴적 변경 사항

비파괴적 변경 사항은 언제든지 발생할 수 있으며 일반적으로 추가 기능을 제공합니다. 비파괴적 변경 사항의 예:
- 새 테이블 또는 뷰 추가
- 기존 테이블 또는 뷰에 열 추가하기

{% alert important %}
새 열은 비파괴적 변경으로 간주되므로 Braze는 `SELECT *` 쿼리를 사용하는 대신 각 쿼리에서 관심 있는 열을 명시적으로 나열할 것을 적극 권장합니다. 또는 열 이름을 명시적으로 지정하는 보기를 생성한 다음, 테이블을 직접 쿼리하는 대신 해당 보기를 쿼리할 수 있습니다.
{% endalert %}

### 파괴적 변경 사항

가능한 경우, 파괴적 변경 사항은 공지와 마이그레이션 기간이 선행됩니다. 파괴적 변경 사항의 예:
- 테이블 또는 뷰 제거
- 기존 테이블 또는 뷰에서 열 제거하기
- 기존 열의 유형 또는 무효화 가능성 변경하기

## 일반 데이터 보호 규정(GDPR) 준수

Braze가 저장하는 거의 모든 이벤트 레코드에는 사용자의 개인 식별 정보(PII)를 나타내는 몇 가지 필드가 포함되어 있습니다. 일부 이벤트에는 이메일 주소, 전화번호, 기기 ID, 언어, 성별 및 위치 정보가 포함될 수 있습니다. 사용자가 Braze에 정보 지우기를 요청하면 해당 사용자에 속하는 이벤트에 대한 PII 필드를 무효화합니다. 이렇게 하면 이벤트의 역사적 기록이 삭제되는 것은 아니지만, 이제 특정 개인과 이벤트가 다시 연결될 수 없습니다.
