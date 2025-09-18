---
nav_title: Toovio
article_title: Toovio
description: "이 참조 문서에서는 실행 가능한 데이터를 발견하고 가장 중요한 요소를 사용하여 사전 정의된 목표에 따라 점진적인 결과를 이끌어내는 데 도움을 주는 서비스형 데이터 회사인 Braze와 Toovio의 파트너십에 대해 설명합니다."
alias: /partners/toovio/
page_type: partner
search_tag: Partner

---

# Toovio

> [Toovio](https://toovio.com/)는 인공지능을 기반으로 하는 서비스형 데이터 회사로, 유용한 데이터를 검색하고 가장 중요한 요소를 사용하여 사전 정의된 목표에 따라 점진적인 결과를 도출할 수 있도록 도와줍니다.

_This integration is maintained by Toovio._

## 통합 정보

Braze와 Toovio의 파트너십은 실시간에 가까운 메시지 트리거링, 성과 향상을 위한 툴, Toovio의 고급 캠페인 측정 툴에 대한 액세스를 제공합니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Toovio 계정 | 이 파트너십을 이용하려면 Toovio 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze 커런츠 | Braze 커런츠를 사용하면 Braze 클라이언트가 이벤트 또는 행동 데이터를 Braze 데이터 파트너(AWS S3, Google Cloud Storage 또는 Microsoft Azure Blob Storage)로 스트리밍하여 Braze 플랫폼 외부에서 처리할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

다음 통합을 통해 Toovio는 특정 고객을 대상으로 트리거를 생성하고 거의 실시간으로 소통할 수 있습니다. Toovio가 결정한 트리거는 Braze [`/users/track` 엔드포인트][3]를 통해 Braze로 전송됩니다.

### 1단계: 데이터 파트너 정의

커런츠 피드의 드롭 위치는 Toovio와 공유해야 하며, 이를 통해 Toovio는 사용자 이벤트 및 행동 데이터에 액세스하고 해당 데이터를 처리할 수 있습니다.

### 2단계: 트리거 캠페인 설정

Toovio가 타겟팅할 고객 이벤트를 기반으로 Braze [API 트리거 캠페인][4]을 생성합니다. 또한 캠페인을 트리거할 타겟 사용자 속성과 값을 정의해야 합니다.

### 3단계: Toovio 계정 설정

계정을 설정하려면 '신규 고객 요청'이라는 제목으로 Toovio([info@toovio.com](mailto:info@toovio.com?subject=New%20Customer%20Request))에 문의합니다. Toovio는 고객과 협력하여 트리거 및 기본 모델을 설정합니다.


[1]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/
[2]: {{site.baseurl}}/api/api_key/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[4]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
