---
nav_title: Kognitiv Inspire
article_title: Kognitiv Inspire
description: "Kognitiv Inspire는 로열티 전략을 구현하고 평가할 수 있는 로열티 기술 시스템으로, 혁신적인 기능과 맞춤형 회원 커뮤니케이션을 제공하여 프로그램 효과를 높일 수 있습니다."
alias: /partners/kognitiv/
page_type: partner
search_tag: Partner
---

# Kognitiv Inspire

> [Kognitiv Inspire][1]는 고객 참여를 확대하고, 지출을 늘리며, 충성도 높은 행동을 장려하는 결과 중심의 로열티 프로그램을 통해 탁월한 고객 경험을 제공하는 로열티 기술 시스템입니다.

_This integration is maintained by Kognitiv Inspire._

## 통합 정보

Braze와 Kognitiv의 통합을 통해 로열티 전략을 구현하고 평가할 수 있으며, 혁신적인 기능과 맞춤형 회원 커뮤니케이션을 제공하여 프로그램 효과를 높일 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| 코그니티브 계정 | 이 파트너십을 이용하려면 [코그니티브][1] 계정이 필요합니다. |
| 코그니티브 API 키 | 코그니티브 REST API 키입니다. 이는 **API 보안 토큰** 페이지에서 만들 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의]({{site.baseurl}}/api/basics/#endpoints) Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

- **개인화된 로열티 프로그램 등록**: 원활한 프로그램 등록과 기본 채널을 통해 전달되는 사용자 지정된 환영 알림을 활용하여 회원의 로열티 여정을 촉진합니다.
- **리워드 지급 및 인게이지먼트 알림**: 각 회원의 마일스톤을 축하하는 리워드를 지급하고 알림을 제공하여 로열티를 지속적으로 촉진합니다.
- **전략적 멤버 계층화 및 세분화**: 지출, 참여도, 단순하거나 복잡한 비즈니스 규칙을 기반으로 회원을 계층화하고 세분화하여 브랜드의 특정 요구사항에 맞게 맞춤화된 참여를 유도할 수 있습니다.
- **실시간 프로모션 자격 알림**: 특별 프로모션 자격에 대한 즉각적인 알림을 통해 각 회원에게 특별함을 선사합니다.

## 통합

로열티 이벤트가 발생하면 코그니티브 웹훅을 사용하여 Braze에 요청을 전송하세요. 다음 예제에서는 Kognitiv와 Braze를 사용하여 리워드를 지급하고, Braze에 Kognitiv 사용자를 등록하며, 환영 이메일을 보내는 방법을 설명합니다.

{% raw %}
### Braze 리워드 지급

다음 코그니티브 예제는 멤버 보상을 발행합니다. Kognitiv Inspire는 웹훅을 통해 해당 리워드 지급 이벤트를 Braze에 커스텀 이벤트로 전달합니다. 보상을 알리는 후속 이메일을 보내려면 해당 사용자 지정 이벤트가 트리거되는 캠페인 또는 캔버스를 만듭니다.

**웹훅 URL**: `<braze-api-rest-endpoint>`
**요청 본문**: `Raw Text`

- **HTTP 메서드**: POST
- **요청 헤더**:
  - **권한 부여**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### 요청 본문

```json
{ 
  "events" : [ 
    { 
    "external_id" : "{{memberId}}", 
    "app_id" : "93ec5a59-3752-4a45-8559-55b61209ba38", 
    "name" : "rewards_issued", 
    "time" : "{{issuedDate}}", 
    "issued_date" : "{{issuedDate}}", 
    "issued_location_name" : "{{issuedLocationName}}", 
    "reward_type" : "{{rewardType}}" 
    } 
  ] 
}
```

### 사용자 만들기 및 환영 이메일 보내기

다음 Kognitiv 예제에서는 KLS에 등록할 때 Braze에서 새 사용자를 생성합니다. 이 사용자에 대한 환영 이메일을 예약하려면 특정 사용자 지정 속성을 기반으로 트리거되는 캠페인 또는 캔버스를 Braze에서 생성하세요.

**웹훅 URL**: `<braze-api-rest-endpoint>` <br>
**요청 본문**: `Raw Text`

- **HTTP 메서드**: POST
- **요청 헤더**:
  - **권한 부여**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### 요청 본문

```json
{ 
  "attributes": [ 
    { 
      "app_id": "93ec5a59-3752-4a45-855b6109ba38", 
      "bio": "Software Architect", 
      "country": "{{memberAddressCO}}", 
      "email": "{{memberEmail}}", 
      "email_subscribe": "opted_in", 
      "external_id": "{{memberId}}", 
      "first_name": "{{memberFirstName}}", 
      "home_city": "{{memberAddressCity}}", 
      "time_zone": "America/Chicago", 
      "total_points_balance": "{{memberPointsAvailable}}", 
      "CreatedKLS": "{{issuedTimestamp}}", 
      "email_contact_allowed" : "{{memberEmailContactAllowed}}", 
      "sms_contact_allowed" : "{{memberSmsContactAllowed}}", 
      "date_joined": "{{issuedDate}}" 
    } 
  ] 
}
```
{% endraw %}

## Kognitiv Inspire 설명서 및 통합 기능

Braze와 Kognitiv Inspire를 통합하면 Kognitiv의 광범위한 API 포트폴리오, 최신 웹훅 기능, 강력한 데이터 가져오기 및 내보내기 기능을 통해 원활한 대량 전송이 가능합니다. Kognitiv Inspire 기능 및 통합 기능에 대한 자세한 내용은 Kognitiv [리소스 가이드][2]를 참조하거나 안내식 데모 요청을 문의하세요.

### 엔드포인트

**REST API 권한 부여**
- 미국 지역: `https://app.kognitivloyalty.com/Auth/connect/token`
- CA/EMEA 지역: `https://ca.kognitivloyalty.com/Auth/connect/token`
- APAC 지역: `https://aus.kognitivloyalty.com/Auth/connect/token`

**REST API(기본 URL)**
- 미국 지역: `https://app.kognitivloyalty.com/api`
- CA/EMEA 지역: `https://ca.kognitivloyalty.com/api`
- APAC 지역: `https://aus.kognitivloyalty.com/api`

**웹 서비스 엔드포인트(기본 URL)**
- 미국 지역: `https://app.kognitivloyalty.com/WS`
- CA/EMEA 지역: `https://ca.kognitivloyalty.com/WS`
- APAC 지역: `https://aus.kognitivloyalty.com/WS`

액세스 토큰 및 SFTP 엔드포인트 구성에 대한 자세한 내용을 보려면 Kognitiv에 데모 요청을 문의하세요.


[1]: http://kognitiv.com
[2]: https://info.kognitivloyalty.com