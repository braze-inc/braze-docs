---
nav_title: Snowplow
article_title: Snowplow
description: "이 참고 문서에서는 데이터 인프라 플랫폼인 Snowplow와 Braze의 파트너십에 대해 설명하며, Snowplow의 이벤트 포워딩을 사용하여 Snowplow 이벤트를 실시간으로 Braze에 전달할 수 있습니다."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [스노우플로는](https://snowplowanalytics.com) 풍부한 고품질, 저지연 데이터 수집을 위한 확장 가능한 플랫폼입니다. 스노우플로는 기업 비즈니스를 위한 고품질의 완전한 행동 데이터를 수집하도록 설계되었습니다.

_This integration is maintained by Snowplow._

## 통합 정보

Braze와 Snowplow 통합을 통해 Snowplow의 이벤트 포워딩 솔루션을 사용하여 Snowplow 이벤트를 실시간으로 Braze에 전달할 수 있습니다. 이 통합을 통해 이벤트를 Braze로 전송하는 동시에 유연성과 제어 기능을 제공할 수 있습니다. 구체적으로, 할 수 있습니다:
- 이벤트를 필터링하고 변환한 후 Braze로 전송하세요.
- 스노우플로우 이벤트 데이터를 Braze 사용자 속성, 커스텀 이벤트 및 구매에 매핑하세요.
- 전달을 선택할 때까지 모든 데이터를 개인 클라우드에 보관하세요.
- 기존 Snowplow 클라우드 계정 내에서 솔루션을 직접 배포하세요. 

스노우플로우의 [이벤트 전달은](https://docs.snowplow.io/docs/destinations/forwarding-events/) 스노우플로우 고객에게 제공되는 유료 애드온 기능입니다. 이 애드온 없이 이벤트를 Braze에 전달하려면 Snowplow의 Google Tag Manager 서버 측 [통합을 사용](https://docs.snowplow.io/docs/destinations/forwarding-events/google-tag-manager-server-side/) 하세요.

Snowplow의 풍부한 행동 데이터를 활용하여 Braze에서 강력한 고객 중심 인터랙션을 유도하고 개인화된 메시지를 실시간으로 전달하세요.

## 필수 조건

| Requirement             | Description                                                                                                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Snowplow pipeline       | 스노우플로 파이프라인을 가동하고 실행해야 합니다.                                                                                                                                                                                                                                          |
| 제설기 콘솔 액세스 | 이벤트 전달자를 구성하려면 스노우플로 콘솔에 액세스할 수 있어야 합니다.                                                                                                                                                                                                                                |
| Braze REST API key      | 다음 권한이 있는 Braze REST API 키입니다: `users.track`, `users.alias.new`, `users.identify`, `users.export.ids`, `users.merge`, `users.external_ids.rename`, `users.alias.update`. <br><br> **설정** > **API 키에서** Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST endpoint     | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance.                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

### Personalized, action-based delivery
Use any of the large number of rich events that Snowplow collects by default, or define your custom events to shape even more granular customer journeys that make sense for your business. Leverage Snowplow's rich behavioral data to design customer funnels and unlock value for your marketing and product teams, helping them to maximize conversion and product usage through Braze.

### Dynamic segmentation
Create dynamic audiences in Braze based on Snowplow's high-quality behavioral data: As users take actions in your product, app, or website, you can leverage the real-time behavioral data that Snowplow collects to automatically add or remove users from relevant segments in Braze.

## Integration

### 1단계: 스노우플로우 콘솔에서 대상 구성하기

이벤트 전달자를 만들려면 다음과 같이 하세요:

1. 제설기 콘솔에서 **대상으로** 이동하여 **새 대상 만들기를** 선택합니다.
2. 연결을 구성할 때 연결 유형으로 **Braze를** 선택합니다.
3. Braze API 키와 REST API 엔드포인트를 입력합니다.
4. 연결을 저장합니다.

### 2단계: 이벤트 전달자 구성

전달자를 구성할 때 전달할 스노우플로우 이벤트를 선택하고 이를 Braze 객체 유형에 매핑할 수 있습니다:

1. **[사용자 속성]({{site.baseurl}}/api/objects_filters/user_attributes_object)**: 고객 프로필 데이터 및 커스텀 사용자 속성을 업데이트합니다.
2. **[커스텀 이벤트]({{site.baseurl}}/api/objects_filters/event_object)**: 사용자 작업 및 행동을 전송합니다.
3. **[구매]({{site.baseurl}}/api/objects_filters/purchase_object)**: 제품 세부 정보가 포함된 트랜잭션 데이터를 전송합니다.

각 개체 유형에 대해 필드 매핑을 구성하여 Snowplow 이벤트 데이터가 Braze 필드에 매핑되는 방식을 지정할 수 있습니다. 자세한 설정 지침과 필드 매핑 구성은 Snowplow의 [전달자 만들기 설명서를](https://docs.snowplow.io/docs/destinations/forwarding-events/creating-forwarders/) 참조하세요.

### 3단계: 통합 검증하기

Braze 계정에서 다음 페이지를 확인하여 이벤트가 도달하고 있는지 확인하세요:

1. **쿼리 빌더**: Braze에서 **분석** > **쿼리 빌더로** 이동합니다. 다음 표에 쿼리를 작성하여 Snowplow에서 전달된 데이터를 미리 볼 수 있습니다: `USER_BEHAVIORS_CUSTOMEVENT_SHARED` 및 `USERS_BEHAVIORS_PURCHASE_SHARED`.
2. **API 사용 대시보드**: Braze에서 **설정** > **API 및 식별자로** 이동하여 시간별 API 사용량 차트를 확인합니다. 스노우플로우가 사용하는 API 키만 필터링하여 성공과 실패를 모두 확인할 수 있습니다.

## 커스텀 속성 보내기

표준 필드 외에 커스텀 속성을 보낼 수 있습니다. 구조는 사용 중인 Braze 객체 유형에 따라 다릅니다:

- **사용자 속성**: 최상위 필드로 추가(예: `subscription_tier`, `loyalty_points`)
- **이벤트 속성정보**: `properties` 개체 아래에 중첩(예: `properties.plan_type`, `properties.feature_flag`)
- **구매 속성정보**: `properties` 개체 아래에 중첩(예: `properties.color`, `properties.size`)

공백이 포함된 속성 이름의 경우 대괄호 표기법(예: `["account type"]` 또는 `properties["campaign source"]`)을 사용합니다.

지원되는 데이터 유형, 속성 명명 요구 사항 및 페이로드 크기 제한에 대한 자세한 내용은 [이벤트 객체 설명서를]({{site.baseurl}}/api/objects_filters/event_object) 참조하세요.

## Limitations

**요금 제한:** Braze는 사용자 추적 API에 대해 3초당 3,000회의 API 호출 속도 제한을 적용합니다. Snowplow는 이벤트 전달자에 대한 일괄 처리를 지원하지 않으므로 이 API 속도 제한은 이벤트 속도 제한으로도 작동합니다. 입력 처리량이 3초당 3,000개의 이벤트를 초과하는 경우 지연 시간이 늘어날 수 있습니다.
