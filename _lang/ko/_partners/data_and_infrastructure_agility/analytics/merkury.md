---
nav_title: Merkury
article_title: Merkury
description: "이 참조 문서에서는 'MerkuryID'를 활용하여 Braze 고객의 사이트 방문자 인식률을 높일 수 있도록 지원하는 앱용 엔터프라이즈 ID 플랫폼인 Merkury와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Merkury

> [Merkury](https://merkury.merkleinc.com/)는 퍼스트파티 쿠키리스 ID 기능을 통해 브랜드가 소비자 인게이지먼트, 경험 및 매출을 극대화할 수 있도록 지원하는 Merkle의 기업용 ID 플랫폼입니다. `MerkuryID` 은 브랜드의 알려진 고객과 알려지지 않은 고객 및 잠재 고객 기록, 사이트/앱 방문 기록, 소비자 데이터를 하나의 영구적인 개인 ID로 통합합니다.

_This integration is maintained by Merkury._

## 통합 정보

Braze와 Merkury의 통합을 통해 `MerkuryID` 을 활용하여 Braze 고객의 사이트 방문자 인지율을 높일 수 있습니다. 브랜드 이메일 가입자인 방문자를 인식하면 Merkury는 가입자의 이메일 주소를 포함하도록 Braze 프로필을 업데이트합니다. `MerkuryID`의 향상된 인식 기능은 인게이지먼트 및 개인화 기회를 개선하고 사이트 유기 이메일 전송량과 관련 매출을 즉각적으로 늘립니다. 

## 필수 조건

| 요구 사항 | 설명 |
| --- | --- |
| Merkle 계정 | 이 파트너십을 이용하려면 Merkle 계정이 필요합니다. |
| Merkle 클라이언트 ID | Merkle 담당자로부터 고객 ID를 확보합니다. |
| Merkury 태그 | 웹사이트에 Merkle의 Merkury 태그를 배치합니다. |
| Braze REST 및 SDK 엔드포인트 | REST 또는 SDK 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에]({{site.baseurl}}/api/basics/#endpoints) 따라 달라집니다. |
| Braze REST API 키 | `users.track, users.export.ids, users.export.segment, and segments.list` 권한이 있는 Braze REST API 키. <br><br>**Braze 대시보드 > 개발자 콘솔 > REST API 키 > 새 API 키 생성**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Braze에 대한 Merkury ID 커넥터 요청은 Braze API 사용량 제한 사양 내에서 작동합니다. 궁금한 점이 있으면 Braze 또는 Merkle 계정 매니저에게 문의하세요.<br><br>Merkury는 적격 세션이 끝나면 최소 한 번의 요청을 전송합니다.
{% endalert %}

## SDK 병렬 통합

Merkle의 클라이언트 측 Merkury 태그를 사용하여 Braze 기기를 캡처하고 식별을 위해 Merkury ID 커넥터 엔드포인트로 전달합니다.

### 1단계: Braze 웹 SDK 태그 설정

이 연동 기능을 사용하려면 웹사이트에 [Braze Web SDK가]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm) 배포되어 있어야 합니다.

### 2단계: Merkle의 Merkury 태그 배포

웹사이트에 Merkury 태그를 배포합니다. 이렇게 하면 웹사이트에서 Merkury ID 커넥터를 사용할 수 있습니다. Merkle 계정 매니저가 자세한 지침이 포함된 가이드를 제공해 드립니다.

### 3단계: 사용자 지정 속성 만들기

다음 필드는 Merkury ID 커넥터에 의해 채워지며 Braze에서 [커스텀 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attributes)으로 생성되어야 합니다.

| 속성 이름 | 데이터 유형 | 설명 |
| --- | --- | --- |
| `hmid` | 문자열 | Merkle의 Merkury ID |
| `confidence_score` | 숫자 | Merkury에서 식별할 수 있는 신뢰도 수준(1~8, 낮을수록 좋음) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 4단계: Merkle에 사용자 이메일 유니버스를 제공하세요.

Merkle은 허용되는 이메일 유니버스의 세분화 내보내기를 권장합니다. 허용되는 활성 사용자의 일일 내보내기를 통해 후속 조치를 취할 수 있습니다.

다음 필드는 필수 입력 사항입니다:

- `braze_id`
- `external_id`
- 이메일 주소

자세한 내용은 Braze 담당자에게 문의하세요.

