---
nav_title: Recurly
article_title: Recurly
description: "Recurly는 구독 및 반복 수익을 늘리고자 하는 소비자 직접 판매 브랜드를 위한 선도적인 구독 관리 및 청구 플랫폼입니다."
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> [Recurly는](https://recurly.com/) 구독 관리 및 청구 플랫폼입니다. Recurly 통합 플랫폼은 팀이 새로운 요금제, 오퍼, 프로모션 테스트부터 결제 방법, 통합, 인사이트 관리까지 가입자 경험을 관리하고 최적화할 수 있도록 지원하여 대규모 가입 생애주기의 자동화를 간소화합니다.

Recurly와 Braze 간 통합을 통해 가입 데이터 공유 프로세스가 간소화되어 고객과 타겟팅된 커뮤니케이션이 가능해집니다.

- Braze에서 반복적으로 가입 생애주기 이벤트(예: 가입 갱신, 일시 중지 또는 취소)를 활용하여 개인화된 캠페인 및 커뮤니케이션을 트리거합니다.
- Recurly 가입 데이터(예: 가입 요금제, 추가 기능 또는 상태)를 활용하여 Braze 사용자, 세그먼트 및 캔버스를 생성하고 관리함으로써 코호트별 캠페인 및 커뮤니케이션을 실행합니다.
- Recurly 데이터를 Braze로 직접 전송하여 추가적인 메시징 사용 사례를 활성화하고 개발 오버헤드 비용을 절감할 수 있습니다.

Braze와 함께 Recurly를 사용하는 방법에 대한 자세한 내용은 [Recurly 설명서](https://docs.recurly.com/docs/braze-integration)를 참조하세요.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Recurly 계정 | 이 파트너십을 활용하려면 Braze 기능 플래그가 활성화된 Elite [Recurly](https://recurly.com/) 가입 요금제가 필요합니다. Recurly 플랫폼에서 크레딧 인보이스도 활성화해야 합니다.|
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이것은 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. Recurly는 `users.track` 엔드포인트만 사용하므로 이 권한으로만 Recurly 특정 키를 프로비저닝하는 것이 좋습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][1]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |

## 통합

시작하기 전에 Braze와 Recurly 모두에 활성 계정이 있는지 확인하세요.

### Braze에 Recurly 연결

1. Recurly에서 **통합** > **Braze로** 이동합니다. Recurly에서 Braze 통합 구성 페이지로 처음 이동하면 인터페이스에서 두 시스템을 연결하라는 프롬프트가 표시됩니다.

2. 다음 자격 증명을 입력합니다:

- **인스턴스 URL:** 프로비저닝된 인스턴스의 Braze REST 엔드포인트.
- **API 키(식별자):** Recurly가 Braze에 요청을 보낼 때 사용해야 하는 Braze REST API 키.

Braze 인스턴스의 URL을 복사하는 것을 잊지 마세요. 예를 들어 URL은 다음과 같을 수 있습니다: 

```
<https://dashboard-03.braze.com/dashboard/app_usage?locale=en>
```

{:start="3"}
3\. 자격 증명을 입력한 후 **연결**을 클릭합니다.

## 이 통합 사용

### 지원되는 식별자

Recurly는 계정의 `account_code`를 Braze의 `external_id`로 사용합니다. 따라서 Recurly 계정의 `account_code`는 Braze 사용자의 `external_id`와 일치해야 합니다.

### 사용자 지정 이벤트

효과적인 고객 참여를 위해서는 Recurly에서 트리거되는 이벤트를 수신하도록 Braze에서 [커스텀 이벤트를 구성][2]해야 합니다. 철저한 데이터 통합을 위해 Recurly의 각 이벤트를 포함해야 합니다. 이러한 이벤트는 [Braze 애널리틱스][3] 내에서도 추적할 수 있습니다. 이러한 사용자 지정 이벤트를 구성한 후에는 사용자를 세분화하거나 메시지를 개인화하는 데 사용할 수 있습니다. 

| Braze 커스텀 이벤트| 반복 이벤트 |
| ----------- | ----------- |
| Recurly 신규 가입              | 구독이 생성되면 트리거됩니다.                            |
| Recurly 가입 갱신됨          | 구독이 갱신될 때 트리거됩니다.                                |
| Recurly 가입 업데이트됨          | 구독 속성이 변경될 때 트리거됩니다(요금제 변경, 가격 변경 또는 수량 변경). |
| 반복적으로 취소된 구독         | 구독이 취소되면 트리거됩니다.                           |
| Recurly 가입 재활성화됨      | 취소된 구독이 다시 활성화되면 트리거됩니다.               |
| 반복적으로 일시 중지된 구독           | 구독이 일시 중지되도록 설정된 경우 트리거됩니다.                   |
| 반복적으로 재개된 구독          | 구독이 일시 중지 해제될 때 트리거됩니다.                              |
| Recurly 가입 만료됨          | 구독이 만료되면 트리거됩니다.                               |
| Recurly 인보이스 생성됨               | 인보이스가 생성되면 트리거됩니다.                                |
| 반복적으로 성공적인 결제            | 인보이스가 성공적으로 수집되면 트리거됩니다.                 |
| Recurly 환불 실행됨                 | 환불이 실행되면 트리거됨                                   |
| 반복적으로 실패한 정기 결제      | 가입 갱신에 대한 인보이스가 실패하면 트리거됨          |

### 일괄 처리 및 속도 제한

Recurly는 Braze `/users/track` 엔드포인트를 사용하므로, 이 통합에는 분당 50,000건의 표준 Braze 요청 사용량 제한이 적용됩니다.

Recurly는 특정 가입 생애주기 이벤트를 Braze에 대한 단일 API 호출로 배치 처리하여 호출 횟수를 줄입니다.

- 동시에 여러 개의 구독을 생성하면 일괄 처리되어 하나의 요청으로 Braze에 전송됩니다.
- 계정에 대해 여러 개의 가입을 동시에 갱신하는 경우 각 갱신은 하나의 요청으로 배치 처리됩니다.
- 동일한 모델 구독 수명 주기 이벤트가 단일 요청으로 전송됩니다. 예를 들어 결제와 함께 새로 생성된 인보이스는 `Recurly Invoice Created` 및 `Recurly Successful Payment` 커스텀 이벤트가 모두 포함된 단일 API 요청을 전송합니다.

배치는 한 번에 최대 75개의 이벤트를 포함한 그룹으로 Braze에 전송됩니다. 예를 들어, 한 번에 100개의 가입이 생성되면 Recurly는 Braze에 두 번의 API 요청을 수행합니다. 자세한 내용은 [사용자 추적 요청 배치 처리][4]를 참조하세요.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[3]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics
[4]: {{site.baseurl}}/api/api_limits/#batch-user-track
