---
nav_title: 귤
article_title: 귤
description: "이 기사는 Braze와 Tangerine Store360 간의 파트너십을 설명합니다. Tangerine Store360은 옴니채널 플랫폼으로, 오프라인 매장과 온라인 매장을 연결하여 소비자와 매장 직원에게 우수한 매장 내 경험을 제공합니다. 이 통합을 통해 Braze 원시 캠페인 및 노출 횟수 데이터는 Snowflake Secure Data Sharing을 통해 Store360에서 사용할 수 있으며, 브랜드는 캠페인이 매장 참여 및 매장 트래픽에 미치는 영향을 측정할 수 있습니다."
alias: /partners/tangerine/
page_type: partner
search_tag: Partner

---

# Tangerine Store360

> Tangerine은 옴니채널 플랫폼인 Store360을 설계, 구축 및 운영합니다. Store360은 옴니채널 활성화 플랫폼으로, 오프라인 매장과 온라인 매장을 연결하여 소비자와 매장 직원의 매장 내 경험을 향상시킵니다. Store360은 소매업체의 모바일 앱 사용자와 매장 내 참여를 포함하여 물리적 매장 방문 트래픽을 추적하고 분석합니다.

Braze와 Tangerine 통합을 통해 Braze의 원시 캠페인 및 노출 횟수 데이터를 Snowflake Secure Data Sharing을 통해 Store360에 통합할 수 있습니다. 브랜드는 이제 이러한 캠페인이 실제 매장 방문 및 매장 내 참여에 미치는 영향을 측정할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Store360 계정 | Store360 계정이 있어야 이 파트너십을 이용할 수 있습니다. |
| Braze 계정 ID | 귀하의 Braze 앱 그룹 ID. |
| 사용자 ID 일치 | Store360 및 Braze의 고객 데이터는 두 플랫폼에서 일치하는 사용자 ID를 가져야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

### 실제 스토어 방문에 대한 캠페인 영향 분석

브랜드는 Braze를 사용하여 소비자에게 캠페인 메시지를 보내 매장 방문을 증가시킵니다. 캠페인 동안, Store360은 사용자 ID로 식별된 모바일 앱 사용자 방문을 캡처합니다.

Store360 인사이트 분석 기능을 사용하면 브랜드는 발송 및 읽은 메시지(데이터는 Braze에서 제공)부터 실제 매장을 방문한 수신자 수(데이터는 Store360에서 제공)까지 캠페인 영향 세부 정보를 시각화할 수 있습니다.

## 통합

### 1단계: Snowflake 보안 데이터 공유 활성화

Braze 팀과 협력하여 Snowflake 보안 데이터 공유를 활성화하고 구성합니다.

### 2단계: Braze 데이터를 가져오도록 Store360 구성

Store360 관리자 매니저 웹 콘솔을 사용하여 Braze 앱 그룹 ID를 Store360 서비스 계정에 구성합니다. 이는 Tangerine 관리자 팀이 Snowflake 데이터 공유를 사용하여 Braze 데이터를 Store360과 동기화하도록 요청할 것입니다.

### 3단계: Store360 SDK를 모바일 앱에 통합

모바일 앱 사용자 스토어 방문 및 스토어 내 활동을 Braze 캠페인 및 노출 횟수 데이터와 함께 추적하고 분석하려면, Store360 SDK 설치 설명서에 제공된 단계를 사용하여 Store360 SDK를 모바일 앱에 통합해야 합니다. 이 설명서는 Tangerine Store 360과 클라이언트 계약을 체결한 후 제공됩니다.

## Store360에서 Braze 데이터를 분석

Snowflake의 안전한 데이터 공유를 활용하여 Braze의 원시 캠페인 및 노출 횟수 데이터를 Store360 인사이트 분석과 공유함으로써 온라인에서 오프라인까지 사용자의 생애 주기와 활동에 대한 전체 그림을 제공합니다.

참고로, Store360 분석에 통합할 수 있는 모든 [Braze 필드]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df)가 여기에 있습니다. 이 단계의 세부 사항은 매우 고객별이며 특별한 구성이 필요합니다. Store360 계정 매니저 또는 support@tangerine.io에게 문의하여 자세히 알아보세요.

## 중요한 정보 및 제한 사항

### 서비스 가용성

현재 Store360 서비스는 일본과 인도네시아에서 상용화되어 있습니다.

Tangerine은 2023년에 다음 국가에서 Store360 제품 출시를 계획하고 있습니다.
- 미국
- 태국
- 싱가포르
- 베트남
- 한국

### 데이터 보존

Snowflake 데이터 공유와 관련해 Braze 데이터의 2년 유지 정책이 적용됩니다.

### Braze 이벤트 데이터 채우기 지연 시간

Braze 이벤트는 스트리밍 기술로 처리되며 거의 실시간으로 사용할 수 있습니다. 일반적으로 이벤트는 발생 후 30분 이내에 제공됩니다.
