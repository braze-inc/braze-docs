---
nav_title: Extole
article_title: Extole
description: "이 문서에서는 친구 추천 및 성장 프로그램의 고객 이벤트 및 속성을 Braze로 가져올 수 있는 추천 마케팅 회사인 Extole와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> SaaS 기업인 [Extole](https://www.extole.com/)은 친구 추천 마케팅 분야의 업계 리더로, 효과적인 추천 마케팅 프로그램을 생성하고 최적화하여 고객 확보를 늘리는 데 도움을 줍니다.

_This integration is maintained by Extole._

## 통합 정보

Braze와 Extole의 통합을 통해 Extole 친구 추천 및 성장 프로그램의 고객 이벤트 및 속성을 Braze로 가져와서 고객 확보, 인게이지먼트, 로열티를 높이는 보다 개인화된 마케팅 캠페인을 만들 수 있습니다. 또한 개인화된 공유 코드 및 링크와 같은 Extole 콘텐츠 속성을 Braze 커뮤니케이션으로 동적으로 가져올 수도 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Extole 계정 | 이 파트너십을 이용하려면 Extole 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키입니다. Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze API URL | Braze API URL은 [Braze 인스턴스에]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) 고유합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

다음 사용 사례는 Extole과 Braze의 통합을 활용하는 몇 가지 방법을 보여줍니다. Extole 구현 및 고객 성공 매니저와 협력하여 회사의 특정 요구 사항에 맞는 옵션을 개발합니다.

- 추천 및 참여 프로그램의 사용자 지정 이벤트를 활용하여 Braze 캠페인 또는 Canvas를 트리거하세요.
- Extole 기반 프로그램의 데이터를 사용하여 커스텀 세그먼트, 대시보드 및 보고 생성
- Braze에서 사용자를 마케팅 목록에 자동으로 가입 또는 탈퇴

## 통합

다음 단계를 완료하여 빠르게 통합을 시작하고 실행합니다. Extole 구현 및 고객 성공 매니저가 이 프로세스를 지원하고 궁금한 점에 대해 답변해 드립니다.

### Braze 계정에 연결

1. 내 Extole 계정의 [파트너](https://my.extole.com/partners) 페이지에서 Braze 통합을 선택합니다.
2. Braze 통합에서 **설치를** 선택하여 Extole과 Braze 간의 연결을 시작합니다.
3. Braze REST API 키부터 시작하여 필수 필드를 작성합니다. 
4. Braze API URL을 입력합니다. 이 URL은 Braze 계정이 프로비저닝된 인스턴스에 따라 다릅니다.
5. Braze에 보내고 싶은 Extole 이벤트를 추가합니다. 기본 이벤트, 이벤트 속성 및 사용자 속성은 [Extole 이벤트 표](https://dev.extole.com/docs/braze#extole-program-events)에 설명되어 있습니다.
6. `FULFILLED` 상태 외에 Braze에 보내고 싶은 리워드 상태를 추가합니다. 사용 가능한 리워드 상태에 대한 설명은 [Extole 리워드 표](https://dev.extole.com/docs/braze#extole-rewards)를 참조하세요.
7. Braze 외부 ID 키 매핑을 선택합니다. 이것이 Extole이 Braze에서 사용자 프로필을 업데이트하는 방법입니다. 사용자에 대해 Braze 외부 ID 키를 Extole의 `email_address` 또는 `partner_user_id`에 매핑할 수 있습니다. `email_address` 대신 `external_id` 을 사용하는 것이 더 안전합니다.
8. 설정을 저장하여 연결을 완료합니다. 이제 Extole 이벤트가 Braze 계정으로 유입될 수 있습니다.

### Extole 프로그램 이벤트

다음은 Extole이 Braze에 전송하는 기본 이벤트, 이벤트 속성정보 및 사용자 속성입니다. Extole 구현 또는 고객 성공 매니저에게 연락하여 추가 Extole 이벤트를 식별하고 통합에 추가합니다.

| 이벤트 | 설명 | 이벤트 등록정보 | 사용자 속성 |
| ----------- | ----------- | ----------- | ----------- |
| `extole_created_share_link` | 참가자는 Extole 공유 경험에 이메일을 입력하여 공유 링크를 생성합니다. | 이벤트 이름  <br>이벤트 시간  <br>파트너(Extole)  <br>퍼널(지지자 또는 친구)  <br>프로그램 | <br>외부 ID <br>이메일  <br>공유 링크 |
| `extole_shared` | 참가자가 자신의 추천 링크를 친구와 공유합니다. | 이벤트 이름  <br>이벤트 시간  <br>파트너(Extole)  <br>외부 ID  <br>퍼널(지지자 또는 친구)  <br>프로그램  <br>채널 공유 | 이메일 <br>이름 <br>성 |
| `outcome` - 결과는 프로그램 구성에 따라 동적으로 달라짐(예: `extole_shipped`, `extole_converted`)| 참가자가 프로그램에 대해 구성된 원하는 결과 이벤트를 전환하거나 완료했습니다. | 프로그램별 동적 | 이메일 <br>이름 <br>성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Extole 가입 상태

| 구독 상태 | 설명 | 이벤트 등록정보 | 사용자 속성 |
| ----------- | ----------- | ----------- | ----------- |
| `subscribed` | 참가자가 마케팅 메시지 수신에 동의했습니다. | N/A | 이메일  <br>목록 유형  <br>외부 ID  <br>이메일 가입(옵트인됨) |
| `unsubscribed` | 참가자가 Extole 이메일 커뮤니케이션 수신을 옵트아웃했습니다.| 이메일  <br>외부 ID  <br>구독 상태(구독 취소)  <br>구독 그룹 ID  | 목록 유형 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Extole 리워드

기본적으로 Braze 캠페인이나 캔버스를 통해 리워드 알림을 트리거할 수 있도록 Extole은 `FULFILLED` 상태의 리워드 이벤트를 Braze로 전송합니다. 추가 리워드 상태는 다음 표를 참조하세요.

| 리워드 상태 | 설명 | 이벤트 등록정보 | 사용자 속성 |
| ----------- | ----------- | ----------- | ----------- |
| `FULFILLED` | 기본 상태입니다. 리워드에는 Extole 보상 공급업체가 가치(예: 쿠폰 또는 기프트 카드)를 할당했습니다. | 이메일 <br>액면가  <br>쿠폰 코드  <br>액면가 유형  | 이메일 <br>이름  <br>성 |
| `EARNED` | 보상이 생성되어 사람과 연결되었습니다. | 이메일 <br>액면가  <br>쿠폰 코드  <br>액면가 유형  | 이메일 <br>이름  <br>성 |
| `SENT` | 리워드가 이행되었으며 이메일 또는 기기를 통해 수신자에게 전송되었습니다. | 이메일 <br>액면가  <br>쿠폰 코드  <br>액면가 유형  | 이메일 <br>이름  <br>성 |
| `REDEEMED` | 수신자가 리워드를 사용했습니다. Extole로 전송된 전환 또는 사용 이벤트에서 확인할 수 있습니다.| 이메일 <br>액면가  <br>쿠폰 코드  <br>액면가 유형  | 이메일 <br>이름  <br>성 |
| `FAILED` | 문제가 발생하여 리워드가 지급되지 않거나 발송되지 않아 주의가 필요합니다. | 이메일 <br>액면가  <br>쿠폰 코드  <br>액면가 유형  | 이메일 <br>이름  <br>성 |
| `CANCELED` | 리워드가 비활성화되었으며 인벤토리로 돌아갑니다. | 이메일 <br>액면가  <br>액면가 유형  | 이메일 <br>이름  <br>성 |
| `REVOKED` | 이행된 리워드가 무효화되었습니다. 예를 들어 Extole은 공급업체 기프트 카드를 요청했다가 카드 전송에 문제가 있음을 확인했습니다. 공급업체가 리워드 취소를 지원하는 경우 Extole은 자금 반환을 요청하고 리워드는 더 이상 유효하지 않습니다. | 이메일 <br>액면가   <br>액면가 유형  | 이메일 <br>이름  <br>성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## 사용자 지정

### Braze에서 사용자 찾기 및 생성

Extole에 외부 ID(사용자 ID)가 없는 새 이메일 또는 SMS 가입과 같은 특정 사용 사례의 경우, Extole은 Braze의 [식별자 엔드포인트별 고객 프로필 내보내기]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)를 사용하여 사용자의 식별자를 확인할 수 있습니다. 사용자가 Braze에 존재하는 경우 Extole은 모든 프로필 속성을 추가하고 업데이트합니다. 요청이 고객 프로필을 반환하지 않으면 Extole은 `/users/track` 엔드포인트를 사용하여 사용자의 이메일 주소를 별칭 이름으로 사용해 사용자 별칭을 생성합니다.

## 이 통합 사용

계정을 연결하면 별도의 조치 없이도 이벤트가 자동으로 Extole에서 Braze로 전송되기 시작합니다. Braze로 전송되는 이벤트의 실시간 보기는 Extole의 아웃바운드 웹훅 센터에서 문제 해결을 위해 확인할 수 있습니다. 

