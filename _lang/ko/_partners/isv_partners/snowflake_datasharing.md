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

### Non-breaking changes

Non-breaking changes can happen at any time and generally provide additional functionality. Examples of non-breaking changes:
- Adding a new table or view
- Adding a column to an existing table or view

{% alert important %}
새 열은 비파괴적 변경으로 간주되므로 Braze는 `SELECT *` 쿼리를 사용하는 대신 각 쿼리에서 관심 있는 열을 명시적으로 나열할 것을 적극 권장합니다. 또는 열 이름을 명시적으로 지정하는 보기를 생성한 다음, 테이블을 직접 쿼리하는 대신 해당 보기를 쿼리할 수 있습니다.
{% endalert %}

### Breaking changes

When possible, breaking changes will be preceded by an announcement and a migration period. Examples of breaking changes include:
- Removing a table or view
- Removing a column from an existing table or view
- 기존 열의 유형 또는 무효화 가능성 변경하기

## SNAPSHOTS 및 CHANGELOGS 테이블이 업데이트될 때

SNAPSHOTS 및 CHANGELOGS 테이블은 캠페인과 캔버스의 변경 사항을 추적합니다. 이 테이블이 업데이트되는 시점을 이해하는 것은 가장 최근의 메시지 변형 및 캔버스 구성을 쿼리하는 데 중요합니다.

### CHANGELOGS_CAMPAIGN_SHARED

다음과 같은 경우 `CHANGELOGS_CAMPAIGN_SHARED`에 행이 추가됩니다:
- 캠페인이 시작되거나,
- 다음의 스냅샷 가능한 필드 중 하나가 변경됩니다:
  - Name
  - 작업(메시지 내용 변경 포함)
  - 전환 행동

{% alert important %}
게시 후 초안 저장 또는 업데이트는 자동으로 업데이트를 트리거하지 않습니다. 업데이트는 캠페인을 시작하거나 게시 후 초안 변경 사항을 활성 캠페인에 적용할 때만 트리거됩니다.
{% endalert %}

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED

`SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED`은 `CHANGELOGS_CAMPAIGN_SHARED`에서 파생됩니다. 이 테이블은 `CHANGELOGS_CAMPAIGN_SHARED`의 작업 열을 개별 메시지 변형 레코드로 추출하고 평탄화합니다. `CHANGELOGS_CAMPAIGN_SHARED`가 업데이트될 때 accordingly 업데이트됩니다.

### CHANGELOGS_CANVAS_SHARED

다음과 같은 경우 `CHANGELOGS_CANVAS_SHARED`에 행이 추가됩니다:
- 캔버스가 시작되거나,
- 다음의 스냅샷 가능한 필드 중 하나가 변경됩니다:
  - Name
  - 전환 행동
  - 변형(비율, 첫 단계 할당, 변형 이름)

{% alert important %}
게시 후 초안 저장 또는 업데이트는 자동으로 업데이트를 트리거하지 않습니다. 업데이트는 캔버스를 시작하거나 게시 후 초안 변경 사항을 활성 캔버스에 적용할 때만 트리거됩니다.
{% endalert %}

### SNAPSHOTS_CANVAS_VARIATION_SHARED

`SNAPSHOTS_CANVAS_VARIATION_SHARED`은 `CHANGELOGS_CANVAS_SHARED`에서 파생됩니다. 이 테이블은 `SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED`와 동일한 추출 패턴을 사용하며 `CHANGELOGS_CANVAS_SHARED`가 업데이트될 때 accordingly 업데이트됩니다.

### SNAPSHOTS_CANVAS_STEP_SHARED

다음과 같은 경우 `SNAPSHOTS_CANVAS_STEP_SHARED`에 행이 추가됩니다:
- 캔버스가 시작되거나,
- 활성 캔버스가 업데이트됩니다(게시 후 초안 적용), 또는
- 다음의 스냅샷 가능한 필드 중 하나가 변경됩니다:
  - Name
  - 작업(메시지 변형 내 메시지 내용 변경 포함)

{% alert important %}
게시 후 초안을 저장하는 것은 자동으로 업데이트를 트리거하지 않습니다. 업데이트는 캔버스를 시작하거나 게시 후 초안 변경 사항을 활성 캔버스에 적용할 때만 트리거됩니다.
{% endalert %}

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED

다음과 같은 경우 `SNAPSHOTS_CANVAS_FLOW_STEP_SHARED`에 행이 추가됩니다:
- 캔버스가 시작되거나,
- 활성 캔버스가 업데이트됩니다(게시 후 초안 적용), 또는
- 다음의 스냅샷 가능한 필드 중 하나가 변경됩니다:
  - Name

{% alert important %}
게시 후 초안을 저장하는 것은 자동으로 업데이트를 트리거하지 않습니다. 업데이트는 캔버스를 시작하거나 게시 후 초안 변경 사항을 활성 캔버스에 적용할 때만 트리거됩니다.
{% endalert %}

## 일반 데이터 보호 규정(GDPR) 준수

{% include partners/snowflake_pii_gdpr.md %}