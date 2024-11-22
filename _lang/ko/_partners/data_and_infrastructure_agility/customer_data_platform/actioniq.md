---
nav_title: ActionIQ
article_title: ActionIQ
description: "이 참고 문서에서는 Braze와 ActionIQ 통합에 대해 설명합니다. ActionIQ는 마케터, 분석가, 기술자를 위한 엔터프라이즈 고객 데이터 플랫폼입니다. 이 통합을 통해 브랜드는 ActionIQ 데이터를 Braze에 직접 동기화하고 매핑할 수 있습니다."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> [ActionIQ][2]는 혼란스러운 고객 경험에 질서를 부여합니다. ActionIQ 고객 경험(CX) 허브는 고객 데이터에 대한 직접적이지만 통제된 방식의 셀프 서비스 액세스를 모든 팀에 제공하여 오디언스를 검색하고 발견하고 대규모로 경험을 오케스트레이션할 수 있도록 지원합니다.

Braze와 ActionIQ의 통합을 통해 브랜드는 ActionIQ 데이터를 Braze에 직접 동기화하고 매핑하여 광범위한 고객 데이터를 기반으로 탁월한 고객 경험을 제공할 수 있습니다. 통합을 통해 사용자는 다음을 수행할 수 있습니다:
- 잠재 고객 세그먼트 또는 사용자 지정 속성을 ActionIQ에서 바로 Braze에 매핑하세요.
- ActionIQ가 추적한 이벤트를 실시간으로 Braze에 전달하여 개인화된 타겟팅 캠페인을 트리거합니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| ActionIQ 계정 | 이 통합 기능을 이용하려면 ActionIQ 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 및 `user.export.ids` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][1]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 오디언스 멤버십

이 통합은 Braze 프로필이 세그먼트의 일부인지 여부를 나타내는 사용자 지정 속성을 생성하여 ActionIQ 오디언스 멤버십을 Braze에 동기화하는 데 사용됩니다. 각 ActionIQ 대상은 고유한 부울 사용자 지정 속성에 해당합니다.

생성된 사용자 지정 속성의 표준 명명 규칙은 `AIQ_<Audience ID>_<Split ID>` 입니다.

이러한 사용자의 세그먼트를 만들려면 Braze에서 **세그먼트로** 이동하여 새 세그먼트를 만든 다음 **사용자 지정 속성을** 필터로 선택합니다. 여기에서 ActionIQ 사용자 지정 속성을 선택할 수 있습니다. 세그먼트가 생성된 후에는 캠페인이나 캔버스를 만들 때 오디언스 필터로 선택할 수 있습니다.

#### 요구 사항

ActionIQ에서 REST API 키와 Braze REST 엔드포인트를 제공하여 Braze 연결을 설정합니다. 

Braze 플랫폼에서 소비자와 매칭하려면 활성화 설정에 다음 식별자를 포함해야 합니다.
- `braze_id`
- `external_id`

연동이 연결되면 정보가 Braze로 전송되기 시작합니다.

### 이벤트

ActionIQ 플랫폼은 스트리밍 수집 서비스를 통해 이벤트 정보를 수신하도록 구성할 수 있습니다. 이 다른 통합 옵션은 마케팅 담당자가 오케스트레이션 또는 마케팅 캠페인 트리거에 사용할 수 있도록 이러한 이벤트를 Braze로 전달합니다.

이벤트 통합은 이벤트 페이로드 내 속성정보의 일부로 추가 ActionIQ 속성을 전송할 수 있습니다.

#### 요구 사항

이벤트 통합은 다음 정보를 Braze에 전송합니다:
- 이벤트 이름
- 소비자 식별자( `braze_id` 또는 `external_id`)
- 타임스탬프
- 내보내기 설정의 추가 속성으로 채워지는 이벤트 속성


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/