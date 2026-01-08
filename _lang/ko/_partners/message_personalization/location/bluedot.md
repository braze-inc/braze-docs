---
nav_title: Bluedot
article_title: Bluedot
alias: /partners/bluedot/
description: "이 참조 문서에서는 앱에 정확하고 간단한 지오펜싱 플랫폼을 제공하는 위치 플랫폼인 Bluedot과 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Bluedot

> [Bluedot](https://bluedot.io/)은 앱에 정확하고 간단한 지오펜싱 플랫폼을 제공하는 위치 플랫폼입니다. Bluedot의 SDK를 사용하여 더 스마트하게 메시지를 보내고, 모바일 주문 체크인을 자동화하고, 워크플로를 최적화하고, 원활한 경험을 만들 수 있습니다. 

_This integration is maintained by Bluedot._

## 통합 정보

Braze와 Bluedot의 통합을 통해 Bluedot 지오펜스 위치 서비스를 사용하여 여정, 캠페인을 구축하고 고객의 행동과 관심사를 분석하는 데 사용할 수 있는 사용자 이벤트를 생성할 수 있습니다. 사용자가 기기에서 생성한 이벤트(진입/종료)는 모든 관련 정보와 함께 Braze로 즉시 전송됩니다. 

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Bluedot 계정 | 이 통합 기능을 이용하려면 Bluedot 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

Bluedot에서 제공하는 커스텀 이벤트 위치 정보는 캠페인에서 다음과 같은 일반적인 사용 사례를 달성하는 데 사용할 수 있습니다.
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/) (퀵 서비스 레스토랑)
- [`Click and Collect`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/) 

## 통합

### 1단계: Bluedot 프로젝트 만들기
Bluedot 계정을 설정하고 [Bluedot 캔버스 대시보드](https://docs.bluedot.io/canvas/)에 로그인합니다. 새 프로젝트를 만드는 방법을 알아보려면 [Bluedot 문서를](https://docs.bluedot.io/canvas/creating-a-new-project/) 참조하세요.

### 2단계: SDK 통합
[Bluedot-Braze 통합](https://docs.bluedot.io/integrations/braze-integration/) 설명서에 제공된 단계를 따라 앱에서 Bluedot 포인트 SDK와 Braze SDK를 통합합니다.

### 3단계: Bluedot SDK 인증
1단계에서 생성한 `projectId`를 사용하여 Bluedot 포인트 SDK를 인증합니다.

### 4단계: Braze에서 Bluedot 이벤트 사용

#### 메시지 트리거

Bluedot SDK에서 생성된 위치 이벤트에 따라 작동하는 푸시 캠페인 또는 캔버스를 설정할 수 있습니다. 이 통합 경로는 사용자가 관심 장소나 거리에 진입한 직후에 실시간 메시징 또는 사용자가 떠난 후 지연된 후속 커뮤니케이션에 적합합니다.

설정된 위치에 따라 메시지를 전송하는 액션 기반 캠페인을 Braze 내에서 설정하세요. 트리거의 경우 다음 스크린샷과 같이 `bluedot_entry` 또는 `bluedot_exit` 의 사용자 지정 이벤트를 사용합니다:

![전달 단계의 액션 기반 캠페인입니다. 여기에는 사용자가 사용자 지정 `bluedot_entry` 또는 `bluedot_exit` 이벤트를 수행할 경우 캠페인을 전송하는 두 가지 예약 옵션이 있습니다.]({%image_buster /assets/img_archive/Campaign-Delivery-BD.png %}){: style="max-width:80%"}

#### 사용자 타겟팅

워크스페이스에 대해 **모든 사용자**를 타겟팅해야 합니다.
![원하는 세그먼트로 '모든 사용자'를 선택하도록 장려하는 타겟 사용자 단계를 포함하는 실행 기반 캠페인.]({%image_buster /assets/img_archive/Campaign-Target_users-BD.png %}){: style="max-width:80%"}

